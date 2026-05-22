import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Sample EV Data
data = {
    "Year": [2019, 2020, 2021, 2022, 2023],
    "EV_Sales": [50000, 120000, 300000, 700000, 1500000]
}

# Create DataFrame
df = pd.DataFrame(data)
# Create Graph
fig = px.line(
    df,
    x="Year",
    y="EV_Sales",
    title="EV Market Growth"
)

# Create App
app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("EV Market Forecast Dashboard"),

    dcc.Graph(figure=fig)

])

# Run App
if __name__ == "__main__":
    app.run(debug=True)