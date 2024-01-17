def computepay():
    if float(Hours) > 40:
        Regular = float(Hours)*float(Rate)
        OT = float(Hours) - 40.0
        Pay = Regular + float(OT) * float(Rate)*0.5
        return Pay
    else:
        Regular = float(Hours)
        Pay = float(Hours)*float(Rate)
        return Pay

Hours =  input('Please Enter Hours:')
Rate = input('Please Enter Rate:')

print (computepay())