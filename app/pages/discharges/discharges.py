import dash
import dash_mantine_components as dmc
import json
from dash import dash_table as dtable, html
from pathlib import Path
import ids

from pages.discharges import CAMPUSES


dash.register_page(__name__, path="/discharges", name="Discharges")

campus_selector = html.Div(
    [
        dmc.SegmentedControl(
            id="campus_selector",
            value=[i.get("value") for i in CAMPUSES if i.get("label") == "UCH"][0],
            data=CAMPUSES,
            persistence=True,
            persistence_type="local",
        ),
    ]
)
dept_selector = dmc.Container(
    [
        dmc.Select(
            placeholder="Select a ward",
            id="dept_selector",
            searchable=True,
            nothingFound="No match found",
            value="UCH T03 INTENSIVE CARE",
            persistence=True,
            persistence_type="local",
        ),
    ],
    fluid=True,
    p="xxs",
)

discharges_table = dmc.Paper(
    dtable.DataTable(
        id="discharges_table",
        columns=[
            {"id": "ward", "name": "Ward"},
            {"id": "full_name", "name": "Full Name"},
            {"id": "age_sex", "name": "Age / Sex"},
            {"id": "news", "name": "NEWS"},
            {"id": "admission_date", "name": "Admission Date"},
            {"id": "pred_discharge", "name": "Predicted Discharge"},
        ],
        style_table={"overflowX": "scroll"},
        style_as_list_view=True,  # remove col lines
        style_cell={
            "fontSize": 11,
            "padding": "5px",
        },
        style_data={"color": "black", "backgroundColor": "white"},
        # striped rows
        markdown_options={"html": True},
        persistence=False,
        persisted_props=["data"],
        sort_action="native",
        filter_action="native",
        filter_query="",
    ),
    shadow="lg",
    p="md",  # padding
    withBorder=True,
)


debug_inspector = dmc.Container(
    [
        dmc.Spoiler(
            children=[
                dmc.Prism(
                    language="json",
                    # id=ids.DEBUG_NODE_INSPECTOR_WARD, children=""
                )
            ],
            showLabel="Show more",
            hideLabel="Hide",
            maxHeight=100,
        )
    ]
)


body = dmc.Container(
    [
        dmc.Grid(
            children=[
                dmc.Col(discharges_table, span=12),
            ],
        ),
    ],
    style={"width": "100vw"},
    fluid=True,
)


def layout() -> dash.html.Div:
    return html.Div(
        children=[
            body,
            # debug_inspector,
        ]
    )
