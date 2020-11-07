
#!/usr/bin/python3
a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

if ((a>b) & (a>c)):
    print("bilangan terbesar :%d", a)
if ((b>c) & (b>a)):
    print("bilangan terbesar :%d", b)
if ((c>a) & (c>b)):
    print("bilangan terbesar :%d", c)
