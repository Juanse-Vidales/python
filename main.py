import http.server
import socketserver

PORT = 8888

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor web activo en el puerto", PORT)
    httpd.serve_forever()
