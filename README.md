# ty.py - a typing game in the terminal

[![2019-09-08-175630-1920x1080-scrot.png](https://i.postimg.cc/1XHxhjPw/2019-09-08-175630-1920x1080-scrot.png)](https://postimg.cc/ZvCs6jW5)

I was inspired by [typeracer](https://play.typeracer.com/).

## Requirements

python

python module [getkey](https://pypi.org/project/getkey/)

## Usage

Start the game
```
python ./ty.py
```

## Notes

-This game does not work on windows.

-The game reads the sentences from a file called `sentences`. So you can add your own sentences in your desired language.

-After hitting space or return the input will be checked. When the input is correct, the word will be shown in green. If it's not correct, the word will be shown in red and you need to type the word again.
