b1=int(input("Result Of  Bangla First Paper:"))
b2=int(input("Result Of Bangla Second Paper:"))
e1=int(input("Result Of English First Paper:"))
e2=int(input("Result Of  English Second Paper:"))
math=int(input("Result Of  Mathematics:"))
hm=int(input("Result Of Higher Mathematics:"))
hm_pra=int(input("Result Of Higher Mathe Pratical:"))
phy=int(input("Result Of  Physics:"))
phy_pra=int(input("Result Of Physics Practical:"))
bi=int(input("Result Of  Biology:"))
bi_pra=int(input("Result Of Biology Practical:"))
che=int(input("Result Of  Chemistry:"))
che_pra=int(input("Result Of Chemistry Practical:"))
so=int(input("Result Of Social Science:"))
ime=int(input("Result Of Islam And Moral Education:"))

if(b1<33 or b2<)


#****************** Bangla First Paper**************************#
if (b1>80):
    print("Bangla 1st paper: A+")
elif (b1>70):
    print("Bangla 1st paper: A")
elif (b1>60):
    print("Bangla 1st paper: A-")
elif (b1>50):
    print("Bangla 1st paper: B")
elif (b1>40):
    print("Bangla 1st paper: C")
elif (b1>33):
    print("Bangla 1st paper: D")
else:
    print("F")
#****************** Bangla Second Paper**************************#
if (b2>80):
    print("Bangla 2nd paper: A+")
elif (b2>70):
    print("Bangla 2nd paper: A")
elif (b2>60):
    print("Bangla 2nd paper: A-")
elif (b2>50):
    print("Bangla 2nd paper: B")
elif (b2>40):
    print("Bangla 2nd paper: C")
elif (b2>33):
    print("Bangla 2nd paper: D")
else:
    print("Bangla 2nd paper: F")
#****************** Overall Bangla **************************#
if(b2>160):
    overallpoint:5
    print("Result Of Overall Bangla :A+")
elif(b2>140):
    overallpoint:4
    print("Result Of Overall Bangla :A")
elif(b2>120):
    overallpoint:3.5
    print("Result Of Overall Bangla :A-")
elif(b2>100):
    overallpoint:3
    print("Result Of Overall Bangla :B")
elif(b2>80):
    overallpoint:2
    print("Result Of Overall Bangla :C")
elif(b2>66):
    overallpoint:1
    print("Result Of Overall Bangla :D")
else:
    overallpoint:0
    print("F")
#****************** English First Paper**************************#
if (e1>80):
    overallpoint:5
    print("A+")
elif (e1>70):
    overallpoint:4
    print("A")
elif (e1>60):
    overallpoint:3.5
    print("A-")
elif (e1>50):
    overallpoint:3
    print("B")
elif (e1>40):
    overallpoint:2
    print("C")
elif (e1>33):
    overallpoint:1
    print("D")
else:
    overallpoint:0
    print("F")
#****************** English Second Paper**************************#
if (e2>80):
    overallpoint:5
    print("A+")
elif (e2>70):
    overallpoint:4
    print("A")
elif (e2>60):
    overallpoint:3.5
    print("A-")
elif (e2>50):
    overallpoint:3
    print("B")
elif (e2>40):
    overallpoint:2
    print("C")
elif (e2>33):
    overallpoint:1
    print("D")
else:
    overallpoint:0
    print("F")
#****************** Overall English **************************#
if (b2>160):
    overallpoint:5
    print("Result Of Overall English :A+")
elif (b2>140):
    overallpoint:4
    print("Result Of Overall English :A")
elif (b2>120):
    overallpoint:3.5
    print("Result Of Overall English :A-")
elif (b2>100):
    overallpoint:3
    print("Result Of Overall English :B")
elif (b2>80):
    overallpoint:2
    print("Result Of Overall English :C")
elif (b2>66):
    overallpoint:1
    print("Result Of Overall English :D")
else:
    overallpoint:0
    print("F")
#****************** Mathematics **************************#
if (math>80):
    overallpoint:5
    print("Mathematics : A+")
elif (math>70):
    overallpoint:4
    print("Mathematics : A")
elif (math>60):
    overallpoint:3.5
    print("Mathematics : A-")
elif (math>50):
    overallpoint:3
    print("Mathematics : B")
elif (math>40):
    overallpoint:2
    print("Mathematics : C")
elif (math>33):
    overallpoint:1
    print("Mathematics : D")
else:
    overallpoint:0
    print("Mathematics : F")
#****************** Higher  Mathematics **************************#
if hm>33 and hm_pra>8:  
    if (hm>80):
        overallpoint:5
        print("Higher  Mathematics : A+")
    elif (hm>70):
        overallpoint:4
        print("Higher  Mathematics : A")
    elif (hm>60):
        overallpoint:3.5
        print("Higher  Mathematics : A-")
    elif (hm>50):
        overallpoint:3
        print("Higher  Mathematics : B")
    elif (hm>40):
        overallpoint:2
        print("Higher  Mathematics : C")
    elif (hm>33):
        overallpoint:1
        print("Higher  Mathematics : D")
    else:
        overallpoint:0
        print("Higher  Mathematics : F")
