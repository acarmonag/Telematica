PORT = 8080
ENCONDING_FORMAT = "utf-8"
RECV_BUFFER_SIZE = 2048
privadas = open('/home/ubuntu/patico2/privadas.txt')
priv= privadas.read().split(",")

IP_SERVER=str(priv[1])
