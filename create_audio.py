import os
from gtts import gTTS

# Script that converts a string to .mp3

DEFAULT_LANG = 'en-us'

def str_to_mp3():
    ''' Convert a string to a .mp3 file '''
    phrase = input(">> Type the word or phrase do you want to convert: ")
    filename = input(">> Type the output (mp3) filename: ")
    try:
        tts = gTTS(phrase, lang=DEFAULT_LANG)
    except ValueError as error:
        print(f"Error: {error}.")
    else:
        if not '.mp3' in filename:
            filename = filename + '.mp3'	# adds the '.mp3' extencion if not set by user
        tts.save(filename.replace('.mp3', '') + '.mp3')
        print(f"[ + ] MP3 file saved successfully!")
        # os.system('mpg123 ' + filename)	# uncoment to play the mp3 after creation (uses mpg123 player)

if __name__ == "__main__":
    str_to_mp3()
