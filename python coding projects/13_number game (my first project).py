import random
com = 10
while True:        #while ye work kar raha ki vo isee band nahi hone deta bar bar esse on rakhata hai 
 user = int(input("TYPE NUMBER HERE:\n"))

 if user==com:
       print("CONGRATES! YOU WON THE MATCH. ")
       break      #break ye kam kara raha hai ki agar yaha condition sahi hai aur result aa raha hai to ye loop ko aage nahi chalne deta 

 elif user>com:
       print("Oohho! YOU CHOOSE SO BIG NUMBER. ")
       
 else:
      print("Oohho! YOU CHOOSE SO SMALL NUMBER. ")  