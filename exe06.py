hora = input("Digite a hora atual: ")
hora_int = int(hora)
if hora_int >= 0 and hora_int <= 11:
    print("Bom dia!")
elif hora_int >= 12 and hora_int <= 17:
    print("Boa tarde!")
else:
    print("Boa noite!")