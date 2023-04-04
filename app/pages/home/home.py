import dash
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

dash.register_page(__name__, path="/", name="Home")

timers = html.Div([])
stores = html.Div([])

_inline = {"display": "inline"}

body = html.Div(
    [
        dmc.Paper(
            children=[
                dmc.Title(
                    children=[
                        "Welcome ",
                        DashIconify(icon="mdi:greeting-outline", inline=True),
                    ],
                    color="#5c7cfa",
                ),
                dmc.Divider(),
                dmc.Text("""This is a demo FlowEHR application. """),
            ],
            style={"padding": "1rem"},
        ),
    ],
    style={"padding": "1rem"},
)


def layout() -> dash.html.Div:
    return html.Div(
        children=[
            timers,
            stores,
            body,
        ]
    )
