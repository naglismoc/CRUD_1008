clothes = [
    {
        'id':1,
        'brand':'nike',
        'type':'shoes',
        'price':35
    },
    {
        'id':2,
        'brand':'puma',
        'type':'hoodie',
        'price':40
    },
    {
        'id':3,
        'brand':'bugatti',
        'type':'shoes',
        'price':120
    }
]

id_counter = 3
while True:
    print("Choose what you want to do")
    print('1. see shop items')
    print('2. add new item')
    print("3. edit item")
    print("4. delete item")
    print("5. exit shop")

    option = input()
    match option:
        case '1':
            print("jus pasirinkote perziureti prekes")
            for item in clothes:
                print(item)
        case '2':
            print("jus pasirinkote itraukti nauja preke i sarasa")
            print("iveskite prekes gamintoja")
            manufacturer = input()
            print("iveskite prekes tipa")
            type = input()
            print("iveskite prekes kaina")
            price = float(input())
            id_counter +=1
            item = {'id':id_counter, "brand":manufacturer, "type":type, "price":price}
            clothes.append(item)

        case '3':
            print("jus pasirinkote redaguoti preke")
            print("irasykite prekes id kuria norite redaguoti")
            edit_id = input()
            for i, item in enumerate(clothes):
                if str(item['id']) == edit_id:
                    print(item)
                    print("iveskite prekes gamintoja")
                    clothes[i]['brand'] = input()
                    print("iveskite prekes tipa")
                    clothes[i]['type'] = input()
                    print("iveskite prekes kaina")
                    clothes[i]['price'] = float(input())
        case '4':
            print("jus pasirinkote pasalinti preke")
            print("irasykite prekes id kuria norite salinti")
            del_id = input()
            for item in clothes:
                if str(item['id']) == del_id:
                    clothes.remove(item)
                    break
        case '5':
            print("jus pasirinkote iseiti is parduotuves")
            break
        case _ : #defaultas, kai ivedama belekas
            print("Pasitikrinkite ka ivedete")






















































































# #          0  1  2   3   4  5
# numbers = [1, 4, 10, 6 , 8 ,5] #list
# print(numbers)
# print(numbers[2])
# student = {'name':"Naglis", 'surname':'Mockevicius', 'age': 35}
# student1 = {'name':"Veronika", 'surname':'Motuzaite', 'age': 35}
# student2 = {'name':"Vikrotas", 'surname':'Tadaras', 'age': 35}
#
# print(student)
# print(student['name'])
# print(student['surname'])
# print(student['age'])
#
# students = []
# students.append(student)
# students.append(student1)
# students.append(student2)
#
# print(students)
#
# print(student.keys())
# print(student.values())
#
# txt = input()
# print(f'jus pasakete {txt}')
#
# print("labas")
#
#

