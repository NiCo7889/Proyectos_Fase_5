# # Cargar ggplot2
# library(ggplot2)

# # Datos para el Gráfico 3
# datos_grafico3 <- data.frame(
#   Enfoque = c("Programación lineal", "Método heurístico", "Búsqueda exhaustiva"),
#   Variables = c(150, 200, 300),
#   Restricciones = c(100, 150, 250)
# )

# # Crear el Gráfico 3
# grafico3 <- ggplot(datos_grafico3, aes(x = Enfoque, y = Variables)) +
#   geom_bar(stat = "identity", aes(fill = Enfoque), width = 0.6) +
#   labs(
#        x = "Enfoque",
#        y = "Número de variables") +
#   theme(legend.position = "none")

# # Mostrar el Gráfico 3
# print(grafico3)

# Crear el Gráfico 4
grafico4 <- ggplot(datos_grafico3, aes(x = Enfoque, y = Restricciones)) +
  geom_bar(stat = "identity", aes(fill = Enfoque), width = 0.6) +
  labs(
       x = "Enfoque",
       y = "Número de restricciones") +
  theme(legend.position = "none")

# Mostrar el Gráfico 4
print(grafico4)

# Datos para el Gráfico 5
datos_grafico5 <- data.frame(
  Enfoque = c("Programación lineal", "Método heurístico", "Búsqueda exhaustiva"),
  Tiempo = c(10, 20, 40)
)

# # Crear el Gráfico 5
# grafico5 <- ggplot(datos_grafico5, aes(x = Enfoque, y = Tiempo)) +
#   geom_bar(stat = "identity", aes(fill = Enfoque), width = 0.6) +
#   labs(title = "Gráfico 5: Tiempo requerido para comprender y aplicar diferentes enfoques de optimización",
#        x = "Enfoque",
#        y = "Tiempo (horas)") +
#   theme(legend.position = "none")

# # Mostrar el Gráfico 5
# print(grafico5)