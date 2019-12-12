cus_name = input("ลูกค้าชื่อ-สกุล: ")
product = input("ชื่อสินค้า: ")
price = int(input("ราคาของสินค้า (ไม่นับภาษีมูลค่าเพิ่มเติม): "))
vat_price = price*(7/100)
price_com_success = price+vat_price
print('\n')  # print('\n') เป็นคำสั่งเว้นบรรทัดโดยไม่ต้องพิมพ์ตัวอักษร
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("คุณ"+cus_name)
print("ชื่อสินค้า: " + product)
print("ยอดราคาสินค้า: " + '%.2f' % price, "บาท")
print("ราคาภาษีมูลค่าเพิ่ม: " + '%.2f' % vat_price, "บาท")
print("ยอดรวมสุทธิ: " + '%.2f' % price_com_success, "บาท")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print('\n')  # print('\n') เป็นคำสั่งเว้นบรรทัดโดยไม่ต้องพิมพ์ตัวอักษร
