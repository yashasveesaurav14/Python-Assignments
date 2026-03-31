from Temperature import f_to_c, c_to_f, c_to_k

try:
    while True:
        print("Choose an option:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Celsius to Kelvin")

        o = int(input("Enter choice: "))

        if o == 1:
            f = float(input("Enter Fahrenheit: "))
            print("Celsius:", f_to_c(f))

        elif o == 2:
            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", c_to_f(c))

        elif o == 3:
            c = float(input("Enter Celsius: "))
            print("Kelvin:", c_to_k(c))

        else:
            print("Invalid choice")
            break

        p = input("Continue? (y/n): ")
        if p.lower() == 'n':
            break

except:
    print("Error occurred")