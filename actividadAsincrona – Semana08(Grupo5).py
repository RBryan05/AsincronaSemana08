# Actividad asincrona semana 8.
print("\nEste es un programa en el cual se han utilizado las condiciones compuestas, multiples y anidadas.\n")

# Datos que se utilizarán en el programa.
# Humanos
pais1 = "Estados Unidos"
pais2 = "El salvador"
pais3 = "Mexico"
pais4 = "Chile"
pais5 = "Guatemala"
pais6 = "Honduras"
pais7 = "Panamá"
pais8 = "Costa Rica"
pais9 = "Argentina"
pais10 = "España"
# Animales
anim1 = "Felinos"
anim2 = "Caninos"
anim3 = "Roedores"
anim4 = "Lagomorfos"
anim5 = "Reptiles"
anim6 = "Primates"
anim7 = "Insectos"
anim8 = "Peces"
anim9 = "Aves"
anim10 = "Mamiferos"

print("En este programa puede ingresar los datos de un humano o de un animal")

# Capturar datos desde teclado.
print("\nPor favor brinde los siguientes datos:")
name = input("\nEscriba el nombre del usuario -> ")

#Menú 1.
menu = input('''
              \tMenú

              1- Humanos
              2- Animales
              
              Elija una opción de menú -> ''').lower()
print("      ")
if menu == "humanos" or menu == "1":
    #Menú 2.
    menu2 = input(f'''"Seleccione su pais de origen"\n
                  \tMenú de paises.

                  1- {pais1}
                  2- {pais2}
                  3- {pais3}
                  4- {pais4}
                  5- {pais5}
                  6- {pais6}
                  7- {pais7}
                  8- {pais8}
                  9- {pais9}
                  10- {pais10}
                  
                  Ingrese una opción del menú de paises -> ''').lower()
    
    if menu2 == "estados unidos" or menu2 == "1":
        print(f"\n{name} usted es de {pais1}, el gentilicio de su pais es estadounidense.")
    elif menu2 == "el Salvadoreño" or menu2 == "2":
        print(f"\n{name} usted es de {pais2}, el gentilicio de su pais es salvadoreño.")
    elif menu2 == "mexico" or menu2 == "3":
        print(f"\n{name} usted es de {pais3}, el gentilicio de su pais es mexicano.")
    elif menu2 == "chile" or menu2 == "4":
        print(f"\n{name} usted es de {pais4}, el gentilicio de su pais es chileno.")
    elif menu2 == "guatemala" or menu2 == "5":
        print(f"\n{name} usted es de {pais5}, el gentilicio de su pais es guatemalteco.")
    elif menu2 == "honduras" or menu2 == "6":
        print(f"\n{name} usted es de {pais6}, el gentilicio de su pais es hondureño.")
    elif menu2 == "panama" or menu2 == "7":
        print(f"\n{name} usted es de {pais7}, el gentilicio de su pais es panameño.")
    elif menu2 == "costa Rica" or menu2 == "8":
        print(f"\n{name} usted es de {pais8}, el gentilicio de su pais es costarricenses.")
    elif menu2 == "argentina" or menu2 == "9":
        print(f"\n{name} usted es de {pais9}, el gentilicio de su pais es argentino.")
    elif menu2 == "españa" or menu2 == "10":
        print(f"\n{name} usted es de {pais10}, el gentilicio de su pais es español.")

    
    else:
        print(f"La opción ingresada ({menu2}) no está definida en el programa.")

elif menu == "animales" or menu == "2":
    #Menú 3
    menu2 = input(f'''
                  \tMenú de especies.

                  1- {anim1}
                  2- {anim2}
                  3- {anim3}
                  4- {anim4}
                  5- {anim5}
                  6- {anim6}
                  7- {anim7}
                  8- {anim8}
                  9- {anim9}
                  10- {anim10}
                  
                  Ingrese una opción del menú -> ''').lower()
     
     #Estructuras anidadas.
    if menu2 == "felinos" or menu2 == "1":
        print(f"\n{name} usted elijió la especie {anim1.lower()}, los animales que se encuentran en esta especie son: gatos, tigres, leones, etc.")
    elif menu2 == "caninos" or menu2 == "2":
        print(f"\n{name} usted elijió la especie {anim2.lower()}, los animales que se encuentran en esta especie son: perros, lobos, coyotes, etc.")
    elif menu2 == "roedores" or menu2 == "3":
        print(f"\n{name} usted elijió la especie {anim3.lower()}, los animales que se encuentran en esta especie son: ratas, cobayas, hámsters, etc.")
    elif menu2 == "lagomorfos" or menu2 == "4":
        print(f"\n{name} usted elijió la especie {anim4.lower()}, los animales que se encuentran en esta especie son: conejos, liebres, etc.")
    elif menu2 == "reptiles" or menu2 == "5":
        print(f"\n{name} usted elijió la especie {anim5.lower()}, los animales que se encuentran en esta especie son: serpientes, cocodrilos, tortugas, etc.")
    elif menu2 == "primates" or menu2 == "6":
        print(f"\n{name} usted elijió la especie {anim6.lower()}, los animales que se encuentran en esta especie son: chimpancés, gorilas, lémures, etc.")
    elif menu2 == "insectos" or menu2 == "7":
        print(f"\n{name} usted elijió la especie {anim7.lower()}, los animales que se encuentran en esta especie son: mosquitos, arañas, avispas, hormigas, etc.")
    elif menu2 == "peces" or menu2 == "8":
        print(f"\n{name} usted elijió la especie {anim8.lower()}, los animales que se encuentran en esta especie son: truchas, salmones, sardinas, pez espada, etc.")
    elif menu2 == "aves" or menu2 == "9":
        print(f"\n{name} usted elijió la especie {anim9.lower()}, los animales que se encuentran en esta especie son: patos, gaviotas, galivan, carpinteros, etc.")
    elif menu2 == "mamiferos" or menu2 == "10":
        print(f"\n{name} usted elijió la especie {anim10.lower()}, los animales que se encuentran en esta especie son: ornitorrincos, canguros, murciélagos, etc.")

    else:
        print(f"La opción ingresada ({menu2}) no está definida en el programa.")

else:
    print(f"\nLa opción ({menu}) no forma parte del programa, asegurate de haber escrito bien tu elección.")

print("\nFin del programa\n")