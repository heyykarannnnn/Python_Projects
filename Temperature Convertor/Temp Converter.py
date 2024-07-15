def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    a = int(input("Enter 1 for Celsius to Fahrenheit conversion\nEnter 2 for Fahrenheit to Celsius conversion\n"))
    if a == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(celsius))
        main()
    elif a == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius: ", fahrenheit_to_celsius(fahrenheit))
        main()
    else:
        print("Invalid choice! Please try again.")
        main()
main()