def merge_the_tools(string, k):
    
    result = []
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique = ''
        for char in substring:
            if char not in unique:
                unique += char
        result.append(unique)
    return result
