from gtts import gTTS

# Script that converts a string to .mp3

DEFAULT_LANG = 'en-us'


def str_to_mp3():
    """Convert a string to a .mp3 file."""
    phrase = input(">> Type the word or phrase do you want to convert: ")
    filename = input(">> Type the output (mp3) filename: ")
    try:
        tts = gTTS(phrase, lang=DEFAULT_LANG)
    except ValueError as error:
        print(f"Error: {error}.")
    else:
        if '.mp3' not in filename:
            filename = filename + '.mp3'  # adds the '.mp3' extension if not set
        tts.save(filename.replace('.mp3', '') + '.mp3')
        print(f"[ + ] {filename} MP3 file saved successfully!")


if __name__ == "__main__":
    str_to_mp3()
