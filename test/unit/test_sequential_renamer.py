import mock
from roverio import sequential_renamer


def test_rename_files_no_force():
    messages, files_updated = sequential_renamer.SequentialRenamer.rename_files('assets', force=False)
    assert 'assets/showcase.png  ->  assets-0.png' in messages
    assert files_updated == 1


@mock.patch('os.rename')
def test_rename_files_force(mock_rename):
    messages, files_updated = sequential_renamer.SequentialRenamer.rename_files('assets', force=True)
    assert mock_rename.called_once()
    assert 'assets/showcase.png  ->  assets-0.png' in messages
    assert files_updated == 1
