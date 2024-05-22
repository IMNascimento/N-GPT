import unittest
from unittest.mock import patch, MagicMock
from src.gpt import OpenAIAPI

class TestOpenAIAPI(unittest.TestCase):
    @patch('openai.ChatCompletion.create')
    def test_get_response(self, mock_create):
        mock_create.return_value = MagicMock(choices=[MagicMock(delta={'content': 'mock response'})])
        
        api_key = 'test_api_key'
        openai_api = OpenAIAPI(api_key)
        
        messages = [{'role': 'user', 'content': 'Hello!'}]
        response = openai_api.get_response(messages)
        
        mock_create.assert_called_once_with(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=0,
            stream=False
        )
        self.assertEqual(response.choices[0].delta['content'], 'mock response')

if __name__ == '__main__':
    unittest.main()