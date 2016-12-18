import utilities

abundant_nums = []

for i in range(0, 28124):
    if utilities.check_abundant(i):
        abundant_nums.append(i)
        print(i)

abundant_nums =  sorted(abundant_nums)

not_sum_of_abundant_nums = []

for i in range(0, 28124):
    for abundant_num in abundant_nums:
        if abundant_num > i:
            not_sum_of_abundant_nums.append(i)
            print(i)
            break

        if i - abundant_num in abundant_nums:
            break
    else:
        not_sum_of_abundant_nums.append(i)
        print(i)

print(not_sum_of_abundant_nums)
print(sum(not_sum_of_abundant_nums))