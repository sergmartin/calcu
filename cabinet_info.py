import pandas as pd
from logg import logging
print('-'*80)
print('Информация о классах')

class_card = {
        'Предмет': ['Русский язык','Химия','Физика','Биология','Информатика'],
        'Номер парты' : ['1','2','3','4','5'],
        'Ряд': ['Первый ряд','Второй ряд','Третий ряд','Четвертый ряд','Пятый ряд'],
        'Вид парты' : ['Одноместная','Одноместная','Двуместная ','Двуместная ','Одноместная'],
        'ID' : ['01','02','03','04','05']
}
    
ca = pd.DataFrame(data = class_card)

with open('cabinet.txt', 'a', encoding='UTF-8') as cl:
        cl.write(f'{ca}')
        cl.write('\n')
        cl.close()
        logging.info("zapis cabinet")
print(ca)
logging.info("vivod cabinet")