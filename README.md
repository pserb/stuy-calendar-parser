# stuy-calendar-parser
Python script to parse Stuyvesant's pdf calendar

## Format
`month day, year - [letter] testing`\
The 2021-2022 formatted calendar is available in `calendar_OUT`

## Usage
* `python3 main.py > calendar_OUT`
* `cat calendar_OUT` to view contents

### For Future Years
#### (Assuming the format remains exactly the same)
* Navigate to [the calendar](https://stuy.entest.org/2021-2022%20School%20Term%20Calendar%20v%203-9-2022.pdf) and downlaod it
	* It can also be found on [stuy's website](https://stuy.enschool.org/) under Students 
* Open the file using Preview on Mac
* Press `⌘A` to select all the text and `⌘C` to copy it
* Using `⌘V` paste it into `calendar_IN`
* `python3 main.py > calendar_OUT`

### Note
If using a future year's calendar, the code is written for the format of the copy/paste that Preview on Mac provides. It is possible that I rewrite the code for the format that the google chrome pdf viewer provides, but as of now I haven't. The google chrome version creates many more newlines. For example "Stuyvesant High School Fall Calendar September 2021," used to determine the month and year of the date, using Preview is one line, but using chrome turns into two lines 
