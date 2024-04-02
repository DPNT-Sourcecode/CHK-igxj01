from collections import Counter

items = {
    'A': {
        'price': 50,
        'deals': [
            {'type': 'nfx',
             'n': 3,
             'x': 130},
            {'type': 'nfx',
             'n': 5,
             'x': 200},             
        ]
    },
    'B': {
        'price': 30,
        'deals': [
            {'type': 'nfx',
             'n': 2,
             'x': 45},
          ]
    },
    'C': {'price': 20},
    'D': {'price': 15},
    'E': {
        'price': 40,
        'deals': [
            {'type': 'bng1f',
             'n': 2,
             'f': 'B'},
        ]
    },
    'F': {
        'price': 10,
        'deals': [
            {'type': 'bng1f',
             'n': 2,
             'f': 'F'},
        ]
    },
    'G': {'price': 20},
    'H': {
        'price': 10,
        'deals': [
            {'type': 'nfx',
             'n': 5,
             'x': 45},
            {'type': 'nfx',
             'n': 10,
             'x': 80},
        ]
    
    },
    'I': {'price': 35},
    'J': {'price': 60},
    'K': {
        'price': 80,
        'deals': [
            {'type': 'nfx',
             'n': 2,
             'x': 150}
        ]
    },
    'L': {'price': 90},
    'M': {'price': 15},
    'N': {
        'price': 40,
        'deals': [
            {'type': 'bng1f',
             'n': 3,
             'f': 'M'}
        ]
    },
    'O': {'price': 10},
    'P': {
        'price': 50,
        'deals': [
            {'type': 'nfx',
             'n': 5,
             'x': 200}
        ]
    },
    'Q': {
        'price': 30,
        'deals': [
            {'type': 'nfx',
             'n': 3,
             'x': 80}
        ]
    },
    'R': {
        'price': 50,
        'deals': [
            {'type': 'bng1f',
             'n': 3,
             'f': 'Q'}
        ]
    },
    'S': {'price': 30},
    'T': {'price': 20},
    'U': {
        'price': 50,
        'deals': [
            {'type': 'bng1f',
             'n': 3,
             'f': 'U'}
        ]
    },
    'V': {
        'price': 50,
        'deals': [
            {'type': 'nfx',
             'n': 2,
             'x': 90},
            {'type': 'nfx',
             'n': 3,
             'x': 130}
        ]
    },
    'W': {'price': 20},
    'X': {'price': 90},
    'Y': {'price': 10},
    'Z': {'price': 50}
}


def apply_bng1f_deal(counts):
    res = dict(counts)

    for sku in counts.keys():
        if sku in items.keys() and 'deals' in items[sku]:
            bng1f_deals = [x for x in items[sku]['deals'] if x['type'] == 'bng1f']

            if len(bng1f_deals) == 0:
                continue

            bng1f_deal = bng1f_deals[0] # NB: assumes only one bng1f deal per item

            if bng1f_deal['f'] == sku:
                if counts[sku] >= bng1f_deal['n'] + 1:
                    free_count = counts[sku] // bng1f_deal['n'] + 1
                    res[sku] -= free_count if counts[sku] - free_count >= 0 else 0

            else:
                free_count = counts[sku] // bng1f_deal['n']
                res[bng1f_deal['f']] -= free_count if counts[bng1f_deal['f']] - free_count >= 0 else 0
    
    return res


def apply_xfn_deals(counts):
    remaining_skus = []
    total = 0

    for sku, count in counts.items():
        if sku in items.keys() and 'deals' in items[sku]:
            xfn_deals = [x for x in items[sku]['deals'] if x['type'] == 'nfx']

            if len(xfn_deals) == 0:
                remaining_skus.extend([sku for _ in range(count)])
                continue

            current_count = count

            print(sku)

            for i, xfn_deal in enumerate(xfn_deals):
                deal = current_count // xfn_deal['n']
                total += deal * xfn_deal['x']

                print(deal, total, current_count)

                current_count = (count - (deal * xfn_deal['n']))
                
                if i == len(xfn_deals) - 1:
                    remaining_skus.extend([sku for _ in range(current_count % xfn_deal['n'])])
                
        else:
            remaining_skus.extend([sku for _ in range(count)])
    
    print(remaining_skus, total)
    
    return remaining_skus, total

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in skus:
        if sku not in items.keys():
            return -1

    total = 0
    counts = Counter(skus)
    remaining_skus = []
    
    counts = apply_bng1f_deal(counts)

    # for sku, count in counts.items():
    #     if sku == 'A':
    #         deal_1 = count // 5
    #         total += deal_1 * 200
    #         total += ((count - (deal_1 * 5)) // 3) * 130
    #         remaining_skus.extend([sku for _ in range((count - (deal_1 * 5)) % 3)])

    #     elif sku == 'B':
    #         total += (count // 2) * 45
    #         remaining_skus.extend([sku for _ in range(count % 2)])

    #     else:
    #         remaining_skus.extend([sku for _ in range(count)])

    remaining_skus, total = apply_xfn_deals(counts)

    for sku in remaining_skus:
        if sku in items.keys():
            total += items[sku]['price']
        else:
            return -1
        
    return total




