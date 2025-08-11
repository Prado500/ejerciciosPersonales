def registrarEmpleado(nombre, posicion, salario):
    if not nombre or not posicion or not salario:
        print("Ingrese un valor idóneo para el nombre, la posición y el salario")
    if not isinstance(nombre, str) or not isinstance(posicion, str) or not isinstance(salario, (float,int)):
        print("Ha ingresado datos inválidos.\nAsegúrese de ingresar nombres y cargos compuestos por cadenas de caracteres.\nAsegúrese que el salario se compone de números positivos mayores que 0 ")
    else:
        return(nombre.capitalize(), posicion.capitalize(), salario)
    
def mostrarEmpleado(empleados):
    for i, (nombre, posicion, salario) in enumerate(empleados, start = 1 ):
        print(f"{i}. {nombre}, {posicion}, ${salario:.2f}")
         
def main():
    
    empleados = []
    
    while True:
        print("\n")
        print("*" * 36)
        print(f"{"*" * 10} MENU PRINCIPAL {"*" * 10}")
        print("*" * 36)
        print("\n")
        print("(1) Registrar empleados")
        print("(2) Mostrar empleados")
        print("(3) Salir")
        opcion = input("Digite alguna opción del menú: ")
        
        if not(opcion.isnumeric()):
            print("Ha digitado una opción inválida. Sólo se permite los números 1, 2 y 3. ")
            
        if opcion > "3" or opcion == "0":
            print("Ha digitado una opción inválida. Sólo se permite los números 1, 2 y 3. ")
        
        else:  
            if opcion.isnumeric() and 4 > int(opcion) >= 1 and opcion == "1":
                
                nombre = input("Ingrese el nombre: ")
                posicion = input("Ingrese la posición: ")
                salario = input("Ingrese el salario: ")
            
                if isinstance(nombre, str) and isinstance(posicion, str) and (salario.isnumeric() and 0 < int(salario)):
                    empleados.append(registrarEmpleado(nombre, posicion, float(salario))) 
                    
                else:
                    print("Los datos ingresados no son correctos.\nPor favor asegúrese de ingresar nombres y cargos reales.\nAsegúrese también de ingresar un salario que sea un número positivo y mayor que 0   ") 
            
            if opcion.isnumeric() and 4 > int(opcion) >= 1 and opcion == "2":
                mostrarEmpleado(empleados)
                    
            if opcion.isnumeric() and 4 > int(opcion) >= 1 and opcion == "3":
                break
        
        


        
            
# Prueba numero 1: usar un else que "controle" los datos equivocados, fallo.

# Pregunta no.1 Por que cuando la lista esta vacia me bota un error de digitacion de vlaores? R./ porque no puedo hacer tuple unpacking sobre una lista vacia
# Pregunta no.2 Por que no puede saltar de un if a otro if?
# Pregunta no.3 Por que no itera la lista? R./ porque la lista no tiene nada y no hay como hacer unpacking.

'''
Lecciones aprendidas:

Puedo mantener un bloque de codigo comentareado usando copilot, y si lo necesito de vuelta en forma de codigo solo de digo a copilot que close.
'''
if __name__ == "__main__":
    main()
    

