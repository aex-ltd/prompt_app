import openai
import requests 
import json
from django.conf import settings

# function to connect to OpenAI API (ChatGPT)
def ask_gpt(question):
    openai.api_key = settings.OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # you can also use 'gpt-4' if you have access to it
            messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=600,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"


# function to connect to gemini  
def ask_gemini(question):
    """Sends a question to the Gemini API and returns the response.

    Args:
        question (str): The question to send to the API.

    Returns:
        str: The response from the API.
    """

    try:
        # Replace with your Gemini API endpoint and token
        api_endpoint = "https://api.geminiai.com/chat"
        api_token = settings.GEMINI_TOKEN

        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

        payload = {
            "prompt": question,
            "model": "gemini-1.5-flash",  # Adjust model as needed
        }

        response = requests.post(api_endpoint, headers=headers, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["response"]
        else:
            raise Exception(f"Gemini API request failed with status code {response.status_code}")

    except Exception as e:
        print(f"Error sending question to Gemini API: {e}")
        return f"Error: {str(e)}"