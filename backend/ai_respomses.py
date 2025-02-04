# backend/ai_responses.py
import openai


def get_ai_response(command):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Update to the new model
            messages=[{"role": "user", "content": command}]
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.OpenAIError as e:
        return f"AI error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

