nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"\nMedia: {media:.2f}")
if media >= 7:
    print("\nAprovado! ")
else:
    print("\nReprovado! ")
