#  Copyright (c) University College London Hospitals NHS Foundation Trust
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from dash import Dash, page_registry, html, dcc
from typing import Any
from layout.appshell import create_appshell
from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
import pyodbc
import pandas as pd
import plotly.express as px


environment = os.environ.get("ENVIRONMENT", default="sandbox")


app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        "assets/style.css",
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400"
        ";500;900&display=swap",
        "https://use.fontawesome.com/releases/v5.8.1/css/all.css",
    ],
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1, "
            "user-scalable=no",
        }
    ],
)

app.config.suppress_callback_exceptions = True
app.layout = create_appshell([page_registry.values()])

server = app.server


def odbc_cursor() -> Any:
    """
    ODBC cursor for running queries against the MSSQL feature store.

    Documentation: https://github.com/mkleehammer/pyodbc/wiki
    """

    connection = pyodbc.connect(os.environ["FEATURE_STORE_CONNECTION_STRING"])
    return connection.cursor()


def cosmos_client() -> "CosmosClient":
    """
    CosmosDB client for connecting with the state store.

    Documentation:
    https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/sdk-python
    """

    client = CosmosClient(
        os.environ["COSMOSDB_ENDPOINT"],
        credential=(
            DefaultAzureCredential()
            if environment != "local"
            else os.environ["COSMOSDB_KEY"]
        ),
        connection_verify=(environment != "local"),
    )
    return client


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8000, debug=(environment == "local"))
