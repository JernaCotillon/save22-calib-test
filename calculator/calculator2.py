def add(num1,num2):
	return num1 + num2

def sub(num1,num2):
	return num1 - num2

def mul(num1,num2):
	return num1 * num2

def div(num1,num2):
	return num1 / num2

def input1():
	return int(raw_input("Enter number 1: "))

def input2():
	return int(raw_input("Enter number 2: "))

def inputop():
	return raw_input("Input operator: ")

def operator(number1,op,number2):
	if op == '+':
		return add(number1,number2)

	elif op == '-':
		return sub(number1,number2)

	elif op == '*':
		return mul(number1,number2)

	elif op == '/':
		return div(number1,number2)
	else:
		print "Invalid Operand"
	return none
 
def output(number1,op,number2,ans):
  return '{} {} {} = {}'.format(number1,op,number2,ans)

def main():
  number1 = input1()
  op = inputop().strip()
  number2 = input1()
  ans = operator(number1,op,number2)
  print output(number1,op,number2,ans)
 
if __name__ == "__main__":
	main()