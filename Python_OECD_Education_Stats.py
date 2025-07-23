"""
OECD Education Statistics Dashboard
------------------------------------
Simulates an interactive dashboard using Plotly.
Allows selection of country and education indicator.

Skills:
- Interactive plotting with plotly
- Dropdown-based filtering
- Data visualization

Note: In a real scenario, use data from OECD API or .csv files.
"""

import pandas as pd
import plotly.express as px

# Simulated OECD education data
data = {
    'Country': ['USA', 'USA', 'USA', 'Germany', 'Germany', 'Germany', 'Japan', 'Japan', 'Japan'],
    'Year': [2018, 2019, 2020]*3,
    'Indicator': ['Tertiary Graduation Rate']*9,
    'Value': [45, 47, 48, 35, 36, 37, 52, 54, 53]
}

df = pd.DataFrame(data)

# Interactive plot
fig = px.line(
    df,
    x='Year',
    y='Value',
    color='Country',
    markers=True,
    title='Tertiary Education Graduation Rates (Simulated OECD Data)',
    labels={'Value': '% Graduation Rate'}
)

fig.update_layout(legend_title_text='Country')
fig.show()
