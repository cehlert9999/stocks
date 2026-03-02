import streamlit as st
from translations import TRANSLATIONS

# Configuration
VERSION = "1.0.1"

# Initialize Session State for language
if "lang" not in st.session_state:
    st.session_state.lang = "de"

# Sidebar for Language Selection
st.sidebar.title(TRANSLATIONS[st.session_state.lang]["sidebar_title"])
lang_choice = st.sidebar.selectbox(
    TRANSLATIONS[st.session_state.lang]["language_select"],
    options=["Deutsch", "English"],
    index=0 if st.session_state.lang == "de" else 1
)

# Update session state based on selection
new_lang = "de" if lang_choice == "Deutsch" else "en"
if new_lang != st.session_state.lang:
    st.session_state.lang = new_lang
    st.rerun()

t = TRANSLATIONS[st.session_state.lang]
APP_TITLE = t["app_title"]

# Page config
st.set_page_config(page_title=APP_TITLE, page_icon="📈", layout="centered")

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
    }
    .stSelectbox > div > div > div {
        background-color: #1e293b;
        color: white;
    }
    h1 {
        color: #60a5fa;
    }
    </style>
    """, unsafe_allow_html=True)

# Prompts Data from Translations
PROMPTS = t["prompts"]

st.sidebar.markdown(f"**{t['version']}:** {VERSION}")

# Main UI
st.title(t["main_title"])
st.markdown(f"*{t['slogan']}*")
st.markdown(t["main_subtitle"])

# Help Section
with st.expander(t["help_title"], expanded=False):
    st.markdown(t["help_intro"])
    st.markdown(f"**{t['strategy_expl_title']}**")
    for title, expl in t["strategy_explanations"].items():
        st.markdown(f"- **{title}**: {expl}")

# Ticker and Strategy Selection
ticker = st.text_input(t["ticker_label"], placeholder=t["ticker_placeholder"]).upper()
if st.button(t["apply_button"], use_container_width=True):
    pass # Streamlit reruns on interaction anyway, but button provides clear action

# Optional Context
with st.expander(t["optional_context"], expanded=False):
    period = st.text_input(t["period_label"], placeholder=t["period_placeholder"])
    transcript = st.text_area(t["transcript_label"], placeholder=t["transcript_placeholder"], height=150)

strategy_titles = [p["title"] for p in PROMPTS]
selected_title = st.selectbox(t["strategy_label"], strategy_titles)

# Get selected prompt
selected_prompt_data = next(p for p in PROMPTS if p["title"] == selected_title)
base_prompt = selected_prompt_data["prompt"].replace("[TICKER]", ticker if ticker else "[TICKER]")

# Dynamic Prompt Construction
final_prompt = base_prompt

if period:
    final_prompt = f"{t['period_prefix']}{period}\n\n" + final_prompt

if transcript:
    final_prompt = f"{t['transcript_prefix']}{transcript}{t['transcript_suffix']}" + final_prompt

# Display Prompt
st.subheader(t["your_prompt"])

# Custom Copy Button using HTML/JS for prominence and mobile-friendliness
copy_button_html = f"""
    <div id="copy-container" style="margin-bottom: 20px;">
        <button id="copy-btn" style="
            width: 100%;
            padding: 15px;
            background: linear-gradient(to right, #3b82f6, #8b5cf6);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: transform 0.1s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        " onclick="copyPrompt()">
            <span>{t['copy_button']}</span>
        </button>
    </div>

    <script>
    function copyPrompt() {{
        const text = `{final_prompt.replace('`', '\\`').replace('$', '\\$')}`;
        navigator.clipboard.writeText(text).then(function() {{
            const btn = document.getElementById('copy-btn');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span>{t['copied_button']}</span>';
            btn.style.background = '#10b981';
            setTimeout(function() {{
                btn.innerHTML = originalText;
                btn.style.background = 'linear-gradient(to right, #3b82f6, #8b5cf6)';
            }}, 2000);
        }}, function(err) {{
            console.error('Could not copy text: ', err);
        }});
    }}
    </script>
"""
st.components.v1.html(copy_button_html, height=80)

# Also show the code for manual selection if needed
st.code(final_prompt, language="markdown")

st.info(t["info_msg"])
