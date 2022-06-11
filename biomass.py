num = float(input("Number of fish (N): "))
a = float(input("A Value: "))
length = float(input("Average length(cm): "))
b = float(input("B Value: "))

biomass = "{:.2f}".format(num * a * length ** b)

print("Biomass(kg): ", biomass)
