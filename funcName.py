records = {'Pedro': 22, 'Juan': 23 , 'Pepe': 24}

def fN(name):
    return name[0]

def age(a):
    return a[1]


choice = raw_input("Function\t  Lambda\nA\tB\tC\tD\nChoice:")

if choice == "A" or choice == "a":
    for spam in sorted(records.items(), key=fN):
        print spam

elif choice == "B" or choice == "b":
  for spam in sorted(records.items(), key=age):
    print spam
    
elif choice == "C" or choice == "c":
  print sorted(records.items(), key=lambda value:value[0])
    
elif choice == "D" or choice == "d":
  print sorted(records.items(), key=lambda value:value[1])

else:
    print "Invalid Input!"