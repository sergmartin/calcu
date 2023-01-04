import pandas as pa
from logg import logging
print('-'*80)
print('Табель учащихся в средней школе №2023')

stud_card = {
        'ID': ['01','02','03','04','05'],
        'Имя' : ['КИРИЛЛ','ЮЛИЯ','РОМАН','ЛЮБОВЬ','АЛЕКСАНДР'],
        'Фамилия': ['БАКАНОВ','МОЙКОВА','АНДРИАНОВ','ШМАДКО','МЕДВЕДЕВ'],
        'Дата рождения' : ['17.08.2000','04.05.2001','01.04.1999','23.02.2002','08.03.2004'],
        'Успеваемость' : ['Отличник','Троечник','Хорошист','Отличник','Хорошист']
}
    
ss = pa.DataFrame(data = stud_card)

with open('students.txt', 'a', encoding='UTF-8') as cl:
        cl.write(f'{ss}')
        cl.write('\n')
        cl.close()
        logging.info("zapis students")
print(ss)
logging.info("vivod students")