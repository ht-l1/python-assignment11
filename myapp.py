from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# The dataset to use is the Plotly built in gapminder dataset. This has, among other things, the per capita GDP for various countries for each year. For a given country, there will be one row per year. This means that the 'countries' column has many duplicates.
df = pldata.gapminder()
countries = df['country'].unique()

# Initialize Dash app
app = Dash(__name__)
server = app.server

# You want a dropdown that has each unique country name. You create a Series called countries that is the list of countries with duplicates removed. You use this Series to populate the dropdown. Give the dropdown the initial value of 'Canada'.
# You give the dropdown the id of 'country-dropdown' and also create a dcc.Graph with id 'gdp-growth'.
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{'label': country, 'value': country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# You create the decorator for the callback, associating the input with the dropdown and the output with the graph.
@app.callback(
    Output('gdp-growth', 'figure'),
    [Input('country-dropdown', 'value')]
)

# The decorator decorates an update_graph() function. This is passed the country name as a parameter. You need to filter the dataset to get only the rows where the country column matches this name. Then you create a line plot for 'year' vs. 'gdpPercap`. Give the plot a descriptive name that includes the country name.
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    
    # line plot
    fig = px.line(filtered_df, 
                  x='year', 
                  y='gdpPercap',
                  title=f'GDP Per Capita Over Time - {selected_country}',
                  labels={'gdpPercap': 'GDP Per Capita ($)', 'year': 'Year'})
    
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 