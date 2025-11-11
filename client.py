import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 5001         # use a port that is free

# Server function
def server_func():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[Server] Listening on {HOST}:{PORT}...")
    
    conn, addr = server_socket.accept()
    print(f"[Server] Connected with {addr}")
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")
        msg = input("Server (you): ")
        conn.send(msg.encode())
    
    conn.close()
    server_socket.close()

# Client function
def client_func():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client_socket.connect((HOST, PORT))
            break
        except ConnectionRefusedError:
            pass  # wait until server starts
    print("[Client] Connected to server!")
    
    while True:
        msg = input("Client (you): ")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

# Start server in a thread
threading.Thread(target=server_func, daemon=True).start()

# Start client in main thread
client_func()
