from bs4 import BeautifulSoup
import requests
import lxml


def get_items(url):

    """
    Obtiene los nombres, las clasificaciones, los precios y las url de los productos
    encontrados segun el criterio de busqueda. Este criterio sera el string que se pase por
    parametro 
    """

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"en",
    }

    product_names=[]
    ratings=[]
    ratings_count=[]
    prices=[]
    product_urls=[]

    # BUSCA EN 10 PAGINAS
    for i in range(1,11):
        print('Procesando {0}...'.format(url + '&page={0}'.format(i)))
        response = requests.get(url + '&page={0}'.format(i), headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        resultados = soup.find_all('div', {'class':'s-result-item', 'data-component-type':'s-search-result'})
        
        # ITERAR EN CADA ARTICULO DE CADA PAGINA
        for result in resultados:
            # product_name = result.h2.text
            
            product_name = result.find('span', {'class':'a-text-normal'}).text 
            
            try:
                rating = result.find('i', {'class':'a-icon'}).text
                rating_count = str(result.find_all('span', {'aria-label':True})[1].text)
                print(rating_count)
                rating_count = rating_count.split(",")
                print()
                if len(rating_count)==2:
                    rating_count = int(rating_count[0] + rating_count[1])
                else:
                    rating_count = int(rating_count[0])
            except AttributeError:
                continue

            try:
                price = (result.find('span',{'class':'a-offscreen'}).text)[1:]
                
                price = float(price)
                
                product_url = 'https://www.amazon.com' + result.h2.a['href']
                product_names.append(product_name)
                ratings.append(rating)
                ratings_count.append(rating_count)
                prices.append(price)
                product_urls.append(product_url) 
                
            except AttributeError:
                continue
        
        break

    return product_names, ratings, ratings_count, prices, product_urls

def get_link(name):
    search_query = name.replace(" ","+")
    url = "https://www.amazon.com/s?k={0}".format(search_query)
    
    return url