import heapq

def min_connection_cost(cables):
    """
    Знаходить мінімальні витрати на з'єднання кабелів

    Args:
        cables (list): Список довжин кабелів

    Returns:
        int: Мінімальні загальні витрати на з'єднання
    """
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Поки в нас є більше одного кабеля
    while len(cables) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Рахуємо вартість їх з'єднання
        connection_cost = first + second
        # Додаємо до загальної вартості
        total_cost += connection_cost

        # Додаємо з'єднаний кабель назад до купи
        heapq.heappush(cables, connection_cost)

    return total_cost

def merge_k_lists(lists):
    """
    Об'єднує k відсортованих списків в один відсортований список
    використовуючи мінімальну купу

    Args:
        lists (List[List[int]]): Список відсортованих списків

    Returns:
        List[int]: Об'єднаний відсортований список
    """
    # Створюємо мінімальну купу для зберігання елементів
    heap = []
    result = []

    # Створюємо початкові елементи купи
    # Додаємо перший елемент кожного списку разом з індексом списку та позицією
    for i, lst in enumerate(lists):
        if lst:  # перевіряємо, що список не порожній
            heapq.heappush(heap, (lst[0], i, 0))

    # Поки купа не порожня
    while heap:
        val, list_ind, elem_ind = heapq.heappop(heap)
        result.append(val)

        # Якщо в поточному списку ще є елементи
        if elem_ind + 1 < len(lists[list_ind]):
            next_elem = lists[list_ind][elem_ind + 1]
            heapq.heappush(heap, (next_elem, list_ind, elem_ind + 1))

    return result

# Тестування функцій
def test_cables():
    print("Тест 1: З'єднання кабелів")
    cables = [4, 3, 2, 6]
    cost = min_connection_cost(cables.copy())
    print(f"Кабелі довжиною {cables}")
    print(f"Мінімальні витрати на з'єднання: {cost}")

    print("\nТест 2: З'єднання кабелів")
    cables = [1, 2, 3, 4, 5]
    cost = min_connection_cost(cables.copy())
    print(f"Кабелі довжиною {cables}")
    print(f"Мінімальні витрати на з'єднання: {cost}")

def test_merge():
    print("\nТест 3: Об'єднання відсортованих списків")
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(lists)
    print(f"Вхідні списки: {lists}")
    print(f"Відсортований список: {merged}")

    print("\nТест 4: Об'єднання відсортованих списків")
    lists = [[1], [2], [3], [4, 5, 6]]
    merged = merge_k_lists(lists)
    print(f"Вхідні списки: {lists}")
    print(f"Відсортований список: {merged}")

if __name__ == "__main__":
    test_cables()
    test_merge()