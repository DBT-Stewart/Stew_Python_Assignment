def sec_large(arr):
    
    unique_numbers = list(set(arr))
    if len(unique_numbers) < 2:
        return None  # Not enough unique elements
    unique_numbers.sort()
    return unique_numbers[-2]
