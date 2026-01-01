# tests/test_app.py
import pytest
from dash import Dash
from dash.testing.application_runners import import_app

# Test 1: Check if the app loads without errors
def test_app_loads(dash_duo):
    # Start the app
    app = import_app("app")  # refers to app.py
    dash_duo.start_server(app)

    # Wait for the app to load
    dash_duo.wait_for_element("#sales-chart", timeout=10)

    # Test 1: Header is present
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Dashboard"

    # Test 2: Visualization (graph) is present
    assert dash_duo.find_element("#sales-chart") is not None

    # Test 3: Region picker (radio buttons) is present
    assert dash_duo.find_element("#region-filter") is not None

    # Optional: Take a snapshot (for debugging)
    # dash_duo.percy_snapshot("app loaded")