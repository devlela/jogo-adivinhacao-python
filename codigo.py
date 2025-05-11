import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Adivinhe o número entre 1 e 100")
while True:
    chute = int(input("Seu chute: "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Acertou em {tentativas} tentativas!")
        break
    elif chute < numero_secreto:
        print("Tente um número maior")
    else:
        print("Tente um número menor")
