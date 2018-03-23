# A multiprocessing web spider with beautiful soup

'''
' The main task of a spider to go to a website and find all the URLs on the
' page and then go to all of those links. You can choose to do something when
' you are on those page, but we are not coding that here
'''

from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

''' Generates a random starting url '''
def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase)
                       for _ in range(3))
    url = ''.join(['http://', starting, '.com'])
    return url


''' Websites generally use local links internally in the hrefs '''
def handle_local_links(url,link):
    if link.startswith('/'):
        return ''.join([url,link])
    else:
        return link


def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url,link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links

    except TypeError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('We probably did not find any useful links, returning empty list')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got None for links, so we are throwing this')
        return []
    except Exception as e:
        print(str(e))
        # log this error 
        return []


def main():
    how_many = 50
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('urls.txt','w') as f:
        f.write(str(data))


if __name__ == "__main__":
    main()
