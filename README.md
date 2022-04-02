# genanki-chinese

Simple package which automates the creation of Chinese notes for Anki.

It produces notes with the following:
* Chinese word or phrase (Simplified)
* Chinese word or phrase (Traditional)
* English translation
* Audio in Chinese
* [Pinyin](https://en.wikipedia.org/wiki/Pinyin) of the phrase or word


## Installation

```
pip install genanki-chinese
```

## Usage

```bash
usage: genanki-chinese [-h] [-o OUTPUT] [-d DECKNAME] file

positional arguments:
  file                  Path of the file to import

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path where to put the result
  -d DECKNAME, --deckname DECKNAME
                        Deck name to update
```

The `file` should have the following structure:

``` 
咖啡<br>	kāfēi<br><br>coffee	
水<br><br>water	
```

This is done so you can export your decks from Anki and improve it creating a new one.

You can also have word by word separated by newlines without the `<br>` html element.

To update decks you have to install the [Anki-Connect](https://github.com/FooSoft/anki-connect) plugin in Anki.
