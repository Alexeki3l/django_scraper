from bs4 import BeautifulSoup
import requests
import lxml
import os


def get_items(url):

    """
    Obtiene los nombres, las clasificaciones, los precios, las imagenes y las url de los productos
    encontrados segun el criterio de busqueda. Este criterio sera el string que se pase por
    parametro 
    """

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"en",
    }

    product_names   =[]
    ratings         =[]
    ratings_count   =[]
    prices          =[]
    product_urls    =[]
    images          =[]

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
                print(rating_count)
                if len(rating_count)==2:
                    rating_count = int(rating_count[0] + rating_count[1])
                    print(rating_count)
                else:
                    rating_count = int(rating_count[0])
                    print(rating_count)
            except AttributeError:
                continue

            try:
                price = (result.find('span',{'class':'a-offscreen'}).text)[1:]
                image = result.find('img',{'class':'s-image'}).get('src')
                

                image = get_image(url,image, headers)

                images.append(image)

                product_url = 'https://www.amazon.com' + result.h2.a['href']
                product_names.append(product_name)
                ratings.append(rating)
                ratings_count.append(rating_count)
                prices.append(price)
                product_urls.append(product_url) 
                
            except AttributeError:
                continue
        break
    return product_names, ratings, ratings_count, prices, product_urls, images

# Se encarga de obtener la URL de cada nombre que se le pase
def get_link(name):
    search_query = name.replace(" ","+")
    url = "https://www.amazon.com/s?k={0}".format(search_query)
    print()
    # return url


# Se encarga de descargar las imagenes y guardarlas en la carpeta 'media'
def get_image(url, url_image, headers):

    index = url.split("https://www.amazon.com/s?k=")[1]
    index = index.split('+')
    if len(index)>1:
        index = index[0]+"_"+index[1]
    else:
        index = index[0]
        
    imagen = requests.get(url_image, headers).content
    name = url_image.split('/')
    name = name[-1]
    name = name[:-4]

    ruta = os.path.dirname(__file__)
    ruta = ruta.split("\scraper_app")
    ruta = ruta[0]
    ruta = os.path.join(ruta, 'media')
    ruta = ruta + "/" + index
    print(ruta)
    if not os.path.exists(ruta):
        os.mkdir(ruta)
        fullname = ruta + "/" + name
        open(fullname +'.jpg', 'wb').write(imagen)
        print('descargando:{}.jpg'.format(name))
    else:
        list_archivos = os.listdir(ruta)
        if name in list_archivos:
            print("Ya existe este archivo")
        else:
            fullname = ruta + "/" + name
    
            open(fullname +'.jpg', 'wb').write(imagen)
            print('descargando:{}.jpg'.format(name))

    return index + "/" + "{}.jpg".format(name)


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
#     "Accept-Language":"en",
#     }

# url_image = 'https://m.media-amazon.com/images/I/71y-jMVFfTL._AC_UY218_.jpg'

# url = 'https://www.amazon.com/s?k=mouse+inalambrico'

# get_image(url, url_image, headers)
    