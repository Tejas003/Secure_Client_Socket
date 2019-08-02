
#Secure Client Socket

1. As we all know Secure means over HTTPs, This program reads '.txt' files stored on both HTTPs and HTTP websites 
2. It takes URL from user and validates if its a http or https url, if https it creates a ssl context and wraps the socket in it 
3. It fetches the domain from the URL and establishes a socket with the host over port 80(As its only for HTTP sites)
3. It then asks for a directory to store data
4. later reads and copies data from the '.txt. file on the internet and stores in the directory as hostname.txt
5. Once done it closes the socket connection

#Python Features used
1. Socket library 
2. Regex Library
3. SSL library

Developed by Tejas Shinde
