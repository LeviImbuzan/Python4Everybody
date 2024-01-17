file= input("enter your filename:")
try:
    filename = open(file)
    readfile = filename.read()
except:
    print("File is not found")
    quit()
word = "X-DSPAM-Confidence:"
result=0
count = 0
for line in filename:
    if line.startswith(word):
        l = len(word)
        number = float(line[l+1:])
        result = result + number
        count = count + 1
        continue
try:
    avg = result/count
except ZeroDivisionError:
    avg =0
print("Average spam confidence:", avg)
