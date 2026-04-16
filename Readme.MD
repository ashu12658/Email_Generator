# 🧠 AI Email Generation & Evaluation System

## 📌 Project Overview
This project is an AI-powered Email Generation Assistant that uses Large Language Models (LLMs) with advanced prompt engineering and a custom evaluation framework.

The system generates professional emails based on:
- Intent
- Key Facts
- Tone

It also evaluates output quality using custom-built metrics and compares two different prompting strategies (Model A vs Model B).

---

## 🚀 Features

### ✉️ Email Generation
- Converts structured input into professional emails
- Supports multiple tones (formal, professional, polite, etc.)
- Ensures all required facts are included

### 🧠 Prompt Engineering
- Role-based prompting (Model A)
- Constraint-based prompting with self-checks (Model B)
- Iterative improvement (A → B)

### 📊 Evaluation System
Custom metrics used:
- **Fact Coverage**
- **Structure Score**
- **Grammar & Fluency Score**
- **Tone Score (LLM-as-a-Judge)**

### ⚖️ Model Comparison
- Model A (baseline prompt)
- Model B (strict optimized prompt)
- Automated evaluation and comparison pipeline
- Stability analysis using variance

---

## 📊 Custom Metric Definitions

### 1. Fact Coverage Score
**Definition:**  
Measures whether all required input facts are included in the generated email.

**Logic:**
- Each fact is broken into keywords
- Email is converted to lowercase
- Checks if all keywords of each fact exist in the email
- Final score:

Fact Coverage = Matched Facts / Total Facts

**Range:** 0 to 1  
**Goal:** Ensure no critical information is missing

---

### 2. Structure Score
**Definition:**  
Evaluates whether the email follows proper professional formatting.

**Checks (each = 0.25):**
- Subject line present
- Greeting present (Dear/Hello)
- Paragraph structure (line breaks)
- Closing present (Regards/Thanks/Sincerely)

**Range:** 0 to 1  
**Goal:** Ensure professional readability and format

---

### 3. Grammar & Fluency Score
**Definition:**  
Evaluates linguistic quality using rule-based heuristics.

**Logic:**
- Starts from 1.0 score
- Applies penalties:
  - Repeated words → -0.1 each
  - Missing punctuation → -0.2
  - Long sentences (>30 words) → -0.1 each
  - Very short email → -0.2
- Final score clipped between 0 and 1

**Range:** 0 to 1  
**Goal:** Ensure readability and natural language quality

---

### 4. Tone Score (LLM-as-a-Judge)
**Definition:**  
Evaluates how well the email matches the requested tone.

**Logic:**
- Uses an LLM as evaluator
- Inputs:
  - Intended tone
  - Intent
  - Generated email
- Outputs score from 0–10

**Range:** 0 to 10  
**Goal:** Ensure correct emotional and professional tone

---

## 📂 Project Structure

email_generator/
│
├── generator.py # Model A (baseline)
├── generator_v2.py # Model B (improved prompt)
├── test_case.py # Benchmark dataset
├── metrics.py # Custom evaluation metrics
├── evaluate.py # Evaluation pipeline
├── comparison_results.csv # Model comparison output


---

## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install langchain-groq python-dotenv

2. Set API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here

3. Run Email Generator
python generator_v2.py
4. Run Evaluation
python evaluate.py

Model Comparison Results

| Metric        | Model A         | Model B        |
| ------------- | --------------- | -------------- |
| Fact Coverage | Moderate        | High           |
| Structure     | High            | High           |
| Grammar       | High            | High           |
| Tone          | Slightly better | Slightly rigid |
| Consistency   | Moderate        | High           |


🏆 Final Outcome

👉 Model B performs better overall

🎯 Key Learnings
Prompt engineering significantly impacts LLM performance
Strong constraints improve factual accuracy
Evaluation frameworks are critical for LLM systems
A/B testing helps optimize prompt design
Trade-off exists between fluency and correctness
📌 Tech Stack
Python
LangChain
Groq LLM
Prompt Engineering
Custom Evaluation Metrics
CSV-based analytics

🚀 Impact

This project demonstrates a production-style LLM evaluation pipeline with:

Automated scoring
Model comparison (A/B testing)
Stability analysis
Data-driven model selection

The system is extensible and can support additional models, metrics, and evaluation strategies.