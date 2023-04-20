import dash_mantine_components as dmc


def create_home_link(label: str) -> dmc.Anchor:
    return dmc.Anchor(
        label,
        size="xl",
        href="/",
        underline=False,
    )


def create_footer() -> dmc.Footer:
    return dmc.Footer(
        height=70,
        fixed=True,
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                style={"height": 70},
                children=dmc.Grid(
                    children=[
                        dmc.Col(
                            [
                                dmc.MediaQuery(
                                    create_home_link("FlowEHR"),
                                    styles={"display": "none"},
                                ),
                            ],
                            span="content",
                            pt=12,
                        ),
                        # Create a search box and pre-populate with page names
                        dmc.Col(
                            span="auto",
                            children=dmc.Group(
                                position="right",
                                spacing="xl",
                                children=[],
                            ),
                        ),
                    ],
                ),
            )
        ],
    )
