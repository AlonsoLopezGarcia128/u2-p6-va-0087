# Alonso Lopez García NC = 0087 | Fecha 27/10/2026
import matplotlib.pyplot as plt
import numpy as np
cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]
plt.plot(cant_productos,precio)
plt.show()

# Personalizar grafica
plt.plot(cant_productos,precio, color="green", marker="d", linestyle ="dashed", linewidth =2, markersize=12)
plt.title("Ventas de Walmart 0087")
plt.xlabel("Cantidad de productos")
plt.ylabel("Precio")
plt.show()


print("Alonso Lopez García NC = 0087 | Fecha 27/10/2026")