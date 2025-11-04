# pip install mysql-connector-python #komanda, kurią pasileidžiame terminale, kad susidiegti į projektą mysql
# connectorių
import mysql.connector

headers = ['id','brand','type','price']
DB_CONFIG = {
    'host':'localhost', #arba 127.0.0.1
    'port':3312,
    'user':'root',
    'password':'root',
    'database':'sinsay'
}
def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_clothes():# ============ JUMS AKTUALIAUSIA FUNKCIJA ================
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from clothes")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    clothes = []
    for row in rows:
        item = {}
        for i in range(len(headers)):
            item[headers[i]] = row[i]
        clothes.append(item)
    return clothes

def add_item(a="",clothes=[]):
    print("jus pasirinkote itraukti nauja preke i sarasa")
    print("iveskite prekes gamintoja")
    manufacturer = input()
    print("iveskite prekes tipa")
    type = input()
    print("iveskite prekes kaina")
    price = float(input())

    conn = get_conn()
    cur = conn.cursor()
    cur.execute('insert into clothes (brand, type, price) values (%s,%s,%s)',(manufacturer,type,price))
    conn.commit()
    cur.close()
    conn.close()

def edit_item(clothes):
    print("jus pasirinkote redaguoti preke")
    print_items(clothes)
    print("irasykite prekes id kuria norite redaguoti")
    edit_id = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from clothes where id = %s",(edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close() #uzdarom connections nes zemiau yra inputai, gali vartotojas ilgai duomenu nesuvesti ir 'kabes'
    # connectionas

    if row is None:
        print("ivestas neteisingas Id, redagavimas nutrauktas")
        return

    print("iveskite prekes gamintoja")
    manufacturer = input()
    print("iveskite prekes tipa")
    type = input()
    print("iveskite prekes kaina")
    price = float(input())

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("update clothes set brand = %s, type = %s, price = %s where id = %s",(manufacturer,type,price,edit_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_item(clothes):
    print("jus pasirinkote pasalinti preke")
    print_items(clothes)
    print("irasykite prekes id kuria norite salinti")
    del_id = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute('delete from clothes where id = %s',(del_id,)) # nepamirskite kablelio
    conn.commit()

    cur.close()
    conn.close()
    print("irasas sekmingai istrintas")

def get_id(clothes = None):
    return 0

def print_items(clothes):
    clothes = load_clothes()
    for item in clothes:
        print(f"{item['id']}. Gamintojas - \"{item['brand']}\", tipas - {item['type']}, kaina -"
              f" {item['price']} "
              f"eur.")