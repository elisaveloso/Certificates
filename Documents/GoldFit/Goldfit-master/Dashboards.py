#Modules and libraries
import dash
from dash import dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json
import math

# Database import
db = pd.read_excel("data.xlsx")
db.insert(1, "idade", db['IdadeCronológica'].astype(int), True)
db_np = np.array(db)

# Clean data
for x in db.index:
    if db["IdadeCronológica"].duplicated()[x] == True:
        db.drop(x, inplace=True)


# Graph
fig1 = px.bar(db, x="IdadeCronológica", y="Estatura", barmode="group")

fig2 = px.scatter(db, x="IdadeCronológica", y="P_Concentração",
                  size="P_ApoioFamilia",
                  log_x=True, size_max=60)

fig3 = px.scatter(db, x="GorduraCorporal", y="Velocidade20m")

# ------------ APP layout -------------

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("GOLDFIT", style={'text-align': 'center'}),

    dcc.Graph(figure=fig1),

    html.Br(),

    dcc.Graph(figure=fig2),

    html.Br(),

    dcc.Graph(figure=fig3),

    html.Br(),

    # Test slider

    dcc.Graph(figure=fig3, id='id_output_graph1'),

    html.Br(),

    dcc.Slider(min=12, max=17, step=1,  value=12, id='id_slider1'),

    html.Br(),

    # Agilidade slider
    dcc.Graph(figure=fig3, id='id_output_graph2'),

    html.Br(),

    dcc.Slider(0, 100, value=90, marks={
        0: {'label': '0%'},
        25: {'label': '25%'},
        50: {'label': '50%'},
        75: {'label': '75%'},
        100: {'label': '100%'},
    }, id='id_slider2'),

    html.Br(),

    # Salto slider
    dcc.Graph(figure=fig3, id='id_output_graph3'),

    html.Br(),

    dcc.Slider(0, 100, value=90, marks={
        0: {'label': '0%'},
        25: {'label': '25%'},
        50: {'label': '50%'},
        75: {'label': '75%'},
        100: {'label': '100%'},
    }, id='id_slider3'),

    html.Br(),

    # Força slider
    dcc.Graph(figure=fig3, id='id_output_graph4'),

    html.Br(),

    dcc.Slider(0, 100, value=90, marks={
        0: {'label': '0%'},
        25: {'label': '25%'},
        50: {'label': '50%'},
        75: {'label': '75%'},
        100: {'label': '100%'},
    }, id='id_slider4')

])

# Test slider callback


@app.callback(
    Output('id_output_graph1', 'figure'),
    Input('id_slider1', 'value')
)
def update_output(value):
    # filtro de idade
    db_filter = db.loc[(db['Ano_Avaliação'] -
                        db["Ano_Nascimento"]) >= value, :]
    fig = px.scatter(db_filter, x="GorduraCorporal", y="Velocidade20m")
    return fig

# Agilidade slider callback


@app.callback(
    Output('id_output_graph2', 'figure'),
    Input('id_slider2', 'value')
)
def update_output(value):
    db_filter = db.loc[db['P_Agilidade'] >= value, :]  # filtro de idade
    fig = px.violin(db_filter, y='Agilidade', x='idade')
    return fig

# Salto slider callback


@app.callback(
    Output('id_output_graph3', 'figure'),
    Input('id_slider3', 'value')
)
def update_output(value):
    db_filter = db.loc[db['P_SaltoVertical'] >= value, :]  # filtro de idade
    fig = px.violin(db_filter, y='SaltoVertical', x='idade')
    return fig

# Força slider callback


@app.callback(
    Output('id_output_graph4', 'figure'),
    Input('id_slider4', 'value')
)
def update_output(value):
    db_filter = db.loc[db['P_ForçaMão'] >= value, :]  # filtro de idade
    fig = px.violin(db_filter, y='ForçaMão', x='idade')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
