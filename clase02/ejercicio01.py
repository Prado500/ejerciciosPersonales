# def registrarEmpleado (nombre, cargo, salario):
#     if not nombre or not cargo or not salario or salario <=0 :
#         raise ValueError ("Datos no validos. Asegúrese que el nombre, el cargo y el salario fueron digitados.\nAsegúrese también que el valor del salario es un numero positivo diferente de 0. ")
#     return(nombre.title(), cargo.title(), float(salario))

# def mostrarEmpleados(empleados):
#     for i, emp in enumerate(empleados, start = 1):
#         print(f"{i}. {nombre} - {cargo} - ${salario:.2f}")
        

def registrarEmpleado (nombre: str, cargo: str, salario):
            
    if not isinstance(nombre, str) or not isinstance(cargo, str):
        raise ValueError("El nombre y el cargo solo pueden contener letras")
    if not nombre or nombre.isnumeric() or not cargo or salario <= 0 or not salario or not isinstance(salario, (int,  float)): # OJO! Si pongo or or not isinstance(salario, int) or not isinstance(salario, float), vuelvo la condicion mutuamente excluyente y nunca va a guardar el dato
        raise ValueError("Ingrese por favor cada uno de los datos de los empleados: nombre, cargo y salario.\nRecuerde que el valor del salario debe ser un numero mayor que 0 y positivo.")
    return (nombre.title(), cargo.title(), salario)

def mostrarEmpleados(empleados):
    for i, (nombre, cargo, salario) in enumerate(empleados, start = 1):
        print(f"{i}. {nombre}, {cargo}, ${salario:.2f}")
        
def main():
    empleados = []
    
    
    # try:
    #     empleados.append(registrarEmpleado("hola", "Ingeniero de Software", 8500))
    #     empleados.append(registrarEmpleado("Andrew Marastuques", "Software Architect", 16400))
    #     empleados.append(registrarEmpleado("Maruel Andarriaga", "Analista de datos", 8000))
    #     empleados.append(registrarEmpleado("Yenika Uflaiga", "Gerente de ventas", 9000))
    #     empleados.append(registrarEmpleado("David Urrega", "Consultor Externo", 1000.89))
    #     empleados.append(registrarEmpleado("Manuel Ortega", "QA Specialist", 4500))
    #     empleados.append(registrarEmpleado("Mario Gamboa", "Front end developer", 3500))
    #     empleados.append(registrarEmpleado("Sofia Pua", "Marketing", 1400))
    # except ValueError as e:
    #     print(e)
    #
    # mostrarEmpleados(empleados)
    
    # while True:
    #     print("~~~~Registro y Visualización de Empleados~~~~")
    #     print("*" * 60)
    #     print(f"{" " * 12} {"*" * 5}  Menú Principal {"*" * 5} ")    
    #     print("\n")
    #     print("Registrar Empleado (1)")
    #     print("Mostrar Empleados (2)")
    #     print("Salir (3)")
    #     try:
    #         opcion = int(input("Ingrese la opción de su preferencia: "))
    #     
    #         if not opcion or not isinstance(opcion, (int, float)) or 0 >= opcion > 3:
    #             raise ValueError("Por favor, seleccione una opcion./nPor favor ingrese un número del 1 al 3.") 
    #         if opcion == 1:
    #                 nombre = input("Digite el nombre: ")
    #                 posicion = input("Digite la posición: ")
    #                 salario = float(input("Digite el salario: "))
    #                 empleados.append(registrarEmpleado(nombre, posicion, salario))
    #             
    #         if opcion == 2:
    #             print("Mostrar empleados")
    #             print("\n")
    #             mostrarEmpleados(empleados)
    #      
    #         if opcion == 3:
    #             break
    #     except ValueError as e:
    #         print(e)
        
    while True:
        print("\n")
        print("~~~~Registro y Visualización de Empleados~~~~")
        print("*" * 60)
        print(f"{" " * 12} {"*" * 5}  Menú Principal {"*" * 5} ")    
        print("\n")
        print("Registrar Empleado (1)")
        print("Mostrar Empleados (2)")
        print("Salir (3)")
        print("\n")
        
        
        try:
            opcion = input("Ingrese la opción de su preferencia: ")
            
            if not(opcion.isnumeric()):
                raise ValueError("Opcion inválida. Asegurese de ingresar un número que corresponda a algúna de las opciones del menú") 
                    
            if not (0 < int(opcion) <= 3):
                raise ValueError("Opcion inválida. Asegurese de ingresar un número entero que sea positivo y que este entre 1 y 3.")
                
            
            if opcion == "1":
                    nombre = input("Digite el nombre: ")
                    posicion = input("Digite la posición: ")
                    salario = float(input("Digite el salario: "))
                    empleados.append(registrarEmpleado(nombre, posicion, salario))
                
            if opcion == "2":
                    print("Mostrar empleados")
                    print("\n")
                    mostrarEmpleados(empleados)
                
            if opcion == "3":
                    break
            
        
        except ValueError as e:
            print(e)
            
if __name__ == "__main__":
    main()
    
    
    
    """
    Lecciones aprendidas:
    
    1.) Si antes de un Raise ValueError("mensaje predeterminado de error") hay un error de tiempo de ejecucion dentro de el bloque
    try, como una convercion a entero de un string distinto a numeros, python se va directo al except y muestra el mensaje de excepcion para el error por defecto.
    
    2.) Si Python logra llegar a las lineas de codigo que dictaminan la necesidad de entrar a un Raise ErrorValue, se va al except
    y muestra el mensaje de error predeterminado.
    
    3.) El try except va en el metodo main y los Raise ValueError van en los metodos.

    4.) Hay un boton que sirve para mostrar en una sola pantalla dos versiones del codigo que estoy haciendo; a la derecha el que edito y a la izquierda el que registra en donde hice cambios (en que linea). Se llama show changes.
    
    5.) A veces es necesario matar el terminal antes de probar un cambio.
    
    """