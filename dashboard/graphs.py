import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker


def transform(covid_csv):
    read_covid_data = pd.read_csv(
        covid_csv, usecols=['Date', 'Cases', 'Recovered', 'Deaths'])
    read_covid_data['Date'] = pd.to_datetime(
        read_covid_data['Date'], format="%Y-%m-%d")
    to_dash = read_covid_data.set_index('Date')

    return to_dash


def by_month(to_dash):
    plt.style.use('seaborn-darkgrid')
    comparison = to_dash.plot.area(figsize=(10, 7))
    comparison.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    comparison.legend(bbox_to_anchor=(
        1, 1), loc='upper left', prop={'size': 13})
    comparison.tick_params(labelsize=15)
    comparison.set_xlabel('Month', fontsize=20, labelpad=15)
    comparison.set_title(
        'Cases, Recovered, Deaths by Month (US)', fontsize=20, pad=13)
    comparison = plt.savefig('/tmp/comparison.jpeg',
                             dpi=150, bbox_inches='tight')

    return comparison


def total_cases(to_dash):
    cases = to_dash.Cases.iat[-1]
    return cases


def total_recovered(to_dash):
    recovered = to_dash.Recovered.iat[-1]
    return recovered


def total_deaths(to_dash):
    deaths = to_dash.Deaths.iat[-1]
    return deaths
