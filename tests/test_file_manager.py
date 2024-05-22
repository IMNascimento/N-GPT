import unittest
import os
from pathlib import Path
from src.file_manager import FileManager
import pickle

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()
        self.test_env_path = Path(__file__).parent.parent / '.env'
        self.test_setup_path = self.file_manager.CONFIG_FOLDER / 'api_key'
        
        # Criar um .env de teste se não existir
        if not self.test_env_path.exists():
            with open(self.test_env_path, 'w') as f:
                f.write("API_KEY=test_api_key")

    def tearDown(self):
        # Remover o .env de teste após os testes
        if self.test_env_path.exists():
            os.remove(self.test_env_path)
        # Remover o arquivo de chave de configuração se existir
        if self.test_setup_path.exists():
            os.remove(self.test_setup_path)
        # Limpar variáveis de ambiente
        if 'API_KEY' in os.environ:
            del os.environ['API_KEY']

    def test_load_api_key_from_env(self):
        os.environ['API_KEY'] = 'test_api_key_from_env'
        api_key = self.file_manager.load_api_key()
        self.assertEqual(api_key, 'test_api_key_from_env')

    def test_load_api_key_from_setup(self):
        with open(self.test_setup_path, 'wb') as f:
            pickle.dump('test_api_key_from_setup', f)
        api_key = self.file_manager.load_api_key()
        self.assertEqual(api_key, 'test_api_key_from_setup')

    def test_save_api_key(self):
        self.file_manager.save_api_key('test_api_key_save')
        with open(self.test_setup_path, 'rb') as f:
            saved_key = pickle.load(f)
        self.assertEqual(saved_key, 'test_api_key_save')

if __name__ == '__main__':
    unittest.main()