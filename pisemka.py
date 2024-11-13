# ZADÁNÍ ÚKOLU:

# Na vstupu jsou prirozena cisla ukoncena -1, vypočtěte jejich aritmetický průměr 
# Kolik čísel je menších než AP a kolik čísel je větších než AP



# Prázdný seznam, kde se budou ukládat vložené čísla
cisla = []

# Vytiskne úlohu, kterou bude muset vykonat uživatel, jinak by program nefungoval
print("Zadejte přirozená čísla. V době, kdy zadáte -1 se vložení čísel ukončí a vypočte se aritmetický průměr:")

# While nám zjistí, zda uživatel zadává přirozená čísla. Pokud zadává, program stále dovoluje zadávat čísla. Pokud ne a zadal -1, program vyhodnotí aritmetický průměr.
while True:
    vstup = int(input())
    if vstup == -1:
        break
    cisla.append(vstup)

# Výpočet aritmetického průměru:
if len(cisla) > 0:
    prumer = sum(cisla) / len(cisla)
    mensi_nez_prumer = len([x for x in cisla if x < prumer])
    vetsi_nez_prumer = len([x for x in cisla if x > prumer])
    
    print(f"Aritmetický průměr zadaných čísel je: {prumer}")
    print(f"Počet čísel menších než průměr: {mensi_nez_prumer}")
    print(f"Počet čísel větších než průměr: {vetsi_nez_prumer}")
else:
    print("Nebyla zadána žádná čísla.")
print("Konec programu")



# Vypracoval Radek Havelka
# IT1 13. 11. 2024