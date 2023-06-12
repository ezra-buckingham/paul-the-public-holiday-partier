import click
import requests
import pandas as pd
from pathlib import Path

BASE_URL = "https://date.nager.at/PublicHoliday"

def get_csv_of_holidays(country: str, year: int) -> Path:
    """_summary_

    Args:
        country (str): _description_
        year (int): _description_

    Returns:
        Path: _description_
    """
    
    current_script_path = Path(__file__).parent.joinpath('./tmp')
    url = f'{BASE_URL}/Country/{country}/{year}/CSV'
    response = requests.get(url)
    
    output_file = current_script_path.joinpath(f'{country}-{year}.csv')
    output_file.write_text(response.text)
    
    return output_file

    
@click.command()
@click.option('-c', '--country', type=str, default='US', help='''
    Country code of holidays to get (Ex: US)
''')
@click.option('-s', '--start-year', type=int, required=True, help='''
    Starting year
''')
@click.option('-e', '--end-year', type=int, required=True, help='''
    Ending year
''')
@click.option('-o', '--output', type=click.Path(exists=False), help='''
    Path to an existing CSV file on disk
''')
def cli(country, start_year, end_year, output):
    """Get holidays and combine all them into a single CSV"""
    
    # Set everything up first
    year_range = range(start_year, end_year, 1)
    output_file = Path(output)
    if output_file.exists(): output_file.unlink()
    output_file.touch()
    csv_files = []
    
    
    
    for year in year_range:
        csv_file = get_csv_of_holidays(country, year)
        csv_files.append(pd.read_csv(str(csv_file.absolute())))
        
    
    df_combined = pd.concat(csv_files)
    df_combined.to_csv(output_file, index=False)
    click.echo(f'Combined CSV saved to "{str(output_file.absolute())}"')


if __name__ == '__main__':
    cli()