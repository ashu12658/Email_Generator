import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# ---------------- FACT COVERAGE ---------------- #
def fact_coverage(email: str, facts: list) -> float:
    if not facts:
        return 1.0

    email_lower = email.lower()
    matched = 0

    for fact in facts:
        fact_words = fact.lower().split()

        if all(word in email_lower for word in fact_words):
            matched += 1

    return matched / len(facts)


# ---------------- STRUCTURE SCORE ---------------- #
def structure_score(email: str) -> float:
    score = 0

    email_lower = email.lower()

    # Subject check
    if "subject:" in email_lower:
        score += 0.25

    # Body check (basic format indicator)
    if "dear" in email_lower or "hello" in email_lower:
        score += 0.25

    # Paragraph structure
    if email.count("\n\n") >= 1:
        score += 0.25

    # Closing check
    if any(word in email_lower for word in ["regards", "thanks", "sincerely"]):
        score += 0.25

    return score


# ---------------- GRAMMAR + FLUENCY SCORE ---------------- #
def grammar_score(email: str) -> float:
    score = 1.0
    text = email.lower()

    # repeated words penalty
    repeated = re.findall(r'\b(\w+)\s+\1\b', text)
    score -= len(repeated) * 0.1

    # missing punctuation
    if not re.search(r'[.!?]', email):
        score -= 0.2

    # long sentence penalty
    sentences = re.split(r'[.!?]', email)
    long_sentences = [s for s in sentences if len(s.split()) > 30]
    score -= len(long_sentences) * 0.1

    # too short email penalty
    if len(email.split()) < 30:
        score -= 0.2

    return max(0.0, min(1.0, score))


# ---------------- TONE SCORE (LLM JUDGE) ---------------- #
judge_model = ChatGroq(model="llama-3.1-8b-instant")

def tone_score(email: str, intent: str, tone: str) -> float:
    prompt = f"""
You are a strict evaluator for email quality.

Evaluate how well the email matches the required tone.

Required tone: {tone}
Intent: {intent}

Email:
{email}

Give a score from 0 to 10 based ONLY on tone accuracy.
Return only a number.
"""

    try:
        res = judge_model.invoke(prompt)
        return float(res.content.strip())
    except:
        return 0.0