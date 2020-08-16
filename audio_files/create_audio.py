import os
from gtts import gTTS


def str_to_mp3():
    ''' Convert a string to a .mp3 file and play it.
        Params:
            phrase (str): word or phrase to be converted.
            filename (str): name of the final file.
        Usage:
            convert("Hello Word", "hello.mp3")
    '''
    phrase = input(">> Type the word or phrase do you want to convert: ")
    filename = input(">> Type the output filename: ")
    try:
        tts = gTTS(phrase, lang='en-us')
    except ValueError as error:
        print(f"Error: {error}.")
    else:
        if not '.mp3' in filename:
            filename = filename + '.mp3'	# adds the '.mp3' extencion if not set by user
        tts.save(filename.replace('.mp3', '') + '.mp3')
        os.system('mpg123 ' + filename)	# uses mpg123 player by default

str_to_mp3()
