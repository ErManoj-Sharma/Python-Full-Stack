import re
str1="aaaa"
str2="bbbbbbbb"
str3="ccccccccccc"
pat1="...."
res1=re.findall(pat1,str1)
res2=re.findall(pat1,str2)
res3=re.findall(pat1,str3)
print(res1)
print(res2)
print(res3)
print()
pat2="^....$"
res1=re.findall(pat2,str1)
res2=re.findall(pat2,str2)
res3=re.findall(pat2,str3)
print(res1)
print(res2)
print(res3)