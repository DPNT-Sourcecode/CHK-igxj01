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


def apply_nfx_deals(counts):
    remaining_skus = []
    total = 0

    for sku, count in counts.items():
        print('sku: ', sku)

        if sku in items.keys() and 'deals' in items[sku]:
            nfx_deals = [x for x in items[sku]['deals'] if x['type'] == 'nfx']
            nfx_deals = sorted(nfx_deals, key=lambda x: x['n'], reverse=True)

            if len(nfx_deals) == 0:
                remaining_skus.extend([sku for _ in range(count)])
                continue

            current_count = count

            for i, nfx_deal in enumerate(nfx_deals):
                deal = current_count // nfx_deal['n']
                total += deal * nfx_deal['x']

                current_count = (count - (deal * nfx_deal['n']))
                
                if i == len(nfx_deals) - 1:
                    print(current_count, nfx_deal['n'], current_count % nfx_deal['n'])
                    remaining_skus.extend([sku for _ in range(current_count % nfx_deal['n'])])                
        else:
            remaining_skus.extend([sku for _ in range(count)])
    
    return remaining_skus, total

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in skus:
        if sku not in items.keys():
            return -1

    counts = apply_bng1f_deal(Counter(skus))
    print(counts)

    remaining_skus, total = apply_nfx_deals(counts)
    print(skus, remaining_skus)

    for sku in remaining_skus:
        if sku in items.keys():
            total += items[sku]['price']
        else:
            return -1
        
    return total





