n= int(input())
list_num=[i for i in range(-n,n+1)]

file=open("File.txt", "r")
a=file.readlines()
list_num=list(map(str.strip, a))

# for i in range (len(a)):
#     a [i]=int(a[i].strip())

multi=1
for i in range (len(a)):
    multi*=list_num[a(i)]
print(multi)

list_num=list(map(str.strip, a))
print (list_num)

