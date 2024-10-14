'''
Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки
 (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для
 "обробки", імітуючи таким чином роботу сервісного центру.



Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для системи обробки заявок:

import Queue

Створити чергу заявок
queue = Queue()

Функція generate_request():
    Створити нову заявку
    Додати заявку до черги

Функція process_request():
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста

Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок



У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує нові заявки та додає їх до
 черги, та process_request(), яка обробляє заявки, видаляючи їх із черги. Головний цикл програми виконує ці функції,
  імітуючи постійний потік нових заявок та їх обробку.
'''
import sys
from queue import Queue
import random

queue = Queue()


class Request:
    def __init__(self, request_id, name, price):
        self.request_id = request_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Request {self.request_id}: {self.name}, Price: {self.price} грн"


def generate_request():
    request_id = random.randint(100000, 999999)
    name = f"Product {random.randint(1, 10)}"
    price = random.uniform(100, 1000)
    order = Request(request_id, name, round(price, 2))
    queue.put(order)
    print(f"New request added: {order}")


def process_request():
    action = input("Press Q for exit")

    if action == "Q":
        sys.exit()

    if not queue.empty():
        request = queue.get()
        print(f"Processing {request}")
    else:
        print("Queue is empty")


while True:
    action = input("Press 'g' to generate a request, 'p' to process a request, or 'q' to quit: ").strip().lower()

    if action == 'g':
        generate_request()
    elif action == 'p':
        process_request()
    elif action == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")
