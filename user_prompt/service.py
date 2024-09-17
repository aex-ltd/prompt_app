import openai
from django.conf import settings

# function to connect to chatgpt 
def ask_chatgpt(question):
    openai.api_key = settings.OPENAI_API_KEY
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=600,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
