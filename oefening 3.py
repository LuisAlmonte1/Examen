

getypte_code = False

count = 0

while not getypte_code and count <3:
    geheime_code = int(input("geheime code"))
    if geheime_code == 5555:
        print("je hebt de kamer verlaten!")
        getypte_code = True
    else:
        print("fout probeer het opnieuw")
        count +=1

if count == 3:
    print("je hebt verloren de kamer blijft gesloten")