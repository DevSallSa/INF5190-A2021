# kwargs = Keyword arguments.
# Ceci permet de passer un nombre arbitraire d'argument a une fonction.
def print_kwargs(**kwargs):
    for arg in kwargs.values():
        print(arg)

    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

# Utilisation
print_kwargs(toto="Titi", titi="Titi", c="Python", test="It's Kwargs !!")
