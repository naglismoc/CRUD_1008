from file_CRUD import *

def print_info():
    print("Pasirinkite, ką norite daryti")
    print("1. Peržiūrėti parduotuvės prekes")
    print("2. Pridėti naują prekę")
    print("3. Redaguoti prekę")
    print("4. Ištrinti prekę")
    print("5. Išeiti iš parduotuvės")

clothes = load_clothes()

id_counter = 3

while True:
    print_info()
    option = input()
    match option:
        case '1':
            print("jus pasirinkote perziureti prekes")
            print_items(clothes)
        case '2':
            id_counter = add_item(id_counter, clothes)
        case '3':
            edit_item(clothes)
        case '4':
            delete_item(clothes)
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

