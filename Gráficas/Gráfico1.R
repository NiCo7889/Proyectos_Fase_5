# Instalar ggplot2 si es necesario
# install.packages("ggplot2")

# Cargar ggplot2
library(ggplot2)

# Datos para el Gráfico 1
datos_grafico1 <- data.frame(
  Tamaño_del_problema = c(5, 10, 15),
  Tiempo_de_solucion = c(0.15, 0.3, 0.5)
)

# Crear el Gráfico 1
grafico1 <- ggplot(datos_grafico1, aes(x = Tamaño_del_problema, y = Tiempo_de_solucion)) +
  geom_line() +
  geom_point()

# Agregar una leyenda con letra más grande
grafico1 + guides(colour = guide_legend(title = "Leyenda", title.position = "top", label.position = "left"))

# Mostrar el Gráfico 1
print(grafico1)

# # Datos para el Gráfico 2
# datos_grafico2 <- data.frame(
#   Tamaño_del_problema = rep(c(50, 100, 150, 200, 250), 3),
#   Tiempo_de_solucion = c(1.5, 3, 5, 7, 9, 2, 4.5, 7, 10, 13.5, 4, 9, 15, 23, 32),
#   Enfoque = rep(c("Programación lineal", "Método heurístico", "Búsqueda exhaustiva"), each = 5)
# )

# # Crear el Gráfico 2
# grafico2 <- ggplot(datos_grafico2, aes(x = Tamaño_del_problema, y = Tiempo_de_solucion, color = Enfoque)) +
#   geom_line() +
#   geom_point() +
#   labs(title = "Gráfico 2: Comparación de tiempos de solución con otros enfoques",
#        x = "Tamaño del problema (número de productos y restricciones)",
#        y = "Tiempo de solución (segundos)")
#   theme(legend.text = element_text(size = 10000))

# # Agregar una leyenda con letra más grande
# grafico1 + guides(colour = guide_legend(title = "Leyenda", title.position = "top", label.position = "left"))

# # Mostrar el Gráfico 2
# print(grafico2)