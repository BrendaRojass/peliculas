print("=============================\n")
print("   Sugerencias de peliculas  \n ")
print("=============================\n")
usuario=input("Buen dia, ¿Cual es tu nombre? ")
print("¿Que queres ver hoy, "+usuario+"?")
nombre_pelicula="Las Guerreras Kpop"
genero_pelicula="Accion"
anio_pelicula=2025
rating_pelicula=7.4
nombre_pelicula2="Troya"
genero_pelicula2="Accion"
anio_pelicula2=2004
rating_pelicula2=7.4
nombre_pelicula3="Spiderman"
genero_pelicula3="Accion"
anio_pelicula3=2002
rating_pelicula3=7.4
nombre_pelicula4="¿Y donde esta el piloto?"
genero_pelicula4="Comedia"
anio_pelicula4=1980
rating_pelicula4=7.7
nombre_pelicula5="Son como niños"
genero_pelicula5="Comedia"
anio_pelicula5=2010
rating_pelicula5=6.0
print("---- GENEROS ----")
print("Accion")
print("Comedia")
genero_favorito=input("¿Que genero te gusta? ")
print("Buscando peliculas del genero "+genero_favorito)
if (genero_pelicula==genero_favorito):
    print(nombre_pelicula)
if (genero_pelicula2==genero_favorito):
    print(nombre_pelicula2)    
if (genero_pelicula3==genero_favorito):
    print(nombre_pelicula3)   
if (genero_pelicula4==genero_favorito):
    print(nombre_pelicula4)
if (genero_pelicula5==genero_favorito):
    print(nombre_pelicula5)