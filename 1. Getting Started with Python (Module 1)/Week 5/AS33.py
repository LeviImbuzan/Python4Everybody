Grade = input('Please Input A Grade:')
try:
    score = float(Grade)
except:
    print('Not A Valid Input')
    quit ()
try:
    if score > 1.0:
        print('Out of Grade Range')
        quit ()
except:
    quit ()
if score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
