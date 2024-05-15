operand_1=int(input('Enter operand1:'))
operand_2=int(input('Enter operand2:'))
operator=input('Enter the operator(+,-,*,/):')

#if(test expr):
    #statement1
#elif(test expr):
    #stetement2
#.....
#else:
    #statementn

if (operator == '+'):
    result = operand_1 + operand_2
elif (operator== '-'):
    result = operand_1 - operand_2
elif (operator == '*'):
    result = operand_1 * operand_2
elif (operator == '/'):
    result = operand_1 / operand_2
else:
    result='wrong operator fedin'

print('Result is :', result)