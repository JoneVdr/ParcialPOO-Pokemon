"""Ejercicio 1 (5 puntos)

Pokémon, qué empezó originalmente como un videojuego, gracias a su elevada popularidad logró expandirse a otros medios de entretenimiento como ha sido series de televisión, películas e incluso juegos de cartas.

En este ejercicio vamos a centrarnos únicamente en la versión de videojuego y vamos a intentar recrear un elemento muy importante de él. Vamos a crear una criatura Pokémon. Estas criaturas son como guerreros combatientes, los cuáles están guiados, entrenados y liderados por su entrenador.


Para quien no esté muy familiarizado con este videojuego, y por añadir un poco más de contexto, cada entrenador va a tener a su cargo un conjunto de criaturas Pokémon, los cuáles les va a servir al entrenador para cuándo él quiera entrar en combate con otro entrenador. Sin embargo, cuando dos entrenadores entran en combate, solamente las criaturas Pokémon son las que compiten entre sí.


En este ejercicio, vamos a hacer una versión programada en Python para que dos jugadores puedan jugar a este juego. Los jugadores se encontrarán representados por los entrenadores de cada uno de los equipos.


No es necesario implementar el docString correspondiente a las funciones y métodos desarrollados, aunque se recomienda hacer el diagrama de flujo de los métodos en papel de forma previa a su resolución.


En base a estas especificaciones se solicita que programe la clase Pokémon:


Cada criatura Pokémon va a estar caracterizado por:

o   ID del Pokémon. Número entero y único que identifica a la criatura Pokémon.

o   Nombre del Pokémon. Nombre de la critarua Pokémon.

o   Tipo de arma que lleva a cabo el Pokémon. En esta primera versión del juego, solamente 4 tipos de arma van a existir: Puñetazo, Patada, Codazo, Cabezazo.

o   Puntos de salud que tiene el Pokémon. Deben de estar entre 1 y 100.

o   Índice de ataque del Pokémon. Deben de estar entre 1 y 10.

o   Índice de defensa del Pokémon. Deben de estar entre 1 y 10.


Nota: Es obligatorio el uso de enumerados para el atributo del tipo de arma. El índice de ataque del Pokémon se recomienda que contenga el valor del tipo de arma. Se recuerda que el enumerado en Python tiene el formato "Clave / Valor".


Se pide:

i.     Incluya los atributos de esta clase y establezca la visibilidad adecuada (público, privado, protegido). Añada cualquier atributo y/o método que considere necesario.

ii.     Programe un método constructor que reciba los datos necesarios para crear un Pokémon. El método debe verificar el tipo y valor de cada uno de los parámetros y lanzar la excepción correspondiente cuando no se cumplan los requisitos. El método constructor debe asegurarse de que el atributo ID es una identificación nueva no tomada por otros Pokémons. Así mismo, programe también un método destructor que se encarge de eliminar la instancia de Pokemon de la variable lista de IDs global.

iii.     Programe un método que mejor corresponda para imprimir objetos de tipo Pokemon según el siguiente ejemplo: “Pokemon ID 8 with name Bulbasaur has as arma PUNCH and health 87.”

iv.     Programe los métodos setters y getters para la clase en función de lo que necesite. Si no necesita algún o ningún getter y/o setter, argumente por qué en un comentario dentro del módulo.

v.     Programe el método is_alive(self) de la clase Pokémon. Este método sirve para saber si el Pokemon está vivo.

vi.     Programe el método fight_attack(self, Pokémon pokemon_to_attack). Método que implementa el ataque del Pokémon usando un golpe sobre otro Pokémon. Este método se basa en el método fight_defense(self, int points_of_damage) del Pokémon atacado. Se aplicará el índice de ataque del Pokémon atacante como representación del golpe dado. Este método devolverá un booleano True si se ha podido atacar a la criatura Pokémon.

vii.     Programe el método fight_defense(self, int points_of_damage). Este método implementa la defensa del Pokémon de un golpe de otro Pokémon. Este método actualiza el atributo de puntos de salud que tiene el Pokémon en base a los puntos de daño recibidos menos el índice de defensa del propio Pokémon. Si el índice de defensa es mayor que los puntos de ataque recibidos, el método devolverá false y el Pokémon no sufrirá ningún daño. Este método devolverá un booleano True si se ha sufrido un ataque por parte de otra criatura Pokémon.

viii.     Pruebe los objetos de la clase Pokémon con los casos de prueba que se le han pasado.



Para ayudar en el desarrollo de este ejercicio, se le hace entrega de un UML parcialmente completo de la posible implementación de este juego. Se puede modificar o realizar un UML completamente distinto, el cuál es necesario explicar brevemente en un documento de texto o en los comentarios de un fichero .py. En caso de realizar un UML diferente, no se aplicarán los criterios en base a los casos de prueba facilitados, que es probable que no funcionen sin una adaptación previa.


Se facilitan también los archivos vacíos dónde deberán estar implementadas las clases que se piden y que tienen que ser completadas por el alumno. En dichas clases, están ya añadidos los casos de prueba de cada una de ellas."""

# Codigo

from enum import Enum

class Pokemon(Enum):

    Puñetazo = 1

    Patada = 2

    Codazo = 3

    Cabezazo = 4

class Pokemon:
        def __init__(self, id, nombre, arma, salud, ataque, defensa):
            self.id = id
            self.nombre = nombre
            self.arma = arma
            self.salud = salud
            self.ataque = ataque
            self.defensa = defensa

        def __del__(self):
            pass

        def __str__(self):
            return "Pokemon ID {} con nombre {} tiene como arma {} y salud {}".format(self.id, self.nombre, self.arma, self.salud)

        def set_id(self, id):
            self.id = id

        def get_id(self):
            return self.id

        def set_nombre(self, nombre):
            self.nombre = nombre

        def get_nombre(self):
            return self.nombre

        def set_arma(self, arma):
            self.arma = arma

        def get_arma(self):
            return self.arma

        def set_salud(self, salud):
            self.salud = salud

        def get_salud(self):
            return self.salud

        def set_ataque(self, ataque):
            self.ataque = ataque

        def get_ataque(self):
            return self.ataque

        def set_defensa(self, defensa):
            self.defensa = defensa

        def get_defensa(self):
            return self.defensa

        def is_alive(self):
            if self.salud > 0:
                return True
            else:
                return False

        def fight_ataque(self, pokemon_to_ataque):
            if self.is_alive() == True:
                return pokemon_to_ataque.fight_defensa(self.ataque)
            else:
                return False

        def fight_defensa(self, points_of_damage):
            if self.defensa > points_of_damage:
                return False
            else:
                self.salud = self.salud - (points_of_damage - self.defensa)
                return True

