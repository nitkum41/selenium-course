




# str1 = "11abc10defg33hh7jjj5mn22asdad11ads3" ##works if last digit is single
str1 = "11abc10defg33hh7jjj5mn22asdad11ads33"  ##if last digit is double
num1=[]
num2=[]
flag= False

for i in range(0,len(str1)):

    if str1[i].isdigit() and i+1<len(str1):
        if str1[i+1].isdigit():
            num1.append(int(str1[i]+str1[i+1]))
            flag = True

        else:
            if not flag:
                num1.append(int(str1[i]))

    elif str1[i].isdigit() and i != len(str1)-1:  ## extra and condition if last dgit is double integers
        num1.append(int(str1[i]))
        flag=True

    else:
        flag = False




print(num1,sum(num1))

#
# input_string = "programming"
#
# print(list(set(input_string)))
#
# num=[]
# for char in input_string:
#     if char not in num:
#         num.append(char)
# print(num)




