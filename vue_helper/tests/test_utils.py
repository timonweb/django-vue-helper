from vue_helper.utils import get_js_and_css_links_from_html


def test_get_js_and_css_links_from_html():
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
  <script src="/js/app.8170fja.js"></script>
  <script src="/js/vendors.8170fja.js"></script>
  <link rel="stylesheet" href="/css/app.8170fja.css">
  <link rel="stylesheet" href="/css/vendors.8170fja.css">
</head>
<body>
<div id="app"></div>
</body>
</html>    
"""
    js, css = get_js_and_css_links_from_html(html)

    assert js == {'/static/example_vue/dist/js/app.8170fja.js', '/static/example_vue/dist/js/vendors.8170fja.js'}
    assert css == {'/static/example_vue/dist/css/app.8170fja.css', '/static/example_vue/dist/css/vendors.8170fja.css'}
