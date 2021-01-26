MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}


def restaurant():
    total = 0

    while True:
        order = input('Order: ')
        if not order:
            break
        if order not in MENU:
            print(f'We are fresh out of {order} today')
            continue
        total += MENU[order]
        print(f'{order} costs {MENU[order]}, total is {total}')

    print(f'Your total is {total}')
