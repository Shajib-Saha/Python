import pyshorteners

link = input("Enter your link : ")

shortener = pyshorteners.Shortener()

new_link = shortener.tinyurl.short(link)

print("New link is : ", new_link)