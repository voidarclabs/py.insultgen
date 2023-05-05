# Python insult generator

This python file will randomly generate an insult and use tts and say it out loud.

To run, use `pip install gtts playsound` and run the [TTStest.py](https://github.com/voidarclabs/py.insultgen/blob/main/TTStest.py) file.

The [tts.py](https://github.com/voidarclabs/py.insultgen/blob/main/tts.py) file does the same, making tts insults.
Instead of reading out the file, it will save it in the `saving` directory. This will be made automatically.
To call the function, use:
```
import tts
tts.tts(<num>)
```
Where <num> is the amount of files you want. They will be saved in `.mp3` format.
Running the function multiple times will erase the contents of `saving` and create new files.

The insults are drawn from the .txt files and can be modified at will to add more words.
The `rude.insult()` function can still be called, but no longer requires the <num> variable.
If you do not need tts, use the [notts](https://github.com/voidarclabs/py.insultgen/tree/notts) branch.