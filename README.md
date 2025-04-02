# Simple Socket Program

Implement a simple client-server application using TCP sockets where both sides exchange a name string and an integer.

## Client Requirements
* Input: 
    * Accept an integer between 1 and 100 from the user
* Operation: 
    * Open a TCP socket to connect with the server
    * Send a message that includes:
        * A string containing the client's name("Client of ___")
        * The user entered integer.
* Response:
    * Wait for the server's reply.
    * Read and display:
        * The client and server name
        * The client and server values
        * The sum of the two integers
* Termination:
    * Close the socket and terminate.

## Server Requirements
* Initialization:
    * Create a name string("Server of ___").
* Operation:
    * Open a TCP listening socket on a chosen port (greater than 1023, recommended above 5000).
    * Accept connections from clients.
    * For each client message:
        * Extract and display the client's name along with the server's name.
        * Choose an integer between 1 and 100
        * Display the client's number, the server's number and their sum.
        * Send a reply message containing, server's name and server-chosen integer.
* Shutdown Trigger:
    * If a client sends an integer out of the valid range, the server should release any sockets and terminate.

## How to Run
1. Start the Server:
    * Run the server program first (python server.py). It will be waiting for client connections.
2. Start the Client:
    * In a different terminal or on another machine, run the client program (python client.py).
    * Enter an integer (between 1 and 100) when prompted.
3. Output:
    * The client will display its own name, the integer entered, the server's name and chosen integer, and the computed sum.
    * The server prints informative messages each it accepts a connection, processes the message, and sends the reply.
4. Termination:
    * If the server receives an integer that is out of range, it will print a message and terminate.
        

