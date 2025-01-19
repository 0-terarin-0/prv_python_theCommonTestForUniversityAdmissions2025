days_to_make = [4,1,3,1,3,4,2,4,3]
num_works = 9
days_clear = [1,1,1]
num_members = 3
for index_works in range(num_works):
    min_index = days_clear.index(min(days_clear))
    print(f'工芸品{index_works + 1}→部員{min_index + 1}:{days_clear[min_index]}日目〜{days_clear[min_index] + days_to_make[index_works] - 1}日目')
    days_clear[min_index] = days_clear[min_index] + days_to_make[index_works]
