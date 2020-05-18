num_stack = []


def push_digits(num):
    while num != 0:
        num_stack.append(num % 10)
        num = int(num / 10)


def reverse_number(num):
    push_digits(num)

    reverse = 0
    i = 1

    while len(num_stack) > 0:
        reverse = reverse + (num_stack[len(num_stack) - 1] * i)
        num_stack.pop()
        i = i * 10

    return reverse


number = 35592
print(reverse_number(number))
