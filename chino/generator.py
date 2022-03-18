import opencc
import os
import tempfile
import shutil
from pypinyin import pinyin
from gtts import gTTS
from translate import Translator
from typing import List
from random import randrange
# https://github.com/salvoventura/pypexels
# https://github.com/yakupadakli/python-unsplash

class Generator(object):

    """Generates a list with the following values:
        * Original word
        * Original word in traditional chinese
        * Pinyin
        * Translated word
        * Filepath for the sound
        * Name of the sound file in Anki format"""

    def __init__(self):
        self.converter = opencc.OpenCC('s2t.json')
        self.translator = Translator(from_lang = "zh", to_lang="en")
        self.tempfolder = tempfile.mkdtemp()

    def convert(self, hanzi: str) -> List[str]:
        sounds = self.create_sound(hanzi)
        return [hanzi,
                self.converter.convert(hanzi),
                Generator.__pinyin(hanzi),
                self.translator.translate(hanzi),
                sounds[0],
                sounds[1]]

    @staticmethod
    def __pinyin(hanzi: str) -> str:
        result = ''
        for pinyin_chars in pinyin(hanzi):
            for pinyin_result in pinyin_chars:
                result = result + pinyin_result
        return result

    def create_sound(self, hanzi: str) -> List[str]:
        """
        Creates a sound in a temporal folder.
        Parameters:
            self (Generator): the instantiated object.
            hanzi (str): the chinese character or word.
        Returns:
            sound (List[str]): A list with the path of the sound and the name in Anki format.
        """
        sound = gTTS(hanzi)
        name = f"{Generator.__pinyin(hanzi)}-{randrange(0,1000)}.mp3"
        path = f"{self.tempfolder}/{name}"
        sound.save(path)
        return [f"[sound:{name}]", path]


    def close(self):
        if os.path.exists(self.tempfolder):
            shutil.rmtree(self.tempfolder)
