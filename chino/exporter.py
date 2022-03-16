import genanki
from typing import List
import random; 

FIELDS_LIST = [
    {'name': 'Original'},
    {'name': 'Traditional'},
    {'name': 'Pinyin'},
    {'name': 'Translation'},
    {'name': 'Sound'}
]

CHINESE_TO_ENGLISH = genanki.Model(
    1450786248,
    'Chinese to English',
    fields=FIELDS_LIST,
    templates=[
        {
            'name': 'Card {{Original}} English to Chinese',
            'qfmt': '{{Original}}<br>{{Traditional}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Pinyin}}<br>{{Translation}}<br>{{Sound}}',
        },
    ])

ENGLISH_TO_CHINESE = genanki.Model(
    1480566997,
    'English to Chinese',
    fields=FIELDS_LIST,
    templates=[
        {
            'name': 'Card {{Original}} English to Chinese',
            'qfmt': '{{Translation}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Original}}<br>{{Traditional}}<br>{{Pinyin}}<br>{{Sound}}',
        },
    ])

AUDIO_ONLY = genanki.Model(
    1899733999,
    'Audio Only',
    fields=FIELDS_LIST,
    templates=[
        {
            'name': 'Card {{Original}} Audio',
            'qfmt': '{{Sound}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Original}}<br>{{Traditional}}<br>{{Pinyin}}<br>{{Translation}}',
        },
    ])

class Exporter:
    """description"""

    def __init__(self, deck_name: str):
        self.deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), deck_name)
        self.package = genanki.Package(self.deck)
        pass

    def create_deck(self, info : List[List[str]]) -> str:
        return ""

