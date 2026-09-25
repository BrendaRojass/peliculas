print("=============================\n")
print("   Sugerencias de peliculas  \n ")
print("=============================\n")
usuario=input("Buen dia, ¿Cual es tu nombre? ")
print("¿Que queres ver hoy, "+usuario+"?")
peliculas=[["Las Guerreras Kpop","Accion",2025,7.4],["John Wick","Accion",2014,7.5],["Logan","Accion",2017,8.5],["Resident Evil:Noche cero","Terror",2026,7.7],["¿Y donde esta el piloto?","Comedia",1980,7.7],["Son como niños","Comedia",2010,6.0],["Los tres chiflados","Comedia",2012,5.2],["El extraño mundo de jack","Animacion",1993,7.9],["Up","Animacion",2009,8.3],["Barbie en el Cascanueces","Animacion",2001,6.4],["It","Terror",2017,7.3]] 
print("---- GENEROS ----")
print("Accion")
print("Comedia")
print("Animacion")
print("Terror")
genero_favorito=input("¿Que genero te gusta? ")
rating_favorito=float(input("¿Cual es el rating minimo?"))
print("Buscando peliculas del genero "+genero_favorito)
encontrar_pelicula=False

for pelicula in peliculas:
    nombre=pelicula[0]
    genero=pelicula[1]
    rating=pelicula[3]
    if (genero_favorito.lower()==genero.lower()) and rating_favorito:
        print(nombre)
        encontrar_pelicula=True
if (not encontrar_pelicula):
  print("No se ha encontrado ninguna pelicula con ese rating.")        

# if (genero_pelicula==genero_favorito) and (rating_favorito<rating_pelicula):

#     print(nombre_pelicula)
#     encontrar_pelicula=True
    
# if (genero_pelicula2==genero_favorito) and (rating_favorito<rating_pelicula2):
#     print(nombre_pelicula2)
#     encontrar_pelicula=True
        
# if (genero_pelicula3==genero_favorito) and (rating_favorito<rating_pelicula3):
#     print(nombre_pelicula3)  
#     encontrar_pelicula=True
    
# if (genero_pelicula4==genero_favorito) and (rating_favorito<rating_pelicula4):
#     print(nombre_pelicula4)
#     encontrar_pelicula=True
    
# if (genero_pelicula5==genero_favorito) and (rating_favorito<rating_pelicula5):
#     print(nombre_pelicula5)
#     encontrar_pelicula=True
   
# if (genero_pelicula6==genero_favorito) and (rating_favorito<rating_pelicula6):
#     print(nombre_pelicula6)
#     encontrar_pelicula=True
       
# if (genero_pelicula7==genero_favorito) and (rating_favorito<rating_pelicula7):
#     print(nombre_pelicula7)
#     encontrar_pelicula=True
   
# if (genero_pelicula8==genero_favorito) and (rating_favorito<rating_pelicula8):
#     print(nombre_pelicula8)
#     encontrar_pelicula=True
   
# if (genero_pelicula9==genero_favorito) and (rating_favorito<rating_pelicula9):
#     print(nombre_pelicula9)
#     encontrar_pelicula:True
# if (genero_pelicula10==genero_favorito) and (rating_favorito<rating_pelicula10):
#     print(nombre_pelicula10)  
#     encontrar_pelicula=True  
# if (not encontrar_pelicula):
#     print("No se ha encontrado ninguna pelicula con ese rating.")