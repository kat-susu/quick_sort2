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


def quick_sort_median(arr, low, high):
    global swaps
    if low < high:
        p_idx = pivot.get_pivot(arr, low, high, strategy="median_of_three")

        arr[p_idx], arr[high] = arr[high], arr[p_idx]
        swaps += 1

        pi = partition_lomuto(arr, low, high)
        quick_sort_median(arr, low, pi - 1)
        quick_sort_median(arr, pi + 1, high)


def quick_sort_last(arr, low, high):
    if low < high:
        pi = partition_lomuto(arr, low, high)
        quick_sort_last(arr, low, pi - 1)
        quick_sort_last(arr, pi + 1, high)


arr_3 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [4, 7, 1, 9, 2, 8, 3, 6, 5]
]

print("Задание 3.")
for arr in arr_3:
    comparisons = 0
    swaps = 0
    print(f"\nИсходный массив: {arr}")
    arr_median = arr.copy()
    quick_sort_median(arr_median, 0, len(arr) - 1)
    print(f"Отсортированный массив (медиана из трех): {arr_median}\n")
    print(f"Сравнений = {comparisons}, Обменов = {swaps}\n")

    comparisons = 0
    swaps = 0
    print(f"\nИсходный массив: {arr}")
    arr_last = arr.copy()
    quick_sort_last(arr_last, 0, len(arr) - 1)
    print(f"Отсортированный массив (последний элемент): {arr_last}\n")
    print(f"Сравнений = {comparisons}, Обменов = {swaps}\n")

'''
Вопросы:

1. Выбор медианы из трёх значительно снижает риски выбора наименьшего или наибольшего значения на отсортированных структурах данных.
Вместо этого алгоритм получает опорный элемент, максимально приближенный к реальной медиане массива,
что гарантирует более сбалансированное деление на подзадачи и защищает производительность от падения.

2. Медиана из трёх лишь защищает от самых плохих сценариев на упорядоченных последовательностях,
но не способна обеспечить деление массива ровно пополам (50/50), так как выборка всего из трех точек дает лишь приблизительную медиану.

3. Да, деградация алгоритма до худшей сложности всё ещё возможна на некоторых последовательностях,
например массив [0, 1, 2, 3, 4, 3, 2, 1, 0]. При оценке трех точек (первой 0, центральной 4 и последней 0) медиана выберет крайний ноль,
который является минимумом для всего набора данных, что приведет к худшему случаю.
'''