#break
for x in range(5):
    if x == 3 :
        break                   #ทำงานเมื่อไหร่หยุด
    print(f" หิว : {x} ")

for y in range(5):
    if y == 3:
        continue                #ทำงานเมื่อไหร่จบรอบนั้น ไปรอบใหหม่ทันที
    print(f"ข้าว : {y} ")