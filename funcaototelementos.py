def calculate_two_num(numbers):
	calculate = sum(numbers)
	count = len(numbers)
	return (calculate, count)
soma, contagem = calculate_two_num([5, 6])
print(f"A soma dos numero é {soma} e o total de elementos é {contagem}")