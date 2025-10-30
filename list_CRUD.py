
def print_items(clothes):
    for item in clothes:
        print(f"{item['id']}. Gamintojas - \"{item['brand']}\", tipas - {item['type']}, kaina -"
              f" {item['price']} "
              f"eur.")
def add_item(id_counter, clothes):
    print("jus pasirinkote itraukti nauja preke i sarasa")
    print("iveskite prekes gamintoja")
    manufacturer = input()
    print("iveskite prekes tipa")
    type = input()
    print("iveskite prekes kaina")
    price = float(input())
    id_counter += 1
    item = {'id': id_counter, "brand": manufacturer, "type": type, "price": price}
    clothes.append(item)
    return id_counter
def edit_item(clothes):
    print("jus pasirinkote redaguoti preke")
    print_items(clothes)
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

def delete_item(clothes):
    print("jus pasirinkote pasalinti preke")
    print_items(clothes)
    print("irasykite prekes id kuria norite salinti")
    del_id = input()
    for item in clothes:
        if str(item['id']) == del_id:
            clothes.remove(item)
            break
