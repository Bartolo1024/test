import click


class Experiment:
    def __init__(run_id: str):
        """
        Args:
            run_id: experiment id
        """
        self.run_id = run_id

    def run():
        """Run the experiment"""
        pass


@click.command()
def main(*args, **kwargs):
    """Some docs xyz"""
    pass


if __name__ == '__main__':
    main()
