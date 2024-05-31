def min_subarray(arr, threshold):
    n = len(arr)
    min_sum = float('inf')
    min_length = float('inf')
    current_sum = 0
    start = 0
    result = []

    for end in range(n):
        current_sum += arr[end]

        # Сдвигаем левую границу окна вправо до тех пор, пока сумма подмассива больше порога
        while current_sum > threshold and start <= end:
            # Если текущая сумма меньше найденной ранее минимальной суммы, обновляем результат
            if current_sum < min_sum or (current_sum == min_sum and (end - start + 1) < min_length):
                min_sum = current_sum
                min_length = end - start + 1
                result = [start, end + 1]

            # Уменьшаем текущую сумму, исключая элемент arr[start] из окна
            current_sum -= arr[start]
            start += 1

    # Если ни один подмассив не найден, возвращаем пустой список
    if min_sum == float('inf'):
        return []

    return arr[result[0]:result[1]]


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 2, 4, 3, 2, 3], 3, "Подмассив для массива {} с порогом {}: {}"),
        ([2, 2, 2, 3, 2, 2, 3], 4, "Подмассив для массива {} с порогом {}: {}"),
        ([1, 2, 3, 4, 5, 1, 2, 3, 5, 4], 11, "Подмассив для массива {} с порогом {}: {}"),
        ([5, 4, 3, 2, 1, 2, 3, 4, 5], 100, "Подмассив для массива {} с порогом {}: {}"),
        ([21, 10, 3, 22], 25, "Подмассив для массива {} с порогом {}: {}"),
        ([1, 1, 1, 1, 1, 4], 2, "Подмассив для массива {} с порогом {}: {}")
    ]

    for arr, threshold, message in test_cases:
        result = min_subarray(arr, threshold)
        print(message.format(arr, threshold, result))
