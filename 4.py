def partition_lomuto(arr, low, high):
    pivot = arr[high][0]
    i = low
    for j in range(low, high):
        if arr[j][0] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quick_sort(arr, low, high):
    if low < high:
        pi = partition_lomuto(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

arr_4 = [
    (5, "A", 0),
    (3, "B", 1),
    (5, "C", 2),
    (2, "D", 3),
    (5, "E", 4),
]

print("Задание 4.")
print(f"\nИсходный массив: {arr_4}")
quick_sort(arr_4, 0, len(arr_4) - 1)
print(f"Отсортированный массив: {arr_4}\n")

elements_5 = [x for x in arr_4 if x[0] == 5]
print(f"Элементы с ключом 5: {[x[1] for x in elements_5]}\n")

'''
Вывод:
Реализованная быстрая сортировка оказалась неустойчивой,
так как изначальный порядок одинаковых элементов `A -> C -> E` полностью перепутался и превратился в `E -> C -> A`.
Это происходит из-за того, что алгоритм меняет элементы местами через весь массив (например, перекидывая опорный элемент из самого конца в середину).
Ему важно лишь сделать так, чтобы числа шли по возрастанию (2, 3, 5, 5, 5), а на сохранение порядка букв внутри этих чисел у него просто нет логических условий.
'''
