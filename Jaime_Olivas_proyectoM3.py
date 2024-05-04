import numpy as np
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_niveles):
    # Inicializar una lista de contadores para cada contenedor
    contadores = [0] * (num_niveles + 1)  
    
    # Iterar sobre cada canica
    for _ in range(num_canicas):
        # Posición inicial en la parte superior de la máquina
        pos = num_niveles // 2  

        # Simular la caída de la canica a través de los niveles de la máquina
        for _ in range(num_niveles):
            # Decidir aleatoriamente si la canica se mueve hacia la izquierda o hacia la derecha
            if np.random.randint(2):  
                pos += 1
            else:
                pos -= 1
            
            # Asegurar que la posición esté dentro de los límites de los contenedores
            pos = max(0, min(pos, num_niveles))  

        # Incrementar el contador del contenedor final donde termina la canica
        if 0 <= pos <= num_niveles:  
            contadores[pos] += 1  
            
    return contadores

def graficar_histograma(contadores):
    # Crear un histograma con los contadores de los contenedores
    plt.bar(range(len(contadores)), contadores)
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de canicas')
    plt.title('Histograma de distribución de canicas en la máquina de Galton')
    plt.show()

def main():
    # Parámetros de la simulación
    num_canicas = 3000
    num_niveles = 12
    
    # Simular la máquina de Galton y obtener los resultados
    resultados = simular_maquina_galton(num_canicas, num_niveles)
    
    # Graficar el histograma de distribución de las canicas en los contenedores
    graficar_histograma(resultados)

if __name__ == "__main__":
    main()