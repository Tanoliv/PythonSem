import poisk_contact as pc
import data_provader as dp

filename = 'Fone_book'
file= open(filename, 'a')
file.close

def main_menu():
    print('МЕНЮ\n')
    print('1. Вывести все контакты')
    print('2. Добавить контакт')
    print('3. Найти контакт')
    print('4. Выйти')
    point= input('Выберите пункт меню: ')
    if point=='1':
        file= open(filename, 'r')
        sps= file.read()
        if len(sps)==0:
            print('список пуст')
        else:
            
            print(sps)
        file.close
        enter= input('Продолжить - ENTER')      
        main_menu()
    elif point=='2':
        dp.contact()
        enter= input('Продолжить - ENTER')
        main_menu()
    elif point=='3':
        pc.poisk()
        enter= input('Продолжить - ENTER')
        main_menu()     
    elif point=='4':
        print('Спасибо')
    else:
        print('Введите корректный пункт меню')
        enter= input('Продолжить - ENTER')
        main_menu()  

    
    


