import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_pedido(pedidos, nombre_cliente, direccion, contacto, sexo, descripcion_lugar, nombre_producto, referencia_producto, cantidad):
    if nombre_cliente not in pedidos:
        pedidos[nombre_cliente] = []
    
    pedido = {
        'Nombre del cliente': nombre_cliente,
        'Dirección': direccion,
        'Contacto': contacto,
        'Sexo': sexo,
        'Descripción del lugar': descripcion_lugar,
        'Producto': {
            'Nombre': nombre_producto,
            'Referencia': referencia_producto,
            'Cantidad': cantidad
        }
    }
    pedidos[nombre_cliente].append(pedido)

def mostrar_pedidos(pedidos):
    clear_console()
    print("=== Pedidos realizados ===")
    for cliente, lista_pedidos in pedidos.items():
        print(f"Cliente: {cliente}")
        for pedido in lista_pedidos:
            print("Información del pedido:")
            for clave, valor in pedido.items():
                if clave == 'Producto':
                    print(" - Detalles del producto:")
                    for detalle, info in valor.items():
                        print(f"   {detalle}: {info}")
                else:
                    print(f" - {clave}: {valor}")
            print("=" * 50)

def main():
    pedidos = {}

    while True:
        clear_console()
        print("\n1. Registrar pedido")
        print("2. Mostrar pedidos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            contacto = input("Ingrese el contacto del cliente: ")
            sexo = input("Ingrese el sexo del cliente: ")
            descripcion_lugar = input("Ingrese la descripción del lugar: ")
            nombre_producto = input("Ingrese el nombre del producto: ")
            referencia_producto = input("Ingrese la referencia del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")

            registrar_pedido(pedidos, nombre_cliente, direccion, contacto, sexo, descripcion_lugar, nombre_producto, referencia_producto, cantidad)
            print("Pedido registrado exitosamente.")
            input("Presione Enter para continuar...")
        
        elif opcion == '2':
            if pedidos:
                mostrar_pedidos(pedidos)
                input("Presione Enter para continuar...")
            else:
                print("No hay pedidos registrados.")
                input("Presione Enter para continuar...")
        
        elif opcion == '3':
            print("chao sapo")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
