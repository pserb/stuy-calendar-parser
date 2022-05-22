from MacOS import MacOS

class CalendarIO:

    FileTypes = {
        "MACOS": MacOS(),
    }

    # determines input type
    def file_type(self, in_file):
        with open(in_file) as f:
            line = f.readline()

            if line.strip().split(" ")[0] == "Stuyvesant":
                return self.FileTypes.get("MACOS")
            elif line.strip.split(" ")[0] == "Ver.5.0":
                print("oops")
            else:
                print("Format not supported")
            

    def parse(self, in_file):
        toParse = self.file_type(in_file)
        toParse.parse(in_file)
        print(toParse)
