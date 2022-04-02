import argparse
from contextlib import closing
from genankichinese import updater, importer, exporter, generator
import sys

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help="Path of the file to import")
    parser.add_argument('-o', '--output', type=str, help="Path where to put the result", default="output.apkg")
    parser.add_argument('-d', '--deckname', type=str, help='Deck name to update')
    args = parser.parse_args(args)
    if args.deckname is None:
        with closing(generator.Generator()) as gen:
            result = []
            for word in importer.Importer(args.file).ingest():
                fields = gen.convert(word)
                result.append(fields)
            exporter.Exporter(args.output).create_deck(result)
    else:
        with closing(generator.Generator()) as gen:
            updater_instance = updater.Updater(args.deckname)
            for word in importer.Importer(args.file).ingest():
                fields = gen.convert(word)
                updater_instance.add_note(fields)

if __name__ == '__main__':
    main(sys.argv[1:])
