number_of_electrons = int(input())

atom_shell = []

for shells in range(1, number_of_electrons + 1):
    maximum_electrons_per_shell = 2 * shells ** 2
    if number_of_electrons >= maximum_electrons_per_shell:
        atom_shell.append(maximum_electrons_per_shell)
        number_of_electrons -= maximum_electrons_per_shell
    else:
        atom_shell.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
    if number_of_electrons == 0:
        break
print(atom_shell)

