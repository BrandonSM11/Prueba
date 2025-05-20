Shop ={}

def Add_New_products(): #  This funtion we request the user login the name, price and amount for new products and add the diccionario
    try:
        name = input ("Ingresa nombre del producto: ")
        price = float(input("Ingresa el precio del pruducto: "))
        amount = int(input("Ingresa la cantidad a adquirir: "))

        New ={
            
            "price" : price,
            "amount" : amount
        }
        
        Shop[name] = New
        print ("Producto agregado ")
    except ValueError:
        print("Error: Ingrese valores válidos.")

def Check_products() : # Funtion check productos in the shop 
 
        if not Shop :
             print ("No hay productos en el inventario")
        else :
             for name, New in Shop.items():
                print(f"\n \033[92m name:\033[0m{name}")     # print the name of product
                print (f"\033[92m  price:\033[0m{New['price']}")  #print the price of product
                print (f"\033[92m  amount:\033[0m{New['amount']}") #print amount of producto
                print("______________________________")


def Search_product():    #Funtion for search one products in the shop
    try:
        name = input ("Ingrese el nombre del producto que deseas buscar: ")   # we request the user login name the product 
        if name in Shop :       #  if name in shop
            new = Shop[name]
            print(f"\n name:{name}")            #print name, price and amount of product
            print (f"price:{new['price']}")  
            print (f"amount:{new['amount']}")
        else:
            print (" \033[91mPRODUCTO NO DISPONIBLE\033[0m")  
    except ValueError:
        print("Error: Ingrese valores válidos.")
def Update_price () : #Funtion for uptape price of products in shop
    try:
        name = input ("Ingrese el nombre del producto que deseas actualizar el precio: ") #Request the user login name of product
        if name in Shop :
            new_price = float(input("Ingrese el nuevo precio del producto: ")) #Request new price 
            Shop[name]['price'] = new_price
            if new_price <0 : #if new price is < zero
                 print("\033[93m El numero debe ser positivo\033[0m") #print 
            if new_price >=1 : #if new price is > or = one 
                print("\n \033 Nuevo precio actualizado\033[0m") #printo 
        
        else :
            print ("\033Producto no encontrado\033[0m")  
    except ValueError:
        print("Error: Ingrese valores válidos.")


def Delete_product() : #funtion for delete products the shop
    try:
        name = input("Ingrese el nombre del producto que deseas eliminar: ")    #Request the user login name of product
        if name in Shop : # if name in shop, print the name is Available
            print (f"El produto {name} esta disponible")
            op= input ("Deseas eliminarlo (si/no)") #request the user, do we want delete?
            if op == "si": # if option is "si", products delete
                Shop.pop(name)
                print("El producto ha sido eliminado") #Print delete product
            else : #else
                print("No se han generado cambios") #print Don't changes
    except ValueError:
        print("Error: Ingrese valores válidos.")
        


def Value_total(): #funtion for calculate value total in the shop
    
     
  ValueTotal = lambda Shop: sum(producto['price'] * producto['amount'] for producto in Shop.values()) # Calculate 
  total = ValueTotal(Shop) 
  print(f"Valor total del inventario: {total}") #print the value total 


while True:                 #Menu 
    print("1. New products ")
    print("2. Consultar productos")
    print("3. Buscar un producto")
    print("4. Actualizar precios ")
    print("5. Delete productos ")
    print("6. Calcular total del inventario ")
    print("7. Salir " )
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        Add_New_products()
    elif opcion == "2":
        Check_products()
    elif opcion == "3":
        Search_product()
    elif opcion == "4":
        Update_price ()
    elif opcion == "5":
        Delete_product()
    elif opcion == "6" :
        Value_total()
    elif opcion == "7":
        print ("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")


