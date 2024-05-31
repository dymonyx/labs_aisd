def min_subarray(arr, threshold):
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    start = 0
    result = []

    for end in range(n):
        current_sum += arr[end]

        # Сдвигаем левую границу окна вправо до тех пор, пока сумма подмассива больше порога
        while current_sum >= threshold and start <= end:
            # Если длина текущего подмассива меньше найденной ранее минимальной длины, обновляем результат
            if (end - start + 1) < min_length:
                min_length = end - start + 1
                result = arr[start:end + 1]

            # Уменьшаем текущую сумму, исключая элемент arr[start] из окна
            current_sum -= arr[start]
            start += 1

    # Если ни один подмассив не найден, возвращаем пустой список
    if min_length == float('inf'):
        return []

    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 4, -2, 3, -1, 2, -4, 3], 3, "Подмассив для массива {} с порогом {}: {}"),
        ([2, -1, 2, 3, -4, 2, -2, 3], 4, "Подмассив для массива {} с порогом {}: {}"),
        ([1, 2, 3, 4, 5, 1, 2, 3, 5, 4], 11, "Подмассив для массива {} с порогом {}: {}"),
        ([-1, -2, -3, -4, -5], -10, "Подмассив для массива {} с порогом {}: {}")
    ]

    for arr, threshold, message in test_cases:
        result = min_subarray(arr, threshold)
        print(message.format(arr, threshold, result))
