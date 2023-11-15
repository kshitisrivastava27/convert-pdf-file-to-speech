import PyPDF2
from gtts import gTTS
import os

def pdf_to_speech(pdf_file, lang='en'):
    #initialize a PDF file reader
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)

        #iterate over each page and extract the text
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text = page.extractText()

            #save the text to a file
            with open(f'page_{page_num}.txt', 'w') as text_file:
                text_file.write(text)
            
            #convert the text to speech
            tts = gTTS(text, lang=lang)

            #save the speech to a file
            tts.save(f'page_{page_num}.mp3')

            #delete the text file
            os.remove(f'page_{page_num}.txt')

pdf_file = (r"C:\\Users\\Dell\\convert\\sample.pdf")
pdf_to_speech(pdf_file)
