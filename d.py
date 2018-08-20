import socket              
import atexit

s = socket.socket()         
host = socket.gethostname()
port = 12345
s.connect((host, port))
while True:
    k = s.recv(1024).decode()
    if k != '':
        if k == "FINCOMING":
            ext = s.recv(1024).decode()
            print(ext)
            if ext == ".JPG":
                del k
                while True:
                    try:
                        print(".")
                        k = s.recv(5396847)
                        kch = k
                        kch += kch
                        if k == "FIN":
                            print("yes")
                            obj= open("YeEt"+ext,"wb")
                            obj.write(kch)
                            obj.close()
                            break
                    except UnicodeDecodeError:
                        pass
                    except ConnectionResetError:
                        print("yes")
                        obj= open("YeEt"+ext,"wb")
                        obj.write(kch)
                        obj.close()
                        break
                    
                
            else:
                obj= open("YeEt"+ext,"w")
                obj.write(k)
                obj.close()
                print("finished")
        else:
            print(k)
        
        
        

