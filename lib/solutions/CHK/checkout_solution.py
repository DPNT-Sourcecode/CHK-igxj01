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
        'price': 70,
        'deals': [
            {'type': 'nfx',
             'n': 2,
             'x': 120}
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
    'S': {'price': 20},
    'T': {'price': 20},
    'U': {
        'price': 40,
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
    'X': {'price': 17},
    'Y': {'price': 20},
    'Z': {'price': 21}
}

group_deals = [
    {'items': ['S', 'T', 'X', 'Y', 'Z'],
     'n': 3,
     'x': 45}
]


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
                    free_count = counts[sku] // (bng1f_deal['n'] + 1)
                    res[sku] -= free_count if counts[sku] - free_count >= 0 else 0
            else:
                free_count = counts[sku] // bng1f_deal['n']
                if bng1f_deal['f'] in res:
                    res[bng1f_deal['f']] -= free_count if counts[bng1f_deal['f']] - free_count >= 0 else 0
    
    return res


def apply_nfx_deals(counts):
    remaining_skus = []
    total = 0

    for sku, count in counts.items():
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
                
                if i == len(nfx_deals) - 1:
                    remaining_skus.extend([sku for _ in range(current_count % nfx_deal['n'])])

                current_count = (count - (deal * nfx_deal['n']))
        else:
            remaining_skus.extend([sku for _ in range(count)])
    
    return remaining_skus, total


def apply_group_deals(counts, remaining_skus, total):
    temp = dict(counts)

    for deal in group_deals:
        while True:
            counts = [{'sku': k, 'count': v, 'price': items[k]['price']} for k, v in temp.items() if k in deal['items'] and v > 0]
            counts_sorted = sorted(counts, key=lambda x: x['price'], reverse=True)

            to_group = []
            for x in counts_sorted:
                for _ in range(x['count']):
                    to_group.append(x['sku'])

            first_group = to_group[:3]

            if len(first_group) == deal['n']:
                total += 45

                for i in range(deal['n']):
                    sku = first_group[i]
                    temp[sku] -= 1
                    del remaining_skus[remaining_skus.index(sku)]
            else:
                break

    return remaining_skus, total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in skus:
        if sku not in items.keys():
            return -1

    counts = apply_bng1f_deal(Counter(skus))
    remaining_skus, total = apply_nfx_deals(counts)
    remaining_skus, total = apply_group_deals(counts, remaining_skus, total)

    for sku in remaining_skus:
        if sku in items.keys():
            total += items[sku]['price']
        else:
            return -1
        
    return total



