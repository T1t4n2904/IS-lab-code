import socket
import hashlib

def compute_hash(data):
    """Compute the SHA256 hash of the given data."""
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    
    print("Server is listening on port 12345...")
    
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        
        # Receive data from the client
        data = conn.recv(1024)
        print(f"Received data: {data}")
        
        # Compute hash of the received data
        received_hash = compute_hash(data)
        print(f"Computed hash: {received_hash}")
        
        # Send the computed hash back to the client
        conn.send(received_hash.encode())
        conn.close()

if __name__ == '__main__':
    start_server()
