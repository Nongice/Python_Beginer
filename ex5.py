#ข้อ 1.1
print('Hello Python')

#ข้อ 1.2
print("Your name")

#ข้อ 1.3
print(25+5)
x = 25+5
print(x)

#ข้อ 1.4
num = '3'+'4'
print(num)

#ข้อ 1.5
hello = "hi"
print(hello * 3)

#ข้อ 1.6
dog = 'box'
print(dog *5)

#ข้อ 1.7
a,b,c = 1.5,5,'Superman'
print(type(a))
print(type(b))
print(type(c))

#ข้อ 1.8
a = "1.265"
print(type(a))
a = int(1.265)
print(type(a))

#ข้อ 1.9
a = 3
b = 3.5
c= 'PCC'
print(' {} {} {} ' .format(a,b,c))
print(' {2} {1} {0} ' .format(a,b,c))

#ข้อ 1.10
x = 2.151617298
print('{0}' .format(x))
print(' {:.2f}' .format(x))

#ข้อ 1.11
x,y,z = 25 , 'SUPER' , 160
print('name:{1} Age:{0} high:{2}'.format(x,y,z))

#ข้อ 1.12
print('Scince', end=' ')
print('Fair2017')

#ข้อ 1.13
area = 22/7 * 2 ** 2
print('Area = {:.2f}' .format(area))

#ข้อ 1.14
a,b = 15,10
X = (a**2)+(b**2)
print(X)

#ข้อ 1.15
X = ((5**2)+(8**2))-(2/(4**3))
print(X)

#ข้อ 1.16
x = 10
y = 5
print(x>=10)
print(y>=10)
print(x>=10 and y>=10)
print(x>=10 or y>=10)

# ข้อ 2.1
n = input("Input n : ")
print(n*2)
print(type(n))

# ข้อ 2.2
n = int(input("Input n : "))
print(n*2)
print(type(n))

# ข้อ 2.3
n = float(input('Enter n :'))
print(n*2)
print(type(n))

# ข้อ 2.4
product = input("Please enter your product name : ")

# ข้อ 2.5
price = input("Please enter your product price : ")

# ข้อ 2.6
amount = input("Please enter amount of your product : ")

#ข้อ 2.7
height = float(input('Enter Height : '))
width = float(input('Enter Width : '))
area = height * width
print('Area :',area)

#ข้อ 2.8
h = int(input("กรุณากรอกจำนวนชั่วโมง : "))
m  = int(input("กรุณากรอกจำนวนนาที : "))
s = int(input("กรุณากรอกจำนวนวินาที : "))
time = (h*(60**2))+(m*60)+s
print('เวลาทั้งหมด {} วินาที' .format(time))

#ข้อ 2.9
x = float(input("กรุณากรอกค่าตัวแปร x : "))
sum = 2 - x + ((3/7)*(x**2)) + ((5/11)*(x**3))
print(sum)

# ข้อ 3.1
c = float(input("กรุณากรอกจำนวนองศาเซลเซียส : "))
f = ((9/5)*c)+32
k = c+273.15
print('{} , {}' .format(f,k))
