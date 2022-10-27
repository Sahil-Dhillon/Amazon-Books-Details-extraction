from bs4 import BeautifulSoup
import requests


for pageno in range(1, 3):
    url = 'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_' + \
        str(pageno)+'?ie=UTF8&pg='+str(pageno)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for d in soup.find_all('div', attrs={'class': "zg-grid-general-faceout"}):
        l = d.find('a', attrs={'class': "a-link-normal"})
        if l is not None:
            l = 'https://www.amazon.in'+l.get('href')
            rq = requests.get(l)
            sp = BeautifulSoup(rq.content, 'html.parser')
            details = sp.find('ul', attrs={
                              'class': "a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"})
            if details is not None:
                r_count = 0
                rev = sp.find('div', attrs={'id': "cm-cr-dp-review-list"})
                reviews = rev.find_all('div', attrs={
                                       'class': "a-expander-content reviewText review-text-content a-expander-partial-collapse-content"})

                for x in details.find_all('span', attrs={'class': "a-list-item"}):
                    y = x.find('span', attrs={'class': "a-text-bold"})

                    if 'Publisher' in y.text:
                        y = x.find('span', attrs={'class': ""})
                        print("Publisher : ", y.text)
                    elif 'Language' in y.text:
                        y = x.find('span', attrs={'class': ""})
                        print("Language : ", y.text)
                    elif 'Paperback' in y.text:
                        y = x.find('span', attrs={'class': ""})
                        print("Paperback : ", y.text)
                    elif 'ISBN-10' in y.text:
                        y = x.find('span', attrs={'class': ""})
                        print("ISBN-10 : ", y.text)
                    elif 'ISBN-13' in y.text:
                        y = x.find('span', attrs={'class': ""})
                        print("ISBN-13 : ", y.text)
                    elif 'Weight' in y.text:
                        y = x.find('span', attrs={'class': ""})
                        print("Weight : ", y.text)
                    elif 'Dimensions' in y.text:
                        y = x.find('span', attrs={'class': ""})
                        print("Dimensions : ", y.text)
                print("Top 3 Reviews : ")
                for r in reviews:
                    r_count = r_count+1
                    if(r_count <= 3):
                        print(r_count, ". ", r.text)
                print("-------------------------------------------------")
