import socket               # Import socket module
import os
soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine nam
print 'Enter the port number: '
port = int(raw_input())            # Reserve a port for your service.
soc.bind((host, port))       # Bind to the port
print 'Listening'
soc.listen(5)                 # Now wait for client connection.
while True:
    conn, addr = soc.accept()     # Establish connection with client.
    print ("Got connection from",addr)
    msg1 = conn.recv(1024)
    print msg1
    msg2 = conn.recv(1024*1024)
    print msg2
    msg3 = conn.recv(1024)
    print msg1, msg2, msg3
    m1=""
    m2=""
    m3=""
    flag = 1
    for m in msg1:
        if m>=' ' or m=='\n':
            m1+=m
    for m in msg2:
        if m>=' ' or m=='\n'  :
            if m=='@' and flag==1:
                flag=0
            elif flag==0:
                m2+=m
    flag=1
    for m in msg3:
        if m>=' ' or m=='\n':
            if m=='#' and flag==1:
                flag=0
            else:
                m3+=m
    print m1, m2, m3
    fobj= open(m1, "w")
    fobj.write(m2)
    fobj.close()
    #os.system('echo "'+m2+'" >> '+m1)
    form=m1.split('.')
    if form[1]=='c':
        s='cc '+m1+' -o temp'
        a=os.system(s)
        print a
        if m3=="" and a==0:
            s='./temp > ans.txt'
        elif a==0:
            fx = open("inp.txt", "w")
            fx.write(m3)
            fx.close()
            s='./temp < inp.txt > ans.txt'
    elif form[1]=='cpp':
        s='g++ '+m1+' -o temp '
        a=os.system(s)
        if m3=="" and a==0:
            s='./temp > ans.txt'
        elif a==0:
            fx = open("inp.txt", "w")
            fx.write(m3)
            fx.close()
            s='./temp < inp.txt > ans.txt'
    elif form[1]=='py':
        if m3=="":
            s='python '+m1+' > ans.txt'
        else:
            fx = open("inp.txt", "w")
            fx.write(m3)
            fx.close()
            s='python '+m1+' < inp.txt > ans.txt'
    elif form[1]=='java':
        s='javac '+m1+' > ans.txt'
        a=os.system(s)
        if m3=="" and a==0:
            s='java '+form[0]+' > ans.txt'
        elif a==0:
            fx = open("inp.txt", "w")
            fx.write(m3)
            fx.close()
            s='java '+form[0]+'< inp.txt > ans.txt'
    a=os.system(s)
    print a
    s='error'
    if a==0:
        fo=open("ans.txt")
        s=fo.read()
    s=s.replace("\n","@");
    s=s+'\n'
    conn.send(s)
