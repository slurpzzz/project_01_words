"""
CSAPX Project1: Words
Author: YOUR NAME HERE

Main program for the words project.
"""
from typing import Annotated
import typer

app = typer.Typer(help="CSAPX Project 1: Words - A unified CLI for unigram analysis.")


@app.command()
def word_count(word: Annotated[str, typer.Argument(help='a word to display the total occurrences of')],
               filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')]) -> None:
    """Generate the total number of occurrences of a word in a unigram file."""
    return None


@app.command()
def first_appearance(word: Annotated[str, typer.Argument(help='the word to search for')],
                     threshold: Annotated[int, typer.Argument(help='the count threshold to cross')],
                     filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')]) -> None:
    """ Find the first year a word crossed a specific usage count threshold."""
    return None


@app.command()
def letter_freq(filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')],
                output: Annotated[bool, typer.Option('-o', '--output',
                                                     help='display letter frequencies to standard output')] = False,
                plot: Annotated[
                    bool, typer.Option('-p', '--plot',
                                       help='plot letter frequencies using matplotlib')] = False) -> None:
    """Generate the frequency distribution for the total of all letters in all the words across all years in the unigram."""
    return None


@app.command()
def word_length(start: Annotated[int, typer.Argument(help='the starting year range')],
                end: Annotated[int, typer.Argument(help='the ending year range')],
                filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')],
                output: Annotated[
                    bool, typer.Option('-o', '--output', help='display the average word lengths over years')] = False,
                plot: Annotated[bool, typer.Option('-p', '--plot',
                                                   help='plot the average word lengths over years')] = False) -> None:
    """Generate and/or plot the average word length for a range of years."""
    return None


@app.command()
def word_velocity(start1: Annotated[int, typer.Argument(help='start year of first range')],
                  end1: Annotated[int, typer.Argument(help='end year of first range')],
                  start2: Annotated[int, typer.Argument(help='start year of second range')],
                  end2: Annotated[int, typer.Argument(help='end year of second range')],
                  filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')],
                  top: Annotated[int, typer.Option('-t', '--top', help='number of top words')] = 5,
                  min_count: Annotated[int, typer.Option('-c', '--min-count',
                                                         help='minimum total count threshold across both eras')] = 50) -> None:
    """Compare word frequencies between two decade ranges to identify surging and fading words."""
    return None


@app.command()
def word_freq(word: Annotated[str, typer.Argument(help='a word to display the overall ranking of')],
              filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')],
              output: Annotated[
                  int | None, typer.Option('-o', '--output',
                                           help='display the top OUTPUT (#) ranked words by number of occurrences')] = None,
              plot: Annotated[bool, typer.Option('-p', '--plot',
                                                 help='plot the word rankings from top to bottom based on occurrences')] = False) -> None:
    """Generate and/or plot the popularity of a given word, by rank, over the entire period of time of the unigram file."""
    return None


if __name__ == "__main__":
    app()
