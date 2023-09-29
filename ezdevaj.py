import random

def marriage_algorithm(girls, boys):
    # اطمینان حاصل کنید تعداد دختران و پسران برابر است
    if len(girls) != len(boys):
        print("تعداد دختران و پسران برابر نیست!")
        return
    
    # ترکیب دختران و پسران به صورت تصادفی
    random.shuffle(girls)
    random.shuffle(boys)
    
    # بررسی همسران تکراری
    for i in range(len(girls)):
        if girls[i] == boys[i]:
            print("دختر", girls[i], "و پسر", boys[i], "دو همسر نداشته باشند!")
            return
    
    # چاپ جفت‌های ازدواج شده
    for i in range(len(girls)):
        print("جفت", i + 1, ":", girls[i], "و", boys[i])
        

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

# اجرای الگوریتم ازدواج
marriage_algorithm(girls, boys)
