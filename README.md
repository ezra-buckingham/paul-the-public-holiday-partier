# Paul the Public Holiday Partier

A tool to scrape holidays from multiple years and combine into a single CSV.

## Usage 

```
Usage: main.py [OPTIONS]

  Get holidays and combine all them into a single CSV

Options:
  -c, --country TEXT        Country code of holidays to get (Ex: US)
  -s, --start-year INTEGER  Starting year  [required]
  -e, --end-year INTEGER    Ending year  [required]
  -o, --output PATH         Path to an existing CSV file on disk
  --help                    Show this message and exit.
```