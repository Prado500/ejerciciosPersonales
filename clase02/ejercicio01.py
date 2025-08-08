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
    if not nombre or not cargo or salario <= 0 or not salario or not isinstance(salario, (int,  float)): # OJO! Si pongo or or not isinstance(salario, int) or not isinstance(salario, float), vuelvo la condicion mutuamente excluyente y nunca va a guardar el dato
        raise ValueError("Ingrese por favor cada uno de los datos de los empleados: nombre, cargo y salario.\nRecuerde que el valor del salario debe ser un numero mayor que 0 y positivo.")
    return (nombre.title(), cargo.title(), salario)

def mostrarEmpleados(empleados):
    for i, (nombre, cargo, salario) in enumerate(empleados, start = 1):
        print(f"{i}. {nombre}, {cargo}, ${salario:.2f}")
        
def main():
    empleados = []
    
    
    try:
        empleados.append(registrarEmpleado("hola", "Ingeniero de Software", 8500))
        empleados.append(registrarEmpleado("Andrew Marastuques", "Software Architect", 16400))
        empleados.append(registrarEmpleado("Maruel Andarriaga", "Analista de datos", 8000))
        empleados.append(registrarEmpleado("Yenika Uflaiga", "Gerente de ventas", 9000))
        empleados.append(registrarEmpleado("David Urrega", "Consultor Externo", 1000.89))
        empleados.append(registrarEmpleado("Manuel Ortega", "QA Specialist", 4500))
        empleados.append(registrarEmpleado("Mario Gamboa", "Front end developer", 3500))
        empleados.append(registrarEmpleado("Sofia Pua", "Marketing", 1400))
    except ValueError as e:
        print(e)
        
    mostrarEmpleados(empleados)
    
if __name__ == "__main__":
    main()