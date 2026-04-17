import os
import sys
from hindsight_client import Hindsight
from dotenv import load_dotenv

# Load env
load_dotenv()

API_KEY = os.getenv("HINDSIGHT_SMRITIBRIEF_API_KEY")

if not API_KEY:
    print("Error : API Key not found.")
    sys.exit(1)

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=API_KEY
)

BANK_ID = "general-memory-agent"

print("\n=== Persistent Memory Agent (Always Learning) ===")
print("Type anything (type 'exit' to stop)\n")


def is_question(text):
    text = text.lower()
    return any(q in text for q in [
        "what", "who", "where", "when", "why", "how",
        "tell", "explain", "describe"
    ])


while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Agent: Goodbye!")
        break

    try:
        # ----------------------
        # STEP 1: ALWAYS STORE
        # ----------------------
        client.retain(
            bank_id=BANK_ID,
            content=user_input
        )

        # ----------------------
        # STEP 2: ANSWER IF QUESTION
        # ----------------------
        if is_question(user_input):

            answer = client.reflect(
                bank_id=BANK_ID,
                query=user_input
            )

            print("\nAgent:")
            print(answer.text)

        else:
            print("Agent: Noted.")

    except Exception as e:
        print("Agent Error:", e)