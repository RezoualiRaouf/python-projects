import requests
from  bs4 import BeautifulSoup

check = False
#send https request to the web
respons = requests.get("https://books.toscrape.com/")

#convert the respons to html string
sope = BeautifulSoup(respons.content, "html.parser")

#find only the books witch are in (article)
books = sope.find_all("article")

#enter the user's book that he want to search for
users_book = str(input("enter your book name :"))

#find the book and print the price rating title 
for book in books:
    if users_book in book.h3.a["title"]:
        price = book.find("p", class_="price_color").text
        title = book.h3.a["title"]
        rating = book.p["class"][1]
        print(title, rating, price)
        check = True

if  not check:
    print("book not found!")