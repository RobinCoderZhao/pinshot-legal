#!/usr/bin/env python3
"""Local-only preview with the same /pinshot-legal/ prefix as GitHub Pages."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse

ROOT=Path(__file__).resolve().parents[1]
PREFIX='/pinshot-legal/'

class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=str(ROOT),**kwargs)

    def prepare(self):
        path=unquote(urlsplit(self.path).path)
        if path in ('/', '/pinshot-legal'):
            self.send_response(302)
            self.send_header('Location', PREFIX)
            self.end_headers()
            return False
        if not path.startswith(PREFIX):
            self.send_error(404)
            return False
        relative=path[len(PREFIX):]
        if any(p.startswith('.') for p in relative.split('/') if p) or relative.startswith('scripts/'):
            self.send_error(404)
            return False
        if (ROOT/relative).is_dir() and not path.endswith('/'):
            query=urlsplit(self.path).query
            self.send_response(301)
            self.send_header('Location', path+'/' + ('?'+query if query else ''))
            self.end_headers()
            return False
        self.path=self.path[len(PREFIX)-1:]
        return True

    def do_GET(self):
        if self.prepare(): super().do_GET()

    def do_HEAD(self):
        if self.prepare(): super().do_HEAD()

    def list_directory(self,path):
        self.send_error(404)
        return None

    def end_headers(self):
        self.send_header('Cache-Control','no-store')
        super().end_headers()

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=int,default=4173)
    args=parser.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    print(f'English: http://127.0.0.1:{args.port}{PREFIX}',flush=True)
    print(f'中文: http://127.0.0.1:{args.port}{PREFIX}zh/',flush=True)
    try: server.serve_forever()
    except KeyboardInterrupt: server.server_close()
