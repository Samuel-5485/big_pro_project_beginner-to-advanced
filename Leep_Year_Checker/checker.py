def is_leep_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                print("Leep Year")

            else:
                print("Not Leep Year")
        else:
            print("Leep Year")
    else:
        print("Not Leep year")
is_leep_year(2007)
