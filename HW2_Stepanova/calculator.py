def multiple(a,b):
	"Функция умножения двух чисел"
	return a*b

def substraction(a, b):
	"Функция вычитания b из a"
	return a - b

def addition (a, b):
	"Функция сложения двух чисел"
	return a + b

def division (a, b):
	"Функция деления a на b"
	if b!= 0:
		return a/b
	else:
		return "деление на 0!"

def main():
    exp=input("Введите выражение: ").split()
    a,operation,b = float(exp[0]), exp[1], float(exp[2])
    if operation == "+":
        print(addition(a,b))
    elif operation == "-":
        print(substraction(a,b))
    elif operation == "*":
        print(multiple(a,b))
    else:
        print(division(a,b))

main()
