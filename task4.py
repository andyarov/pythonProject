# list comprehension [что-то с переменной for переменная in итерируемый объект]
nums = [int(i) for i in input().split()]
digits = [nums[n] for n in range(1, len(nums)) if nums[n-1] < nums[n]]
'''for i in range(1,len(nums)-1):
    if nums[i-1] < nums[i]:
        digits.append(i)'''
print(digits)
