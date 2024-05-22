import openai

class OpenAIAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def get_response(self, messages, model='gpt-3.5-turbo', temperature=0, stream=False):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            stream=stream
        )
        return response