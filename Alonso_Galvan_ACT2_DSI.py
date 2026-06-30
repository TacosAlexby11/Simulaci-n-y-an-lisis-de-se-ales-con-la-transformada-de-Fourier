# ==========================================================
# ACTIVIDAD FORMATIVA 2
# Simulación y análisis de señales con la Transformada de Fourier
#
# Alumno:
# Materia:
# Fecha:
#
# Descripción:
# Este programa genera diferentes señales en el dominio del
# tiempo, calcula su Transformada de Fourier mediante FFT,
# representa su magnitud y fase, y verifica algunas propiedades
# importantes de la Transformada de Fourier.
# ==========================================================

# ==========================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================

import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================
# CREAR CARPETA DE RESULTADOS
# ==========================

if not os.path.exists("resultados"):
    os.makedirs("resultados")

print("=" * 60)
print("SIMULACIÓN Y ANÁLISIS DE SEÑALES")
print("Transformada de Fourier utilizando Python")
print("=" * 60)

# ==========================
# PARÁMETROS DE LA SIMULACIÓN
# ==========================

fs = 1000          # Frecuencia de muestreo (Hz)
T = 2              # Duración de la señal (segundos)
N = fs * T         # Número de muestras

# Vector de tiempo
t = np.linspace(-1, 1, N, endpoint=False)

print(f"Frecuencia de muestreo: {fs} Hz")
print(f"Número de muestras: {N}")
print()

# ==========================================================
# FUNCIÓN PARA GRAFICAR UNA SEÑAL EN EL DOMINIO DEL TIEMPO
# ==========================================================

def graficar_tiempo(t, señal, titulo, archivo):

    plt.figure(figsize=(10,4))

    plt.plot(t, señal, color="royalblue", linewidth=2)

    plt.title(titulo, fontsize=14)

    plt.xlabel("Tiempo (s)")

    plt.ylabel("Amplitud")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("resultados/" + archivo)

    plt.show()

# ==========================================================
# FUNCIÓN PARA CALCULAR LA FFT
# ==========================================================

def calcular_fft(señal):

    fft = np.fft.fft(señal)

    frecuencia = np.fft.fftfreq(len(señal), d=1/fs)

    fft = np.fft.fftshift(fft)

    frecuencia = np.fft.fftshift(frecuencia)

    return frecuencia, fft

# ==========================================================
# FUNCIÓN PARA GRAFICAR MAGNITUD
# ==========================================================

def graficar_magnitud(f, fft, titulo, archivo):

    plt.figure(figsize=(10,4))

    plt.plot(f, np.abs(fft), color="darkred")

    plt.title(titulo)

    plt.xlabel("Frecuencia (Hz)")

    plt.ylabel("Magnitud")

    plt.xlim(-50,50)

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("resultados/" + archivo)

    plt.show()

# ==========================================================
# FUNCIÓN PARA GRAFICAR FASE
# ==========================================================

def graficar_fase(f, fft, titulo, archivo):

    plt.figure(figsize=(10,4))

    plt.plot(f, np.angle(fft), color="green")

    plt.title(titulo)

    plt.xlabel("Frecuencia (Hz)")

    plt.ylabel("Fase (rad)")

    plt.xlim(-50,50)

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("resultados/" + archivo)

    plt.show()

print("Funciones cargadas correctamente.")
print()
# ==========================================================
# CREACIÓN DE LAS SEÑALES
# ==========================================================

print("=" * 60)
print("GENERACIÓN DE LAS SEÑALES")
print("=" * 60)

# ----------------------------------------------------------
# 1. Señal senoidal
# ----------------------------------------------------------

frecuencia_seno = 10      # Hz
amplitud = 1

senal_seno = amplitud * np.sin(2 * np.pi * frecuencia_seno * t)

print("✓ Señal senoidal generada.")

# ----------------------------------------------------------
# 2. Pulso rectangular
# ----------------------------------------------------------

ancho_pulso = 0.2

pulso_rectangular = np.where(np.abs(t) <= ancho_pulso, 1, 0)

print("✓ Pulso rectangular generado.")

# ----------------------------------------------------------
# 3. Función escalón
# ----------------------------------------------------------

