
import student_info as si
import cabinet_info as cab
from logg import logging

def vibor():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает  студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        try:
            surn = str(input("Введите фамилию ученика: "))
            logging.info("vopros famolii")
            if surn.upper() in si.stud_card['Фамилия']:
                index = si.stud_card['Фамилия'].index(surn.upper())
            print(f"ID ученика: {si.stud_card['ID'][index]},\nИмя: {si.stud_card['Имя'][index]},\nФамилия: {si.stud_card['Фамилия'][index]},\nдата рождения: {si.stud_card['Дата рождения'][index]},\nУспеваемость: {si.stud_card['Успеваемость'][index]}")
        except:
            logging.warning("no gut enter")
            print("Введено что-то не то!")
        num = input('\nХотите выполнить какую-то другую операцию??? да/нет: ')
        if num.lower() == 'да':
            vibor()
        logging.info("exit")
        exit()
        logging.info("exit")

    elif ch == 2:
        c = input('Введите ID студента для вывода по классам: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" Сидит в классе - {cab.class_card['Предмет'][index]}\n\, за партой номер - {cab.class_card['Номер парты'][index]}, это {cab.class_card['Ряд'][index]}, парта - {cab.class_card['Вид парты'][index]}, Имя: {si.stud_card['Имя'][index]}, Фамилия - {si.stud_card['Фамилия'][index]}, и успеваемасть у студента: {si.stud_card['Успеваемость'][index]}")
            logging.info("vivod zaprosa")
          
            num = input('\nХотите выполнить другую операцию??? да/нет: ')
            logging.info("zapros prodolzhenia")
            if num.lower() == 'да':
                vibor()
            exit()
    else:
        print('еще раз')
    exit()

logging.info("starting")
vibor()
