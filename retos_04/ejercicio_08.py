# Reto 15 - ejercicio_08.py

# Tienes un sistema de semáforos que controla el tráfico de una ciudad mediante un programa que recibe información de tres sensores. 
# El primer sensor envía un valor entero de 0 a 100 que representa la cantidad de vehículos frente a él. 
# El segundo sensor envía una cadena de guiones - que representa la cantidad de peatones esperando para cruzar. 
# El tercer sensor envía un valor entero que indica si hay una emergencia 1 o no 0.

# El programa debe determinar el estado del semáforo (Verde, Amarillo, Rojo) según las siguientes reglas:

#     Si hay una emergencia, el semáforo debe estar en Verde.
#     Si no hay emergencia y la cantidad de vehículos es mayor a 70, el semáforo debe estar en Verde.
#     Si no hay emergencia y la cantidad de vehículos es menor o igual a 70, el semáforo debe estar en Amarillo.
#     Si no hay emergencia y hay más de 5 peatones esperando, el semáforo debe estar en Rojo.

# 📥 Ejemplo de entrada:

# 80, ----, False
# 20,, True
# 50, --, False
# 50 , -----, False

# 🖥️ Ejemplo de salida:

# Semáforo: Verde
# Semáforo: Verde
# Semáforo: Amarillo
# Semáforo: Rojo

# 🚫 Restricciones:

#     Utiliza el valor de Truthiness para los tipos de datos en Python.
#     No puedes usar estructuras de control (for, while)
#     No puedes definir funciones (def, lambda)
#     No puedes utilizar las funciones map, filter o reduce
#     No puedes utilizar excepciones (try, except)


# Entrada 
entrada = input().split(",")  

vehiculos = int(entrada[0].strip())
peatones = entrada[1].strip()
emergencia = entrada[2].strip() == "True"

semaforo = (
    emergencia and "Verde"
    or (len(peatones) > 5) and "Rojo"
    or (vehiculos > 70) and "Verde"
    or "Amarillo"
)
#salida
print("Semáforo:", semaforo)

