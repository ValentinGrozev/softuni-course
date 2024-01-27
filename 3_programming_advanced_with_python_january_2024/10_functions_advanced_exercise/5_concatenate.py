def concatenate(*args, **kwargs):
    word = ''
    for arg in args:
        word += arg

    for key, value in kwargs.items():
        if key in word:
            word = word.replace(key, value)
    return word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))