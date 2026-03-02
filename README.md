# Stock Analysis Suite

A collection of tools for professional equity research, using high-performance prompts and AI models.

## Available Tools

### 1. StockVision (React App)
A premium dashboard for deep-dive analysis using the Kimi K2.5 model via Fireworks.ai.
- **Features**: AI Analysis, Ticker Lookup, Strategy Search, Copy-to-Clipboard.
- **Run**: `./start.sh` (Starts the Vite dev server on port 5173).

### 2. Prompt Generator (Streamlit App)
A simplified, password-protected tool optimized for copying prompts to other LLMs like ChatGPT, Claude, or Grok.
- **Features**: Password protection, easy copy-to-clipboard, zero-configuration.
- **Run**: `streamlit run streamlit_app.py`
- **Password**: `stocks-research`

## Project Structure
- `spec/prompts/prompts.md`: Source of the 10 professional equity research prompts.
- `spec/constitution.md`: Core principles for code quality and testing.
- `streamlit_app.py`: Self-contained Streamlit application.
- `src/`: React source code for the main web app.

## Setup
1. Clone the repository.
2. Install dependencies:
   - React: `npm install`
   - Streamlit: `pip install streamlit`
3. Running:
   - React: `./start.sh`
   - Streamlit: `streamlit run streamlit_app.py`
