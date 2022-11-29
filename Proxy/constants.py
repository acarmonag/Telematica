
privadas = open('/home/ubuntu/pibl/proxy/privadas.txt')
priv= privadas.read().split(",")
publicas = open('/home/ubuntu/pibl/proxy/publicas.txt')
publ= publicas.read().split(",")

IP_SERVER=str(priv[0])

IP_SERVERS=[publ[1],publ[2],publ[3]]


PORT = 8080
ENCONDING_FORMAT = "utf-8"
RECV_BUFFER_SIZE = 2048
QUIT = 'QUIT'
print(IP_SERVERS)
print(IP_SERVER)
