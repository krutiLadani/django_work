from BaseHTTPServer import BaseHTTPRequestHandler
from os import curdir, sep
import cgi
from collections import OrderedDict
from db_config import DatabaseFunc

db = DatabaseFunc()


class GetHandler(BaseHTTPRequestHandler):
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
            # html_file = open("index.html")
            self.wfile.write(html_file.read())
            html_file.close()

        except IOError:
            self.send_error(404,"File Not Found")

    def do_POST(self):

        if self.path == "/Display":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            self.send_response(200)
            self.end_headers()
            data = OrderedDict()
            for field in form.keys():
                field_item = form[field]
                if field_item.filename:
                    file_data = field_item.file.read()
                    file_len = len(file_data)
                    self.wfile.write("uploaded %s as %s (%d bytes)" % (field,field_item.filename,file_len))
                else:
                    self.wfile.write("\n {0} = {1}".format(field,form[field].value))
                data[field] = form[field].value
            db.insert_record("user_register", data)
            return


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    try:

        server = HTTPServer(('0.0.0.0', 8080), GetHandler)
        print 'Starting server, use <Ctrl + F2> to stop'
        server.serve_forever()

    except KeyboardInterrupt:

        server.socket.close()
