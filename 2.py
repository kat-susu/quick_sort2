import pivot

comparisons = 0
swaps = 0


def partition_lomuto(arr, low, high):
    global comparisons, swaps
    pivot = arr[high]
    i = low

    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    swaps += 1
    return i


def quick_sort(arr, low, high):
    global swaps
    if low < high:
        p_idx = pivot.get_pivot(arr, low, high, strategy="random")

        arr[p_idx], arr[high] = arr[high], arr[p_idx]
        swaps += 1

        pi = partition_lomuto(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr_2 = [
    [1, 2, 3, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1],
    [4, 1, 7, 3, 6, 2, 5],
    [3, 3, 3, 3, 3]
]

print("Задание 2.")
for arr in arr_2:
    comparisons = 0
    swaps = 0
    print(f"\nИсходный массив: {arr}")
    quick_sort(arr, 0, len(arr) - 1)
    print(f"Отсортированный массив: {arr}\n")
    print(f"Сравнений = {comparisons}, Обменов = {swaps}\n")

'''
Вопросы:

1. Случайный выбор опорного элемента необходим для защиты алгоритма от падения производительности на специфических (например, уже упорядоченных) входных данных,
так как он разрушает фиксированную зависимость между исходной структурой массива и логикой разделения элементов.

2. Теоретически худший сценарий всё еще возможен,
если генератор случайных чисел на каждом шаге рекурсии будет случайно выбирать исключительно минимальный или максимальный элемент подмассива,
однако вероятность такого совпадения на практике очень мала.

3. Pivot превращает худший случай в случайную величину,
благодаря чему на любых реальных входных данных алгоритм демонстрирует стабильную среднюю скорость вне зависимости от того, был ли массив изначально отсортирован.
'''

