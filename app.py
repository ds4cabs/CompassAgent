'''
Compass agent app using streamlit (VERY EPIC)
'''

import streamlit as st
from cv_parser import extract_text, match_keywords
from agent import generate_briefing
from export import export_briefing


#Customization stuff
st.set_page_config(
    page_title="CompassAgent",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('Compass Agent DashBoard📊')
st.caption("Upload your CV file(PDF or DOCX)")

#st.sidebar.header("Filters")

'''
HTML code for styling the dashboard
'''

st.markdown("""
<div style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-bottom: 20px;">
     Welcome to the Dashboard 😀
    <p style="margin:5px 0 0 0; opacity:0.8;">Real-time analysis at your command</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a file", type = ["pdf", "docx"])
location = st.text_input("Enter the desired location for your job")
generate_clicked = st.button("Generate briefing")

# Check if a file has been uploaded
if uploaded_file is not None:
    text = extract_text(uploaded_file)
    hits = match_keywords(text)
    st.write(hits)

    if generate_clicked:
        briefing = generate_briefing(hits, location)
        st.write(briefing)
        filepath = export_briefing(briefing, "testuser")
        st.write(f"Saved to {filepath}")