from unittest.mock import patch
from chino import updater
import unittest


class UpdaterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.updater = updater.Updater('test')
        self.info = ['你好', '你好', 'nǐhǎo', 'Hello', '[sound:nǐhǎo-413.mp3]', './tests/resources/nǐhǎo-413.mp3']

    def test_create_json(self):
        result = updater.Updater.create_json(self.info, 'deck_name', 'model_name')
        self.assertEqual(result, '{"action": "addNote", "version": 6, "params": {"note": {"deckName": "deck_name", "modelName": "model_name", "fields": {"Original": "你好", "Traditional": "你好", "Pinyin": "nǐhǎo", "Translation": "Hello"}, "options": {"allowDuplicate": false, "duplicateScope": "deck", "duplicateScopeOptions": {"deckName": "Default", "checkChildren": false, "checkAllModels": false}}, "tags": [], "audio": [{"path": "/home/ruben/local_workspace/chino/tests/resources/nǐhǎo-413.mp3", "filename": "nǐhǎo-413.mp3", "fields": ["Sound"]}]}}}')

    @patch('chino.updater.requests.post')
    def test_add_note(self, post):
        self.updater.add_note(self.info)
