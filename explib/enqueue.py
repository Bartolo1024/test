import click
from . import experiment


def test_method():
  """
  This is a test method

  | Arguments:
  | arg1: arg1 description
  | arg2: arg2 description

  | Returns:
  | None
  """
  print('I am a test method')


@click.command()
def main(*args, **kwargs):
    """Some docs xyz"""
    pass


if __name__ == '__main__':
    main()
