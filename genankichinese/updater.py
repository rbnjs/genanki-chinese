import requests
import json
import os
from genankichinese import exporter
from typing import List

class Updater(object):

    """Updater class"""

    def __init__(self, deck_name : str, base_url : str = 'http://localhost:8765'):
        self.base_url = base_url
        self.deck_name = deck_name

    def add_note(self, fields: List[str]):
        for model in [exporter.CHINESE_TO_ENGLISH, exporter.ENGLISH_TO_CHINESE, exporter.AUDIO_ONLY]:
            result = requests.post(self.base_url, Updater.create_json(fields, self.deck_name, model.name).encode('utf8'))
            print(f"Request result: {result.text}")

    @staticmethod
    def create_json(fields: List[str], deck_name: str, model_name: str) -> str:
        result = {
            'action': 'addNote',
            'version' : 6,
            'params': {
                'note': {
                    'deckName': deck_name,
                    'modelName': model_name,
                    'fields': {
                        'Original': fields[0],
                        'Traditional': fields[1],
                        'Pinyin': fields[2],
                        'Translation': fields[3],
                    },
                    'options': {
                        'allowDuplicate': False,
                        'duplicateScope': 'deck',
                        'duplicateScopeOptions': {
                            'deckName': 'Default',
                            'checkChildren': False,
                            'checkAllModels': False
                        }
                    },
                    'tags': [],
                    'audio': [{
                        'path': os.path.abspath(fields[5]),
                        'filename': Updater.__get_file_name(fields[4]),
                        'fields': ['Sound']
                    }]
                }
            }
        }
        return json.dumps(result, ensure_ascii=False)

    @staticmethod
    def __get_file_name(ankiname: str) -> str:
        return ankiname.replace('[sound:', '')[:-1]
