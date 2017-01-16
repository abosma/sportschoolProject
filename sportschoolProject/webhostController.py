from http import server
import socketserver
import webbrowser
import threading

def startLocalHost():
    '''Start een localhost http server
    Heeft geen extra data nodig'''
    PORT = 8888

    Handler = server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("serving at port" + str(PORT))
    httpd.serve_forever()

def openBrowser():
    '''Open de internet browser naar de index.html die lokaal gehost wordt
    Heeft geen extra data nodig'''
    url = 'http://localhost:8888/index.html'
    try:
        webbrowser.open_new_tab(url)
    except:
        webbrowser.open_new(url)

def openWebsite():
    '''Start de thread voor de localhost http server en opent de browser naar de lokale index.html
    Heeft geen extra data nodig'''
    a = threading.Thread(target=startLocalHost)
    a.start()
    openBrowser()