def is_symmetric_array(arr):
    # بررسی تعداد عناصر آرایه
    n = len(arr)
    # بررسی متقارن بودن آرایه
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            return False
    return True


# گرفتن آرایه از کاربر
input_str = input("araye ra vared konid va anasor an ra ba space az hm joda konid : ")
array = input_str.split()

# تبدیل عناصر به اعداد صحیح
array = [int(element) for element in array]

# فراخوانی تابع برای بررسی متقارن بودن آرایه
result = is_symmetric_array(array)

# چاپ نتیجه
if result:
    print("motaqaren ast")
else:
    print("motaqaren nist")