fptr1=open("img1.png","rb")
fptr2=open("img2.png",'wb')
data=fptr1.read()
print(data)
fptr2.write(data)
fptr1.close()
fptr2.close()