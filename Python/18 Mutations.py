def mutate_string(string, position, character):
    stringlist = list(string)
    stringlist[position] = character
    string = ''.join(stringlist)
    return string
