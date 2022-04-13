from bs4 import BeautifulSoup

with open('Html.html','r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents,'lxml')
        for tag in soup:
                print(f'{tag.text}')
