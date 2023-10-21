from PIL import Image
import pytesseract
import pyttsx3

def ImagetoString():
    img = Image.open('11.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    result = pytesseract.image_to_string(img)
    return result

def speech():
    text_speech = pyttsx3.init()
    text_speech.say(ImagetoString())
    text_speech.runAndWait()


speech()