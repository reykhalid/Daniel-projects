import requests
from bs4 import BeautifulSoup
URL_CHART = "https://www.billboard.com/charts/hot-100/"
response = requests.get(URL_CHART)
billboard_web = response.content
soup = BeautifulSoup(billboard_web, "html.parser")
date = input("what year would you like to travel to? Type this format YYY-MM-DD: ")
songs = soup.find_all(name="p", class_="c-tagline  a-font-primary-medium-xs u-font-size-11@mobile-max u-letter-spacing-0106 u-letter-spacing-0089@mobile-max lrv-u-line-height-copy lrv-u-text-transform-uppercase lrv-u-margin-a-00 lrv-u-padding-l-075 lrv-u-padding-l-00@mobile-max")
print(songs)


#class="c-heading larva  a-font-primary-bold-l u-font-size-30@tablet lrv-u-padding-r-1 lrv-u-padding-r-00@mobile-max"