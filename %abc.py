import string
import os
abc = string.ascii_lowercase
names = os.listdir(os.getcwd() + '\\texts')
path_to_text = os.getcwd() + '\\texts'
path_to_data = os.getcwd() + '\\texts_data'


def get_info(text_name):

    with open(path_to_text + '\\' + text_name) as text:

        text_ = text.read()
        text_ = text_.encode('ascii', 'ignore').decode()
        length = len(text_)

        try:
            b = os.path.getsize(path_to_data + '\\' + 'statistics_' + text_name)
            if b > 0:
                os.truncate(path_to_data + '\\' + 'statistics_' + text_name, 0)
        except FileNotFoundError:
            pass

        for iterator in abc:
            letter = text_.count(iterator)
            with open(path_to_data + '\\' + 'statistics_' + text_name, 'a+') as stat:
                stat.write(iterator + ' ' + str(letter) + '\n')

        with open(path_to_data + '\\' + 'statistics_' + text_name, 'r') as stat:
            total = 0
            for line in stat:
                total = total + int(line[2:])

        with open(path_to_data + '\\' + 'statistics_' + text_name, 'a+') as stat:
            stat.write('total letters - ' + str(total) + '\n')
            stat.write('total length - ' + str(length) + '\n')


def get_general_stat():

    try:
        b = os.path.getsize(path_to_data + '\\' + 'general_statistics.txt')
        if b > 0:
            os.truncate(path_to_data + '\\' + 'general_statistics.txt', 0)
    except FileNotFoundError:
        pass

    for letter in abc:
        total_letter = []

        for text_name in names:
            with open(path_to_data + '\\' + 'statistics_' + text_name, 'r') as stat:
                for line in stat:
                    if line.startswith(letter) and line[1] == ' ':
                        total_letter.append(int(line[2:]))

        with open(path_to_data + '\\' + 'general_statistics.txt', 'a+') as gen_stat:
            gen_stat.write(letter + ' - ' + str(sum(total_letter)) + '\n')


def summary():
    try:
        b = os.path.getsize(path_to_data + '\\' + 'analysis.txt')
        if b > 0:
            os.truncate(path_to_data + '\\' + 'analysis.txt', 0)
    except FileNotFoundError:
        pass
    sum_list = []
    letter_dict = {}
    ttl = 0
    with open(path_to_data + '\\' + 'general_statistics.txt', 'r') as gen_stat:
        for line in gen_stat:
            sum_list.append(int(line[4:]))
            letter_dict[line[0]] = int(line[4:])
        total_letters = sum(sum_list)
    for letter in abc:
        with open(path_to_data + '\\' + 'analysis.txt', 'a+') as statistics:
            statistics.write(letter + ' - ' + str((letter_dict[letter] / total_letters) * 100) + '%' + '\n')
        with open(path_to_data + '\\' + 'proof.txt', 'a+') as statistics:
            ttl += (letter_dict[letter] / total_letters) * 100
            statistics.write(str(ttl) + '\n')


# for i in range(10, 51):
#     with open(path_to_text + '\\' + 'text{}.txt'.format(i), 'a+') as txt:
#         pass


for name in names:
    try:
        get_info(name)
    except:
        print(name)
get_general_stat()
summary()
