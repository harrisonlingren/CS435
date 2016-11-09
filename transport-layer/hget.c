/*
    get a file via http
    http://www.binarytides.com/winsock-socket-programming-tutorial/
    gcc hget.c -o hget.exe -lwsock32
*/

#include<stdio.h>
#include<time.h>
#include<winsock2.h>

#pragma comment(lib,"ws2_32.lib") //Winsock Library

int main(int argc , char *argv[])
{
    WSADATA wsa;
    SOCKET s;
    struct sockaddr_in server;
    char *message , server_reply[2000];
    int recv_size;
    char *hostname = "blue.butler.edu";
    char ip[100];
    struct hostent *he;
    struct in_addr **addr_list;
    int i;
    clock_t begin, end;
    double time_spent;


    printf("\nInitialising Winsock...");
    if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
    {
        printf("Failed. Error Code : %d",WSAGetLastError());
        return 1;
    }

    printf("Initialised.");

    if((s = socket(AF_INET , SOCK_STREAM , 0 )) == INVALID_SOCKET)
    {
        printf("Could not create socket : %d" , WSAGetLastError());
    }

    printf("Socket created.\n");

    if ( (he = gethostbyname( hostname ) ) == NULL)
    {
        //gethostbyname failed
        printf("gethostbyname failed : %d" , WSAGetLastError());
        return 1;
    }

    //Cast the h_addr_list to in_addr , since h_addr_list also has the ip address in long format only
    addr_list = (struct in_addr **) he->h_addr_list;

    for(i = 0; addr_list[i] != NULL; i++)
    {
        //Return the first one;
        strcpy(ip , inet_ntoa(*addr_list[i]) );
    }

    printf("%s resolved to : %s\n" , hostname , ip);

    server.sin_addr.s_addr = inet_addr(ip);
    server.sin_family = AF_INET;
    server.sin_port = htons( 80 );

    // time connection and transfer...
    begin = clock();
    
    //Connect to remote server
    if (connect(s , (struct sockaddr *)&server , sizeof(server)) < 0)
    {
        puts("connect error");
        return 1;
    }

    puts("Connected");
    
    //Send some data
    message = "GET /~npartenh/10 HTTP/1.1\r\nHost: blue.butler.edu\r\nConnection: close\r\n\r\n";
    if( send(s , message , strlen(message) , 0) < 0)
    {
        puts("Send failed");
        return 1;
    }
    puts("Data Sent\n");

    //Receive a reply from the server
    int data_remaining = 10485762;
    while(((recv_size = recv(s , server_reply , 2000 , 0)) > 0) && (data_remaining > 0)) {
        data_remaining -= recv_size;
        // printf("Received: %dB, %dB remaining\n", recv_size, data_remaining);
    }
    end = clock();
    time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    puts("Reply received\n");
    printf("that took %fs\n\n", time_spent);

    //Add a NULL terminating character to make it a proper string before printing
    //server_reply[recv_size] = '\0';
    //puts(server_reply);

    closesocket(s);
    WSACleanup();

    return 0;
}