funcion_escalon = np.where(t >= 0, 1, 0)

print("✓ Función escalón generada.")

print()

# ==========================================================
# GRAFICAR LAS SEÑALES EN EL DOMINIO DEL TIEMPO
# ==========================================================

graficar_tiempo(
    t,
    senal_seno,
    "Señal Senoidal - Dominio del Tiempo",
    "seno_tiempo.png"
)

graficar_tiempo(
    t,
    pulso_rectangular,
    "Pulso Rectangular - Dominio del Tiempo",
    "pulso_tiempo.png"
)

graficar_tiempo(
    t,
    funcion_escalon,
    "Función Escalón - Dominio del Tiempo",
    "escalon_tiempo.png"
)

# ==========================================================
# COMPARACIÓN DE LAS TRES SEÑALES
# ==========================================================

plt.figure(figsize=(12,6))

plt.plot(t, senal_seno, label="Señal senoidal", linewidth=2)

plt.plot(t, pulso_rectangular, label="Pulso rectangular", linewidth=2)

plt.plot(t, funcion_escalon, label="Función escalón", linewidth=2)

plt.title("Comparación de las señales en el dominio del tiempo")

plt.xlabel("Tiempo (s)")

plt.ylabel("Amplitud")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig("resultados/comparacion_senales.png")

plt.show()

print("=" * 60)
print("SEÑALES GRAFICADAS CORRECTAMENTE")
print("=" * 60)
print()
# ==========================================================
# TRANSFORMADA DE FOURIER DE LAS SEÑALES
# ==========================================================

print("=" * 60)
print("CÁLCULO DE LA TRANSFORMADA DE FOURIER")
print("=" * 60)

# ----------------------------------------------------------
# FFT de la señal senoidal
# ----------------------------------------------------------

f_seno, fft_seno = calcular_fft(senal_seno)

graficar_magnitud(
    f_seno,
    fft_seno,
    "Magnitud del Espectro - Señal Senoidal",
    "seno_magnitud.png"
)

graficar_fase(
    f_seno,
    fft_seno,
    "Fase del Espectro - Señal Senoidal",
    "seno_fase.png"
)

print("✓ FFT de la señal senoidal calculada.")

# ----------------------------------------------------------
# FFT del pulso rectangular
# ----------------------------------------------------------

f_pulso, fft_pulso = calcular_fft(pulso_rectangular)

graficar_magnitud(
    f_pulso,
    fft_pulso,
    "Magnitud del Espectro - Pulso Rectangular",
    "pulso_magnitud.png"
)

graficar_fase(
    f_pulso,
    fft_pulso,
    "Fase del Espectro - Pulso Rectangular",
    "pulso_fase.png"
)

print("✓ FFT del pulso rectangular calculada.")

# ----------------------------------------------------------
# FFT de la función escalón
# ----------------------------------------------------------

f_escalon, fft_escalon = calcular_fft(funcion_escalon)

graficar_magnitud(
    f_escalon,
    fft_escalon,
    "Magnitud del Espectro - Función Escalón",
    "escalon_magnitud.png"
)

graficar_fase(
    f_escalon,
    fft_escalon,
    "Fase del Espectro - Función Escalón",
    "escalon_fase.png"
)

print("✓ FFT de la función escalón calculada.")

print()

# ==========================================================
# RESUMEN DEL ANÁLISIS
# ==========================================================

print("=" * 60)
print("ANÁLISIS DE LOS RESULTADOS")
print("=" * 60)

print("""
Señal senoidal
--------------
• La energía se concentra prácticamente en una sola frecuencia.
• El espectro presenta dos picos simétricos debido a la FFT.
• La fase depende del origen temporal de la señal.

Pulso rectangular
-----------------
• Su energía se distribuye en varias frecuencias.
• Presenta un espectro ancho.
• La magnitud disminuye conforme aumenta la frecuencia.

Función escalón
---------------
• Predominan las bajas frecuencias.
• Existe una fuerte componente en frecuencia cero (DC).
• El espectro es diferente al de una señal periódica.
""")
# ==========================================================
# PROPIEDADES DE LA TRANSFORMADA DE FOURIER
# ==========================================================

