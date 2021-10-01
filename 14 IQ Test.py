def iq_test(numbers):
    numbers, counter_is_odd, counter_is_even = numbers.split(), 0, 0
    index_first_odd, index_first_even = 0, 0 
    numbers = [int(numbers[i]) for i in range(len(numbers))]
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1 or numbers[i] == '1':
            if counter_is_odd == 0:
                index_first_odd = i
            counter_is_odd += 1
        elif numbers[i] % 2 == 0:
            if counter_is_even == 0:
                index_first_even = i
            counter_is_even += 1
    if counter_is_odd >= 2 and counter_is_even == 1:
        return index_first_even + 1
    elif counter_is_even >= 2 and counter_is_odd == 1:
        return index_first_odd + 1
