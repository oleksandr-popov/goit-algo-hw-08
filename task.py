import heapq


def min_cost_to_connect_cables(cable_lengths):
    """
    Обчислює мінімальну вартість з'єднання всіх кабелів в один цілий кабель.
    Вартість з'єднання двох кабелів дорівнює сумі їхніх довжин.
    """

    # Ініціалізуємо список як мін-купу (min-heap)
    # Властивість купи є критичною для ефективного пошуку двох найкоротших кабелів.
    heapq.heapify(cable_lengths)

    # Ініціалізуємо лічильник загальної вартості
    total_cost = 0

    # Продовжуємо злиття, доки в купі не залишиться лише один кабель (кінцевий об'єднаний)
    while len(cable_lengths) > 1:
        # Вилучаємо два найменші кабелі з купи
        # Це операція складності O(log n).
        first_shortest = heapq.heappop(cable_lengths)
        second_shortest = heapq.heappop(cable_lengths)

        # Обчислюємо вартість злиття (сума їхніх довжин)
        merge_cost = first_shortest + second_shortest

        # Додаємо вартість злиття до загальної суми
        total_cost += merge_cost

        # Додаємо довжину новооб'єднаного кабелю назад до купи
        # Це представляє новий кабель, який може бути об'єднаний на наступних кроках.
        heapq.heappush(cable_lengths, merge_cost)

        # Виводимо проміжні результати для відстеження процесу
        print(
            f"Об'єднання кабелів {first_shortest} та {second_shortest} коштує {merge_cost}. Загальна вартість: {total_cost}"
        )
        print(f"Поточні довжини кабелів у купі: {cable_lengths}")

    # Кінцевий результат – це загальна накопичена вартість
    return total_cost


if __name__ == "__main__":
    # Приклад довжин кабелів
    initial_lengths = [7, 1, 6, 4]

    # Варіант використання випадкових значень для довжин кабелів
    # import random
    # initial_lengths = [random.randint(1, 25) for _ in range(6)]
    print(f"Початкові довжини кабелів: {initial_lengths}")
    print("-" * 50)

    # Запускаємо функцію
    min_cost = min_cost_to_connect_cables(initial_lengths)

    print("-" * 50)
    print("Мінімальні витрати для об'єднання усіх кабелів:", min_cost)
