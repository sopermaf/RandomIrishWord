"""Command-line interface."""
import click

from . import words


@click.command()
@click.version_option()
def main() -> None:
    """Teanglann."""
    word = words.get_random_definition()
    click.echo(word)


if __name__ == "__main__":
    main(prog_name="random_irish_word")  # pragma: no cover
