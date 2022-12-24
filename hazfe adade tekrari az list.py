

#لیست اعداد خود را با یک فاصله وارد کنید

#مثال :  1 2 7 5 5 8 9 2 1
 
input_string = input('enter your numbers with one space:')

print("\n")

user_list = input_string.split()


# چاپ لیست

print('list: ', user_list)

my_list=list(set(user_list))

print("my_list= ", my_list)
