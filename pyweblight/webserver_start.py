#!/usr/bin/env python

"""
Web server for development purposes, light weight with some features.

    Mark Veltzer

TODO:
- call this project dws.
- fix the logging of the web server to go to .dws_logs
- fix it so the cwd of the web server will not change to /.
- fix it so if there is a problem with the web server I will print the error
    to the screen.
- self.path has parameters in it. strip them.
- /favicon.ico return 500 and should return 404.
- make the search path much more elaborate so that I can easy searching for files inside
libraries.
- make the transport of requests be UTF-8 so that the browser will shut up about
the fact that all my documents do not have ending in them.
"""

# pylint: disable=deprecated-module
import cgi
import os
import time
import http.server
import mimetypes
import daemon


class StoppableHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    """http request handler with QUIT stopping the server"""

    def do_QUIT(self):
        """send 200 OK response, and set server.stop to True"""
        self.send_response(200)
        self.end_headers()
        self.server.set_stop()


class MyHandler(StoppableHttpRequestHandler):
    def __init__(self, *args):
        # order is important here and base class is fucked up
        self.encoding = "utf8"
        self.search_path = ":".join([
            ".",
            "/usr/share/javascript",
            "/usr/share/javascript/jquery",
        ])
        super().__init__(*args)

    def handle_static(self, resolved, mimetype):
        # note that this potentially makes every file on your computer
        # readable by the internet. A real web server also checks that
        # the file that it is serving is inside into service 'realm'.
        with open(resolved, "rb") as f:
            self.send_response(http.HTTPStatus.OK)
            if mimetype[0]:
                self.send_header('Content-type', mimetype[0])
            if mimetype[1]:
                self.send_header('Content-Encoding', mimetype[1])
            self.end_headers()
            self.wfile.write(f.read())
            f.close()

    def resolve(self, name):
        for folder in self.search_path.split(':'):
            to_consider = os.path.join(folder, name)
            if os.path.exists(to_consider):
                return to_consider
        return None

    def write(self, message):
        self.wfile.write(bytes(message, self.encoding))

    def handle_esp(self):
        self.send_response(http.HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.write('time is the ' + str(time) + '<br/>')
        self.write('today is the ' + str(time.localtime()[7]) + '<br/>')
        self.write('day in the year ' + str(time.localtime()[0]) + '<br/>')

    def to_path(self):
        # add a '.' to path to make it a local file path
        # /->./
        # /index.html -> ./index.html
        r = self.path[1:]
        if r == '':
            r = '.'
        return r

    def handle_dir(self, real_path):
        self.send_response(http.HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.write('<html><body>')
        for x in os.listdir(real_path):
            ref = os.path.join('http://localhost:8001', self.path, x)
            message = '<a href=\'' + ref + '\'>' + x + '</a><br/>'
            self.write(message)
        self.write('</body></html>')

    def get(self):
        # our dynamic content
        if self.path.endswith('.esp'):
            self.handle_esp()
            return

        # handle real files
        real_path = self.to_path()
        resolved = self.resolve(real_path)
        if resolved:
            if os.path.isfile(resolved):
                mimetype = mimetypes.guess_type(resolved)
                if mimetype[0]:
                    self.handle_static(resolved, mimetype)
                    return
                self.send_error(
                    500, f"Unrecognized file type: {self.path}")
                return
            if os.path.isdir(resolved):
                self.handle_dir(real_path)
                return

        # any other thing
        self.send_error(http.HTTPStatus.NOT_FOUND)

    def do_GET(self):
        # this is the method called by the framework... any lower level error
        # should send internal error to the client...
        # pylint: disable=broad-except
        try:
            self.get()
        except Exception:
            self.send_error(http.HTTPStatus.INTERNAL_SERVER_ERROR)

    def do_POST(self):
        try:
            content_type, parameter_dict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if content_type == 'multipart/form-data':
                query = cgi.parse_multipart(self.rfile, parameter_dict)
            else:
                raise ValueError("not a form")
            self.send_response(301)
            self.end_headers()
            upload_content = query.get('upload')
            self.write('<html><body>POST OK.<br/><br/>')
            self.write('<b>file content is:</b><br/><code>')
            self.write(upload_content[0])
            self.write('</code></body></html>')
        # pylint: disable=broad-except
        except Exception:
            self.send_error(http.HTTPStatus.INTERNAL_SERVER_ERROR)

    # pylint: disable=redefined-builtin
    def log_message(self, format, *args):
        """
        override the log method and call the parent
        """
        # return super().log_message(fmt, *args, **kwargs)


class StoppableHttpServer(http.server.HTTPServer):
    """http server that reacts to self.stop flag"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stop = False

    def serve_forever(self, poll_interval=0.5):
        """Handle one request at a time until stopped."""
        self.stop = False
        while not self.stop:
            self.handle_request()


def main():
    host = 'localhost'
    port = 8001
    url = f"http://{host}:{port}"
    server = StoppableHttpServer((host, port), MyHandler)
    print(f"contact me at [{url}]")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('CTRL+C received, shutting down server')
        server.server_close()


with daemon.DaemonContext():
    main()
