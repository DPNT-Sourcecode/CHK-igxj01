from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0

    counts = Counter(skus)
    remaining_skus = []

    for sku, count in counts.items():
        if sku == 'A':
            total += (count // 3) * 130
            remaining_skus.extend([sku for _ in range(count % 3)])
        
        elif sku == 'B':
            total += (count // 2) * 45
            remaining_skus.extend([sku for _ in range(count % 2)])

        else:
            remaining_skus.extend([sku for _ in range(count)])

    for sku in remaining_skus:
        if sku == 'A':
            total += 50
        elif sku == 'B':
            total += 30
        elif sku == 'C':
            total += 20
        elif sku == 'D':
            total += 15
        else:
            return -1
        
    return total


