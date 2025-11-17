from typing import Iterable, Iterator, List, TypeVar
import heapq
import random

T = TypeVar("T")


def merge_k_lists(lists: Iterable[Iterable[T]]) -> List[T]:
    """Об'єднує k відсортованих ітерованих об'єктів в один відсортований список.

    Використовує мін-купу (min-heap), щоб багаторазово брати найменший головний
    елемент серед активних ітераторів. Вхідні ітеровані об'єкти мають бути
    відсортовані за зростанням.

    Args:
        lists: Ітерований об'єкт, що містить відсортовані ітеровані об'єкти
               (наприклад, списки, кортежі, генератори).

    Returns:
        Новий список, що містить усі елементи з вхідних даних,
        відсортовані за зростанням.

    Notes:
        - Порожні ітеровані об'єкти ігноруються.
        - Якщо вхідні ітеровані об'єкти не відсортовані, результат не буде
          глобально відсортованим; перед викликом переконайтеся, що вхідні
          дані відсортовані.
    """
    heap: list = []
    # Створюємо ітератори та додаємо перший елемент кожного (якщо він є) до купи.
    for idx, seq in enumerate(lists):

        it = iter(seq)
        try:
            first = next(it)
        except StopIteration:
            # пропускаємо порожні ітеровані об'єкти
            continue
        # Додаємо кортеж (значення, індекс_джерела, ітератор), щоб при рівності
        # значень порівняння відбувалося за індексом
        heapq.heappush(heap, (first, idx, it))

    merged: List[T] = []
    # Продовжуємо, доки купа не стане порожньою
    while heap:
        # Вилучаємо найменший елемент (значення, індекс, ітератор) з купи
        value, src_idx, it = heapq.heappop(heap)
        merged.append(value)

        # Намагаємося отримати наступний елемент з того ж ітератора
        try:
            nxt = next(it)
        except StopIteration:
            # Якщо ітератор вичерпано, переходимо до наступної ітерації циклу
            continue

        # Додаємо наступний елемент до купи
        heapq.heappush(heap, (nxt, src_idx, it))

    return merged


# Генерує відсортований список із випадковими цілими числами в інтервалі [min, max]
def rand_list(n, min=0, max=100):
    return sorted([random.randint(min, max) for _ in range(n)])


if __name__ == "__main__":
    # Приклад використання
    lists = [rand_list(10), rand_list(8), rand_list(6)]

    print("Початкові списки:", lists)
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
