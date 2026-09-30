import mysql.connector

conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sistema_cafeteria"
)

def create():
    print("__ Tomar Pedido __")
    print("Para tomar su orden necesitamos:")
    name=input("Nombre: ")
    print("===== MENU =====")

    lista=["1. Cafe Simple = Q15","2. Cafe con leche = Q20","3. Cafe con cremora = Q20","4. Capuchino = Q25","5. Especial de la casa =  Q30"]
    for listas in lista:
        print(listas)
    name_product=input("Nombre del cafe: ").lower()
    if name_product == "cafe simple":
        precio=15
    elif name_product=="cafe con leche":
        precio=20
    elif name_product=="cafe con cremora":
        precio=20
    elif name_product=="capuchino":
        precio=25
    elif name_product=="especial de la casa":
        precio=30
    else:
        print("Opcion no valida")
        
    print("__________________________")
    cantidad=int(input("Cuantos desea ordenar: "))
    print("__________________________")
    tipo=["Regular","Estudiante","Docente"]
    for tipos in tipo:
        print(tipos)
    typp=input("Para quien es la orden: ").lower()
    
    if typp == "estudiante":
        des=10
        Total=(cantidad*precio)-10

    elif typp == "docente":
        des=15
        Total=(cantidad*precio)-15
    else:
        des=0
        Total=cantidad*precio
    
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="INSERT INTO pedidos(customerName, productName,quantity,orderType,discount,total ) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,name_product,cantidad,typp,des,Total))
        conexion.commit()
        print("=========================")
        print("RESUMEN DE ORDEN")
        print(f"Su orden es: {cantidad} {name_product}")
        print(f"Descuento: Q{des}")
        print (f"Su total es de: Q{Total}")
        print(f"Su numero de ID: {cursor.lastrowid}")



def read():
    print("REVISAR PEDIDOS")
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="SELECT * FROM pedidos"
        cursor.execute(query,)
        coffe=cursor.fetchall()
        for fila in coffe:
            print(fila)


def update():
    print("EDITAR PEDIDO")
    id_buscar=int(input("Ingrese el número ID de la orden: "))
    if conexion.is_connected():
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE idpedidos = %s", (id_buscar,))
        dato=cursor.fetchone()

        if dato :
            print("Registro encontrado")
            print(dato)

            new_name=input("Nuevo nombre: ")
            print("_______________________")
            lista=["1. Cafe Simple = Q15","2. Cafe con leche = Q20","3. Cafe con cremora = Q20","4. Capuchino = Q25","5. Especial de la casa =  Q30"]
            for listas in lista:
                print(listas)
            new_product=input("Nombre del cafe: ").lower()
            print("________________________")
           

            if new_product == "cafe simple":
                precio=15
            elif new_product=="cafe con leche":
                precio=20
            elif new_product =="cafe con cremora":
                precio=20
            elif new_product =="capuchino":
                precio=25
            elif new_product =="especial de la casa":
                precio=30
            else:
                print(f"{new_product} No esta en el menu")
            
            new_cantidad=int(input("Cantidad: "))
            tipo=["Regular","Estudiante","Docente"]
            for tipos in tipo:
                print(tipos)

            new_typp=input("Quien ordena: ").lower()


            if new_typp == "estudiante":
                des=10
                Total=(new_cantidad*precio)-10
            
            elif new_typp == "docente":
                des=15
                Total=(new_cantidad*precio)-15
            else:
                des=0
                Total=new_cantidad*precio

            
        else:
            print("Registro no encontrado")


        query ="""
            UPDATE pedidos
            SET customerName = %s,
                productName=%s,
                quantity=%s,
                orderType=%s,
                discount=%s,
                total=%s
        
            WHERE idpedidos=%s

"""

        cursor.execute(query,(new_name,new_product,new_cantidad,new_typp,des,Total,id_buscar))
        conexion.commit()
        print("Actualización Guardada")



def delete():
    print("__ ELIMINAR PEDIDO")
    id=int(input("Ingrese el número ID del pedido: "))

    if conexion.is_connected():
        cursor=conexion.cursor()
        query="DELETE FROM pedidos WHERE idpedidos = %s"
        cursor.execute(query,(id,))
        conexion.commit()
        print("Se eliminó correctamente")





    
def menu():

    print("BIENVENIDO A LA CAFETERIA")
    while True:
        try:

            lista=["1. Tomar orden","2. Revisar pedidos","3. Editar pedido","4. Eliminar"]
            for listas in lista:
              print(listas)
            
            desi=int(input("Ingrese el número de opcón que realizará: "))
            break
        except ValueError:
            print("ERROR")

    if desi == 1:
        create()
    elif desi == 2:
        read()
    elif desi == 3:
        update()
    elif desi == 4:
        delete()
    else:
        print("Esta opcion no es válida")
            
    

menu()