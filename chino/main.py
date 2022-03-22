import argparse
from contextlib import closing
import generator
import importer
import exporter
import sys

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help="Path of the file to import")
    parser.add_argument('-o', '--output', type=str, help="Path where to put the result", default="output.apkg")
    args = parser.parse_args(args)
    with closing(generator.Generator()) as gen:
        result = []
        for word in importer.Importer(args.file).ingest():
            fields = gen.convert(word)
            result.append(fields)
        exporter.Exporter(args.output).create_deck(result)


if __name__ == '__main__':
    main(sys.argv[1:])
