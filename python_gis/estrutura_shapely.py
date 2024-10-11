'''
Objetivo: Entender conceito de ponto linha e polígono.
'''
# Importando componentes
from shapely.geometry import Point, LineString, Polygon;

# Pontos
pontoA = Point(4.4, 8.4)    # Formado por uma coordenada x e y. E em alguns casos inclui a coordenada z, exemplo altitude.
pontoB = Point(-5.3,-10.3)
pontoC = Point(8.5,-3.8)

print(type(pontoA))
print(pontoA)

## Coordenadas
print(("Obtendo coordenadas do ponto A"))
print(pontoA.coords.xy)

## Distância
print('Obtendo distância do ponto B até o A')
print(pontoB.distance(pontoA))

# Linestring
