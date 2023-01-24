# Модуль ввода данных

import time as t
import string as st
import secrets as sec



filename = 'Fone_book'
file= open(filename, 'a')
file.close

# Ввод имени и фамилии
def first_name():
    first= input('Введите  имя: ')
    slett= first[1:]
    flett= first[0]
    name= flett.upper()+ slett
    return name

def last_name():
    first= input('Введите фамилию: ')
    slett= first[1:]
    flett= first[0]
    name= flett.upper()+ slett
    return name

# Генерация id
def gen_key():
    alphabet = st.ascii_letters + st.digits
    key = ''.join(sec.choice(alphabet) for i in range(7))
    return key
# Запись в телефонный справочник
def contact():
    phone= input('Введите номер телефона: ')    
    firstname= first_name()
    lastname= last_name()
    key= gen_key()
    time= t.time()
    time2= t.ctime(time)
    data_contact= (f'{time2} id: {key}  {lastname}  {firstname} телефон: {phone}\n')
    file= open(filename, 'a')
    file.write(data_contact) 
    print(f'Новая запись в телефонном справочнике: {data_contact} ')
   

#print(contact())



