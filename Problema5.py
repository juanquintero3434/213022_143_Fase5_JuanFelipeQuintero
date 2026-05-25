#Datos del estudiante:
#Nombre: Juan Felipe Quintero
#Grupo: 213022_143
#Código fuente: Autoría propia

#Matriz de horas trabajadas

HORAS_TRABAJADAS = [
    ["Ana",8,8,7,9,10],
    ["Luis",6,8,9,8,7],
    ["María",9,9,8,10,9],
    ["Pedro",8,7,8,9,8]
]

#Titulo del reporte
print("↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔")
print(f"        REPORTE DE HORAS TRABAJADAS        ")
print("↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔↔")
#Función para calcular el total de horas trabajadas por cada empleado

def calcular_horas_y_clasificacion(recurso):
    
    nombre = recurso [0]
    
    total_horas = sum(recurso[1:])
    
    if total_horas > 40:
        clasificacion = "Sobretiempo"
        
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion

#Recorrido de la matriz para mostrar resultados

for recurso in HORAS_TRABAJADAS:
    nombre, total_horas, clasificacion = calcular_horas_y_clasificacion(recurso)
    
    print("---------------------------------------------")
    print(f"Nombre: {nombre}")
    print(f"Total horas semanales: {total_horas}") 
    print(f"Clasificación de jornada: {clasificacion}")
    print()