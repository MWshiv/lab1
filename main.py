documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}


def p():
 a = input("Введите номер документа: ")
 for i in documents:
      if a in i['number']:
        b = i['name']
        break
      else:
        b = 0
 print("Документ не найден в базе") if b == 0 else print("Владелец документа: ", b)
 return


def s():
 a = input("Введите номер документа: ")
 for i in directories:
      if a in directories[i]:
        b = i
        break
      else:
        b = 0
 print("Документ не найден в базе") if b == 0 else print("Документ хранится на полке: ", b)
 return


def l():
 for i in documents:
     a = i['number']
     for j in directories:
         if a in directories[j]:
             b = j
     print("№", i['number'], ",", "тип:", i['type'], ",", "владелец:", i['name'], ",", "полка хранения:", b)
 return


def ads():
 a = input("Введите номер полки: ")
 if a in directories:
    print("Такая полка уже существует")
 else:
      directories.setdefault(a, [])
      print("Полка добавлена")
 b = list(directories.keys())
 b = ", ".join(b)
 print("Текущий перечень полок: " )
 return print(b)


def ds():
 a = input("Введите номер полки: ")
 if a in directories:
  for i in directories:
       if a == i:
            if directories[i] == []:
                del directories[i]
                print("Полка удалена")
                break
            else:
                print("На полке есть документы, удалите их перед удалением полки")
                break
 else:
   print("Такой полки не существует")
 b = list(directories.keys())
 b = ", ".join(b)
 print("Текущий перечень полок: ")
 return print(b)


def ad():
 number = input("Введите номер документа: ")
 type = input("Введите тип документа: ")
 owner = input("Введите владельца документа: ")
 shelf = input("Введите полку для хранения: ")
 if shelf in directories:
  directories[shelf].append(number)
  documents.append({'type': type, 'number': number, 'name': owner})
  print("Документ добавлен")
 else:
  print("Такой полки не существует. Добавьте полку командой as")
  print("Текущий список документов: ")
  l()
  return
 print("Текущий список документов: ")
 l()
 return


while True:
   A = input("Введите команду: ")
   if A == "p":
        p()
   elif A == "s":
        s()
   elif A == "l":
        l()
   elif A == "ads":
        ads()
   elif A == "ds":
        ds()
   elif A == "ad":
        ad()
   elif A == "q":
       print('Работа окончена.')
       break
   else:
       print("Такой команды не существует")