print("=" * 60)
print("VERIFICACIÓN DE LAS PROPIEDADES")
print("=" * 60)

# ==========================================================
# 1. PROPIEDAD DE LINEALIDAD
# ==========================================================

print("\n1. Propiedad de linealidad")

a = 2
b = 0.5

senal_lineal = a * senal_seno + b * pulso_rectangular

fft_lineal = np.fft.fft(senal_lineal)

fft_combinada = a * np.fft.fft(senal_seno) + b * np.fft.fft(pulso_rectangular)

if np.allclose(fft_lineal, fft_combinada):
    print("✓ La propiedad de linealidad se cumple correctamente.")
else:
    print("✗ La propiedad de linealidad NO se cumple.")

plt.figure(figsize=(10,4))

plt.plot(t, senal_lineal, color="purple")

plt.title("Combinación lineal de señales")

plt.xlabel("Tiempo (s)")

plt.ylabel("Amplitud")

plt.grid(True)

plt.tight_layout()

plt.savefig("resultados/linealidad.png")

plt.show()

# ==========================================================
# 2. DESPLAZAMIENTO EN EL TIEMPO
# ==========================================================

print("\n2. Desplazamiento temporal")

desplazamiento = 250

senal_desplazada = np.roll(senal_seno, desplazamiento)

plt.figure(figsize=(10,4))

plt.plot(t, senal_seno, label="Original", linewidth=2)

plt.plot(t, senal_desplazada,
         label="Desplazada",
         linestyle="--",
         linewidth=2)

plt.title("Desplazamiento temporal")

plt.xlabel("Tiempo (s)")

plt.ylabel("Amplitud")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("resultados/desplazamiento.png")

plt.show()

print("✓ Señal desplazada correctamente.")

# ==========================================================
# COMPARACIÓN DE MAGNITUDES
# ==========================================================

f_original, fft_original = calcular_fft(senal_seno)

f_desplazada, fft_desplazada = calcular_fft(senal_desplazada)

plt.figure(figsize=(10,4))

plt.plot(f_original,
         np.abs(fft_original),
         label="Original")

plt.plot(f_desplazada,
         np.abs(fft_desplazada),
         linestyle="--",
         label="Desplazada")

plt.xlim(-40,40)

plt.title("Magnitud del espectro")

plt.xlabel("Frecuencia (Hz)")

plt.ylabel("Magnitud")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("resultados/desplazamiento_fft.png")

plt.show()

print("La magnitud prácticamente no cambia.")
print("Lo que cambia es la fase del espectro.")

# ==========================================================
# 3. ESCALAMIENTO EN FRECUENCIA
# ==========================================================

print("\n3. Escalamiento en frecuencia")

senal_20hz = np.sin(2*np.pi*20*t)

senal_40hz = np.sin(2*np.pi*40*t)

plt.figure(figsize=(10,4))

plt.plot(t,
         senal_seno,
         label="10 Hz")

plt.plot(t,
         senal_20hz,
         label="20 Hz")

plt.plot(t,
         senal_40hz,
         label="40 Hz")

plt.xlim(0,0.3)

plt.title("Comparación de frecuencias")

plt.xlabel("Tiempo (s)")

plt.ylabel("Amplitud")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("resultados/escalamiento_tiempo.png")

plt.show()

# FFT

f10, fft10 = calcular_fft(senal_seno)

f20, fft20 = calcular_fft(senal_20hz)

f40, fft40 = calcular_fft(senal_40hz)

plt.figure(figsize=(10,4))

plt.plot(f10,
         np.abs(fft10),
         label="10 Hz")

plt.plot(f20,
         np.abs(fft20),
         label="20 Hz")

plt.plot(f40,
         np.abs(fft40),
         label="40 Hz")

plt.xlim(-50,50)

plt.title("Escalamiento en frecuencia")

plt.xlabel("Frecuencia (Hz)")

plt.ylabel("Magnitud")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("resultados/escalamiento_fft.png")

plt.show()

print("✓ Se observa que el pico espectral cambia de posición.")
# ==========================================================
# COMPARACIÓN FINAL ENTRE LAS SEÑALES
# ==========================================================

