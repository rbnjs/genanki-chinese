import genanki
# https://libretranslate.com/?source=en&target=es&q=Hello%2520friends
# https://github.com/BYVoid/OpenCC

def main():
    # Models needed:
    # * Audio only -> Chinese
    # * Chinese to English
    # * English to Chinese
    my_model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])
    my_note = genanki.Note(
          model=my_model,
          fields=['Capital of Argentina', 'Buenos Aires'])
    my_deck = genanki.Deck(
          2059400110,
          'Country Capitals')

    my_deck.add_note(my_note)
    genanki.Package(my_deck).write_to_file('output.apkg')

if __name__ == '__main__':
    main()
