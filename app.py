import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Medical Report Analyzer")

st.title("🏥 AI Medical Report Analyzer")

uploaded_file = st.file_uploader(
    "Upload Medical Report (PDF)",
    type=["pdf"]
)

def extract_text(pdf_file):
    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

if uploaded_file:

    with st.spinner("Reading report..."):
        report_text = extract_text(uploaded_file)

    st.subheader("Extracted Report")

    st.text_area(
        "Report Content",
        report_text,
        height=250
    )

    if st.button("Analyze Report"):

        prompt = f"""
        You are a healthcare assistant.

        Analyze the medical report below.

        Provide:
        1. Summary
        2. Important observations
        3. Any abnormal values
        4. Simple explanation for a patient

        Medical Report:
        {report_text}
        """

        with st.spinner("Analyzing..."):

            response = model.generate_content(prompt)

            st.subheader("AI Analysis")

            st.write(response.text)