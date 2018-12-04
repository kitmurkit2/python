def function (num1,num2):
     if num1 < 0 or num2 < 0:
       raise Exception('Oops!That was not valid number.')
     temp = False
     if num1%num2 == 0 :
        temp = True
     return temp

print(function(num1 = int(input('Enter first number: ')),num2 = int(input('Enter second number: '))))
