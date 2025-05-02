import streamlit as st
from transformers import pipeline


# Set page config and custom styling
st.set_page_config(page_title="Text Summarizer", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg,rgb(69, 173, 243) 0%,rgb(56, 153, 233) 100%);
    }
    .stTextArea textarea, 
    .stTextArea textarea:focus,
    .stTextArea textarea:hover {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border: 2px solid #764ba2 !important;
        color: #000000 !important;
    }
    .stTextArea textarea::placeholder {
        color: #666666 !important;
    }
    .stTextArea label {
        color: #ffffff !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #FF6B6B 0%, #FF8E53 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #FF8E53 0%, #FF6B6B 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .stSlider {
        background-color: rgba(228, 228, 228, 0.95);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #764ba2;
    }
    .stSlider label {
        color: #000000 !important;
    }
    .stSlider p {
        color: #000000 !important;
    }
    .stSlider [data-testid="stMarkdown"] {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📝 Text Summarizer using Hugging Face Transformers")

# User input
text = st.text_area("Paste your long text below to summarize:", height=200)

# Summary length selector
summary_length = st.slider(
    "Select summary length:",
    min_value=30,
    max_value=250,
    value=100,
    step=10,
    help="Choose the length of your summary"
)

# Load summarizer without caching
if 'summarizer' not in st.session_state:
    st.session_state.summarizer = pipeline("summarization")

if st.button("Summarize Text"):
    if text.strip():
        with st.spinner("Summarizing..."):
            summary = st.session_state.summarizer(
                text,
                max_length=summary_length,
                min_length=30,
                do_sample=False
            )
            st.success("Here's your summary:")
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
                          padding: 20px; 
                          border-radius: 10px; 
                          box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                          color: #2d3436;
                          font-weight: 500;'>
                    {summary[0]['summary_text']}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to summarize.")
