# Ejecucion
 
python application.py o application.py

Se envían peticiones en cada thread con entityId M2M-Device-Test-<num_thread>
Si se arrancan 3 threads los threads se numeran del 0 al 2.

TransactionInfo es 69
entityType es device

# Configuracion

(Si no se puede cargar web.py no se crea el servidor local para test)

El fichero config.py tiene las propiedades

Url donde se envian las peticiones. La que esta puesta es un servidor que acepta un POST
url='http://localhost:8080/test'

Numero de threads
threads=10

Tiempo entre envios en cada thread (milisegundos)
time=5000

Numero de peticiones en cada thread
requests=2


