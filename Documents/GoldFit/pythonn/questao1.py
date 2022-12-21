vendedores = int(input("Quantidade de vendedores: "))

for i in range(1, vendedores, 1):
    print("Vendedor " + i)
    veiculos_faturados = int(
        input("  " + "Quantidade de veiculos faturados: "))
    vendas = float(input("  " + "Valor em vendas (R$): "))
