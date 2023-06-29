import requests
from bs4 import BeautifulSoup

# Make a GET request to the Billboard Charts website
url = 'https://www.billboard.com/charts/hot-100'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the chart container that holds the song entries
chart_container = soup.find(name='p', class_="c-tagline  a-font-primary-medium-xs u-font-size-11@mobile-max u-letter-spacing-0106 u-letter-spacing-0089@mobile-max lrv-u-line-height-copy lrv-u-text-transform-uppercase lrv-u-margin-a-00 lrv-u-padding-l-075 lrv-u-padding-l-00@mobile-max")

print(chart_container)