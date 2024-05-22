def calculate(operation,a,b):
    match operation:
        case '+':
            result = a+b
            print(f'{a} + {b} = {result}')
        case '-':
            result = a - b
            print(f'{a} - {b} = {result}')
        case '*':
            result = a * b
            print(f'{a} * {b} = {result}')
        case '/':
            if b!=0:
                result = a / b
                print(f'{a} / {b} = {result}')
            else:
                print("Dzielenie przez 0 jest wyjątkiem")
        case _:
            print("Niewłaściwy operator, tylko -> {+,-,*,/}")
