
def join_numbers(numbers):
    return ''.join([str(numbers[0]), str(numbers[-1])])


def find_numbers(line):
    valid_text_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]

    numbers = []

    for index, char in enumerate(line):
        if char.isdigit():
            numbers.append(int(char))
        elif char.isalpha():
            for number in valid_text_numbers:
                if number in line[index:index+len(number)]:
                    numbers.append(valid_text_numbers.index(number) + 1)
                    break

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