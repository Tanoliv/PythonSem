#Модуль поиска контактов
filename = 'Fone_book'
file= open(filename, 'a')
file.close

def poisk():
    name= input('Поиск: введите имя контакта: ')
    slett= name[1:]
    flett= name[0]
    fname= flett.upper()+ slett
    file= open(filename, 'r')
    sps= file.readlines()
    #psk= False
    for i in sps:
        if fname in i:
            print('Найден: ')
            print(i)
            #psk= True
            
        else:
            print(f'Контакт {fname} не найден')
  

#poisk()

