#       in this program we know how to check spelling 
from textblob import TextBlob
a = "khati"
b = TextBlob(a)    #textblob library hai jo spelling check karti hai 
print(str(a))
print(str(b.correct()))    #correct ka meaning hai ki uss word ki uss jagah usse similar word show kara dena 





# in this program we know to about language of varrriable 
# from textblob import TextBlob
# a = "Ram "
# b = TextBlob(a)


# print(str(a))
# print(str(b.detect_language()))




# from textblob import TextBlob
# a = "Ram "
# b = TextBlob(a)


# print(str(a))
# print(str(b.sentences))