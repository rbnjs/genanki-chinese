
from typing import List


class Importer(object):

    """Reads a file and get the first word so we can translate it."""

    def __init__(self, file_path: str, separator: str = "<br>"):
        self.file_path = file_path
        self.separator = separator

    def ingest(self) -> List[str]:
        result = []
        with open(self.file_path) as fp:
            lines = fp.readlines()
            for line in lines:
                result.append(self.get_question_from_card(line))
        return result

    def get_question_from_card(self, line : str) -> str:
        return line.split(self.separator)[0].strip()
