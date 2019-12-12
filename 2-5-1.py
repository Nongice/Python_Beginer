st_name = "กรวิชญ์"
st_surname = " ดวงตา" # เว้นวรรคไว้เพื่อความสวยงาม โดยการเว้นนี้ไม่มีผลต่อโค้ดที่เขียน
th_score = 10
en_score = 12
social_score = 18
sci_score = 15
math_score = 20
average = (th_score + en_score + social_score + sci_score + math_score) / 5
print(st_name + st_surname+"ได้คะแนนเฉลี่ยรวม " + '%.2f' % average + " คะแนน")
