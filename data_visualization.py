import matplotlib.pyplot as plt

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Kubikzahl
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**3 for i in x]  # Kubikzahl
z = [i**2 for i in x]  # Quadrat

# Liniendiagramm erstellen
plt.plot(x, y, label='Kubikzahl')
plt.plot(x, z, label='Quadrat')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Kubikzahl von 0 bis 9')
plt.xlabel('x')
plt.ylabel('y')

# Legende anzeigen
plt.legend()

# Diagram speichern
plt.savefig("Diagram2.png")

# Diagramm anzeigen
plt.show()