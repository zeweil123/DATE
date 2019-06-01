year = int(input("Enter the year(2018): "))
while year!=2018:
    print("Error")
    year = int(input("Enter the year(2018): "))

Month=['January','February','March','April',
       'May','June','July','August',
       'September','October','November','December']

Day=['Sun','Mon','Tue','Wed','Thr','Fri','Sat']

day1=[1,4,4,0,2,5,
      0,3,6,1,4,6,]

MonthDay=[31,28,31,30,31,30,
          31,31,30,31,30,31]

def printMain(year,cou):
    if day1[cou] != 7:
        for i in range(1, day1[cou] + 1):
            s = " "
            print("%-4s" % s, end="")
    for j in range(day1[cou] + 1, day1[cou] + MonthDay[cou] + 1):

        if j % 7 == 0:
            print("%-4d" % (j - day1[cou]))
        else:
            print("%-4d" % (j - day1[cou]), end="")
            
for i in range (0,12):
    print()
    print(Month[i])
    for j in range (0,7):
        print(Day[j],end=' ')
    print()
    printMain(year,i)
    print()