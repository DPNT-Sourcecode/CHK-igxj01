from collections import Counter

items = {
    'A': {'price': 50},
    'B': {'price': 30},
    'C': {'price': 20},
    'D': {'price': 15},
    'E': {'price': 40},
    'F': {'price': 10},
    'G': {'price': 20},
    'H': {'price': 10},
    'I': {'price': 35},
    'J': {'price': 60},
    'K': {'price': 80},
    'L': {'price': 90},
    'M': {'price': 15},
    'N': {'price': 40},
    'O': {'price': 10},
    'P': {'price': 50},
    'Q': {'price': 30},
    'R': {'price': 50},
    'S': {'price': 30},
    'T': {'price': 20},
    'U': {'price': 50},
    'V': {'price': 50},
    'W': {'price': 20},
    'X': {'price': 90},
    'Y': {'price': 10},
    'Z': {'price': 50}
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    counts = Counter(skus)
    remaining_skus = []

    free_b = counts['E'] // 2
    counts['B'] -= free_b if counts['B'] - free_b >= 0 else 0

    if counts['F'] >= 3:
        free_f = counts['F'] // 3
        
        counts['F'] -= free_f if counts['F'] - free_f >= 0 else 0

    for sku, count in counts.items():
        if sku == 'A':
            deal_1 = count // 5
            total += deal_1 * 200
            total += ((count - (deal_1 * 5)) // 3) * 130
            remaining_skus.extend([sku for _ in range((count - (deal_1 * 5)) % 3)])

        elif sku == 'B':
            total += (count // 2) * 45
            remaining_skus.extend([sku for _ in range(count % 2)])

        else:
            remaining_skus.extend([sku for _ in range(count)])

    for sku in remaining_skus:
        if sku in items.keys():
            total += items[sku]['price']
        else:
            return -1
        
    return total

