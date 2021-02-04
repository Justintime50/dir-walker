import pytest


@pytest.fixture
def mock_path():
    return './'


@pytest.fixture
def mock_csv_path():
    return './test_csv.csv'


@pytest.fixture
def mock_readmy_readme_rules():
    return './test/unit/test_readmy_readme_rules.txt'


@pytest.fixture
def mock_headers():
    return [
        ['header1'],
        ['header2'],
        ['header3']
    ]


@pytest.fixture
def mock_data():
    return [
        ['data1'],
        ['data2'],
        ['data3']
    ]
