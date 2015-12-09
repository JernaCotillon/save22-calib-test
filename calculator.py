def add(num1,num2):
	sum= num1 + num2
	return sum

def sub(num1,num2):
	diff= num1 - num2
	return diff

def mul(num1,num2):
	prod= num1 * num2
	return prod

def div(num1,num2):
	quot= num1 / num2
	return quot

def input1(int1):
	return int1

def input1(int2):
	return int2
		
def main():
	number1 = input("Number 1: ")
	input1(number1)

	operator = raw_input("Operand: ")

	number2 = input("Number 2: ")
	input1(number2)

	if operator == 'add' or operator == '+'  or operator == 'addition' or operator == 'plus':

		print "The sum of number %d and number %d is %d"% (number1, number2,add(number1,number2))

	elif operator == 'sub' or operator == '-'  or operator == 'subtration' or operator == 'minus':
		print "The difference of number %d and number %d is %d"% (number1, number2,sub(number1,number2))

	elif operator == 'mul' or operator =='multiply' or operator == '*'  or operator == 'multiplication' or operator == 'times':
		print "The product of number %d and number %d is %d"% (number1, number2,mul(number1,number2))

	elif operator == 'div' or operator == 'divide' or operator == '/'  or operator == 'division':
		print "The quotient of number %d and number %d is %d"% (number1, number2,div(number1,number2))
	else:
		print "Invalid Operand"

	

if __name__ == "__main__":
	main()