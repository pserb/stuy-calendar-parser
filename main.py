from Day import Day

day = ""
month = ""
year = ""
dayType = ""
letter = ""

days = []

with open("alt_IN") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        
        splt = line.split(" ")
       
        # Stuyvesant High School Fall Calendar September 2021
        # ----- identifier ----- |-- skip --|  month     year
        
        # gets month and year
        if splt[0] == "Stuyvesant" and splt[1] == "High" and splt[2] == "School":
            month = splt[5]
            year = splt[-1]
        
        spltDay = splt[0].split("—")
        # print()
        # print(splt)
        # print(spltDay)
        if len(spltDay) > 1:
            day = spltDay[0]
    
            splt.pop(0)
            half = " ".join([str(item) for item in splt])
            dayType = f"{spltDay[1]} {half}"
            
            # next line is letter

        # if len(splt) == 1:
        for item in splt:
            if item == "A" or item == "A1" or item == "A2" or item == "B" or item == "B1" or item == "B2":
                letter = item

                day = Day(day, month, year, dayType, letter)
                print(day)
                # print()

# Day: (day, month, year, dayType, letter)
d1 = Day("30", "April", "2022", "Weekend", "B2")
#print(d1)
