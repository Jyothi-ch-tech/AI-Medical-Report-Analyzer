# 🏥 AI Medical Report Analyzer

## 📌 Overview

AI Medical Report Analyzer is a healthcare application that helps users understand their medical reports more easily. Users can upload a PDF medical report, and the system extracts the report content and generates a patient-friendly explanation using Google's Gemini AI.

The application simplifies complex medical information and provides insights in multiple languages, making healthcare information more accessible to everyone.

---

## ✨ Features

* 📄 Upload Medical Reports in PDF format
* 🔍 Automatic Text Extraction from reports
* 🤖 AI-Powered Medical Report Analysis
* 📊 Identification of Important Observations
* ⚠️ Detection of Abnormal Values
* 💡 Simple Patient-Friendly Explanations
* 🌐 Multi-Language Support

  * English
  * Hindi
  * Tamil
  * Telugu
  * Kannada
  * Malayalam
* 📥 Download Analysis Report

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini 1.5 Flash

### Libraries

* PyPDF2
* Google Generative AI
* Python Dotenv

---

## 📂 Project Structure

```text
AI-Medical-Report-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── sample_report.pdf
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Medical-Report-Analyzer.git
cd AI-Medical-Report-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Gemini API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. Upload a medical report PDF.
2. The application extracts report content using PyPDF2.
3. User selects the preferred language.
4. Gemini AI analyzes the report.
5. The system generates:

   * Summary
   * Important observations
   * Abnormal findings
   * Health recommendations
   * Patient-friendly explanations
6. User can download the generated analysis.

---

## 🎯 Sample Use Cases

* Understanding blood test reports
* Identifying abnormal health parameters
* Translating medical findings into regional languages
* Improving healthcare accessibility
* Assisting patients in understanding lab reports

---

## 🔮 Future Enhancements

* Disease Risk Prediction
* Health Dashboard & Visualizations
* OCR Support for Scanned Reports
* Medical Chatbot Integration
* Report History Tracking
* RAG-Based Healthcare Knowledge Assistant

---

## 📚 Learning Outcomes

* Generative AI Integration
* Prompt Engineering
* Healthcare AI Applications
* PDF Processing
* Streamlit Development
* Multi-Language AI Systems

---

## 👩‍💻 Author

**Jyothi**

BE Artificial Intelligence & Data Science

Chaitanya Bharathi Institute of Technology

