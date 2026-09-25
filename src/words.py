"""
CSAPX Project1: Words
Author: Justin Spadone

Main program for the words project.
"""
from collections import defaultdict
from typing import Annotated

import matplotlib.pyplot as plt
import typer
from rich.columns import Columns
from rich.console import Console
from rich.table import Table

from utils import *

app = typer.Typer(help="CSAPX Project 1: Words - A unified CLI for unigram analysis.")


@app.command()
def word_count(word: Annotated[str, typer.Argument(help='a word to display the total occurrences of')],
               filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')]) -> None:
    """Generate the total number of occurrences of a word in a unigram file."""
    unigram = load_unigram(filename)
    if word not in unigram:
        print(f'Error: {word} does not appear!', file=sys.stderr)
        return
    count = sum(unigram[word].values())
    print(f'{word}: {count}')


@app.command()
def first_appearance(word: Annotated[str, typer.Argument(help='the word to search for')],
                     threshold: Annotated[int, typer.Argument(help='the count threshold to cross')],
                     filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')]) -> None:
    """ Find the first year a word crossed a specific usage count threshold."""

    unigram = load_unigram(filename)
    first_year = None
    if word in unigram:
        for year, count in unigram[word].items():
            if count >= threshold and (first_year is None or year < first_year):
                first_year = year
    if first_year is None:
        print(f"'{word}' never reached a count of {threshold} in {filename}")
    else:
        print(f"'{word}' first reached {threshold} in {first_year}")


@app.command()
def letter_freq(filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')],
                output: Annotated[bool, typer.Option('-o', '--output',
                                                     help='display letter frequencies to standard output')] = False,
                plot: Annotated[
                    bool, typer.Option('-p', '--plot',
                                       help='plot letter frequencies using matplotlib')] = False) -> None:
    """Generate the frequency distribution for the total of all letters in all the words across all years in the unigram."""
    unigram = load_unigram(filename)
    letter_counts = {}
    for word in unigram:
        word_total = sum(unigram[word].values())
        for letter in word:
            if letter not in letter_counts:
                letter_counts[letter] = word_total
            else:
                letter_counts[letter] += word_total
    total_letters = sum(letter_counts.values())
    letter_freqs = {}
    for letter in letter_counts:
        letter_freqs[letter] = letter_counts[letter] / total_letters
    letter_freqs_sorted = sorted(letter_freqs)
    if output:
        for letter in letter_freqs_sorted:
            print(f'{letter}: {letter_freqs[letter]}')
    if plot:
        plt.bar(letter_freqs_sorted, [letter_freqs[letter] for letter in letter_freqs_sorted])
        plt.title(f'Letter Frequencies: {filename}')
        plt.xlabel('Letter')
        plt.ylabel('Frequency')
        plt.show()


@app.command()
def word_length(start: Annotated[int, typer.Argument(help='the starting year range')],
                end: Annotated[int, typer.Argument(help='the ending year range')],
                filename: Annotated[str, typer.Argument(help='a comma separated value unigram file')],
                output: Annotated[
                    bool, typer.Option('-o', '--output', help='display the average word lengths over years')] = False,
                plot: Annotated[bool, typer.Option('-p', '--plot',
                                                   help='plot the average word lengths over years')] = False) -> None:
    """Generate and/or plot the average word length for a range of years."""
    if not output and not plot:
        return
    unigram = load_unigram(filename)
    if start > end:
        print('Error: start year must be less than or equal to end year!', file=sys.stderr)
        sys.exit(1)
    year_chars = defaultdict(int)
    year_words = defaultdict(int)
    for word in unigram:
        w_len = len(word)
        for year, occurrences in unigram[word].items():
            if year < start or year > end:
                continue
            year_chars[year] += w_len * occurrences
            year_words[year] += occurrences
    year_lengths = {}
    for year in sorted(year_words):
        year_lengths[year] = year_chars[year] / year_words[year]
        if output:
            print(f'{year}: {year_lengths[year]}')
    if plot:
        plt.plot(year_lengths.keys(), year_lengths.values())
        plt.title(f'Average word lengths from {start} to {end}: {filename}')
        plt.xlabel('Year')
        plt.ylabel('Average word length')
        plt.show()


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
    if start1 > end1 or start2 > end2:
        print('Error: Start years must be less than or equal to end years', file=sys.stderr)
        sys.exit(1)
    unigram = load_unigram(filename)
    c1 = 0
    c2 = 0
    era1_word_counts = defaultdict(int)
    era2_word_counts = defaultdict(int)
    era1_word_freqs = {}
    era2_word_freqs = {}
    era1_total_words = 0
    era2_total_words = 0
    for word in unigram:
        for year, occurrences in unigram[word].items():
            if start1 <= year <= end1:
                era1_word_counts[word] += occurrences
                era1_total_words += occurrences
            if start2 <= year <= end2:
                era2_word_counts[word] += occurrences
                era2_total_words += occurrences

    era1_word_counts = {k: v for k, v in era1_word_counts.items() if v >= min_count}
    era2_word_counts = {k: v for k, v in era2_word_counts.items() if v >= min_count}

    for word in era1_word_counts:
        era1_word_freqs[word] = era1_word_counts[word] / era1_total_words
    for word in era2_word_counts:
        era2_word_freqs[word] = era2_word_counts[word] / era2_total_words
    word_velocities = {}
    for word in era1_word_freqs:
        if word in era2_word_freqs:
            f1 = era1_word_freqs[word]
            f2 = era2_word_freqs[word]
            word_velocities[word] = (f2 - f1) / f1

    print_table(word_velocities, start1, end1, start2, end2, top)


def print_table(word_velocities, start1, end1, start2, end2, top):
    console = Console()
    surging_table = Table(title='Surging Words')
    fading_table = Table(title='Fading Words')
    surging_table.add_column('Word')
    surging_table.add_column('Change')
    fading_table.add_column('Word')
    fading_table.add_column('Change')
    surging_velocities = {}
    fading_velocities = {}
    for word, change in word_velocities.items():
        if change > 0:
            surging_velocities[word] = change
        elif change < 0:
            fading_velocities[word] = change
    for word, change in sorted(surging_velocities.items(), key=lambda entry: entry[1], reverse=True)[:top]:
        surging_table.add_row(word, f'+{change:.2%}')

    for word, change in sorted(fading_velocities.items(), key=lambda entry: entry[1])[:top]:
        fading_table.add_row(word, f'{change:.2%}')
    side_by_side = Columns([surging_table, fading_table],
                           title=f'Word Velocity Comparison ({start1}-{end1} vs {start2}-{end2})')
    console.print(side_by_side)


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
