import os
import genanki
from typing import List
import random

FIELDS_LIST = [
    {'name': 'Original'},
    {'name': 'Traditional'},
    {'name': 'Pinyin'},
    {'name': 'Translation'},
    {'name': 'Sound'}
]

MODEL_CSS = '''
.card {
    font-family: arial;
    font-size: 48px;
    text-align: center;
    color: black;
    background-color: white;
    line-height: 2em;
}
'''

CHINESE_TO_ENGLISH = genanki.Model(
    1450786248,
    'Chinese to English',
    fields = FIELDS_LIST,
    css =  MODEL_CSS,
    templates=[
        {
            'name': 'Card {{Original}} English to Chinese',
            'qfmt': '<div class="card">{{Original}}<br>{{Traditional}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Pinyin}}<br>{{Translation}}<br>{{Sound}}</div>',
        },
    ])

ENGLISH_TO_CHINESE = genanki.Model(
    1480566997,
    'English to Chinese',
    fields = FIELDS_LIST,
    css = MODEL_CSS,
    templates=[
        {
            'name': 'Card {{Original}} English to Chinese',
            'qfmt': '<div class="card">{{Translation}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Original}}<br>{{Traditional}}<br>{{Pinyin}}<br>{{Sound}}</div>',
        },
    ])

AUDIO_ONLY = genanki.Model(
    1899733999,
    'Audio Only',
    fields = FIELDS_LIST,
    css =  MODEL_CSS,
    templates=[
        {
            'name': 'Card {{Original}} Audio',
            'qfmt': '<div class="card">{{Sound}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Original}}<br>{{Traditional}}<br>{{Pinyin}}<br>{{Translation}}</div>',
        },
    ])

class Exporter:

    def __init__(self, deck_name: str):
        self.deck = genanki.Deck(Exporter.get_unique_id(), deck_name)
        self.package = genanki.Package(self.deck)
        self.deck_name = f"{self.deck.name}.apkg"

    def create_deck(self, info : List[List[str]]):
        media_files = []
        for fields in info:
            note_fields = Exporter.get_note_fields(fields)
            self.deck.add_note(genanki.Note(guid = Exporter.get_unique_id(), model = CHINESE_TO_ENGLISH, fields = note_fields))
            self.deck.add_note(genanki.Note(guid = Exporter.get_unique_id(), model = ENGLISH_TO_CHINESE, fields = note_fields))
            self.deck.add_note(genanki.Note(guid = Exporter.get_unique_id(), model = AUDIO_ONLY, fields = note_fields))
            media_files.append(Exporter.get_media_path(fields))
        self.package.media_files = media_files
        self.package.write_to_file(self.deck_name)

    @staticmethod
    def get_note_fields(fields: List[str]) -> List[str]:
        return fields[0:5]

    @staticmethod
    def get_media_path(fields: List[str]) -> str:
        return fields[5]

    @staticmethod
    def get_unique_id() -> int:
        return random.randrange(1 << 30, 1 << 31)

    def close(self):
        if os.path.exists(self.deck_name):
            os.remove(self.deck_name)
