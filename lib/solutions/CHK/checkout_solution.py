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
        
        if sku == 'B':
            total += (count // 2) * 45
            remaining_skus.extend([sku for _ in range(count % 2)])

    print(total, remaining_skus)
    exit()



    for sku in skus:
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

if __name__ == "__main__":
    checkout("AABBAABCD")

