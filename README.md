# Telematica
## Entrega Proyecto 1
### PIBL
Integrantes:
- Carlos Mosquera
- Antonio Carmona

#### Que es un Proxy Inverso?
En términos generales, un servidor proxy es una interfaz de comunicación en una red que se hace cargo de las peticiones y las transmite en calidad de representante 
a un ordenador de destino. En las redes corporativas se recurre a esta estructura para que los dispositivos cliente tengan un acceso controlado a Internet. El servidor 
configurado como proxy se presenta, en este caso, como la única posibilidad de conexión con la red pública. Se puede hablar, así, de un proxy de reenvío (forward proxy).

#### Que se utilizo?
Implementacion completa en nube de AWS con lenguajes como Python, Django y HTML

#### Como se desarrollo?
Se creo un archivo llamado "pb.py" que actua como el proxy recibiendo las peticiones http enviadas por el host almacena el registro de la peticion y luego la envia a cada
servidor buscando el servidor menos congestionado devolviendolo al host y registrandolo; en la creacion de los servidores se intento crear un servidor en django que se 
encontrara corriendo en cada una de las maquinas pero sin mucho exito por problemas de decodificacion por lo cual se crearon unos servidores en python con el nombre 
"pato.py" que se ecargaron de devolver un archivo html como respuesta de la peticion del proxy

#### Conclusion
Durante el desarrollo de este método, pudimos poner en práctica muchos de los conceptos relacionados con la implementación de proxy inversos, el procesamiento de sockets
y el envío de solicitudes HTTP a través de una red simulada, pudiendo concluir que la utilidad de un proxy para las solicitudes de red, filtrado, balanceo y gestión de
red, son esenciales.

#### Referencias 
Codigo de laboratorio del profesor Juan Carlos Montoya: (MultiHilos) https://github.com/ST0255/st0255-20222/tree/main/LabSocketsMultiThread

Codigo de taller3 proyecto integrador https://github.com/acarmonag/ProjectoIntegradorTaller3
