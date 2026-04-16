import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize model (Model B - stricter)
model = ChatGroq(model="llama-3.1-8b-instant")


def generate_email_v2(intent, facts, tone):
    """
    Generates a professional email using strict prompt constraints (Model B).
    """

    # Format facts properly
    facts_text = "\n".join([f"- {f}" for f in facts]) if facts else "None"

    prompt = f"""
You are a highly strict and detail-oriented corporate email writing expert.

Your task is to generate a professional email with maximum factual accuracy and structural consistency.

----------------------
### INPUT
Intent:
{intent}

Facts:
{facts_text}

Tone:
{tone}
----------------------

### HARD CONSTRAINTS (VERY IMPORTANT)
1. You MUST include ALL provided facts explicitly.
2. Each fact MUST be expressed as a clear, complete sentence.
3. No fact should be skipped, merged vaguely, or implied.
4. Do NOT introduce ANY new information beyond the given facts.
5. Do NOT assume context not present in input.

----------------------
### CONTROLLED WRITING RULES
- Maintain a strict {tone} tone throughout.
- Use clear, concise, and precise language.
- Avoid unnecessary elaboration or fluff.
- Avoid overly creative or expressive writing.

----------------------
### STRUCTURE (STRICT ENFORCEMENT)
The email MUST follow this exact format:

1. Subject line (specific to intent)
2. Greeting:
   - Use "Dear Hiring Team," or "Dear Sir/Madam,"
3. Body:
   - Paragraph 1: State purpose clearly
   - Paragraph 2: Include ALL facts (each fact clearly expressed)
   - Paragraph 3: Closing intent or expectation
4. Closing:
   - Polite and professional

----------------------
### LENGTH CONTROL
- Keep the email concise (100–130 words)
- Do NOT make it too long or overly descriptive

----------------------
### SIGNATURE RULE
- End strictly with:
  Best regards,
- Do NOT add any name or placeholder

----------------------
### SELF-VALIDATION STEP
Before final output, verify:
- All facts are present (100% coverage)
- No extra information is added
- Structure is strictly followed
- Tone is consistent

----------------------
### OUTPUT FORMAT (STRICT)

Subject: <one line subject>

Email:
<final email only>
"""

    response = model.invoke(prompt)
    return response.content


# -------------------------
# INTERACTIVE RUN (LIKE MODEL A)
# -------------------------
if __name__ == "__main__":
    intent_input = input("Enter intent: ")

    print("Enter facts (comma separated):")
    facts_raw = input()

    # Clean facts input
    facts_input = [
        f.strip() for f in facts_raw.split(",")
        if f.strip() and f.strip().lower() != "nothing"
    ]

    tone_input = input("Enter tone: ")

    print("\nDEBUG INPUT:")
    print(intent_input, facts_input, tone_input)

    email_output = generate_email_v2(
        intent_input,
        facts_input,
        tone_input
    )

    print("\nGenerated Email (Model B):\n")
    print(email_output)