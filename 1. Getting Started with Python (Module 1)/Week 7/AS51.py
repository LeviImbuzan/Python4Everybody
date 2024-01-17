num =0
total = 0
while True:
    x = input('Please Enter a Number: ')
    if x == 'done':
        break
    try:
        y = float(x)
    except:
        print('Invalid Input')
        continue
    #print (y)
    num = num +1
    total = total + num

#print('ALL DONE')
print('Total:',total, 'Count:',num,'Average:',total/num)
quit()
