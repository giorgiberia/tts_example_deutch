from gtts import gTTS
import os
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = """
    Juliana kommt aus Paris. Das ist die Hauptstadt von Frankreich. In diesem Sommer macht sie einen Sprachkurs in Freiburg. Das ist eine Universitätsstadt im Süden von Deutschland.
    """
    language = "de"
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    os.system("start text.mp3")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
