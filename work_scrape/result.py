
b1=int(input("Enter Your Number Bangla First Paper:"))
b2=int(input("Enter Your Number Bangla Second Paper:"))
e1=int(input("Enter Your Number English First Paper:"))
e2=int(input("Enter Your Number English Second Paper:"))
math=int(input("Enter Your Number Mathematics:"))
bgl=int(input("Enter Your Number Bangladesh And Global Studies:"))
ime=int(input("Enter Your Number Islam And Moral Education:"))
phy=int(input("Enter Your Number Physics:"))
che=int(input("Enter Your Number Chemistry:"))
hm=int(input("Enter Your Number Higher Mathematics:"))
pe=int(input("Enter Your Number Physical Education:"))
bi=int(input("Enter Your Number Biology:"))
ict=int(input("Enter Your Number Ict:"))

score=(b1+b2+e1+e2+math+bgl+ime+phy+che+hm+pe+bi)/12

if (score<=32):
    print("Here Your Result Grade Point:F")
elif (score<=39):
    print("Here Your Result Grade Point:D")
elif (score<=49):
    print("Here Your Result Grade Point:c")
elif (score<=59):
    print("Here Your Result Grade Point:B")
elif (score<=69):
    print("Here Your Result Grade Point:A-")
elif (score<=79):
    print("Here Your Result Grade Point:A")
elif (score<=100):
    print("Here Your Result Grade Point:A+")
else:
    print("Failed Process")