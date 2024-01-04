import webbrowser

def pesquisa(value):
    url = "https://www.google.com/search?q="
    webbrowser.get().open(url + value)
