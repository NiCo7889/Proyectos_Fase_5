# Cargar ggplot2
library(ggplot2)

# Datos para el Gráfico 6
datos_grafico6 <- data.frame(
  Enfoque = c("Programación lineal", "Método heurístico", "Búsqueda exhaustiva"),
  Ajustes_necesarios = c(5, 10, 15)
)

# Crear el Gráfico 6
grafico6 <- ggplot(datos_grafico6, aes(x = Enfoque, y = Ajustes_necesarios)) +
  geom_bar(stat = "identity", aes(fill = Enfoque), width = 0.6) +
  labs(title = "Gráfico 6: Comparación de la adaptabilidad de diferentes enfoques de optimización",
       x = "Enfoque",
       y = "Ajustes necesarios") +
  theme(legend.position = "none")

# Mostrar el Gráfico 6
print(grafico6)

# Datos para el Gráfico 7
datos_grafico7 <- data.frame(
  Enfoque = c("Programación lineal", "Método heurístico", "Búsqueda exhaustiva"),
  Tiempo = c(2, 6, 12)
)

# Crear el Gráfico 7
grafico7 <- ggplot(datos_grafico7, aes(x = Enfoque, y = Tiempo)) +
  geom_bar(stat = "identity", aes(fill = Enfoque), width = 0.6) +
  labs(title = "Gráfico 7: Tiempo requerido para adaptar diferentes enfoques de optimización a nuevos escenarios",
       x = "Enfoque",
       y = "Tiempo (horas)") +
  theme(legend.position = "none")

# Mostrar el Gráfico 7
print(grafico7)