print()
print("=" * 60)
print("COMPARACIÓN FINAL")
print("=" * 60)

fig, axs = plt.subplots(3, 2, figsize=(14, 10))

# ----------------------------------------------------------
# Señal senoidal
# ----------------------------------------------------------

axs[0,0].plot(t, senal_seno, color="royalblue")
axs[0,0].set_title("Senoidal - Tiempo")
axs[0,0].set_xlabel("Tiempo (s)")
axs[0,0].set_ylabel("Amplitud")
axs[0,0].grid(True)

axs[0,1].plot(f_seno, np.abs(fft_seno), color="darkred")
axs[0,1].set_title("Senoidal - Frecuencia")
axs[0,1].set_xlim(-50,50)
axs[0,1].set_xlabel("Frecuencia (Hz)")
axs[0,1].set_ylabel("Magnitud")
axs[0,1].grid(True)

# ----------------------------------------------------------
# Pulso rectangular
# ----------------------------------------------------------

axs[1,0].plot(t, pulso_rectangular, color="royalblue")
axs[1,0].set_title("Pulso rectangular - Tiempo")
axs[1,0].set_xlabel("Tiempo (s)")
axs[1,0].set_ylabel("Amplitud")
axs[1,0].grid(True)

axs[1,1].plot(f_pulso, np.abs(fft_pulso), color="darkred")
axs[1,1].set_title("Pulso rectangular - Frecuencia")
axs[1,1].set_xlim(-50,50)
axs[1,1].set_xlabel("Frecuencia (Hz)")
axs[1,1].set_ylabel("Magnitud")
axs[1,1].grid(True)

# ----------------------------------------------------------
# Función escalón
# ----------------------------------------------------------

axs[2,0].plot(t, funcion_escalon, color="royalblue")
axs[2,0].set_title("Escalón - Tiempo")
axs[2,0].set_xlabel("Tiempo (s)")
axs[2,0].set_ylabel("Amplitud")
axs[2,0].grid(True)

axs[2,1].plot(f_escalon, np.abs(fft_escalon), color="darkred")
axs[2,1].set_title("Escalón - Frecuencia")
axs[2,1].set_xlim(-50,50)
axs[2,1].set_xlabel("Frecuencia (Hz)")
axs[2,1].set_ylabel("Magnitud")
axs[2,1].grid(True)

plt.tight_layout()

plt.savefig("resultados/comparacion_general.png")

plt.show()

# ==========================================================
# ESTADÍSTICAS
# ==========================================================

print()
print("=" * 60)
print("ESTADÍSTICAS")
print("=" * 60)

print(f"Frecuencia de muestreo : {fs} Hz")
print(f"Número de muestras     : {N}")
print(f"Duración               : {T} segundos")

print()

print("Señales analizadas")

print("- Señal senoidal")
print("- Pulso rectangular")
print("- Función escalón")

print()

print("Transformadas calculadas")

print("- FFT Senoidal")
print("- FFT Pulso rectangular")
print("- FFT Escalón")

print()

print("Propiedades verificadas")

print("✓ Linealidad")

print("✓ Desplazamiento temporal")

print("✓ Escalamiento en frecuencia")

# ==========================================================
# CONCLUSIONES
# ==========================================================

print()
print("=" * 60)
print("CONCLUSIONES DEL ANÁLISIS")
print("=" * 60)

print("""

1. La Transformada de Fourier permite conocer las
   frecuencias presentes en una señal.

2. La señal senoidal concentra prácticamente toda
   su energía en una frecuencia específica.

3. El pulso rectangular contiene una gran cantidad
   de componentes frecuenciales.

4. La función escalón presenta una fuerte componente
   de baja frecuencia.

5. La propiedad de linealidad se comprobó mediante
   la combinación de señales.

6. El desplazamiento temporal modifica la fase,
   pero mantiene la magnitud del espectro.

7. Al aumentar la frecuencia de una señal senoidal,
   el pico del espectro también cambia de posición.

""")


print("Las imágenes fueron guardadas en la carpeta:")

print("resultados/")

print()

plt.close('all')
