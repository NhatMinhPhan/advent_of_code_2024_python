text = ''
sum = 0

with (open('adventofcode_input.txt', 'r') as file):
    text = file.read().strip()

    while True:
        mul_index = text.find('mul(')

        if mul_index < 0:
            break

        test_index = 4
        factors = ['', '']
        factor_index = 0
        while True:
            if text[test_index].isdigit():
                factors[factor_index] += text[test_index]
            elif text[test_index] == ',' and factor_index == 0:
                factor_index = 1
            elif text[test_index] == ')' and factor_index == 1:
                if factors[0] != '' and factors[1] != '':
                    sum += (int(factors[0]) * int(factors[1]))
                break
            else:
                break
            test_index += 1


        text = text[test_index:]

    print(sum)