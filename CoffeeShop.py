from bs4 import BeautifulSoup
import requests

class CoffeeShop:
    #Menus
    
    def __init__(self, url_oficial, menu , nombre):
        self.url_oficial = url_oficial
        self.nombre = nombre
        self.menu = menu

    def get_page_oficial(self):
        response = requests.get(self.url_oficial)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    def get_page_menu(self):
        response_menus = requests.get(self.menu)
        soups = BeautifulSoup(response_menus.text, 'html.parser')
        return soups

starbucks = CoffeeShop("https://www.starbucks.com.ar/","https://www.starbucks.com.ar/menu", "Starbucks")

#Usamos esto para Buscar elementos
star = starbucks.get_page_oficial()
star_menus = starbucks.get_page_menu()

#Titulo de la Paginas Oficiales
star_titulos = star.title.get_text()

#Validar Seleccion
try:
    print("Bienvenido/a a 'Coffee Shop'\n")
    seleccion_empresa = int(input("1.Starbucks\nSeleccione '1' para Comenzar:"))
except ValueError as error:
    print("Valor Incorrecto")
    print(f"Error:{error}")
    
#Extraemos el Menu de la Pagina
tipos_cafes = []
for me in star_menus.find_all("h1",class_="display-sm text-semibold"):
    tipos_cafes.append(me.get_text())
    
#Seleccion de Starbucks
if seleccion_empresa == 1:
    print(f"--{star_titulos}--")
    
    #Mostramos todo el Menu de Cafes
    for i in range(len(tipos_cafes)):
        print(f"{i}.{tipos_cafes[i]}")
        
    print("-------")
    selec_tipo_cafe = int(input("Seleccione el Tipo de Cafe:"))
    
    #Cafe Caliente,Seleccionado = Cafe Caliente
    if selec_tipo_cafe == 0:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/bebidas/cafes-calientes", "https://www.starbucks.com.ar/menu/bebidas/cafes-calientes", "Cafe Caliente") 
        coffeee = Cafe_seleccionado.get_page_oficial()  
        #Extraemos todo los Tipos de Cafes Calientes             
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="subtitle line"):
            cafe_sell.append(coffee.get_text())
        #Mostramos los Cafes Calientes
        print("Lista de Cafes Calientes:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        #Evaluamos el Cafe Seleccionado
        try:
            select = int(input("Selecciona su Cafe Caliente:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        #Guardamos el Cafe Caliente
        cafe_comprado = cafe_sell[select]
    
    #Seleccion = Cafe Helados
    if selec_tipo_cafe == 1:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/bebidas/cafes-helados", "https://www.starbucks.com.ar/menu/bebidas/cafes-helados", "Cafe Helado") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="subtitle line"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Cafes Helados:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Cafe Helado:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Frappucino
    if selec_tipo_cafe == 2:
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/bebidas/frappuccino", "https://www.starbucks.com.ar/menu/bebidas/frappuccino", "Frappucino") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Frappucinos:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Frappucino:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Te Caliente
    if selec_tipo_cafe == 3:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/bebidas/te-caliente", "https://www.starbucks.com.ar/menu/bebidas/te-caliente", "Te Caliente") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Te calientes:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Te Caliente:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
     #Cafe Seleccionado = Te Helado
    if selec_tipo_cafe == 4:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/bebidas/te-helado", "https://www.starbucks.com.ar/menu/bebidas/te-helado", "Te Helado") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Te Helados:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Te Helado:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Heladas
    if selec_tipo_cafe == 5:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/bebidas/frias", "https://www.starbucks.com.ar/menu/bebidas/frias", "Frias") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Heladas:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Helada:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Calientes
    if selec_tipo_cafe == 6:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/bebidas/calientes", "https://www.starbucks.com.ar/menu/bebidas/calientes", "Calientes") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Calientes:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Caliente:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Bakery
    if selec_tipo_cafe == 7:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/comida/bakery", "https://www.starbucks.com.ar/menu/comida/bakery", "Bakery") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="subtitle line"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Bakery:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Bakery:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Sándwichs & preparados
    if selec_tipo_cafe == 8:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/comida/almuerzos", "https://www.starbucks.com.ar/menu/comida/almuerzos", "Almuerzo") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Sándwichs & preparados:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Sándwichs & preparados:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Snacks
    if selec_tipo_cafe == 9:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/comida/snacks", "https://www.starbucks.com.ar/menu/comida/snacks", "Snack") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Snacks:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Snack:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Cafe en Granos
    if selec_tipo_cafe == 10:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/en-casa/cafe-en-granos", "https://www.starbucks.com.ar/menu/en-casa/cafe-en-granos", "Cafe en Grano") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Cafe en Granos:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Cafe en Grano:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
    #Cafe Seleccionado = Te
    if selec_tipo_cafe == 11:
        
        Cafe_seleccionado = CoffeeShop("https://www.starbucks.com.ar/menu/en-casa/te", "https://www.starbucks.com.ar/menu/en-casa/te", "Te") 
        coffeee = Cafe_seleccionado.get_page_oficial()               
        cafe_sell = []
        for coffee in coffeee.find_all("div",class_="field field-product field-product-name"):
            cafe_sell.append(coffee.get_text())
        print("Lista de Tes:")
        for i in range(len(cafe_sell)):
            print(f"{i}.{cafe_sell[i]}")
        print("")
        try:
            select = int(input("Selecciona su Te:"))
        except ValueError as error:
            print("¡UPS! Parece que hubo un Error")
            print(f"Tipo de Error:{error}")
        
        cafe_comprado = cafe_sell[select]
        
print("")
print("¡Compra Finalizada!")
print(f"Producto:{cafe_comprado}")