import os
result = []
work_dir = '/Users/andrei/PycharmProjects/fileparser/files'
to_find = 'a'


# ищем строку, содержащую искомый текст. Если в файле находится строка, запихиваем имя файла в список result
def get_string(target):
    f = open(target, 'r')
    for line in f:
        if to_find in line:
            result.append(target)
    f.close()


# проверяем наличие файла "result.txt", если он есть, стираем (оказалось,нахер не надо).
def file_prep():
    if os.path.isfile(os.getcwd() + '/result.txt'):
        print('удаляем')
        os.remove(os.getcwd() + '/result.txt')


# записываем результаты в файл строка на имя файла
def file_save():
    f = open(os.getcwd()+'/result.txt', 'w')
    for index in result:
        f.write(index + '\n')
    f.close()


# переходим в папку с файлами
os.chdir(work_dir)
# запихиваем список файлов в список "listdir"
listdir = os.listdir(path=".")
# для каждога файла запускаем функцию GetString (передаём ему по очереди каждое именя файла)
for i in listdir:
    get_string(i)
result.sort()
# работаем с файлом, содержащим список искомых файлов
file_prep()
file_save()

print(result)
