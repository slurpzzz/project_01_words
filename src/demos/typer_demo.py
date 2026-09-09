"""
Typer CLI reference demo for students
Run with: python3 typer_demo.py --help

Key Features, Mechanics & CLI Examples:

  * Command Auto-Naming:
      Function names in snake_case (e.g., `analyze_text`) automatically map 
      to POSIX-standard kebab-case CLI commands (`analyze-text`).
      Example CLI Usage:
        $ python typer_demo.py analyze-text "hello world"

  * Required Positional Arguments:
      Mandatory inputs use `typer.Argument(...)`. Failing to pass them exits with an error.
      Example CLI Usage:
        $ python typer_demo.py run-simulation 10

  * Optional Flags with Default Values:
      Optional inputs use `typer.Option(default_value, ...)`. If omitted, defaults apply.
      Example CLI Usage:
        $ python typer_demo.py run-simulation 10 --player-name "Alex"

  * Short Flag Aliases:
      Define shorthand flags (e.g., "-m", "--min-length") to support concise typing.
      Example CLI Usage:
        $ python typer_demo.py analyze-text "hello world" -m 4
        $ python typer_demo.py analyze-text "hello world" --min-length 4

  * Boolean Toggles:
      Parameters typed as `bool` act as on/off switches (passing the flag sets it to True).
      Example CLI Usage:
        $ python typer_demo.py analyze-text "hello world" -u
        $ python typer_demo.py run-simulation 10 --double-points

  * Auto-Generated Interactive Help:
      Typer automatically builds help pages from docstrings and `help="..."` parameters.
      Example CLI Usage:
        $ python typer_demo.py --help
        $ python typer_demo.py analyze-text --help
"""

import sys
import typer

app = typer.Typer(
    help="A sample CLI application demonstrating Typer features."
)


@app.command()
def analyze_text(
    # mandatory positional argument
    text: str = typer.Argument(
        ..., 
        help="The raw text string to analyze"
    ),
    # optional integer flag with short alias (-m) and default value
    min_length: int = typer.Option(
        3, 
        "-m", "--min-length", 
        help="Filter out words shorter than this length"
    ),
    # optional boolean flag (-u / --uppercase). Defaults to False.
    uppercase: bool = typer.Option(
        False, 
        "-u", "--uppercase", 
        help="Convert matching words to uppercase in output"
    ),
) -> None:
    """
    Filter and count words from an input string based on minimum length.
    """
    words = [w for w in text.split() if len(w) >= min_length]

    if uppercase:
        words = [w.upper() for w in words]

    print(f"Found {len(words)} word(s) matching criteria:")
    for w in words:
        print(f" - {w}")


@app.command()
def run_simulation(
    # mandatory integer argument
    rounds: int = typer.Argument(
        ..., 
        help="Number of simulation rounds to run"
    ),
    # optional string option with default value
    player_name: str = typer.Option(
        "Hero", 
        "-p", "--player-name", 
        help="Name of the player"
    ),
    # boolean flag
    double_points: bool = typer.Option(
        False, 
        "-d", "--double-points", 
        help="Enable 2x point multiplier"
    ),
) -> None:
    """
    Simulate a quick turn-based game scoring routine.
    """
    # input validation check
    if rounds <= 0:
        sys.stderr.write("Error: rounds must be a positive integer!\n")
        raise typer.Exit(code=1)

    multiplier = 2 if double_points else 1
    total_score = rounds * 10 * multiplier

    print(f"Running {rounds} rounds for {player_name}...")
    print(f"Final Score: {total_score}")


if __name__ == "__main__":
    app()