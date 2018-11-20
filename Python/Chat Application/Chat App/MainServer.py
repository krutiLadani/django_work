# coding=utf-8
from BaseHTTPServer import BaseHTTPRequestHandler
from os import curdir, sep
import cgi
import socket
from datetime import datetime
import threading


# tLock = threading.Lock()
# shutdown = False
#
#
# def receiving(name, sock):
#     while not shutdown:
#         try:
#             tLock.acquire()
#             while True:
#                 data, addr = sock.recvfrom(2012)
#                 print data
#         except:
#             pass
#         finally:
#             tLock.release()


host = "0.0.0.0"
port = 5454

clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)


def StartBaseServer():

    # pickle.dump(time.ctime(time.time())+"\n",open_log,-1)
    quitting = False
    open_log = open("log.txt", "w+")
    open_log.writelines("")
    open_log.close()

    open_user = open("users.txt", "w+")
    open_user.writelines("")
    open_user.close()

    while not quitting:
        try:
            users = open("users.txt",'r')
            if users.read() == "":
                open_log = open("log.txt", "w+")
                open_log.writelines("")
                open_log.close()

            data, addr = s.recvfrom(2012)
            if addr not in clients.keys():

                clients[addr] = data
                open_user = open("users.txt", "a")
                open_user.writelines(clients[addr] + "\n")
                open_user.close()

                data = str(data) + " Δ Joined the room"
                file_data = "IP: " + str(addr[0]) + " PORT: " + str(addr[1]) + "," + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " --> " + data
                print file_data
                open_log = open("log.txt", "a")
                open_log.writelines(file_data + "\n")
                open_log.close()
                # pickle.dump(file_data+"\n",open_log,-1)
                for client in clients.keys():
                    if addr != client:
                        s.sendto(data, client)
                continue

            data = clients[addr] + " Δ " + str(data)

            file_data = "IP: " + str(addr[0]) + " PORT: " + str(addr[1]) + "," + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " --> " + data
            print file_data
            open_log = open("log.txt", "a")
            open_log.writelines(file_data + "\n")
            open_log.close()
            # pickle.dump(file_data + "\n", open_log, -1)

            for client in clients.keys():
                # if client != addr:
                s.sendto(data, client)

        except KeyboardInterrupt:
            quitting = True
        except:
            pass
    s.close()

class GetHandler(BaseHTTPRequestHandler):

    clients = {}

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        try:
            content_type = "text/html"
            if self.path.endswith(".html"):
                content_type = 'text/html'
            if self.path.endswith(".htm"):
                content_type = 'text/htm'
            if self.path.endswith(".jpg"):
                content_type = 'image/jpg'
            if self.path.endswith(".jpeg"):
                content_type = 'image/jpeg'
            if self.path.endswith(".png"):
                content_type = 'image/png'
            if self.path.endswith(".gif"):
                content_type = 'image/gif'
            if self.path.endswith(".js"):
                content_type = 'application/javascript'
            if self.path.endswith(".css"):
                content_type = 'text/css'
            if self.path.endswith(".txt") or self.path.endswith(".text"):
                content_type = 'text/plain'
            if self.path.endswith(".ttf"):
                content_type = "application/x-font-ttf"
            if self.path.endswith(".woff2"):
                content_type = "application/font-woff2"
            if self.path.endswith(".woff"):
                content_type = "application/font-woff"

            self.send_response(200)
            self.send_header("Content-type", content_type)
            self.end_headers()
            if self.path == "/":
                self.path = "index.html"
            html_file = open(curdir + sep + self.path)
            self.wfile.write(html_file.read())
            html_file.close()

        except IOError:
            self.send_error(404, "File Not Found")

    def do_POST(self):

        if self.path == "/chatroom.html":
            self.do_GET()

        if self.path.startswith("/sendname"):
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            self.send_response(200)
            self.end_headers()
            name = form['name'].value

            host = ""
            port = 0

            server = ("172.10.29.72", 5454)
            self.clients[self.client_address[0]] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.clients[self.client_address[0]].bind((host, port))
            self.clients[self.client_address[0]].setblocking(0)

            # rT = threading.Thread(target=receiving, args=("RecvThread", self.clients[self.client_address[0]]))
            # rT.start()

            self.clients[self.client_address[0]].sendto(name, server)

        if self.path.startswith("/sendmsg"):
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            self.send_response(200)
            self.end_headers()
            msg = form['msg'].value
            server = ("172.10.29.72", 5454)
            self.clients[self.client_address[0]].sendto(msg, server)

        if self.path.startswith("/leave"):
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            self.send_response(200)
            self.end_headers()
            name = form['nick_name'].value
            f = open("users.txt", "r")
            lines = f.readlines()
            f.close()
            f = open("users.txt","w")
            for line in lines:
                if line != name + "\n":
                    f.write(line)
            f.close()
            server = ("172.10.29.72", 5454)
            self.clients[self.client_address[0]].sendto("Left the room", server)

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    try:

        server = HTTPServer(('0.0.0.0', 8888), GetHandler)
        print 'Starting server, use <Ctrl + F2> to stop'

        threading.Thread(target=StartBaseServer).start()

        server.serve_forever()

    except KeyboardInterrupt:

        server.socket.close()
