from pprint import pprint

file_name = 'byron.txt'
with open (file_name, mode = 'r', encoding='utf8') as file:
    for line in file:
        print(line, end='')

print(file.closed)
#with open(file_name...) предпочтительнее использовать, т.к. в этой конструкции
# произойдет автоматическое закрытие файла даже если внутри блока между открытием
# и закрытием файла возникнет какая-то непредвиденная ситуация.