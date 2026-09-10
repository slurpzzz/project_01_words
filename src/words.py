"""
CSAPX Project1: Words
Author: YOUR NAME HERE

Main program for the words project.
"""

import typer

app = typer.Typer(help="CSAPX Project 1: Words - A unified CLI for unigram analysis.")

@app.command()
def word_count() -> None:
    return None

@app.command()
def first_appearance() -> None:
    return None

@app.command()
def letter_freq() -> None:
    return None

@app.command()
def word_length() -> None:
    return None

@app.command()
def word_velocity() -> None:
    return None

@app.command()
def word_freq() -> None:
    return None

if __name__ == "__main__":
    app()