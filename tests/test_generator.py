import unittest
from genankichinese import generator

class GeneratorTest(unittest.TestCase):

    def setUp(self):
        self.generator = generator.Generator()

    def tearDown(self):
        self.generator.close()

    def test_convert(self):
        result = self.generator.convert("你好")
        print(result)
        assert len(result) == 6


if __name__ == '__main__':
    unittest.main()

