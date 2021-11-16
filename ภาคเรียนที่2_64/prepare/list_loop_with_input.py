import time
data = []
input_key = 0
print("**********************\
    \nโปรแกรมลูปข้อมูลเท่าที่ใจมึงอยากลูป\
    \n**********************")
time.sleep(0.5)
print("โปรแกรมจะจบลงเมื่อคุณพิมพ์เพียงเลข 1 และห้ามมีเว้นวรรคเท่านั้น")
time.sleep(2)
print("เริ่มกรอกได้เลย!")
while data == [] or input_key != "1":
    input_key = input("")
    if input_key != "1":
        data.append(input_key)
    x = len(data)
for i in data:
    count_loop = (len(data)-x)+1
    print("[%s]"%count_loop,"; %s"%i)
    x -= 1
else:
    print("โปรแกรมจบการทำงาน")
