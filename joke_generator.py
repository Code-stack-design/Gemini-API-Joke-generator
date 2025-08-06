import google.generativeai as genai

# Set your API key
genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your actual key

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Ask for a joke
prompt = "Tell me a silly joke suitable for kids."
response = model.generate_content(prompt)

# Print the joke
print("Here's a silly joke:")
print(response.text)
