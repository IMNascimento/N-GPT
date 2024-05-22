import re
from pathlib import Path
import pickle
from unidecode import unidecode
from dotenv import load_dotenv
import os

class FileManager:
    CONFIG_FOLDER = Path(__file__).parent.parent / 'setup'
    MESSAGE_FOLDER = Path(__file__).parent.parent / 'messages'
    ENV_PATH = Path(__file__).parent.parent / '.env'
    CACHE = {}

    def __init__(self):
        self.CONFIG_FOLDER.mkdir(exist_ok=True)
        self.MESSAGE_FOLDER.mkdir(exist_ok=True)
        load_dotenv(dotenv_path=self.ENV_PATH)

    def convert_message_name(self, message_name):
        file_name = unidecode(message_name)
        file_name = re.sub(r'\W+', '', file_name).lower()
        return file_name

    def revert_message_name(self, file_name):
        if file_name not in self.CACHE:
            message_name = self.read_message_by_file_name(file_name, key='message_name')
            self.CACHE[file_name] = message_name
        return self.CACHE[file_name]

    def get_message_name(self, messages):
        message_name = ''
        for message in messages:
            if message['role'] == 'user':
                message_name = message['content'][:30]
                break
        return message_name

    def save_messages(self, messages):
        if len(messages) == 0:
            return False
        message_name = self.get_message_name(messages)
        file_name = self.convert_message_name(message_name)
        file_to_save = {'message_name': message_name,
                        'file_name': file_name,
                        'messages': messages}
        with open(self.MESSAGE_FOLDER / file_name, 'wb') as f:
            pickle.dump(file_to_save, f)

    def read_message_by_file_name(self, file_name, key='messages'):
        with open(self.MESSAGE_FOLDER / file_name, 'rb') as f:
            messages = pickle.load(f)
        return messages[key]

    def read_messages(self, messages, key='messages'):
        if len(messages) == 0:
            return []
        message_name = self.get_message_name(messages)
        file_name = self.convert_message_name(message_name)
        with open(self.MESSAGE_FOLDER / file_name, 'rb') as f:
            messages = pickle.load(f)
        return messages[key]

    def list_conversations(self):
        conversations = list(self.MESSAGE_FOLDER.glob('*'))
        conversations = sorted(conversations, key=lambda item: item.stat().st_mtime_ns, reverse=True)
        return [c.stem for c in conversations]

    def load_api_key(self):
        # Check if user has provided an API key in setup
        if (self.CONFIG_FOLDER / 'api_key').exists():
            with open(self.CONFIG_FOLDER / 'api_key', 'rb') as f:
                return pickle.load(f)
        
        # Fall back to environment variable
        return os.getenv('API_KEY', '')

    def save_api_key(self, key):
        with open(self.CONFIG_FOLDER / 'api_key', 'wb') as f:
            pickle.dump(key, f)