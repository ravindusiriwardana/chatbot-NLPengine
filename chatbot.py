import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=" * 50)
print("          Gemini Console Chatbot")
print("=" * 50)
print("Type 'exit' to quit.\n")

# Stores the ID of the previous conversation turn
previous_interaction_id = None

while True:

    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if not user_input:
        continue

    try:

        if previous_interaction_id is None:

            interaction = client.interactions.create(
                model="gemini-3.8-flash",
                input=user_input
            )

        else:

            interaction = client.interactions.create(
                model="gemini-3.8-flash",
                input=user_input,
                previous_interaction_id=previous_interaction_id
            )

        print("Bot:", interaction.output_text)
        print()

        previous_interaction_id = interaction.id

    except Exception as e:

        print("Error:", e)
        print()