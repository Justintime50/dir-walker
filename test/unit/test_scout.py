from gatekeeper import scout


def test_scout():
    result = scout.Scout.run('gatekeeper', 'def main()')
    assert 'Search: def main():' in result[0]
    assert 'Search: def main():' in result[1]
    assert 'Search: def main():' in result[2]
