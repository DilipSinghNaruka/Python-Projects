import pywhatkit as pwt
message = input("Type Your message Here:-")
number = (input("Type Your number Here:-"))   #yaha nmbr ko string me lena hai int me nahi lena hai vrna ye kam nahi karega 
time_h = int(input("Type Time only hour"))
time_m = int(input("Type Time only minute"))
pwt.sendwhatmsg(number,message, time_h, time_m)