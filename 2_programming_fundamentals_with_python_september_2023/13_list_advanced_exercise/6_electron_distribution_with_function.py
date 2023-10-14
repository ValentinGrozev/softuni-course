def shells(shell):
    maximum_electrons_per_shell = 2 * shell ** 2
    return maximum_electrons_per_shell


def electron_lefts (electrons):
    atom_shell = []
    for shell in range(1, electrons + 1):
        if electrons > shells(shell):
            atom_shell.append(shells(shell))
            electrons -= shells(shell)
        else:
            atom_shell.append(electrons)
            electrons -= electrons
        if electrons == 0:
            return atom_shell


number_of_electrons = int(input())
print(electron_lefts(number_of_electrons))

