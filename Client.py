import socket              
import atexit

s = socket.socket()         
host = socket.gethostname()
port = 12345
s.connect((host, port))
rec = b''
while True:
    k = s.recv(1024).decode()
    if k != '':
        if k == "FINCOMING":
            ext = s.recv(1024).decode()
            size = s.recv(1024).decode("utf-16")
            filename = s.recv(1024).decode()
            if ext == ".JPG" or ext == ".png" or ext==".jpg":
                while True:
                    print(".")
                    k = s.recv(int(size))
                    if k != b'FIN':
                        rec += k
                    if k == b'FIN':
                        print("FINISHED")
                        obj= open(filename,"wb")
                        obj.write(rec)
                        obj.close()
                        break
                    
                
            else:
                rec = s.recv(1024).decode()
                obj= open(filename,"w")
                obj.write(rec)
                obj.close()
                print("FINISHED")
        else:
            print(k)
        
        
        

