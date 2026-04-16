from generator import generate_email
from generator_v2 import generate_email_v2
from test_case import test_cases
from metrics import fact_coverage, structure_score, tone_score, grammar_score

import csv
import os
import numpy as np
from datetime import datetime

print("🚀 Evaluation Started")

results = []

# -------------------------
# FINAL SCORE FUNCTION
# -------------------------
def final_score(fact, struct, grammar, tone):
    return (
        fact * 0.4 +
        struct * 0.2 +
        grammar * 0.2 +
        tone * 0.2
    )


# -------------------------
# RUN EVALUATION
# -------------------------
for i, case in enumerate(test_cases):

    print(f"Running case {i + 1}")

    # Model A
    email_a = generate_email(
        case["intent"],
        case["facts"],
        case["tone"]
    )

    # Model B
    email_b = generate_email_v2(
        case["intent"],
        case["facts"],
        case["tone"]
    )

    # -------------------------
    # METRICS - MODEL A
    # -------------------------
    fa = fact_coverage(email_a, case["facts"])
    sa = structure_score(email_a)
    ga = grammar_score(email_a)
    ta = tone_score(email_a, case["intent"], case["tone"]) / 10  # normalize

    # -------------------------
    # METRICS - MODEL B
    # -------------------------
    fb = fact_coverage(email_b, case["facts"])
    sb = structure_score(email_b)
    gb = grammar_score(email_b)
    tb = tone_score(email_b, case["intent"], case["tone"]) / 10  # normalize

    results.append({
        "case_id": i + 1,
        "intent": case["intent"],
        "tone": case["tone"],

        "fact_A": fa,
        "struct_A": sa,
        "grammar_A": ga,
        "tone_A": ta,
        "score_A": final_score(fa, sa, ga, ta),

        "fact_B": fb,
        "struct_B": sb,
        "grammar_B": gb,
        "tone_B": tb,
        "score_B": final_score(fb, sb, gb, tb),
    })


# -------------------------
# SAFETY CHECK
# -------------------------
if not results:
    print("❌ No results generated")
    exit()

# -------------------------
# CSV OUTPUT
# -------------------------
output_file = f"comparison_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

output_path = os.path.join(os.path.dirname(__file__), output_file)

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\n✅ CSV saved at: {output_path}")


# -------------------------
# FINAL ANALYSIS
# -------------------------
avg_A = np.mean([r["score_A"] for r in results])
avg_B = np.mean([r["score_B"] for r in results])

std_A = np.std([r["score_A"] for r in results])
std_B = np.std([r["score_B"] for r in results])

print("\n=== FINAL COMPARISON ===")
print(f"Model A Score: {avg_A:.3f}")
print(f"Model B Score: {avg_B:.3f}")

print("\n=== STABILITY CHECK ===")
print(f"Model A Variance: {std_A:.3f}")
print(f"Model B Variance: {std_B:.3f}")


# -------------------------
# DECISION LOGIC
# -------------------------
if avg_B > avg_A and std_B <= std_A:
    print("\n👉 Model B is better for production (higher + stable)")
elif avg_A > avg_B and std_A <= std_B:
    print("\n👉 Model A is better for production (higher + stable)")
else:
    better = "B" if avg_B > avg_A else "A"
    print(f"\n👉 Model {better} is better based on average score")