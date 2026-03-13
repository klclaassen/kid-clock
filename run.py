import http.server
import socketserver
import webbrowser
import socket

PORT = 8000

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

local_ip = get_local_ip()

with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
    print()
    print("Clock server running")
    print(f"Computer: http://localhost:{PORT}/clock.html")
    print(f"Tablet:   http://{local_ip}:{PORT}/clock.html")
    print()
    print("Press Ctrl+C to stop")
    print()

    try:
        webbrowser.open(f"http://localhost:{PORT}/clock.html")
    except Exception:
        pass

    httpd.serve_forever()