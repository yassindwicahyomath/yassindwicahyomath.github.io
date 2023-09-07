from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from kalkulator import calculate


class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/calculate'):
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)

            operator = query_params['operator'][0]
            num1 = float(query_params['num1'][0])
            num2 = float(query_params['num2'][0])

            result = calculate(operator, num1, num2)
            self._set_response()
            self.wfile.write(str(result).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
