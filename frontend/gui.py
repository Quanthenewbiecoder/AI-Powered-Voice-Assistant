import tkinter as tk
import requests
import os

# Initialize the main window
root = tk.Tk()
root.title("Voice Assistant")

# Set window size
root.geometry("400x200")

# Create a StringVar for holding the response
response_text = tk.StringVar()

# Function to send command and display response
def send_command():
    user_input = command_entry.get()  # Get the input from the entry field
    try:
        # Get API key from environment variable (or you can hardcode it directly)
        api_key = os.getenv('OPENAI_API_KEY')  # Replace this with actual API key if not using env variable

        if not api_key:
            response_text.set("API key is missing.")
            return

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        # Make an API request
        response = requests.post("https://api.openai.com/v1/completions", 
                                 json={"model": "gpt-3.5-turbo", "prompt": user_input, "max_tokens": 100},
                                 headers=headers)

        # Print the raw response to debug
        print("Raw Response:", response.text)

        if response.status_code == 200 and response.text:
            try:
                # Parse the response as JSON
                json_response = response.json()
                message = json_response.get("choices", [{}])[0].get("text", "Error")  # Retrieve message from response
                response_text.set("Response: " + message.strip())
            except ValueError:
                # Handle the case when the response is not valid JSON
                response_text.set("Error: Response is not valid JSON")
        else:
            # Handle errors like no response or failed status code
            response_text.set(f"Error: {response.status_code} - No response or failed to connect")

    except requests.exceptions.RequestException as e:
        # Handle network or request errors
        response_text.set(f"Request Error: {str(e)}")

# Create the UI elements
command_label = tk.Label(root, text="Enter Command:")
command_label.pack(pady=10)

command_entry = tk.Entry(root, width=40)
command_entry.pack(pady=5)

send_button = tk.Button(root, text="Send Command", command=send_command)
send_button.pack(pady=10)

response_label = tk.Label(root, textvariable=response_text, wraplength=350)
response_label.pack(pady=10)

# Run the application
root.mainloop()
