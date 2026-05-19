import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# נתונים לדוגמה
df = pd.DataFrame({
    "קטגוריה": ["A", "B", "C", "D"],
    "ערך": [4, 1, 2, 6]
})

# אתחול אפליקציית Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("דשבורד אינטרקטיבי לדוגמה"),
    dcc.Dropdown(
        id='dropdown',
        options=[{"label": cat, "value": cat} for cat in df["קטגוריה"]],
        value="A"
    ),
    dcc.Graph(id='bar-graph')
])

@app.callback(
    Output('bar-graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(selected_category):
    filtered_df = df[df["קטגוריה"] == selected_category]
    fig = px.bar(filtered_df, x="קטגוריה", y="ערך", title=f"ערך לקטגוריה {selected_category}")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)