from http import server
import socketserver
import webbrowser
import threading

def startLocalHost():
    PORT = 8888

    Handler = server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print("serving at port" + str(PORT))
    httpd.serve_forever()

def openBrowser():
    url = 'http://localhost:8888/index.html'
    try:
        webbrowser.open_new_tab(url)
    except:
        webbrowser.open_new(url)

def openWebsite():
    a = threading.Thread(target=startLocalHost)
    a.start()
    openBrowser()