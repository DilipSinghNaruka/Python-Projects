user_input = str(input("Enter a Phrase: "))
text = user_input.split()   #split is ditect a word from a paragrapha like this 'dilip', 'singh','naruka'
a = " "
for i in text:
    a = a+str(i[0]).upper()    #upper ka mtlb jo bhi word likhenge a variable me vo capital me aayega
print(a)


#in this we get output is that all words first number is captital show 