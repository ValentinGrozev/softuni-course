def vowel_filter(function):
    def wrapper():
        result = function()
        vowel_list = ["a", "e", "u", "o", "y", "i"]
        final_result = [vowel for vowel in result if vowel.lower() in vowel_list]
        return final_result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
