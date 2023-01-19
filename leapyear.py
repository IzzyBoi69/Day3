year = int(input("Which year you wanna check? "))
if (year%4 == 0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not Leap year")





