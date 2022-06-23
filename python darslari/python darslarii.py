ism = input("Ismingiz nima: ")
if ism.lower() != 'ali':
    print(f"Uzur {ism.title()} biz alini kutyapmiz")

else:
    print("Salom ali")

javob = float(input("12*6 nechiga teng: "))
if javob!=72:
    print('Javob xato')




yosh = int(input("Yoshingiz nechida: "))
if yosh>=18:
    print("Xush kelibsiz")
else:
    print("Kirish mumkin emas")


login = input('Yangi login yozing: ')
if len(login)<=5:
    print("Login 5ta harfdan kam bo'lmasligi kerak")






yil = int(input("Tug'ilgan yilingizni yozing: "))
if 2022-yil<18:
    print(f"Yoshingiz {2022-yil} da ekan,")
    print("Kirish mumkin emas")
else:
    print("xush kelibsiz")



yosh = int(input("Yoshingiz nechida? \n>>>"))
if yosh>65: print("Siz COVID-19 risk guruxida ekansiz")


x,y=25,5
print("x>y")  if x>y else print("x<y")



cars = ['toyoto','mazda','hyundai','gm','kia']
for car in cars:
    if car =='gm':
        print(car.upper())
else:
    print(car.title())

login = input('Login kiriting: ')
if login.lower() =='admin':
    print("Xush kelibsiz Admin, Foydalanuvchilar ro'yxatini ko'rasizmi?,")
else:
    print(f"Xush kelibsiz {login.title()}!")



a =float(input("1-Sonni kiriting: "))
b=float(input("2-Sonni kiriting: "))
if a ==b:
    print(f"sONLAR TENG: {a}={b}")



c = int(input("son kiriting: "))
if c>0:
    print("Musbat son")
else:
    print("Manfiy son")




d = float(input("son kiriting:"))
print(d**(1/2)) if d>0 else print('Musba son kiriting: ')



yosh = int (input("Yoshingiz nechida: "))
if yosh<=4:
    narh = 0
elif yosh<=12:
    narh = 5000

elif yosh<=18:
    narh = 8000
else:
    narh = 10000
    print(f" Sizga kirish {narh} so'm")






kun = input("Bugun nima kun: ")
if kun .lower()=='shanba'or kun.lower()=='yakshanba':
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")


kun = input("Bugun nima kun: ")
harorat = float(input("Havo harorati qanday: "))
if kun.lower()=='shanba'or kun.lower()=='yakshanba' and harorat>=30:
    print("Co'milgani ketdik")
elif kun.lower()=='yakshanba'or kun.lower()=='shanba' and harorat<30:
    print("Uyda dam olamiz")





kun = input("Bugun nima kun: ")
harorat = float(input('Havo harorati qanday: '))
if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
    print("Cho'milgani ketdik")
elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
    print("Uyda dam olamiz")


narh = 15000
choy = True
salat = True


if choy and salat:
    narh=narh + 10000
elif choy or salat:
        narh=narh +5000
        print(f"Jamik {narh} so'm")




from tkinter import Menu


menu = ['somsa','shashlik','manti']
ovqat = input("Nima ovqat yeysiz: >>>")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilinda")
else:
        print("Afsuski bizda bunday ovqat yo'q")





