def mutate_string(string, position, character):
    
    if not (0 <= position < len(string)):
        raise IndexError("Position out of range.")
    return string[:position] + character + string[position+1:]
