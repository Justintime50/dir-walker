from gatekeeper import scout


def test_scout():
    result = scout.Scout.run('gatekeeper', 'def main()')
    assert 'File: gatekeeper/scout.py\nSearch: def main():\nLine: 66\n' in result
