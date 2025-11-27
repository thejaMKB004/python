str1=input("Enter first string:")
str2=input("Enter the second string:")

new_str1=str2[1]+str[1:] if len(str1)>1 and len(str2)>1 else str1
new_str2=str1[1]+str2[1:] if len(str1)>1 and len(str2)>1 else str2

result=new_str+""+new_str2
print("Result:",result)