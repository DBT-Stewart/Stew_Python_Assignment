def can_stack(cubes):
    left = 0
    right = len(cubes) - 1
    last = float('inf')
    
    while left <= right:
        if cubes[left] >= cubes[right]:
            pick = cubes[left]
            left += 1
        else:
            pick = cubes[right]
            right -= 1
        
        if pick > last:
            return "No"
        last = pick
    
    return "Yes"
