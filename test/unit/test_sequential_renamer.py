import mock
from roverio import sequential_renamer


def test_rename_files_no_force():
    messages, files_updated = sequential_renamer.SequentialRenamer.rename_files('.github/workflows', force=False)
    assert '.github/workflows/build.yml  ->  workflows-1.yml' in messages
    assert files_updated == 2


@mock.patch('os.rename')
def test_rename_files_force(mock_rename):
    messages, files_updated = sequential_renamer.SequentialRenamer.rename_files('.github/workflows', force=True)
    assert mock_rename.called_once()
    assert '.github/workflows/build.yml  ->  workflows-1.yml' in messages
    assert files_updated == 2
