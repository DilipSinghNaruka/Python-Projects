filename= input("Type here file Adress with filename and must be use  extention   :-")
with open(filename) as f:
   a =  f.read()


jisko_karna_hai = input(" Type here jisko karna hai ")
jo_hoga = input(" Type here jo karna hai  ")

a = a.replace(jisko_karna_hai, jo_hoga )

with open(filename, "w") as f:
   c =  f.write(a)
 