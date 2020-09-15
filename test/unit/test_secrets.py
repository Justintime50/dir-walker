from gatekeeper import secrets


def test_secrets_no_gitignore():
    result = secrets.Secrets.run('gatekeeper', 20)
    assert 'File: gatekeeper/file_extension.py\nSecret: file_extension_files\nLine: 43\n' in result  # noqa


def test_secrets_gitignore():
    result = secrets.Secrets.run('./', 20)
    assert 'File: ./setup.py\nSecret: long_description_content_type\nLine: 11\n' in result  # noqa
