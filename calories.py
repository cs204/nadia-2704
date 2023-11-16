fruitList = {
'Apple': 130,
'Avocado': 50,
'Lime': 20,
}

fruit = input("Фрукт: ")
if fruit in fruitList:
    print(f"Калории: {fruitList.get(fruit)}")