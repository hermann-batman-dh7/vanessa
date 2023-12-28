import http
import webbrowser
import os

def pesquisa(value):
    url = "https://www.google.com/search?q="
    webbrowser.get().open(url + value)
