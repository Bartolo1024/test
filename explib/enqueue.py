import click
from . import experiment


def test_method(x: int, y: int):
    """
    Args:
        x: xxx
        y: yyy

    Returns:
        None
    """
    print('I am a test method')


@click.command()
def main(*args, **kwargs):
    """Some docs xyz"""
    pass


if __name__ == '__main__':
    main()
