    nums = list(map(int, input().split("+")))
    sorted_nums = sorted(nums)
    count = 0
    for i in sorted_nums:
        if count == (len(sorted_nums) - 1):
            print(i)
        else:
            print(i, end="+")
            count += 1
