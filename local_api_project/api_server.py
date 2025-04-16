from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

DATA_FILE = "data_store.json"

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/data':
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as f:
                    data = json.load(f)
            else:
                data = {'data': []}
            self._set_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_error(404, 'Not Found')

    def do_POST(self):
        if self.path == '/api/data':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                received = json.loads(post_data.decode())
            except json.JSONDecodeError:
                self._set_headers(400)
                self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode())
                return

            # Load existing data or initialize
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as f:
                    data = json.load(f)
            else:
                data = {'data': []}

            # Save new data
            data['data'].append(received)
            with open(DATA_FILE, 'w') as f:
                json.dump(data, f, indent=2)

            self._set_headers(201)
            self.wfile.write(json.dumps({'status': 'Data received'}).encode())
        else:
            self.send_error(404, 'Not Found')

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("🚀 API Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
