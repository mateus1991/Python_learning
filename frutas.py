def calc_preco (morango, maca):

    if morango > 5:
        preco_mo = morango * 2.2
    else:
        preco_mo = morango * 2.5

    if maca > 5:
        preco_ma = maca * 1.5
    else:
        preco_ma = maca * 1.8

    preco_total = preco_mo + preco_ma

    if (morango+maca > 8) or (preco_total > 25):
        preco_total *= 0.9

    return preco_total



morango = float(input("Quantos quilos de morango:"))
maca = float(input("Quantos quilos de maça:"))

print ("O total a pagar será de R$"+str(calc_preco(morango,maca)))