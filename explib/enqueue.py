import click
from . import experiment


def test_method(x: int, y: int):
    """ Google
    Args:
        x: xxx
        y: yyy

    Returns:
        None
    """
    print('I am a test method')


def test_method_2(x, y):
    """ PEP
    :param x - x:
    :param y - y:
    """
    print('I am a test method 2')


def test_method_3(x, y):
    """
    :param x: x
    :param y: y
    """
    print('I am a test method 3')


def test_method_4(x:int, y: int):
    """ Numpy
    Parameters
    ----------
    x : type
        Description of parameter `x`.
    y
        Description of parameter `y` (with type not specified)
    """
    print('I am a test method 4')


@click.command()
def main(*args, **kwargs):
    """Some docs xyz"""
    test_method(1, 2)
    test_method_2(1, 2)


if __name__ == '__main__':
    main()
