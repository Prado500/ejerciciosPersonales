def registrarEmpleado (nombre, cargo, salario):
    if not nombre or not cargo or not salario or salario <=0 :
        raise ValueError ("Datos no validos. Asegúrese que el nombre, el cargo y el salario fueron digitados.\nAsegúrese también que el valor del salario es un numero positivo diferente de 0. ")
    return(nombre.title(), cargo.title(), float(salario))

# def mostrarEmpleados(empleados):
#     for i, emp in enumerate(empleados, start = 1):
#         print(f"{i}. {nombre} - {cargo} - ${salario:.2f}")
        

def mostrarEmpleados(empleados):
    for i, (nombre, cargo, salario) in enumerate(empleados, start = 1):
        print(f"{i}. {nombre}, {cargo}, ${salario:.2f}")
        
def main():
    
    empleados = []
    
    try:
        empleados.append(registrarEmpleado("Jose barustes", "Ingeniero de Software", 8500))
        empleados.append(registrarEmpleado("Andrew Marastuques", "Software Architect", 16400))
        empleados.append(registrarEmpleado("Maruel Andarriaga", "Analista de datos", 8000))
        empleados.append(registrarEmpleado("Yenika Uflaiga", "Gerente de ventas", 9000))
        
    except ValueError as e:
        print(e)
        
    mostrarEmpleados(empleados)
    
if __name__ == "__main__":
    main()