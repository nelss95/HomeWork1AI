from search import Graph
#
# Sus respuestas para las preguntas falso y verdadero deben tener la siguiente forma.
# Sus respuestas deben verse como las dos siguientes:
#ANSWER1 = True
#ANSWER1 = False

# 1: Falso o Verdadero - busqueda Hill Climbing garantiza encontrar una respuesta
#    si es que la hay
ANSWER1 = False

# 2: Falso o Verdadero - busqueda Best-first encontrara una ruta optima
#    (camino mas corto).
ANSWER2 = False

# 3: Falso o Verdadero - Best-first y Hill climbing hacen uso de el
#    valor de la heuristica de los nodos.
ANSWER3 = True

# 4: Falso o Verdadero - A* utiliza un conjunto extendido de nodos
ANSWER4 = True

# 5: Falso o Verdadero - Anchura primero esta garantizado a encontrar un
#    camino con el minimo numero de nodos posible
ANSWER5 = True

# 6: Falso o Verdadero - El Branch and bound regular utiliza valores de
#    la heuristica para acelerar la busqueda de un camino optimo
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation

# Implemente estos y los puede revisar con el modulo tester

def bfs(graph, start, goal):
    queue = []
    set = []
    queue.append([start])
    while len(queue) != 0:
        set = queue.pop(0)
        current = set[-1]
        if current == goal:
            return set
        else:
            adjacent = graph.get_connected_nodes(current)
            for i in range(len(adjacent)):
                path = list(set)
                path.append(adjacent[i])
                queue.append(path)


## Si hizo el anterior el siguiente debe ser muy sencillo
def dfs(graph, start, goal):
    queue = []
    set = []
    visit = []
    queue.append([start])
    while len(queue) != 0:
        set = queue.pop(0)
        current = set[-1]
        if current == goal:
            return set
        else:
            if not current in visit:
                visit.append(current)
                adjacent = graph.get_connected_nodes(current)
                for i in range(len(adjacent)):
                    path = list(set)
                    path.append(adjacent[i])
                    queue.insert(0,path)


## Ahora agregue heuristica a su busqueda
## La busqueda debe ser hacia los valores mas bajos que indica la heuristica
def hill_climbing(graph, start, goal):
    raise NotImplementedError

## Ahora implementamos beam search, una variante de BFS
## que acota la cantidad de memoria utilizada para guardar los caminos
## Mantenemos solo k caminos candidatos de tamano n en nuestra agenda en todo momento.
## Los k candidatos deben ser determinados utilizando la
## funcion (valor) de heuristica del grafo, utilizando los valores mas bajos como los mejores
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Ahora se implemente busqueda optima, Las anteriores NO utilizan
## las distancias entre los nodos en sus calculos

## Esta funcion toma un grafo y una lista de nombres de nodos y retorna
## la suma de los largos de las aristas a lo largo del camino -- la distancia total del camino.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## Es util determinar si un grafo tiene una heuristica admisible y consistente
## puede dar ejemplos de grafos con heuristica admisible pero no consistente
## consistente pero no admisible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
