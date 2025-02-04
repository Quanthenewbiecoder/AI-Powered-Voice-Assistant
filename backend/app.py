from flask import Flask, request, jsonify
from ai_responses import get_ai_response  # Function to get AI response based on the command
from text_to_speech import speak  # Function to convert AI response to speech

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the AI Voice Assistant!"

@app.route('/voice-command', methods=['POST'])
def voice_command():
    if request.method == 'POST':
        # Extract command from the JSON body of the POST request
        command = request.json.get('command', '').lower()

        # Handle the command with AI and/or TTS
        if command:
            # Get AI's response to the command
            ai_response = get_ai_response(command)
            # Optionally, convert response to speech
            speak(ai_response)

            # Return the AI response as JSON
            return jsonify({"message": ai_response})
        else:
            return jsonify({"message": "No command received"}), 400

    return jsonify({"message": "Method Not Allowed"}), 405

if __name__ == "__main__":
    app.run(debug=True, port=5001)
