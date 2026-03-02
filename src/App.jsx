import React, { useState, useEffect, useMemo } from 'react';
import ReactMarkdown from 'react-markdown';
import { Search, Settings, TrendingUp, AlertCircle, Loader2, Send, Copy, Check } from 'lucide-react';
import { PROMPTS } from './constants/prompts';
import './index.css';

const FIREWORKS_API_URL = 'https://api.fireworks.ai/inference/v1/chat/completions';
const DEFAULT_MODEL = 'accounts/fireworks/models/kimi-k2p5';

function App() {
  const [ticker, setTicker] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedPrompt, setSelectedPrompt] = useState(PROMPTS[0]);
  const [apiKey, setApiKey] = useState(localStorage.getItem('fireworks_api_key') || '');
  const [showSettings, setShowSettings] = useState(!apiKey);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);
  const [lookupLoading, setLookupLoading] = useState(false);

  const filteredPrompts = useMemo(() => {
    if (!searchTerm) return PROMPTS;
    const lowerSearch = searchTerm.toLowerCase();
    return PROMPTS.filter(p =>
      p.title.toLowerCase().includes(lowerSearch) ||
      p.prompt.toLowerCase().includes(lowerSearch)
    );
  }, [searchTerm]);

  const handleLookupTicker = async (query) => {
    if (!query) return;
    if (!apiKey) {
      setShowSettings(true);
      return;
    }

    setLookupLoading(true);
    setError('');

    try {
      const response = await fetch(FIREWORKS_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
          model: DEFAULT_MODEL,
          messages: [
            {
              role: 'system',
              content: 'You are a financial data assistant. Return ONLY the primary stock ticker symbol for the company mentioned. If you find multiple, return the most prominent one. Format: JUST the ticker, no extra text. Example: "AAPL" or "MBG.DE".'
            },
            {
              role: 'user',
              content: `What is the primary stock ticker for ${query}?`
            }
          ],
          max_tokens: 20,
          temperature: 0
        })
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.error?.message || 'Lookup failed');
      }

      const data = await response.json();
      const content = data.choices[0].message.content.trim();

      // Better parsing: find something that looks like a ticker (all caps/numbers/dots/dashes)
      // Usually the model returns just the ticker, but we extract the first sequence matching a ticker pattern
      const match = content.match(/[A-Z0-9\.-]+/);
      const foundTicker = match ? match[0].toUpperCase() : null;

      if (foundTicker) {
        setTicker(foundTicker);
      } else {
        setError(`Could not find a valid ticker in: "${content}"`);
      }
    } catch (err) {
      setError('Ticker lookup failed: ' + err.message);
    } finally {
      setLookupLoading(false);
    }
  };

  const handleAnalyze = async () => {
    if (!ticker) {
      setError('Please enter a stock ticker');
      return;
    }
    if (!apiKey) {
      setShowSettings(true);
      return;
    }

    setLoading(true);
    setResult('');
    setError('');

    const promptText = selectedPrompt.prompt.replace('[TICKER]', ticker.toUpperCase());

    try {
      const response = await fetch(FIREWORKS_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
          model: DEFAULT_MODEL,
          messages: [
            {
              role: 'system',
              content: 'You are a professional equity research analyst with a focus on deep value and risk assessment.'
            },
            {
              role: 'user',
              content: promptText
            }
          ],
          max_tokens: 4096,
          temperature: 0.7
        })
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.error?.message || 'Failed to fetch analysis');
      }

      const data = await response.json();
      setResult(data.choices[0].message.content);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleCopyPrompt = () => {
    const promptText = selectedPrompt.prompt.replace('[TICKER]', ticker || '[TICKER]');
    navigator.clipboard.writeText(promptText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const saveApiKey = (key) => {
    setApiKey(key);
    localStorage.setItem('fireworks_api_key', key);
    setShowSettings(false);
  };

  return (
    <div className="app-container">
      <button className="settings-button" onClick={() => setShowSettings(true)}>
        <Settings size={20} />
      </button>

      <header className="header">
        <h1>StockVision</h1>
        <p>AI-Powered Equity Research via Kimi K2.5</p>
      </header>

      <div className="controls">
        <div className="input-group">
          <label htmlFor="ticker">Stock Ticker</label>
          <div className="ticker-input-wrapper">
            <input
              id="ticker"
              type="text"
              className="ticker-input"
              placeholder="e.g. NVDA or 'Apple'"
              value={ticker}
              onChange={(e) => setTicker(e.target.value)}
              onKeyPress={(e) => {
                if (e.key === 'Enter') {
                  if (ticker.length > 5 || ticker.includes(' ')) {
                    handleLookupTicker(ticker);
                  } else {
                    handleAnalyze();
                  }
                }
              }}
            />
            <button
              className="lookup-button"
              onClick={() => handleLookupTicker(ticker)}
              disabled={lookupLoading || !ticker}
              title="Lookup ticker by name"
            >
              {lookupLoading ? <Loader2 className="animate-spin" size={18} /> : <Search size={18} />}
              <span>Find Ticker</span>
            </button>
            <button
              className="copy-prompt-button"
              onClick={handleCopyPrompt}
              title="Copy prompt for other LLMs"
              disabled={!ticker}
            >
              {copied ? <Check size={18} color="#10b981" /> : <Copy size={18} />}
              <span>{copied ? 'Copied!' : 'Copy Prompt'}</span>
            </button>
          </div>
          <p className="input-helper">Enter a ticker or a company name and click "Find Ticker"</p>
        </div>

        <div className="input-group">
          <div className="label-with-search">
            <label>Select Analysis Strategy</label>
            <div className="search-wrapper">
              <Search size={16} />
              <input
                type="text"
                placeholder="Search strategies..."
                className="search-input"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
          </div>
          <div className="prompts-grid">
            {filteredPrompts.map((p) => (
              <button
                key={p.id}
                className={`prompt-card ${selectedPrompt.id === p.id ? 'active' : ''}`}
                onClick={() => setSelectedPrompt(p)}
              >
                <h3>{p.title}</h3>
                <p>{p.prompt.split('\n')[0].substring(0, 100)}...</p>
              </button>
            ))}
            {filteredPrompts.length === 0 && (
              <p className="no-results">No strategies found matching "{searchTerm}"</p>
            )}
          </div>
        </div>

        <button
          className="analyze-button"
          onClick={handleAnalyze}
          disabled={loading || !ticker}
        >
          {loading ? (
            <><Loader2 className="animate-spin" size={20} /> Analyzing...</>
          ) : (
            <><Send size={20} /> Run Analysis</>
          )}
        </button>
      </div>

      <div className="result-container">
        {error && (
          <div className="error-message" style={{ color: '#ef4444', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <AlertCircle size={20} /> {error}
          </div>
        )}

        {loading ? (
          <div className="result-placeholder">
            <div className="loading-spinner"></div>
            <p>Kimi K2 is crunching the numbers for {ticker.toUpperCase()}...</p>
          </div>
        ) : result ? (
          <div className="markdown-content">
            <ReactMarkdown>{result}</ReactMarkdown>
          </div>
        ) : (
          <div className="result-placeholder">
            <TrendingUp size={48} />
            <p>Select a strategy and enter a ticker to begin your deep dive.</p>
          </div>
        )}
      </div>

      {showSettings && (
        <div className="modal-overlay">
          <div className="modal">
            <h2>API Settings</h2>
            <div className="input-group">
              <label htmlFor="api-key">Fireworks.ai API Key</label>
              <input
                id="api-key"
                type="password"
                className="ticker-input"
                style={{ fontSize: '1rem', textTransform: 'none' }}
                placeholder="Paste your key here"
                defaultValue={apiKey}
                onBlur={(e) => saveApiKey(e.target.value)}
              />
              <p style={{ fontSize: '0.8rem', color: '#64748b', marginTop: '0.5rem' }}>
                Your key is stored locally in your browser.
              </p>
            </div>
            <button
              className="analyze-button"
              style={{ width: '100%', marginTop: '1.5rem' }}
              onClick={() => setShowSettings(false)}
            >
              Continue
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
