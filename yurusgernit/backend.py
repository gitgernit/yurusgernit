a = input().split()
answer= 0
if(len(a)== 3):
    if(a[1]=="+"):
        answer = int(a[0])+int(a[2])
    elif(a[1]=="-"):
        answer = int(a[0])-int(a[2])
    elif (a[1] == "*"):
        answer = int(a[0])*int(a[2])
    elif (a[1] == "/"):
        answer = int(a[0])/int(a[2])
elif(len(a)== 1):
    if("+" in a[0]):
        firstnumber= a[0][:a[0].index("+")]
        sucondnumber= a[0][a[0].index("+")+1:]
        answer= int(firstnumber) + int(sucondnumber)
    elif ("-" in a[0]):
        firstnumber = a[0][:a[0].index("-")]
        sucondnumber = a[0][a[0].index("-") + 1:]
        answer = int(firstnumber) - int(sucondnumber)
    elif ("*" in a[0]):
        firstnumber = a[0][:a[0].index("*")]
        sucondnumber = a[0][a[0].index("*") + 1:]
        answer = int(firstnumber) * int(sucondnumber)
    elif ("/" in a[0]):
        firstnumber = a[0][:a[0].index("/")]
        sucondnumber = a[0][a[0].index("/") + 1:]
        answer = int(firstnumber) / int(sucondnumber)
print(answer)