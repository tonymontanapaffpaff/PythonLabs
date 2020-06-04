import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
countries = ['Belarus', 'Ukraine', 'Russia']
df = df[df['Country'].isin(countries)]

df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

df = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries

colors = {'Belarus': '#045275', 'Ukraine': '#089099', 'Russia': '#7CCBA2'}
plt.style.use('fivethirtyeight')
plot = covid.plot(figsize=(12, 8), color=list(colors.values()), linewidth=4, legend=False)
plot.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('Number of cases')

for country in list(colors.keys()):
    plot.text(x=covid.index[-1], y=covid[country].max(), c=colors[country], s=country, weight='bold')

plot.text(x=covid.index[1], y=int(covid.max().max()) + 45000, s="COVID-19 cases by Country", fontsize=23, weight='bold',
          alpha=.75)
plot.text(x=covid.index[1], y=int(covid.max().max()) + 15000, s="For the Belarus, Ukraine and Russia", fontsize=15,
          alpha=.5)

plt.show()
