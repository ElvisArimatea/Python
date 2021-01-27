entrada = input().split()
item = [] + entrada             #nesta linha não apontamos "item = entrada" pois qualquer modificação modifica as DUAS!

if int(entrada[0]) >= 1:
    while int(entrada[0]) >= 1:
        if int(entrada[1]) * float(entrada[2]) > int(item[1]) * float(item[2]):
            item[0] = entrada[0]
            item[1] = entrada[1]
            item[2] = entrada[2]

        entrada = input().split()

    print("Item mais caro")
    print("Codigo:", item[0])
    print("Quantidade:", item[1])
    print("Custo: {:.2f}".format(round((int(item[1]) * float(item[2])), 2)))

else:
    print("nao tem compras")