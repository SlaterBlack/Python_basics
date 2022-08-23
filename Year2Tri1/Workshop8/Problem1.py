def rotate(numbers):
    x = (len(numbers))
    print(numbers)
    for i in range(len(numbers)):
        numbers.append(0)
        for k in range(len(numbers)):
            temp=numbers[k-1]
            numbers[k-1]=numbers[k]
            numbers[k]=temp
        number.pop(-1)
        print(numbers)
    return
num = (input('Please enter values '))
number = num.split(',')
rotate(number)


