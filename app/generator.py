import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize model
model = ChatGroq(model='llama-3.3-70b-versatile')


def build_prompt(intent, facts, tone):
    """Formats the input into a structured instruction for the LLM."""

    facts_text = "\n".join([f"- {fact}" for fact in facts]) if facts else "None"

    prompt = f"""
    You are a senior corporate communication expert with extensive experience in writing high-quality professional emails.

    Your task is to generate a clear, natural, and well-structured email based ONLY on the provided inputs.

    ----------------------
    ### INPUT
    Intent:
    {intent}

    Key Facts:
    {facts_text}

    Tone:
    {tone}
    ----------------------

    ### CORE REQUIREMENTS
    - The email must fully address the given intent.
    - ALL provided facts MUST be included explicitly.
    - Facts should be naturally rephrased into complete sentences (do NOT copy verbatim).
    - Do NOT introduce any new facts or assumptions beyond the input.

    ----------------------
    ### TONE CONTROL
    - The tone must influence writing style (formal, polite, firm, empathetic, etc.).
    - Tone should NOT appear explicitly in the email.
    - Do NOT use tone as a name, role, or signature.

    ----------------------
    ### WRITING QUALITY
    - Use natural, human-like, and professional language.
    - Avoid robotic, repetitive, or overly generic phrasing.
    - Improve clarity and fluency of given facts while preserving meaning.
    - Avoid weak expressions like "it was nice" or "good experience".

    ----------------------
    ### STRUCTURE (STRICT)
    The email MUST follow this structure:

    1. Subject line (clear and relevant)
    2. Greeting:
       - Use: "Dear Hiring Team," or "Dear [Recipient],"
       - Do NOT use only "Hello"
    3. Body:
       - 2–3 paragraphs
       - Each paragraph must contain at least 2–3 meaningful sentences
       - Each paragraph should serve a clear purpose (context, details, closing)
    4. Closing:
       - Polite and professional ending

    ----------------------
    ### LENGTH & DEPTH CONTROL
    - Target length: 120–150 words
    - Ensure the email feels complete and well-developed
    - Avoid overly short or under-explained responses

    ----------------------
    ### FORMAT RULES
    - Add one blank line after greeting
    - Add one blank line between paragraphs
    - Maintain clean and readable formatting

    ----------------------
    ### SIGNATURE RULE
    - End the email with:
      Best regards,
    - Do NOT add any name or placeholder

    ----------------------
    ### SELF-CHECK (MANDATORY)
    Before generating final output, ensure:
    - All facts are included
    - Tone is consistent
    - No hallucinated or extra information is added
    - Structure strictly follows the defined format
    - Language is natural, clear, and professional
    - The email is sufficiently detailed (not too short)

    ----------------------
    ### OUTPUT FORMAT (STRICT)

    Subject: <one line subject>

    Email:
    <complete email body>
    """

    return prompt


def generate_email(intent, facts, tone):
    """Invokes the model with the generated prompt."""
    prompt = build_prompt(intent, facts, tone)
    response = model.invoke(prompt)
    return response.content


if __name__ == "__main__":
    intent_input = input("Enter intent: ")

    print("Enter facts (comma separated):")
    facts_raw = input()

    # 🔥 FINAL CLEANING (IMPORTANT)
    facts_input = [
        f.strip() for f in facts_raw.split(",")
        if f.strip() and f.strip().lower() != "nothing"
    ]

    tone_input = input("Enter tone: ")

    print("\nDEBUG INPUT:")
    print(intent_input, facts_input, tone_input)

    email_output = generate_email(intent_input, facts_input, tone_input)

    print("\nGenerated Email:\n")
    print(email_output)