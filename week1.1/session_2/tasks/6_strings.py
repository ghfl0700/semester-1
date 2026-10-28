# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")                      # print the original string entered by the user
print(f"Modified String 1: {user_string.lower()}")              # 所有字符串的字母都变成小写
print(f"Modified String 2: {user_string.upper()}")              #所有字符串的字母都变成大写
print(f"Modified String 3: {user_string.strip()}")              #删除字符串的开头和结尾的空格
print(f"Modified String 4: {user_string.replace('a', '@')}")    #将字符串中的a换成@符号
print(f"Modified String 5: {user_string.capitalize()}")         #将字符串中的字母都大写
print(f"Modified String 6: {user_string[::-1]}")                #字符串的顺序反转
print(f"Modified String 7: {user_string.title()}")              #每个单词首字母大写，剩下字母全部小写
print(f"Modified String 8: {len(user_string)}")                 #包含空格的总字符数量
print(f"Modified String 9: {user_string.find('a')}")            #查找第一个字母a的下标位置，找不到返回-1
print(f"Modified String 10: {user_string.count('a')}")          #统计a出现了几次
print(f"Modified String 11: {user_string.startswith('Hello')}") #判断是不是以hello开头，返回true/false
print(f"Modified String 12: {user_string.endswith('!')}")       #判断是不是以！结尾，返回true/false
print(f"Modified String 13: {user_string.isalnum()}")           #检查字符串里面是不是都是字母或数字，若有空格，标点，符号返回false
print(f"Modified String 14: {user_string.isalpha()}")           #检查字符串里面是不是都是英文字母，有别的返回false
print(f"Modified String 15: {user_string.isdigit()}")           #检查字符串里面是不是都是数字，有别的返回false



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!