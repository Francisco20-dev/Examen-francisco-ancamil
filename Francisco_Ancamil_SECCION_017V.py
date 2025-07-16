
#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

def mostrarstockmarca():
    clasificaion= input("ingrese una maraca de equipo para consultar su stock: ").upper()
    clasificaion= clasificaion.strip().upper()
    encontrados=[]

    for codigo, valor in productos():
       
        if clasificaion.upper()==clasificaion:
            marca,stoc=stock[codigo]
            encontrados.append((codigo,marca,stoc))
    if encontrados:
        print("productos encontrados")
        for codigo,marca,stoc in encontrados:
            print(f"codigo:{codigo}, maarca:{marca}, stock:{stoc}")
    else:
        print("no se encontraron productos")
   

def mostrarprecio():
    try:
        p_min=int(input("Ingrese un valor de precio minimo: "))
        p_max=int(input("Ingrese un valor de precio maxmo"))
    except ValueError:
        print("Error debe ingresar valores enteros")
        return
    resultados=[]
    for codigo, datos in stock.items():
        precio,stock=datos
        if p_min<=precio <=p_max and stock>0:
            resultados.append((productos[codigo],precio,codigo))

    if resultados:
        resultados.sort()
        print("nootebooks encontrados: ")

        for modelo, precio , codigo in resultados:
            print(f"codigo:{codigo}, modelo:{modelo},precio:{precio}")
        else:
            print("no hay notebooks en ese rango de precios.")

def actualizar_precio():
    while True:
        actualiza_p=(input("ingrese el codigo del computador: "))
        if  actualizar_precio in stock:
            try:
                nuevo_precio=int(input("ingrese el nuevo precio "))
                stock[codigo][0]=nuevo_precio
                print("precio actualizado con exito")
            except ValueError:
                print("debe ingresar un valor entero")
        else:
            print("el codigo del notebook no existe")
        continuar=input("desea actualizar otro precio(S/N)?").lower()
        if continuar!="s":
            break
    

while True:
    print("1. Stock marca.")
    print("2  Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    opcion=input("ingrese la opccion que desea: ")

    if opcion =="1":
        mostrarstockmarca()
    elif opcion=="2":
         mostrarprecio()
    elif opcion=="3":
        actualizar_precio()
            
    elif opcion=="4":
        print("saliendo del programa")
        break
    