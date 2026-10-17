from app import app


def test_stock_route_is_registered():
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    assert "/stock" in routes
