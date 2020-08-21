import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    
    #section = soup.findAll('section', {})
    #div = soup.find('div').get('id')
    #h1 = soup.find('h1').find('a').get('href')    
    #h2 = soup.findAll('h2')    
    #print(type(h2))
    #print(dir(h2))    
    #for h in h2:
    #    print(h.text)

    
    
    section = soup.findAll('section', {'class': 'plugin-section'})[1]
    plugins = section.findAll('article')
    for plugin in plugins:
        h3 = plugin.find('h3')
        rating = plugin.find('span', {'class': 'rating-count'})
        print(h3.text, rating.text)
        
    
    #print(len(section))
    #print(section)


def main():
    
    #html = get_html('https://ru.wordpress.org/')
    html = get_html('https://ru.wordpress.org/plugins/')
    data = get_data(html)

if __name__ == '__main__':
    main()

