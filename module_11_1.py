import numpy as np

# Создаем массив чисел от 0 до 9
arr = np.arange(10)

# Умножаем все элементы массива на 2
arr_mult = arr * 2
print("Массив, умноженный на 2:", arr_mult)

# Вычисляем сумму всех элементов массива
arr_sum = np.sum(arr)
print("Сумма элементов массива:", arr_sum)

# Создаем двумерный массив и вычисляем его среднее значение
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mean_value = np.mean(matrix)
print("Среднее значение матрицы:", mean_value)
