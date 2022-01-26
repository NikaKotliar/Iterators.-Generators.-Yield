# Написать генератор, который принимает список списков, и возвращает их плоское представление.
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, ['noiwenf', 4,6,7, 9648498], 2, None],
]

flat_list = []

def flat_generator(lists):
	for i in range(len(lists)):
		if type(lists[i]) == list:
			my_list = flat_generator(lists[i])
			for i in my_list:
				yield i
		else:
			yield lists[i]

for item in  flat_generator(nested_list):
	print(item, end=' ')



# for item in  flat_generator(nested_list):
# 	print(item, end=' ')





# Работает для вложенности 2

# def flat_generator(lists):
# 	for i in range(len(lists)):
# 		for j in range(len(lists[i])):
# 			yield lists[i][j]
#
# for item in  flat_generator(nested_list):
# 	print(item, end=' ')