#****************** Higher  Mathematics Practical**************************#
    if (hm_pra>21):
        overallpoint:5
        print("Higher  Mathematics : A+")
    elif (hm_pra>19):
        overallpoint:4
        print("Higher  Mathematics : A")
    elif (hm_pra>16):
        overallpoint:3.5
        print("Higher  Mathematics : A-")
    elif (hm_pra>13):
        overallpoint:3
        print("Higher  Mathematics : B")
    elif (hm_pra>10):
        overallpoint:2
        print("Higher  Mathematics : C")
    elif (hm_pra>8):
        overallpoint:1
        print("Higher  Mathematics : D")
    else:
        overallpoint:0
        print("Higher  Mathematics : F")
else:
    print("Higher  Mathematics : F")
#****************** Physics **************************#
if phy> 33 and phy_pra> 8:
    if (phy>80):
        overallpoint:5
        print("Physics : A+")
    elif (phy>70):
        overallpoint:4
        print("Physics : A")
    elif (phy>60):
        overallpoint:3.5
        print("Physics : A-")
    elif (phy>50):
        overallpoint:3
        print("Physics : B")
    elif (phy>40):
        overallpoint:2
        print("Physics : C")
    elif (phy>33):
        overallpoint:1
        print("Physics : D")
    else:
        overallpoint:0
        print("Physics : F")
#****************** Physics Practical **************************#
    if (phy_pra>21):
        overallpoint:5
        print("Physics : A+")
    elif (phy_pra>19):
        overallpoint:4
        print("Physics : A")
    elif (phy_pra>16):
        overallpoint:3.5
        print("Physics : A-")
    elif (phy_pra>13):
        overallpoint:3
        print("Physics : B")
    elif (phy_pra>10):
        overallpoint:2
        print("Physics : C")
    elif (phy_pra>8):
        overallpoint:1
        print("Physics : D")
    else:
        overallpoint:0
        print("Physics : F")
else:
    print("Physics : F")
#****************** Biology  **************************#
if bi> 33 and bi_pra> 8:
    if (bi>80):
        overallpoint:5
        print("Biology : A+")
    elif (bi>70):
        overallpoint:4
        print("Biology : A")
    elif (bi>60):
        overallpoint:3.5
        print("Biology : A-")
    elif (bi>50):
        overallpoint:3
        print("Biology : B")
    elif (bi>40):
        overallpoint:2
        print("Biology : C")
    elif (bi>33):
        overallpoint:1
        print("Biology : D")
    else:
        overallpoint:0
        print("Biology : F")
#****************** Biology Practical **************************#
    if (bi_pra>21):
        overallpoint:5
        print("Biology : A+")
    elif (bi_pra>19):
        overallpoint:4
        print("Biology : A")
    elif (bi_pra>16):
        overallpoint:3.5
        print("Biology : A-")
    elif (bi_pra>13):
        overallpoint:3
        print("Biology : B")
    elif (bi_pra>10):
        overallpoint:2
        print("Biology : C")
    elif (bi_pra>8):
        overallpoint:1
        print("Biology : D")
    else:
        overallpoint:0
        print("Biology : F")
else:
    print("Biology : F")
#******************  Chemistry **************************#
if che>33 and che_pra>8:
    if (che>80):
        overallpoint:5
        print("Chemistry : A+")
    elif (che>70):
        overallpoint:4
        print("Chemistry : A")
    elif (che>60):
        overallpoint:3.5
        print("Chemistry : A-")
    elif (che>50):
        overallpoint:3
        print("Chemistry : B")
    elif (che>40):
        overallpoint:2
        print("Chemistry : C")
    elif (che>33):
        overallpoint:1
        print("Chemistry : D")
    else:
        overallpoint:0
        print("Chemistry : F")
#******************  Chemistry Practical **************************#
    if (che_pra>21):
        overallpoint:5
        print("Chemistry : A+")
    elif (che_pra>19):
        overallpoint:4
        print("Chemistry : A")
    elif (che_pra>16):
        overallpoint:3.5
        print("Chemistry : A-")
    elif (che_pra>13):
        overallpoint:3
        print("Chemistry : B")
    elif (che_pra>10):
        overallpoint:2
        print("Chemistry : C")
    elif (che_pra>8):
        overallpoint:1
        print("Chemistry : D")
    else:
        overallpoint:0
        print("Chemistry : F")
else:
    print("Chemistry : F")        
#******************  Social Science **************************#
if (so>80):
    overallpoint:5
    print("Social Science : A+")
elif (so>70):
    overallpoint:4
    print("Social Science : A")
elif (so>60):
    overallpoint:3.5
    print("Social Science : A-")
elif (so>50):
    overallpoint:3
    print("Social Science : B")
elif (so>40):
    overallpoint:2
    print("Social Science : C")
elif (so>33):
    overallpoint:1
    print("Social Science : D")
else:
    overallpoint:0
    print("Social Science : F")
#****************** Islam And Moral Education  **************************#
if (ime>80):
    overallpoint:5
    print("Islam : A+")
elif (ime>70):
    overallpoint:4
    print("Islam : A")
elif (ime>60):
    overallpoint:3.5
    print("Islam : A-")
elif (ime>50):
    overallpoint:3
    print("Islam : B")
elif (ime>40):
    overallpoint:2
    print("Islam : C")
elif (ime>33):
    overallpoint:1
    print("Islam : D")
else:
    overallpoint:0
    print("Islam : F")      
ov= overallpoint    

print("overall:",ov)