# Cake name type
print("********** Question 1 **********")
cake1="1)black forest"
cake2="2)Vanila cake"
cake3="3)Red valvet"
cake4="4)Lemon Sponge"
cake5="5)Chocolate cake"
print("The flavor types of each cake:",cake1,cake2,cake3,cake4,cake5)
print("************************************")
print("********** Question 2 **********")
#row matterial cost
r_m_b_f=180
r_m_v_c=150
r_m_r_v=220
r_m_l_s=165
r_m_c_c=170
#transportation cost
t_s_b_f=150
t_s_v_c=150
t_s_r_v=150
t_s_l_s=150
t_s_c_c=150
#row meaterial cost and transportation cost
t_c_b_f = r_m_b_f + t_s_b_f
t_c_v_c = r_m_v_c + t_s_v_c
t_c_r_v = r_m_r_v + t_s_r_v
t_c_l_s = r_m_l_s + t_s_l_s
t_c_c_c = r_m_c_c + t_s_c_c
#utlity cost per pound
u_c_b_f = (t_c_b_f*3)/100
u_c_v_c = (t_c_v_c*3)/100
u_c_r_v = (t_c_r_v*3)/100
u_c_l_s = (t_c_l_s*3)/100
u_c_c_c = (t_c_c_c*3)/100
#Space cost and staff cost
s_p_s_t_b_f=50+60
s_p_s_t_v_c=50+60
s_p_s_t_r_v=50+60
s_p_s_t_l_s=50+60
s_p_s_t_c_c=50+60
#total Inventroy cost per pound cake
t_n_b_f = t_c_b_f + u_c_b_f + s_p_s_t_b_f
t_n_v_c = t_c_v_c + u_c_v_c + s_p_s_t_v_c
t_n_r_v = t_c_r_v + u_c_r_v + s_p_s_t_r_v
t_n_l_s = t_c_l_s + u_c_l_s + s_p_s_t_l_s
t_n_c_c = t_c_c_c + u_c_c_c + s_p_s_t_c_c
#print Each Per Pound Cake
print("Inventory Cost Of Black Forest Per Pound :",t_n_b_f)
print("Inventory Cost Of Vanilla Cake Per Pound :",t_n_v_c)
print("Inventory Cost Of Red Velvet Per Pound :",t_n_r_v)
print("Inventory Cost Of Lemon Sponge Cake Per Pound :",t_n_l_s)
print("Inventory Cost Of Chocolate Cake Per Pound :",t_n_c_c)
print("**************************************")
print("********** Question 3 **********")
#Before discount Cake selling price
b_f_b_f=780
b_f_v_c=600
b_f_r_v=800
b_f_l_s=650
b_f_c_c=660

print("Selling Cost Of Black Forest Before Discount:",b_f_b_f)
print("Selling Cost Of Vanilla Cake Before Discount:",b_f_v_c)
print("Selling Cost Of Red Velvet Before Discount:",b_f_r_v)
print("Selling Cost Of Lemon Sponge Before Discount:",b_f_l_s)
print("Selling Cost Of Chocolate Cake Before Discount:",b_f_c_c)
print("***************************************")
print("********** Question 4 **********")
#after Discount cake Selling Price
a_f_b_f = (780*5)/100
a_f_v_c = (600*5)/100
a_f_r_v = (800*5)/100
a_f_l_s = (650*7)/100
a_f_c_c = (660*7)/100

#total cost after discount

t_a_b_f = b_f_b_f - a_f_b_f
t_s_v_c = b_f_v_c - a_f_v_c
t_a_r_v = b_f_r_v - a_f_r_v
t_a_l_s = b_f_l_s - a_f_l_s
t_a_c_c = b_f_c_c - a_f_c_c

print("Selling Cost Of Black Forest After Discount:",t_a_b_f)
print("Selling Cost Of Vanilla Cake After Discount:",t_s_v_c)
print("Selling Cost Of Red Velvet After Discount:",t_a_r_v)
print("Selling Cost Of Lemon Sponge After Discount:",t_a_l_s)
print("Selling Cost Of Chocolate Cake After Discount:",t_a_c_c)
print("*************************************")