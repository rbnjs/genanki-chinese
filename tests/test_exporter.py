
from chino.exporter import Exporter
import unittest


class ExporterTest(unittest.TestCase):

    def setUp(self):
        self.exporter = Exporter(deck_name = "test_deck")
        self.info = [['你好', '你好', 'nǐhǎo', 'Hello', '[sound:nǐhǎo-413.mp3]', './tests/resources/nǐhǎo-413.mp3']]

    def tearDown(self):
        #self.exporter.close()
        pass

    def test_create_deck(self):
        self.exporter.create_deck(self.info)

    def test_get_note_fields(self):
        assert Exporter.get_note_fields(self.info[0]) == ['你好', '你好', 'nǐhǎo', 'Hello', '[sound:nǐhǎo-413.mp3]']

    def test_get_media_path(self):
        assert Exporter.get_media_path(self.info[0]) == './tests/resources/nǐhǎo-413.mp3'
