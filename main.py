def get_series(n):
    even_list = []
    odd_list = []
    square_list = []
    for i in range(n):
        if i % 2 == 0:
            even_list.append(i)
        elif i % 2 == 1:
            odd_list.append(i)
        square_list.append(i**2)

    return even_list, odd_list, square_list


n = 10
series = get_series(n)
print(series[0])
print(series[1])
print(series[2])
