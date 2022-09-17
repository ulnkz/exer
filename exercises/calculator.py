lang = "EN"
lang_opt = input("Enter L to change language or Enter to continue: ")
while lang_opt == 'l':
    if lang == "RU":
        lang = "EN"
        lang_opt = input("Enter L to change language or Enter to continue: ")
    else:
        lang = "RU"
        lang_opt = input("Введите L, чтобы сменить язык, или нажмите на Enter, чтобы продолжить: ")
if lang == "EN":
    a = "Enter first number: "
    o = "Enter operation (+, -, *, /)"
    b = "Enter second number: "
    r = "Result: "
    e = "Error, use just math symbols"
    c = "Enter 'y' to continue and other key to finish"
if lang_opt == "RU":
    a = "Введите первую цифру: "
    o = "Введите операцию (+, -, *, /): "
    b = "Введите вторую цифру: "
    r = "Результат: "
    e = "Ошибка, введите только математические символы"
    c = "Введите 'y' чтобы продолжить, либо любую другую клавишу чтобы закончить: "

cont = 'y'
while cont == 'y':
    num_a = int(input(a))
    oper = input(o)
    num_b = int(input(b))

    if oper == "+":
        print(r, num_a + num_b)
    elif oper == "-":
        print(r, num_a - num_b)
    elif oper == "*":
        print(r, num_a * num_b)
    elif oper == "/":
        print(r, num_a / num_b)
    else:
        print(e)