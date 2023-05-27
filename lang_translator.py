from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('./test.txt.txt',mode='r+') as file1:
        text = file1.read()
        translation = translator.translate(text)with open('./file2.txt',mode='w') as file2:
            file2.write(translation)
except FileNotFoundError as e:
    print('file not found')