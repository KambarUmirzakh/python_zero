def info_sudent(name:str, age:int, group:str):
    student = {
        "name": name,
        "age": age,
        "group": group
        }
    print(student)

def task1(n:str):
    print("task1 - " , n)

def price_info():
    prices = {"bread": 150, "milk": 300, "cheese": 1500}
    prices = list(map(lambda p: p*2, prices.values()))

    print(prices)