"""
Rich Nested Table Demo for Students
-----------------------------------
Demonstrates single-header columns alongside a split column using nested tables.
Run with: python3 rich_demo.py
"""

from rich.console import Console
from rich.table import Table


def main() -> None:
    console = Console()

    # 1. Create the outer/main table
    main_table = Table(title="Academic Department Summary")

    # Single header columns
    main_table.add_column("Department", style="cyan", no_wrap=True)
    main_table.add_column("Department Head", style="bold white")

    # Main column that will hold our 2-column sub-tables
    main_table.add_column("Active Courses (Code & Capacity)")

    # 2. Build sub-table 1 (Splits into 2 sub-columns for CS)
    cs_subtable = Table(show_header=True, header_style="bold green")
    cs_subtable.add_column("Course Code", style="dim")
    cs_subtable.add_column("Enrolled", justify="right")

    cs_subtable.add_row("CS-141", "250")
    cs_subtable.add_row("CS-242", "120")

    # 3. Build sub-table 2 (Splits into 2 sub-columns for Math)
    math_subtable = Table(show_header=True, header_style="bold green")
    math_subtable.add_column("Course Code", style="dim")
    math_subtable.add_column("Enrolled", justify="right")

    math_subtable.add_row("MATH-181", "310")
    math_subtable.add_row("MATH-221", "95")

    # 4. Add rows to main table (pass the sub-tables directly as the 3rd cell value)
    main_table.add_row("Computer Science", "Dr. Alan Turing", cs_subtable)
    main_table.add_row("Mathematics", "Dr. Emmy Noether", math_subtable)

    # 5. Render output
    console.print(main_table)


if __name__ == "__main__":
    main()