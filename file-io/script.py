my_file = open('test.txt')

# my_file.seek(0)
# print(my_file.readlines())

# my_file.close()
try:
    with open('test.text', mode='r+') as my_file:
        text = my_file.write('Yoooo it\'s me!!')
    except FileNotFoundError as err:
        print('file does not exist')
        raise err

    except IOError as err:
        print('IO error')
        raise err