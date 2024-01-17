Hours =  input('Please Enter Hours:')
Rate = input('Please Enter Rate:')
if float(Hours) > 40:
    Regular = float(Hours)*float(Rate)
    OT = float(Hours) - 40.0
    Pay = Regular + float(OT) * float(Rate)*0.5
    print('Overtime:' , OT )
else:
    Regular = float(Hours)
    Pay = float(Hours)*float(Rate)
    print('Regular:', Regular)
print('Your Pay Is:', Pay)
