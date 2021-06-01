from roverio import secrets


def test_secrets_no_gitignore():
    """This test isn't great but asserts against something that should
    hopefully stay pretty constant - `setup.py`
    """
    result = secrets.Secrets.search_for_secrets('roverio', 20)
    assert 'File: roverio/file_extension.py\nSecret: file_extension_files\nLine: 52\n' in result


def test_secrets_gitignore():
    """This test isn't great but asserts against something that should
    hopefully stay pretty constant - `setup.py`
    """
    result = secrets.Secrets.search_for_secrets('./', 20)
    assert 'File: ./setup.py\nSecret: long_description_content_type\nLine: 23\n' in result
