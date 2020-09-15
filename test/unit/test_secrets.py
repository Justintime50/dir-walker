from gatekeeper import secrets


def test_secrets_no_gitignore():
    result = secrets.Secrets.run('gatekeeper', 20)
    assert 'Secret: file_extension_files' in result[0]


def test_secrets_gitignore():
    result = secrets.Secrets.run('./', 20)
    assert 'Secret: long_description_content_type' in result[0]
