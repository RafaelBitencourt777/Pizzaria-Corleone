print("=== Pizzaria Python ===")

sabores = ["Calabresa", "Mussarela", "Frango com Catupiry", "Portuguesa", "Quatro Queijos", "Marguerita"]
print("\nSabores disponíveis:")
for i, sabor in enumerate(sabores, 1):
    print(f"{i} - {sabor}")

nome = input("\nDigite seu nome: ")
endereco = input("Digite seu endereço: ")

pedidos = []
while True:
    pedido = input("\nDigite o número do sabor desejado (ou 'sair' para finalizar): ")
    if pedido.lower() == "sair":
        break
    if pedido.isdigit() and 1 <= int(pedido) <= len(sabores):
        pedidos.append(sabores[int(pedido) - 1])
        print("Pizza adicionada!")
    else:
        print("Opção inválida.")

print("\n=== Pedido Final ===")
print(f"Cliente: {nome}")
print(f"Endereço: {endereco}")
print("Pizzas pedidas:")
for p in pedidos:
    print("-", p)

print("\nObrigado por comprar na Pizzaria Python!")