🧠 AI Email Generation & Evaluation System
📌 Project Overview

This project is an LLM-powered Email Generation system that generates professional emails from structured inputs and evaluates output quality using a custom evaluation framework.

It compares two prompting strategies:

Model A (Baseline Prompt)
Model B (Strict Constraint-Based Prompt)

The system performs automated A/B testing using custom metrics and selects the best-performing model.

🏗️ System Architecture
Test Cases (10 Scenarios)
        ↓
Evaluation Pipeline (evaluate.py)
        ↓
Model A & Model B Execution
        ↓
Generated Emails
        ↓
Metrics Engine
        ↓
Score Aggregation
        ↓
CSV Output
        ↓
Final Model Comparison

🚀 Features

✉️ Email Generation
Converts structured input into professional emails
Supports multiple tones (formal, polite, urgent, empathetic)
Ensures all required facts are included

🧠 Prompt Engineering
Model A → Flexible baseline prompt
Model B → Strict constraint-driven prompt with self-check logic

📊 Evaluation System

Evaluates outputs using 4 metrics:
Fact Coverage Score (0–1)
Structure Score (0–1)
Grammar & Fluency Score (0–1)
Tone Score (0–10, LLM judge)

⚖️ Model Comparison
Same dataset for both models
Identical evaluation pipeline
Final decision based on average score

📊 Custom Metric Definitions
1. Fact Coverage Score

Ensures all input facts are included in the generated email.

Formula:

Fact Coverage = Matched Facts / Total Facts

Range: 0 to 1

2. Structure Score

Checks proper email formatting.

Criteria (0.25 each):

Subject line
Greeting
Paragraph structure
Closing statement

Range: 0 to 1

3. Grammar & Fluency Score

Rule-based evaluation of language quality.

Penalties:

Repeated words (-0.1)
Missing punctuation (-0.2)
Long sentences (-0.1 each)
Short email (-0.2)

Final score normalized between 0 and 1.

4. Tone Score (LLM-as-a-Judge)

Evaluates tone alignment using an LLM.

Input:

Intent
Tone
Generated email

Output:

Score (0–10)
📂 Project Structure
email_generator/
│
├── generator.py          # Model A
├── generator_v2.py       # Model B
├── test_case.py          # 10 test scenarios
├── metrics.py            # Evaluation metrics
├── evaluate.py           # Main evaluation pipeline
├── comparison_results.csv# Output results
└── .env                  # API keys (not pushed)

⚙️ How to Run
1. Install dependencies
pip install langchain-groq python-dotenv numpy
2. Create .env file
GROQ_API_KEY=your_api_key_here
3. Run evaluation (MAIN COMMAND)
python evaluate.py

This will:

Run Model A + Model B
Evaluate all test cases
Apply custom metrics
Generate CSV output
Print final comparison

📊 Results Summary
| Metric        | Model A  | Model B        |
| ------------- | -------- | -------------- |
| Fact Coverage | Moderate | High           |
| Structure     | High     | High           |
| Grammar       | High     | High           |
| Tone          | Better   | Slightly rigid |
| Consistency   | Moderate | High           |


🏆 Final Outcome

👉 Model B is recommended for production

Reasons:

Higher factual accuracy
Strong constraint adherence
Consistent outputs
Better reliability in structured tasks

🎯 Key Learnings
Prompt engineering directly impacts LLM performance
Strong constraints improve factual correctness
Evaluation frameworks are essential for LLM systems
A/B testing enables data-driven model selection
Trade-off exists between fluency and accuracy
