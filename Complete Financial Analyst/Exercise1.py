import pandas as pd

df = pd.read_excel(r'Exercise+1.xlsx', sheet_name='Raw Data (Source = IMF)')

# 1. Copy the tab at the bottom of Excel called "Raw Data (Source = IMF)"
# and create a new tab in this Excel file called "Economic Analysis"
economic_analysis = df.copy()

# 2. Hide columns A, B and C.
economic_analysis = economic_analysis.iloc[:, 3:]

# Questions 3-6 unnecessary in pandas
# 7. Filter the Units column by "U.S. dollars"
economic_analysis = economic_analysis.loc[(economic_analysis['Units'] == 'U.S. dollars'), :]

# 8. What was the 2012 Gross Domestic Product (GDP) of Japan in US Dollars?
q8 = economic_analysis.loc[(economic_analysis['Country'] == 'Japan') &
                           (economic_analysis['Subject Descriptor']
                            == 'Gross domestic product, current prices'),
                           ['Scale', 2012]]

# 9. On the tab you created called "Economic Analysis", what was the 2007 Gross Domestic Product (GDP)
# of Germany per capita (meaning per person)?
q9 = economic_analysis.loc[(economic_analysis['Country'] == 'Germany') &
                           (economic_analysis['Subject Descriptor']
                            == 'Gross domestic product per capita, current prices'),
                           ['Scale', 2007]]

# 10. What is the IMF forecasting for the top 20 countries in the world for GDP per capita in U.S. dollars for 2022?
# Please show all 20 countries sorted by highest to lowest.
q10 = economic_analysis.loc[(economic_analysis['Subject Descriptor']
                            == 'Gross domestic product per capita, current prices'),
                            ['Country', 'Scale', 2022]].sort_values(by=[2022], ascending=False)[:20]

# 11. Make a vertical bar chart of the answer of the previous question.
# q11 = q10.plot.bar(x='Country', y=2022, title='Top 20 GDP per capita projected 2022')

# 12. change the look
q12 = q10.plot.bar(x='Country', y=2022,
                   title='Projected 2022 GDP Per Capita *',
                   legend=False, xlabel='COUNTRY',
                   ylabel='GDP PER CAPITA IN USD'
                   )
q12.set_facecolor('k')

# 13. N/A
# 14. make it a pie chart
q14 = q10.plot.pie(y=2022,
                   title='Projected 2022 GDP Per Capita *', labels=q10.Country.values)
