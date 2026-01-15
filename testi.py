# Kirjoita ratkaisu tähän
saaennuste = print("Kerro huominen sääennuste: ")
lampotila = int(input("Lämpötila: "))
sade = input("Sataako (Kyllä/ei: ")


if lampotila <= 5:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if 5 < lampotila <= 10:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")
    print("Pue päälle takki")

if 10 < lampotila <= 20:
    print("Pue housut ja t-paita")
    print("Ota myös pitkähihainen paita")

if lampotila > 20:
    print("Pue housut ja t-paita")

if sade == "Kyllä":
    print("Muista sateenvarjo!")