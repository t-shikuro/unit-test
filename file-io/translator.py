from translate import Translator

translator = Translator(to_lang="ko")
try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # with open('d:/z2m/python-developer/file-io', mode='w') as my_file2:
        #     my_file2.write(translation)
        print(translation)
except FileNotFoundError as err:
    print('check your file path silly')
