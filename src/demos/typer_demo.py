"""
Typer CLI reference demo for students
Run with: python3 typer_demo.py --help

Key Features & CLI Examples:

  * Command Auto-Naming (snake_case -> kebab-case):
      Function names in snake_case notation automatically map to kebab-case CLI commands.
      Sample: 'send_notice' function becomes 'send-notice' CLI command
      Example CLI Usage:
        $ python typer_demo.py send-notice Alice

  * Required Positional Arguments:
      Mandatory inputs use `typer.Argument(...)` without a default value.
      Failing to pass them exits with an error.
      Example CLI Usage:
        $ python typer_demo.py greet Alice

  * Optional Positional Arguments:
      Parameters with default values using typer.Argument(...) become optional positional arguments.
      Takes an input value. If omitted, the default is used.
      Example CLI Usage:
        $ python typer_demo.py greet Alice True

  * Optional Argument with Short Flag Aliases:
      Parameters with default values using typer.Option(...) allow defining
      shorthand flags (e.g., "-p", "--priority") to support concise typing.
      Example CLI Usage:
        $ python typer_demo.py send-notice Alice -p 3
        $ python typer_demo.py send-notice Alice --priority 3

  * Boolean Toggles:
      Optional parameters typed as `bool` act as on/off switches (passing the flag sets it to True).
      Example CLI Usage:
        $ python typer_demo.py send-notice Alice -u
        $ python typer_demo.py send-notice Alice --urgent

  * Auto-Generated Interactive Help:
      Typer automatically builds help pages from docstrings and `help="..."` parameters.
      Example CLI Usage:
        $ python typer_demo.py --help
        $ python typer_demo.py send-notice --help
"""

from typing import Annotated

import typer

app = typer.Typer(
    help="A sample CLI application demonstrating Typer features."
)


@app.command()
def greet(
        # positional argument required (no default value)
        name: Annotated[str, typer.Argument()],
        # optional positional argument (has a default value, takes an input value)
        formal: Annotated[bool, typer.Argument()] = False,
) -> None:
    """Greet a person by name."""
    message = f"Good day, {name}." if formal else f"Hello, {name}!"
    print(message)


@app.command()
def send_notice(
        # positional argument required (no default value)
        username: Annotated[
            str,
            typer.Argument(help="Target username (Required)")
        ],
        # named optional argument (has default value, takes an input value)
        priority: Annotated[
            int,
            typer.Option("-p", "--priority", help="Priority level 1-5")
        ] = 1,
        # boolean optional flag (default False, acts as on/off switch)
        urgent: Annotated[
            bool,
            typer.Option("-u", "--urgent", help="Mark notice as urgent")
        ] = False,
) -> None:
    """
    Send a notification to a recipient.
    Prints a prioritized message to the given user applying optional urgency and priority.
    """
    notice_type = "URGENT NOTICE" if urgent else "Standard Notice"
    print(f"[{notice_type}] Priority {priority} -> Sent to user: {username}")


if __name__ == "__main__":
    app()