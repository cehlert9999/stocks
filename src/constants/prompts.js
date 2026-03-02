export const PROMPTS = [
  {
    id: 1,
    title: "Deep Dive Business Breakdown",
    prompt: `Break down [TICKER]'s business model like I'm a potential acquirer evaluating the company:

- How does this company actually make money? Walk through each revenue stream and its percentage of total revenue
- What's the growth trajectory of each segment?
- Who are they competing against, and what's their defensible advantage?
- What would have to go wrong for this company to be irrelevant in 5 years?
- What's the single biggest risk the market might be underpricing right now?

Don't give me a balanced corporate overview. Give me the version where you're trying to find reasons NOT to buy this company.`
  },
  {
    id: 2,
    title: "Earnings Call Translator",
    prompt: `Translate the corporate speak into plain English for [TICKER]:

- What did management actually commit to vs what was vague deflection?
- Where did they dodge analyst questions or give non-answers?
- What forward guidance is genuinely new information vs repackaged old targets?
- What are they NOT talking about that they probably should be?
- If I could only remember 3 things from this call, what matters most for the stock over the next 12 months?`
  },
  {
    id: 3,
    title: "Competitive Moat Audit",
    prompt: `Evaluate [TICKER]'s competitive moat. Be skeptical, not generous.

Rate each moat factor 1-10 with specific evidence:

- Switching costs: how painful is it for customers to leave?
- Network effects: does the product get better as more people use it?
- Cost advantages: can they undercut competitors sustainably?
- Brand power: do customers pay a premium specifically for this name?
- Regulatory or IP barriers: what keeps new entrants out?
- Data advantages: do they have proprietary data that compounds over time?

Then answer: is this moat widening or narrowing? What's the evidence for each direction?`
  },
  {
    id: 4,
    title: "Bull/Bear Steelman",
    prompt: `First, make the strongest possible bear case against [TICKER]. Not the obvious risks. The ones that would actually make me sell. Think like a short seller who's done 6 months of research.

Then make the strongest possible bull case. A DIFFERENT bull case I might not be seeing.

Finally, tell me: what's the one data point or event that would definitively prove the thesis right or wrong? What should I be watching?`
  },
  {
    id: 5,
    title: "Sector/Theme Mapper",
    prompt: `Map out the [SECTOR/THEME] investment landscape for [TICKER].

- Who are the major players and what's each one's specific angle?
- Which companies are the pure-play bets vs diversified businesses with exposure?
- Where's the market consensus and where do I have an opportunity to be early?
- What's the TAM and is it actually growing or is that number recycled from a 2021 pitch deck?
- What are the risks to the entire theme, not just individual stocks?
- If I could only own 3 names to capture this trend over the next 3-5 years, which 3 and why?

Be specific with tickers. I don't want a textbook overview. I want an actionable map.`
  },
  {
    id: 6,
    title: "Valuation Sanity Check",
    prompt: `Help me figure out if I'm paying too much for [TICKER].

- What are the most relevant valuation metrics for THIS type of business?
- How does the current valuation compare to its own 3 and 5 year historical range?
- How does it compare to its closest peers?
- What growth rate is the current price implying? Does that feel realistic based on the company's actual trajectory?
- At what price would this stock be an obvious bargain? At what price is it obviously expensive?
- Am I paying a premium for hype or for genuine quality?

I don't need a DCF model. I need a gut check backed by numbers.`
  },
  {
    id: 7,
    title: "10-K / Filing Decoder",
    prompt: `Pull out the information that actually matters from [TICKER]'s latest filings:

- What's buried in the risk factors that most investors skim past?
- Any red flags in revenue recognition, accounting changes, or related party transactions?
- What does the cash flow statement tell me that the income statement is hiding?
- Are insider transactions or equity compensation telling a different story than the earnings call?
- What changed from the PREVIOUS filing? What did they add, remove, or reword?

Focus on what's unusual or what changed. I can read the standard boilerplate myself.`
  },
  {
    id: 8,
    title: "Catalyst Timeline Builder",
    prompt: `Build a catalyst timeline for [TICKER] over the next 6-12 months.

For each catalyst:
- What's the event and approximate date?
- What's the bull case outcome vs bear case outcome?
- How is the market currently positioned for it?
- How significant is it, on a scale of 1-10, for the stock price?

Include: earnings dates, product launches, regulatory decisions, contract announcements, industry conferences, competitor events that could impact the stock, and macro factors that specifically affect this name.`
  },
  {
    id: 9,
    title: "Portfolio Overlap Detector",
    prompt: `Tell me what I can't see about [TICKER] in my portfolio:

- Which of these stocks would all drop together in a broad selloff? Group them by correlation
- Am I making the same bet multiple times without realizing it?
- Where am I geographically or sector concentrated?
- Which position is most vulnerable to a single risk factor (rates, regulation, one customer)?
- If I had to cut 2 positions to reduce risk without reducing upside potential, which 2 and why?`
  },
  {
    id: 10,
    title: "Investment Thesis One-Pager",
    prompt: `Help me write a tight investment thesis for [TICKER] that I can reference whenever the stock drops and I'm tempted to panic sell.

Structure:
- The thesis in 2 sentences. Why I own this.
- 3 things that must stay true for the thesis to hold
- 3 things that would break the thesis and trigger an exit
- My target hold period
- What I expect to happen in the next 12 months
- What I'd do if the stock drops 20% tomorrow (buy more, hold, or sell - and why)

Write it in my voice. Direct. No hedging. This is for me, not for a research report.`
  }
];
