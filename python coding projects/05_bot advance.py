import random
greeting = ["hii ","hii", "hlo", "any one here", "ram ram ", ]
kaise = ["kaise ho", "kaise ho ", "how do you do"]
greeting2= ["byy", "by", "see you later", "good bye", "tata", "i am leaving", "have a good day ", "chhoko chal" ]
names = ["whats your name", "tera naam kya h", "what is your name", "naam ?"]
doing = ["what are you doing", "kya kar rhe ho ", "kya karte ho"]


while True:
    a = input("you" " \t")

    if a.lower() in greeting:
        pc = input("pc -" "sorry i dont know how are you ? \n please say me your name :-\t")
        print("pc -", "hello", pc, "sorry I'm Forgate")
        pc = input("pc - kaise ho\n type here :-",)
        # print(pc)
        print("that's greate")


    elif a.lower() in greeting2:
        pc = ["ok byy", "ok tata", "okk"]
        print("pc" " -" +random.choice(pc))
    elif a.lower() in names:
        pc = ["dilip's pc", "daniel"]
        print("pc" " -" +random.choice(pc))
    elif a.lower() in doing:
        pc = ["wait of dilip", ["nothing"]]
        print("pc" " -" +random.choice(pc))
    elif a.lower() in kaise:
        pc = ["badiya", "chhoka chha"]
        print('pc" " -'+random.choice(pc))

    else:
        print("pc" " -  sorry i am not understand")
