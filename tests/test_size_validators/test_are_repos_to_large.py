from fiasko_bro.pre_validation_checks import are_repos_too_large

from fiasko_bro import defaults

def test_repo_size_fail_single(general_repo_path):
    max_py_files_count = 1
    directories_to_skip = defaults.VALIDATOR_SETTINGS['directories_to_skip']
    output = are_repos_too_large(general_repo_path, directories_to_skip, max_py_files_count)
    assert isinstance(output, tuple)
    assert output[0] == 'Repo is too large'


def test_repo_size_fail_double(general_repo_path, general_repo_origin_path):
    max_py_files_count = 1
    directories_to_skip = defaults.VALIDATOR_SETTINGS['directories_to_skip']
    output = are_repos_too_large(
        general_repo_path,
        directories_to_skip,
        max_py_files_count,
        general_repo_origin_path
    )
    assert isinstance(output, tuple)
    assert output[0] == 'Repo is too large'


def test_repo_size_ok_single(general_repo_path):
    max_py_files_count = 1000
    directories_to_skip = defaults.VALIDATOR_SETTINGS['directories_to_skip']
    output = are_repos_too_large(general_repo_path, directories_to_skip, max_py_files_count)
    assert output is None


def test_repo_size_ok_double(general_repo_path, general_repo_origin_path):
    max_py_files_count = 1000
    directories_to_skip = defaults.VALIDATOR_SETTINGS['directories_to_skip']
    output = are_repos_too_large(
        general_repo_path,
        directories_to_skip,
        max_py_files_count,
        general_repo_origin_path
    )
    assert output is None
