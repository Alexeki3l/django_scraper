from bs4 import BeautifulSoup
import requests
import lxml


def get_link(name):
    search_query = name.replace(" ","+")
    url = "https://www.amazon.com/s?k={0}".format(search_query)
    return url

