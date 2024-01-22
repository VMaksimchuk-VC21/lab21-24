def calculator(operation, a, b):
    if operation == 'addition':
        return a + b
    elif operation == 'multiplication':
        return a * b
    else:
        return None


result = calculator('addition', 4, 5)
print(result)

result = calculator('multiplication', 4, 5)
print(result)