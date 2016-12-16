sum_of_squares = 0

for i in range(1, 101):
    sum_of_squares += i ** 2

square_of_sum = sum(range(1, 101)) ** 2

print(str(square_of_sum) + " - " + str(sum_of_squares) + " = " + str(square_of_sum - sum_of_squares))