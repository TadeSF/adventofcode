
def join_numbers(numbers):
    return ''.join([str(numbers[0]), str(numbers[-1])])


def find_numbers(line):
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(int(char))
    
    if len(numbers) == 1:
        numbers.append(numbers[0])

    return join_numbers(numbers)


def main():
    numbers = []
    with open('1.txt', 'r') as f:
        for line in f:
            numbers.append(find_numbers(line))
    
    summe = 0
    for number in numbers:
        print(number)
        summe += int(number)
    
    print(summe)

main()