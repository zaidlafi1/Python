import requests

# BeautifulSoup is imported with the name bas4
import bs4

URL = 'https://salahat.elevatustesting.xyz/jobs'

# Fetch all the HTML source from the url
response = requests.get(URL)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.select('a')

# Print out the result
for link in links:
    print(link.get_text())
    if link.get('href') != None:
        if 'https://' in link.get('href'):
            print(link.get('href'))
        else:
            print('https://salahat.elevatustesting.xyz/jobs' + link.get('href'))  # Convert relative URL to absolute URL

    print('----------------------------')  # Just a line break
