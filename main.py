from Day import Day

day = ""
month = ""
year = ""
dayType = ""
letter = ""

days = []
letters = ["A", "A1", "A2", "B", "B1", "B2"]

with open("calendar_IN") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        
        splt = line.split(" ")
       
        # gets month and year
        if splt[0] == "Stuyvesant" and splt[1] == "High" and splt[2] == "School":
            month = splt[5]
            year = splt[-1]
        
        spltDay = splt[0].split("—")
        if len(spltDay) > 1:
            day = spltDay[0]
    
            splt.pop(0)
            half = " ".join([str(item) for item in splt])
            dayType = f"{spltDay[1]} {half}"
            
        for item in splt:
            if item in letters:
                letter = item

                day = Day(day, month, year, dayType, letter)
                print(day)
