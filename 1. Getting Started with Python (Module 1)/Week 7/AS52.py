small = None
large = None
while True:
    x = input('Please Enter a Number: ')
    if x == 'done':
        break
    try:
        a = float(x)
    except:
        print('Invalid Input')
        continue
for value in [a] :
    if small is None:
        small = value
    elif value < None:
        small = value
for value in [a] :
    if large is None:
        large = value
    elif value > None:
        large = value
print('Maximum is', large)
print('Minimum is', small)
quit()
