import plotly.express as px
import plotly.data as pldata
import pandas as pd
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# Clean the data. You need to convert the 'strength' column to a float. Use of str.replace() with regex is one way to do this, followed by type conversion.
df['strength'] = df['strength'].astype(str).str.replace(r'[^\d.]', '', regex=True)
df['strength'] = pd.to_numeric(df['strength'], errors='coerce')

# Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
fig = px.scatter(df, 
                x='strength', 
                y='frequency', 
                color='direction',
                title='Wind Strength vs Frequency by Direction',
                labels={'strength': 'Wind Strength', 'frequency': 'Frequency'})

# Save as HTML
fig.write_html('wind.html')
print("Plot saved as wind.html")

# Show the plot
fig.show()