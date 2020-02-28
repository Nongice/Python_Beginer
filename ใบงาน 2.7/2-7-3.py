# ใบงานที่ 2.7.3

print("-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

print("การคำนวณค่าคอมมิชชั่น")

print("-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

staff_name = input("ชื่อพนักงาน:")

sum_sales = float(input("ยอดขาย:"))

print("-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

if sum_sales >= 1 and sum_sales <= 200000 :

  commiss = sum_sales * 5/100

  print("ค่าคอมมิชชั่น", '%.2f' % commiss, "บาท")

elif sum_sales >= 200001 and sum_sales <= 500000:

  commiss = sum_sales * 7/100

  print("ค่าคอมมิชชั่น", '%.2f' % commiss, "บาท")

elif sum_sales >= 500001 and sum_sales <= 800000:

  commiss = sum_sales * 10/100

  print("ค่าคอมมิชชั่น", '%.2f' % commiss, "บาท")

elif sum_sales >= 800001 and sum_sales <= 1000000:

  commiss = sum_sales * 12/100

  print("ค่าคอมมิชชั่น", '%.2f' % commiss, "บาท")

print("-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
