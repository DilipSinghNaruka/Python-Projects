#download instagram profile pic 
import instaloader
loader = instaloader.Instaloader()
# loader.download_hashtag('amg', max_count=20)
user=input("Enter instagram username:")

loader.download_profile(user,profile_pic_only=True)     #download_profile ka meaning ye hai ki ye only profile hi download karega 