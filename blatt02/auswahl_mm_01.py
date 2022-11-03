from random import randrange


# def auswahl(nichterlaubt, bereich):
#     x = randrange(bereich)
#     for x in range(bereich):
#         if x not in nichterlaubt:
#             return x


tead = [0]

# print(auswahl(tead, 3))


def auswahl02(nichterlaubt=set(), bereich=0):
    aw = randrange(bereich)
    while aw in nichterlaubt:
        aw = randrange(bereich)
    return aw

print(auswahl02(tead, 3))