# LyricalGenious
Python graph application that automatically opens a folder which is filled with txts of song lyrics and creates a graph based on what it is found inside the txts.

Once the graph is created the application chooses a random node and starts to generate a song based on the weights of the graph.

TODO: delete this after finishing
Grafos
	estructuras de datos que no siguen ninguna logica y se representan atravez de nodos
	no tienen nodos principales
	estan formados por nodos y edges
	los nodos de un grafo estan formados por el contenido y una lista de edges
	las edges son uniones entre 2 nodos, 
	int size
	una lista con todos los nodos 
	para generar la cancion elegimos un nodo al azar de la lista
	
Grafos ponderados
	los edges tienen pesos que indican el orden(el mayor peso es el primero)
	
Edges
	formado por dos nodos y un int que es el peso

Practica
	carpeta de songs min 10 ficheros
		s1.txt
		s2.txt
		s3.txt
		s4.txt
	programa que coge las cancione y crea los grafos
	programa python que abre los ficheros y los lee palabra por palabra
		el programa coje la primera palabra y pregunta al grafo si hay algun nodo para la palabra escogida, si no lo hay lo crea y lo enlaza con el nodo anterior si el edge no existe, si el edge existe le incrementa el peso.
		si 
		si llega a un nodo que no tiene "salida", se elegira otro nodo para continuar 
	estructuras de datos
		clase edge
		clase graph
		clase node
		
		main
			metodo que crea grapho(path carpeta)
				
			metodo que crea cancion(grafo)
