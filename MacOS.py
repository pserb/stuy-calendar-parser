import os
from Day import Day

# parsing input from MacOS Preview app
class MacOS:
        
    save_path = "out"
    file_name = "OUT_MACOS"
    completeName = os.path.join(save_path, file_name)

    letters = ["A", "A1", "A2", "B", "B1", "B2"]

    def parse(self, in_file):
        try:
            out_file = open(self.completeName, "w")
        except:
            os.mkdir("out")
            out_file = open(self.completeName, "w")
        
        with open(in_file) as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                
                splt = line.split(" ")
            
                # gets month and year
                if splt[0] == "Stuyvesant":
                    month = splt[5]
                    year = splt[-1]
                
                spltDay = splt[0].split("—")
                if len(spltDay) > 1:
                    day = spltDay[0]
            
                    splt.pop(0)
                    half = " ".join([str(item) for item in splt])
                    dayType = f"{spltDay[1]} {half}"
                    
                for item in splt:
                    if item in self.letters:
                        letter = item

                        #day = Day(day, month, year, dayType, letter)
                        #out_file.write(f"{day.__str__()}\n")
                        out_file.write(f'"{month} {day}, {year}": ["{letter}", "{dayType}"],\n')


            out_file.close()

    def __str__(self):
        return "Successfully parsed into 'out/OUT_MACOS'"
