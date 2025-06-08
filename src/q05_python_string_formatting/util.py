def print_formatted(number):
    
    size = len("{0:b}".format(number))
    formatted_lines = []
    for i in range(1, number + 1):
        formatted_lines.append(
            "{0:{s}d} {0:{s}o} {0:{s}X} {0:{s}b}".format(i, s=size)
        )
    return formatted_lines
