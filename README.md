# Simulaci-n-y-an-lisis-de-se-ales-con-la-transformada-de-Fourier
# Actividad Formativa 2
## Simulación y análisis de señales con la Transformada de Fourier

### Descripción

Este proyecto fue desarrollado en Python con el objetivo de analizar señales en el dominio del tiempo y en el dominio de la frecuencia utilizando la Transformada Rápida de Fourier (FFT). Se implementaron diferentes señales elementales y se analizaron sus características mediante gráficos y el estudio de sus espectros de frecuencia.

---

## Objetivos

- Generar señales básicas en el dominio del tiempo.
- Aplicar la Transformada de Fourier utilizando `np.fft.fft()`.
- Visualizar la magnitud y la fase del espectro de frecuencia.
- Analizar las propiedades de la Transformada de Fourier.
- Comparar el comportamiento de las señales en los dominios del tiempo y la frecuencia.

---

## Señales implementadas

- Señal senoidal
- Pulso rectangular
- Función escalón

---

## Propiedades analizadas

- Linealidad
- Desplazamiento en el tiempo
- Escalamiento en frecuencia

---

## Tecnologías utilizadas

- Python 3.12
- NumPy
- Matplotlib

---

## Librerías necesarias

Instalar las dependencias ejecutando el siguiente comando:

```bash
pip install numpy matplotlib scipy
```

---

## Estructura del proyecto

```
Actividad_Formativa_2/
│
├── fourier.py
├── README.md
└── resultados/
    ├── seno_tiempo.png
    ├── seno_magnitud.png
    ├── seno_fase.png
    ├── pulso_tiempo.png
    ├── pulso_magnitud.png
    ├── pulso_fase.png
    ├── escalon_tiempo.png
    ├── escalon_magnitud.png
    ├── escalon_fase.png
    ├── linealidad.png
    ├── desplazamiento.png
    ├── desplazamiento_fft.png
    ├── escalamiento_tiempo.png
    ├── escalamiento_fft.png
    └── comparacion_general.png
```

---

## Ejecución

1. Abrir el archivo `fourier.py`.
2. Ejecutar el programa.
3. Esperar a que se generen las gráficas.
4. Revisar la carpeta **resultados**, donde se almacenan automáticamente las imágenes obtenidas.

---

## Resultados obtenidos

Durante la ejecución del programa se generan gráficos que muestran:

- Representación de las señales en el dominio del tiempo.
- Magnitud del espectro de frecuencia.
- Fase del espectro.
- Comparación entre señales.
- Verificación de las propiedades de la Transformada de Fourier.

---

## Conclusiones

La Transformada de Fourier es una herramienta fundamental para analizar señales, ya que permite identificar las frecuencias que las componen. En este proyecto se observó que la señal senoidal concentra su energía en una frecuencia específica, mientras que el pulso rectangular y la función escalón presentan distribuciones espectrales diferentes. Además, se comprobó la propiedad de linealidad, el efecto del desplazamiento temporal sobre la fase y el comportamiento del escalamiento en frecuencia.

---

## Autor

**Alonso Galván**

Actividad Formativa 2  
Simulación y análisis de señales con la Transformada de Fourier

---
