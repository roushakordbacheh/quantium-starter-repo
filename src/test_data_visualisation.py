from data_visualisation import build_app

def test_header_is_present(dash_duo):
    """
    Validate to see if the header is present
    in the HTML code.
    """
    app = build_app()
    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal('h1', "Soul Foods", timeout=5)
    assert dash_duo.find_element('h1').text == 'Soul Foods'

def test_visualisation_is_present(dash_duo):
    """
    Validate to see if the visualisation has loaded correctly.
    """
    app = build_app()
    dash_duo.start_server(app)

    dash_duo.wait_for_element('#pink_morsel_total_sales', timeout=5)
    assert dash_duo.find_element('#pink_morsel_total_sales') is not None


def test_region_picker_is_present(dash_duo):
    """
    Validate to see if the region is present in the HTML code.
    """
    app = build_app()
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#region_selector", timeout=5)
    assert dash_duo.find_element("#region_selector") is not None