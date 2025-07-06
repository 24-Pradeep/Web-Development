while True:
    ch = input("Enter operator(+,-,*,/,%) or q for quiting: ")
    
    if ch == "q":
       print("Exiting Calculator")
       break
    
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    

   

    match ch:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            if b == 0:
                print("Error: Division by zero")
            else:
                print(a/b)
        case "%":
            if b == 0:
                print("Error: Modulo by zero")
            else:
                print(a%b)
        case _:
            print("Invalis operator.")        