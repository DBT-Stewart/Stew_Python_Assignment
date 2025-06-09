from itertools import combinations
def probability_of_a(letters, k):
    n = len(letters)
    all_combos = list(combinations(range(n), k))

    favorable = sum(1 for combo in all_combos if 'a' in [letters[i] for i in combo])

    probability = favorable / len(all_combos) if all_combos else 0.0
    return round(probability, 3)
                 
