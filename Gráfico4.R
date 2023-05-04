# Cargar ggplot2
library(ggplot2)

# Datos para el Gráfico 8
datos_grafico8 <- data.frame(
  Enfoque = c("Programación lineal", "Método heurístico", "Búsqueda exhaustiva"),
  Tiempo = c(3, 12, 48)
)

# Crear el Gráfico 8
grafico8 <- ggplot(datos_grafico8, aes(x = Enfoque, y = Tiempo)) +
  geom_bar(stat = "identity", aes(fill = Enfoque), width = 0.6) +
  labs(title = "Gráfico 8: Comparación del tiempo de resolución de diferentes enfoques de optimización para problemas de gran escala",
       x = "Enfoque",
       y = "Tiempo (horas)") +
  theme(legend.position = "none")

# Mostrar el Gráfico 8
print(grafico8)

# Datos para el Gráfico 9
datos_grafico9 <- data.frame(
  Enfoque = c("Programación lineal", "Método heurístico", "Búsqueda exhaustiva"),
  Precision = c(95, 80, 60)
)

# Crear el Gráfico 9
grafico9 <- ggplot(datos_grafico9, aes(x = Enfoque, y = Precision)) +
  geom_bar(stat = "identity", aes(fill = Enfoque), width = 0.6) +
  labs(title = "Gráfico 9: Comparación de la precisión de diferentes enfoques de optimización para problemas de gran escala",
       x = "Enfoque",
       y = "Precisión (%)") +
  theme(legend.position = "none")

# Mostrar el Gráfico 9
print(grafico9)