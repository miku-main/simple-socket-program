import socket
def main():
    CLIENT_NAME = "Client of Gui Sen"
    HOST = "localhost" # Change this to the server's IP if running on different machines
    PORT = 5001 # Must match the server's port number
    
    # Prompt the user to enter an integer between 1 and 100
    while True:
        try:
            user_input = input("Enter an integer between 1 and 100: ")
            client_integer = int(user_input)
            break
        except ValueError:
            print("Invalid input. PLease enter a valid integer.")
            
    # Create a TCP socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print(f"COnnected to server at {HOST}:{PORT}")
    except Exception as e:
        print("Failed to connect to server:", e)
        return
    
    # Compose and send the message in the format "Client Name|Integer"
    message = f"{CLIENT_NAME}|{client_integer}"
    client_socket.sendall(message.encode())
    print(f"Sent message to server: {message}")
    
    # Wait for the server's reply
    reply = client_socket.recv(1024).decode()
    if not reply:
        print("No reply received from server.")
        client_socket.close()
        return
    print(f"Received reply from server: {reply}")
    
    try:
        # Expect reply in the format "Server of Gui Sen|<server_integer>"
        parts = reply.split('|')
        if len(parts) != 2:
            print("Invalid reply format from server.")
            client_socket.close()
            return
        server_name = parts[0].strip()
        server_integer = int(parts[1].strip())
    except Exception as e:
        print("Error parsing server reply:", e)
        client_socket.close()
        return
    
    # Compute and display the sum along with names and numbers
    sum_numbers = client_integer + server_integer
    print("\n----- Summary -----")
    print(f"Client's name: {CLIENT_NAME}")
    print(f"Client's integer: {client_integer}")
    print(f"Server's name: {server_name}")
    print(f"Server's integer: {server_integer}")
    print(f"Sum: {sum_numbers}")
    
    client_socket.close()
    print("Close client socket. Terminating.")
    
if __name__ == '__main__':
    main()