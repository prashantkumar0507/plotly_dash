import plotly.express as px

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
# fig.show()

#add more features to the pie chart

fig = px.pie(df, values='pop', names='country', title='Population of European continent', hole=0.2,height=400, width=600)

# fig.show()

fig.update_traces(textinfo="none", insidetextfont={"color":"white"},hoverlabel={"align":"left","font_color":"white","bgcolor":"black"})

fig.update_layout(legend={"itemclick":False})

fig.show()

