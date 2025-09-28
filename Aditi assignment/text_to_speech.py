

from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    """
    Converts given text into speech with Indian English accent and saves as an mp3 file.
    
    Parameters:
        text (str): The input text/paragraph to convert.
        filename (str): The name of the output audio file.
    """
    
    tts = gTTS(text=text, lang='en', tld='co.in', slow=False)
    
    tts.save(filename)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    
    paragraph = """Hello ! This is a demo of a text to speech conversion  project . i am Aditi hope you all are doing well. thank you"""
    
    text_to_speech(paragraph, "indian_accent.mp3")
    

    os.system("start indian_accent.mp3")  
