"""

"""
import pytest
from _pytest.fixtures import FixtureRequest


def pytest_addoption(parser):
    """
    For option arguments, see 'class Action(_AttributeHolder)'
    in ~/.pyenv/versions/3.7.0/lib/python3.7/argparse.py
    """
    parser.addoption(
        '--env',
        action='store',
        default='prod',
        help='environment value, defaulting to "prod"',
        choices=[
            'prod', 'qa'
        ]
    )


@pytest.fixture(scope='session')
def env(request: FixtureRequest):
    return request.config.getoption('--env')
