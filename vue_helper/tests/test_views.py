def test_view_has_scripts_and_styles(client):
    response = client.get('')
    assert 'rel="stylesheet"' in str(response.content), "A Vue stylesheet is present in HTML output"
    assert '<script src="' in str(response.content), "A Vue scripts are present in HTML output"
