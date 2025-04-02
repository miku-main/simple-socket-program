import socket

def main():
    # Define server configuration and name string
    SERVER_NAME = "Server of Gui Sen"
    # The server's chosen integer; you can change this or randomize if you like.
    SERVER_CHOSEN_INTEGER = 10
    HOST = '' # Bind to all available interfaces
    PORT = 5001 # Use a port number greater than 1023 (recommended >5000)
    
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server started on port {PORT}. Waiting for connections...")
    
    while True:
        conn, addr = server_socket.accept()
        print(f"\nAccepted connection from {addr}.")
        data = conn.recv(1024).decode() # Receive data (assumes UTF-8)
        if not data:
            print("No data received. Closing connection.")
            conn.close()
            continue
        
        print(f"Received data from client: {data}")
        try:
            # Expecting message format: "Client of Gui Sen|Integer"
            parts = data.split("|")
            if len(parts) != 2:
                print("Invalid message format. Expected 'Name|Integer'.")
                conn.close()
                continue
            client_name = parts[0].strip()
            client_integer = int(parts[1].strip())
        except Exception as e:
            print("Error parsing received data:", e)
            conn.close()
            continue
        
        # Check if client's integer is within the valid range
        if not (1 <= client_integer <= 100):
            print(f"Client's integer {client_integer} is out of range. Termination server.")
            conn.close()
            break
        
        # Display client and server names and numbers
        print(f"Client's name: {client_name}")
        print(f"Server's name: {SERVER_NAME}")
        print(f"Client's integer: {client_integer}")
        print(f"Server's integer: {SERVER_CHOSEN_INTEGER}")
        sum_numbers = client_integer + SERVER_CHOSEN_INTEGER
        print(f"Sum: {sum_numbers}")
        
        # Send reply to client: server's name and chosen integer in the same format
        reply = f"{SERVER_NAME}|{SERVER_CHOSEN_INTEGER}"
        conn.sendall(reply.encode())
        print("Sent reply to client.")
        
        conn.close()
        print("Closed connection with client.")
        
    print("Shutting down server.")
    server_socket.close()
    
if __name__ == '__main__':
    main()