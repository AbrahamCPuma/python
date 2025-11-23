import numpy as np
import matplotlib.pyplot as plt

def logistic_model(t, capacidad_maxima, velocidad, inicio_parametro):
    return capacidad_maxima / (1 + inicio_parametro * np.exp(-velocidad * t))

# --- TUS PERILLAS ---
K = 80000   # Meta
r = 0.4     # Velocidad (La subiste a 0.8, ¡modo turbo!)
A = 99      # Inicio

# --- CÁLCULO AUTOMÁTICO DEL PUNTO DE INFLEXIÓN ---
# Matemáticamente, la inflexión ocurre cuando el término exponencial vale 1/A
# t = ln(A) / r
tiempo_inflexion = np.log(A) / r
valor_inflexion = K / 2

print(f"La desaceleración empieza exactamente en el mes: {tiempo_inflexion:.2f}")

# --- GRAFICACIÓN ---
t = np.linspace(0, 24, 100)
ingresos = logistic_model(t, K, r, A)

plt.figure(figsize=(10, 6))
plt.plot(t, ingresos, color='green', linewidth=3, label='Trayectoria')

# 1. Línea de Meta (Roja)
plt.axhline(y=K, color='red', linestyle='--', label=f'Meta: ${K}')

# 2. MARCADOR DINÁMICO DE DESACELERACIÓN
# Dibujamos un punto grande justo donde ocurre el cambio
plt.scatter([tiempo_inflexion], [valor_inflexion], color='orange', s=100, zorder=5, label='Inicio Desaceleración')

# Dibujamos líneas punteadas hacia los ejes para ver el tiempo y el dinero
plt.vlines(x=tiempo_inflexion, ymin=0, ymax=valor_inflexion, colors='orange', linestyles=':')
plt.hlines(y=valor_inflexion, xmin=0, xmax=tiempo_inflexion, colors='orange', linestyles=':')

plt.title(f'Proyección Dinámica (r={r})')
plt.xlabel('Meses')
plt.ylabel('Ingresos (USD)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()