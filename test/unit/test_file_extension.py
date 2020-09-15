from gatekeeper import file_extension


def test_file_extension():
    result = file_extension.FileExtension.run('gatekeeper', '.py')
    assert 'gatekeeper/file_extension.py' in result
