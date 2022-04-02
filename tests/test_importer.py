import unittest
from genankichinese import importer

class ImporterTest(unittest.TestCase):

    def setUp(self):
        self.importer = importer.Importer("./tests/resources/test.txt")

    def test_convert(self):
        result = self.importer.ingest()
        assert result == ['饺子', '包子', '鸡肉', '猪肉', '羊肉']

if __name__ == '__main__':
    unittest.main()

