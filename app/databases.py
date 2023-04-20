
import os
from typing import Any

from azure.cosmos import CosmosClient
from azure.identity import DefaultAzureCredential
import pyodbc
environment = os.environ.get("ENVIRONMENT", default="sandbox")


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
