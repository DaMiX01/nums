def find_missing_nums(nums):
	a = len(nums)
	list = [i for i in range(1, a + 1) if i not in nums]
	return print(list)
