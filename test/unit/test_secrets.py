from roverio import secrets


def test_secrets_no_gitignore():
    result = secrets.Secrets.search_for_secrets('roverio', 20)
    assert 'File: roverio/file_extension.py\nSecret: file_extension_files\nLine: 52\n' in result


def test_secrets_gitignore():
    result = secrets.Secrets.search_for_secrets('./', 20)
    assert 'File: ./setup.py\nSecret: long_description_content_type\nLine: 15\n' in result
