def function (num1,num2):
    if num1 < 0 or num2 < 0:
        raise Exception('Oops!That was not valid number.')
    list =[]
    if num2 <  num1 :
        for num in range(num2, num1 + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
        print(list)
    else:
        for num in range(num1, num2 + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
        print(list)
    if not list:
        print('NoSimpleDigits')

function(num1 = int(input('Enter first number: ')),num2 = int(input('Enter second number: ')))


