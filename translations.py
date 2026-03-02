# translations.py

TRANSLATIONS = {
    "de": {
        "app_title": "Stock Analysis Prompt Tool",
        "sidebar_title": "App-Einstellungen",
        "version": "Version",
        "language_select": "Sprache wählen",
        "main_title": "🚀 Aktien-Analyse",
        "main_subtitle": "Generiere Prompts für deine bevorzugte KI.",
        "ticker_label": "Aktien-Ticker",
        "ticker_placeholder": "z.B. NVDA, AAPL",
        "optional_context": "➕ Optional: Kontext hinzufügen (Transkript / Zeitraum)",
        "period_label": "Quartal / Jahr",
        "period_placeholder": "z.B. Q4 2023",
        "transcript_label": "Earnings-Transkript oder News-Daten",
        "transcript_placeholder": "Text hier einfügen...",
        "strategy_label": "Strategie wählen",
        "your_prompt": "Dein Prompt",
        "copy_button": "📋 Für KI kopieren",
        "copied_button": "✅ Kopiert!",
        "info_msg": "💡 Tippe auf 'Für KI kopieren' und füge es direkt in deinen Chat ein.",
        "slogan": "Der sen. Stock Analyst für die Hosentasche und fast gratis",
        "help_title": "ℹ️ Hilfe / Was kann dieses Tool?",
        "help_intro": "Dieses Tool generiert hochspezialisierte Prompts für KI-Modelle (wie ChatGPT, Claude oder Perplexity), um Aktien tiefgreifend zu analysieren. Wähle eine Strategie, gib den Ticker ein und kopiere den Prompt.",
        "strategy_expl_title": "💡 Die Strategien erklärt:",
        "strategy_explanations": {
            "Deep Dive Business Breakdown": "Analysiert das Geschäftsmodell wie ein Käufer. Fokus auf Umsatzströme, Gräben (Moats) und Risiken. Warum sollte man NICHT kaufen?",
            "Earnings Call Übersetzer": "Filtert 'Corporate Speak' aus Quartalsberichten. Was hat das Management wirklich gesagt? Was wurde verschwiegen?",
            "Competitive Moat Audit": "Hinterfragt den Wettbewerbsvorteil (Moat) kritisch auf einer Skala von 1-10.",
            "Bull/Bear Steelman": "Erstellt das stärkstmögliche Szenario für beide Seiten, um Confirmation Bias (Bestätigungsfehler) zu vermeiden.",
            "Sektor/Themen-Mapper": "Erstellt eine Landkarte für ganze Sektoren. Wer sind die echten Player?",
            "Bewertungs-Check": "Prüft, ob der Preis durch Qualität oder Hype gerechtfertigt ist. Kein trockenes DCF, sondern ein Zahlen-Check.",
            "10-K / Filing Decoder": "Findet Warnsignale in den langen SEC-Berichten, die andere übersehen.",
            "Catalyst Timeline Builder": "Erstellt einen Zeitplan für die wichtigsten Ereignisse der nächsten 6-12 Monate.",
            "Portfolio Overlap Detector": "Findet versteckte Klumpenrisiken und Korrelationen in deinen Positionen.",
            "Investment Thesis One-Pager": "Schreibt eine klare Begründung für dein Investment – wichtig für Disziplin bei fallenden Kursen."
        },
        "transcript_prefix": "--- UNTERLAGEN / TRANSKRIPT ---\n",
        "transcript_suffix": "\n--- ENDE UNTERLAGEN ---\n\nBasierend auf den oben genannten Unterlagen: ",
        "period_prefix": "Zielzeitraum: ",
        "prompts": [
            {
                "title": "Deep Dive Business Breakdown",
                "prompt": """Analysiere das Geschäftsmodell von [TICKER] aus der Sicht eines potenziellen Käufers, der das Unternehmen bewertet:

- Wie verdient dieses Unternehmen tatsächlich Geld? Gehe jeden Umsatzstrom und seinen Prozentsatz am Gesamtumsatz durch.
- Wie ist die Wachstumstrajektorie jedes Segments?
- Gegen wen treten sie an und was ist ihr verteidigungsfähiger Vorteil (Moat)?
- Was müsste schiefgehen, damit dieses Unternehmen in 5 Jahren irrelevant ist?
- Was ist das größte Einzelrisiko, das der Markt derzeit möglicherweise unterbewertet?

Gib mir keinen ausgewogenen Unternehmensüberblick. Gib mir die Version, in der du versuchst, Gründe zu finden, dieses Unternehmen NICHT zu kaufen."""
            },
            {
                "title": "Earnings Call Übersetzer",
                "prompt": """Übersetze das "Corporate Speak" von [TICKER] in einfaches Deutsch:

- Wozu hat sich das Management tatsächlich verpflichtet im Gegensatz zu vagen Ausflüchten?
- Wo sind sie Analystenfragen ausgewichen oder haben keine wirklichen Antworten gegeben?
- Welche Prognosen (Forward Guidance) sind wirklich neue Informationen im Vergleich zu neu verpackten alten Zielen?
- Worüber sprechen sie NICHT, was sie wahrscheinlich tun sollten?
- Wenn ich mir nur 3 Dinge aus diesem Call merken könnte, was ist für die Aktie in den nächsten 12 Monaten am wichtigsten?"""
            },
            {
                "title": "Competitive Moat Audit",
                "prompt": """Bewerten den Wettbewerbsvorteil (Moat) von [TICKER]. Sei skeptisch, nicht großzügig.

Bewerte jeden Moat-Faktor auf einer Skala von 1-10 mit spezifischen Belegen:

- Wechselkosten: Wie schmerzhaft ist es für Kunden, zu wechseln?
- Netzwerkeffekte: Wird das Produkt besser, je mehr Menschen es nutzen?
- Kostenvorteile: Können sie Konkurrenten nachhaltig unterbieten?
- Markenmacht: Zahlen Kunden einen Aufpreis speziell für diesen Namen?
- Regulatorische oder IP-Barrieren: Was hält neue Marktteilnehmer fern?
- Datenvorteile: Verfügen sie über proprietäre Daten, die sich mit der Zeit summieren?

Beantworte dann: Wird dieser Moat breiter oder schmaler? Was sind die Belege für die jeweilige Richtung?"""
            },
            {
                "title": "Bull/Bear Steelman",
                "prompt": """Erstelle zuerst das stärkstmögliche Bear-Case-Szenario gegen [TICKER]. Nicht die offensichtlichen Risiken, sondern jene, die mich tatsächlich zum Verkauf bewegen würden. Denke wie ein Shortseller, der 6 Monate recherchiert hat.

Erstelle dann das stärkstmögliche Bull-Case-Szenario. Ein ANDERES Bull-Case-Szenario, das ich vielleicht nicht sehe.

Sag mir abschließend: Welcher Datenpunkt oder welches Ereignis würde die These definitiv als richtig oder falsch erweisen? Worauf sollte ich achten?"""
            },
            {
                "title": "Sektor/Themen-Mapper",
                "prompt": """Skizziere die Investitionslandschaft im Bereich [SECTOR/THEME] für [TICKER].

- Wer sind die Hauptakteure und was ist der spezifische Ansatz jedes einzelnen?
- Welche Unternehmen sind reine Wetten (Pure-Play) vs. diversifizierte Unternehmen mit Engagement in diesem Bereich?
- Wo liegt der Marktkonsens und wo habe ich die Chance, frühzeitig dabei zu sein?
- Wie hoch ist der TAM (Total Addressable Market) und wächst er tatsächlich, oder ist diese Zahl aus einem Pitch-Deck von 2021 recycelt?
- Was sind die Risiken für das gesamte Thema, nicht nur für einzelne Aktien?
- Wenn ich nur 3 Namen besitzen könnte, um diesen Trend in den nächsten 3-5 Jahren abzubilden, welche 3 wären das und warum?

Sei spezifisch mit Tickern. Ich möchte keinen Lehrbuch-Überblick, sondern eine umsetzbare Karte."""
            },
            {
                "title": "Bewertungs-Check",
                "prompt": """Hilf mir herauszufinden, ob ich für [TICKER] zu viel bezahle.

- Was sind die relevantesten Bewertungskennzahlen für DIESE Art von Unternehmen?
- Wie schneidet die aktuelle Bewertung im Vergleich zur eigenen historischen 3- und 5-Jahres-Spanne ab?
- Wie schneidet sie im Vergleich zu den engsten Mitbewerbern ab?
- Welche Wachstumsrate impliziert der aktuelle Preis? Fühlt sich das basierend auf der tatsächlichen Entwicklung des Unternehmens realistisch an?
- Zu welchem Preis wäre diese Aktie ein offensichtliches Schnäppchen? Ab welchem Preis ist sie offensichtlich teuer?
- Zahle ich einen Aufpreis für Hype oder für echte Qualität?

Ich brauche kein DCF-Modell. Ich brauche einen Bauchgefühl-Check, der durch Zahlen gestützt wird."""
            },
            {
                "title": "10-K / Filing Decoder",
                "prompt": """Extrahiere die Informationen, die aus den neuesten Berichten von [TICKER] tatsächlich wichtig sind:

- Was ist in den Risikofaktoren vergraben, die die meisten Anleger überfliegen?
- Gibt es Warnsignale bei der Umsatzrealisierung, Rechnungslegungsänderungen oder Transaktionen mit nahestehenden Personen?
- Was verrät mir die Kapitalflussrechnung, was die Gewinn- und Verlustrechnung verbirgt?
- Erzählen Insidertransaktionen oder aktienbasierte Vergütungen eine andere Geschichte als der Earnings Call?
- Was hat sich im Vergleich zum VORHERIGEN Bericht geändert? Was wurde hinzugefügt, entfernt oder umformuliert?

Konzentriere dich auf das Ungewöhnliche oder das, was sich geändert hat. Den Standardtext kann ich selbst lesen."""
            },
            {
                "title": "Catalyst Timeline Builder",
                "prompt": """Erstelle einen Zeitplan für Katalysatoren für [TICKER] über die nächsten 6-12 Monate.

Für jeden Katalysator:
- Was ist das Ereignis und das ungefähre Datum?
- Was ist das Bull-Case-Ergebnis im Vergleich zum Bear-Case-Ergebnis?
- Wie ist der Markt derzeit dafür positioniert?
- Wie wichtig ist es auf einer Skala von 1-10 für den Aktienkurs?

Berücksichtige: Earnings-Termine, Produkteinführungen, regulatorische Entscheidungen, Vertragsankündigungen, Branchenkonferenzen, Wettbewerberereignisse, die die Aktie beeinflussen könnten, und Makrofaktoren, die speziell diesen Namen betreffen."""
            },
            {
                "title": "Portfolio Overlap Detector",
                "prompt": """Sag mir, was ich über [TICKER] in meinem Portfolio nicht sehe:

- Welche dieser Aktien würden in einem breiten Ausverkauf alle zusammen fallen? Gruppiere sie nach Korrelation.
- Gehe ich dieselbe Wette mehrmals ein, ohne es zu merken?
- Wo bin ich geografisch oder sektoral konzentriert?
- Welche Position ist am anfälligsten für einen einzelnen Risikofaktor (Zinsen, Regulierung, ein einziger Kunde)?
- Wenn ich 2 Positionen streichen müsste, um das Risiko zu senken, ohne das Aufwärtspotenzial zu verringern, welche 2 wären das und warum?"""
            },
            {
                "title": "Investment Thesis One-Pager",
                "prompt": """Hilf mir, eine prägnante Investmentthese für [TICKER] zu schreiben, auf die ich mich beziehen kann, wenn die Aktie fällt und ich in Versuchung gerate, in Panik zu verkaufen.

Struktur:
- Die These in 2 Sätzen. Warum ich das besitze.
- 3 Dinge, die wahr bleiben müssen, damit die These Bestand hat.
- 3 Dinge, die die These brechen und einen Ausstieg auslösen würden.
- Meine angestrebte Haltedauer.
- Was ich in den nächsten 12 Monaten erwarte.
- Was ich tun würde, wenn die Aktie morgen um 20% fällt (nachkaufen, halten oder verkaufen - und warum).

Schreibe es in meinem Stil. Direkt. Ohne Absicherung. Das ist für mich, nicht für einen Forschungsbericht."""
            }
        ]
    },
    "en": {
        "app_title": "Stock Analysis Prompt Tool",
        "sidebar_title": "App Settings",
        "version": "Version",
        "language_select": "Select Language",
        "main_title": "🚀 Stock Analysis",
        "main_subtitle": "Generate prompts for your favorite AI.",
        "ticker_label": "Stock Ticker",
        "ticker_placeholder": "e.g. NVDA, AAPL",
        "optional_context": "➕ Optional: Add Context (Transcript / Period)",
        "period_label": "Quarter / Year",
        "period_placeholder": "e.g. Q4 2023",
        "transcript_label": "Earnings Transcript or News Data",
        "transcript_placeholder": "Paste text here...",
        "strategy_label": "Select Strategy",
        "your_prompt": "Your Prompt",
        "copy_button": "📋 Copy for AI",
        "copied_button": "✅ Copied!",
        "info_msg": "💡 Tap 'Copy for AI' and paste it directly into your chat.",
        "slogan": "The Senior Stock Analyst in your pocket - at almost no cost",
        "help_title": "ℹ️ Help / What can this tool do?",
        "help_intro": "This tool generates high-end prompts for AI models (like ChatGPT, Claude, or Perplexity) to analyze stocks in-depth. Select a strategy, enter the ticker, and copy the prompt.",
        "strategy_expl_title": "💡 Strategies explained:",
        "strategy_explanations": {
            "Deep Dive Business Breakdown": "Breaks down the business model from a buyer's perspective. Focus on moats, risks, and reasons NOT to buy.",
            "Earnings Call Translator": "Decodes 'Corporate Speak' from quarterly reports. What was actually committed vs. deflected?",
            "Competitive Moat Audit": "Critically evaluates competitive advantages on a scale of 1-10.",
            "Bull/Bear Steelman": "Builds the strongest possible case for both sides to avoid confirmation bias.",
            "Sector/Theme Mapper": "Maps out entire investment themes. Who are the pure-plays vs. diversified players?",
            "Valuation Sanity Check": "Checks if the price is justified by quality or hype. A gut check backed by numbers.",
            "10-K / Filing Decoder": "Unearths red flags in long SEC filings that most investors miss.",
            "Catalyst Timeline Builder": "Builds a timeline of the most important events for the next 6-12 months.",
            "Portfolio Overlap Detector": "Identifies hidden concentration risks and correlations in your holdings.",
            "Investment Thesis One-Pager": "Writes a concise investment thesis to keep you disciplined during market volatility."
        },
        "transcript_prefix": "--- DOCUMENTS / TRANSCRIPT ---\n",
        "transcript_suffix": "\n--- END OF DOCUMENTS ---\n\nBased on the documents above: ",
        "period_prefix": "Target Period: ",
        "prompts": [
            {
                "title": "Deep Dive Business Breakdown",
                "prompt": """Break down [TICKER]'s business model like I'm a potential acquirer evaluating the company:

- How does this company actually make money? Walk through each revenue stream and its percentage of total revenue
- What's the growth trajectory of each segment?
- Who are they competing against, and what's their defensible advantage?
- What would have to go wrong for this company to be irrelevant in 5 years?
- What's the single biggest risk the market might be underpricing right now?

Don't give me a balanced corporate overview. Give me the version where you're trying to find reasons NOT to buy this company."""
            },
            {
                "title": "Earnings Call Translator",
                "prompt": """Translate the corporate speak into plain English for [TICKER]:

- What did management actually commit to vs what was vague deflection?
- Where did they dodge analyst questions or give non-answers?
- What forward guidance is genuinely new information vs repackaged old targets?
- What are they NOT talking about that they probably should be?
- If I could only remember 3 things from this call, what matters most for the stock over the next 12 months?"""
            },
            {
                "title": "Competitive Moat Audit",
                "prompt": """Evaluate [TICKER]'s competitive moat. Be skeptical, not generous.

Rate each moat factor 1-10 with specific evidence:

- Switching costs: how painful is it for customers to leave?
- Network effects: does the product get better as more people use it?
- Cost advantages: can they undercut competitors sustainably?
- Brand power: do customers pay a premium specifically for this name?
- Regulatory or IP barriers: what keeps new entrants out?
- Data advantages: do they have proprietary data that compounds over time?

Then answer: is this moat widening or narrowing? What's the evidence for each direction?"""
            },
            {
                "title": "Bull/Bear Steelman",
                "prompt": """First, make the strongest possible bear case against [TICKER]. Not the obvious risks. The ones that would actually make me sell. Think like a short seller who's done 6 months of research.

Then make the strongest possible bull case. A DIFFERENT bull case I might not be seeing.

Finally, tell me: what's the one data point or event that would definitively prove the thesis right or wrong? What should I be watching?"""
            },
            {
                "title": "Sector/Theme Mapper",
                "prompt": """Map out the [SECTOR/THEME] investment landscape for [TICKER].

- Who are the major players and what's each one's specific angle?
- Which companies are the pure-play bets vs diversified businesses with exposure?
- Where's the market consensus and where do I have an opportunity to be early?
- What's the TAM and is it actually growing or is that number recycled from a 2021 pitch deck?
- What are the risks to the entire theme, not just individual stocks?
- If I could only own 3 names to capture this trend over the next 3-5 years, which 3 and why?

Be specific with tickers. I don't want a textbook overview. I want an actionable map."""
            },
            {
                "title": "Valuation Sanity Check",
                "prompt": """Help me figure out if I'm paying too much for [TICKER].

- What are the most relevant valuation metrics for THIS type of business?
- How does the current valuation compare to its own 3 and 5 year historical range?
- How does it compare to its closest peers?
- What growth rate is the current price implying? Does that feel realistic based on the company's actual trajectory?
- At what price would this stock be an obvious bargain? At what price is it obviously expensive?
- Am I paying a premium for hype or for genuine quality?

I don't need a DCF model. I need a gut check backed by numbers."""
            },
            {
                "title": "10-K / Filing Decoder",
                "prompt": """Pull out the information that actually matters from [TICKER]'s latest filings:

- What's buried in the risk factors that most investors skim past?
- Any red flags in revenue recognition, accounting changes, or related party transactions?
- What does the cash flow statement tell me that the income statement is hiding?
- Are insider transactions or equity compensation telling a different story than the earnings call?
- What changed from the PREVIOUS filing? What did they add, remove, or reword?

Focus on what's unusual or what changed. I can read the standard boilerplate myself."""
            },
            {
                "title": "Catalyst Timeline Builder",
                "prompt": """Build a catalyst timeline for [TICKER] over the next 6-12 months.

For each catalyst:
- What's the event and approximate date?
- What's the bull case outcome vs bear case outcome?
- How is the market currently positioned for it?
- How significant is it, on a scale of 1-10, for the stock price?

Include: earnings dates, product launches, regulatory decisions, contract announcements, industry conferences, competitor events that could impact the stock, and macro factors that specifically affect this name."""
            },
            {
                "title": "Portfolio Overlap Detector",
                "prompt": """Tell me what I can't see about [TICKER] in my portfolio:

- Which of these stocks would all drop together in a broad selloff? Group them by correlation
- Am I making the same bet multiple times without realizing it?
- Where am I geographically or sector concentrated?
- Which position is most vulnerable to a single risk factor (rates, regulation, one customer)?
- If I had to cut 2 positions to reduce risk without reducing upside potential, which 2 and why?"""
            },
            {
                "title": "Investment Thesis One-Pager",
                "prompt": """Help me write a tight investment thesis for [TICKER] that I can reference whenever the stock drops and I'm tempted to panic sell.

Structure:
- The thesis in 2 sentences. Why I own this.
- 3 things that must stay true for the thesis to hold
- 3 things that would break the thesis and trigger an exit
- My target hold period
- What I expect to happen in the next 12 months
- What I'd do if the stock drops 20% tomorrow (buy more, hold, or sell - and why)

Write it in my voice. Direct. No hedging. This is for me, not for a research report."""
            }
        ]
    }
}
