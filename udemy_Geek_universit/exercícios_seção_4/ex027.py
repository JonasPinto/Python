# 27. Leia uma medida de area em hectare e converta-apara m² m = h *10000

h = float(input('Digite a area em hectares: '))
m = h * 10_000
print(f'{h} hectares correspondem a {m:.2f} m²')
