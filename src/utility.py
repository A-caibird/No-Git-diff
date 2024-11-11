import sys
from pathlib import Path
from difflib import Differ
from rich.console import Console
from rich.text import Text


def read_file(file_path):
    """
    Read the content of a file.
    Expands ~ to the user's home directory.

    Args:
        file_path (str): Path to the file.

    Returns:
        list[str]: Lines of the file content.
    """
    expanded_path = Path(file_path).expanduser()
    if not expanded_path.is_file():
        print(f"Error: File not found - {expanded_path}")
        sys.exit(1)
    with open(expanded_path, "r") as f:
        return f.readlines()


def highlight_diff(file1, file2, context_lines=3):
    """
    Compare two files and output highlighted differences with line numbers, showing context.

    Args:
        file1 (list[str]): First file content (lines).
        file2 (list[str]): Second file content (lines).
        context_lines (int): Number of context lines around changes.
    """
    console = Console()
    d = Differ()

    diff = list(d.compare(file1, file2))
    line_number1 = 0
    line_number2 = 0
    output_buffer = []
    show_diff = False

    for i, line in enumerate(diff):
        if line.startswith("  "):  # Unchanged line
            line_number1 += 1
            line_number2 += 1
            if show_diff:
                output_buffer.append((line_number1, line_number2, "  ", line[2:]))
        elif line.startswith("- "):  # Removed line
            line_number1 += 1
            show_diff = True
            output_buffer.append((line_number1, None, "- ", line[2:]))
        elif line.startswith("+ "):  # Added line
            line_number2 += 1
            show_diff = True
            output_buffer.append((None, line_number2, "+ ", line[2:]))
        elif line.startswith("? "):  # Markers for changes
            continue  # Skip detailed change markers

        # Flush context if no changes in the next few lines
        if show_diff and (i + 1 == len(diff) or diff[i + 1].startswith("  ")):
            for idx, (ln1, ln2, prefix, content) in enumerate(output_buffer):
                if idx < context_lines or idx >= len(output_buffer) - context_lines:
                    if prefix == "  ":
                        console.print(f"{ln1:>4} | {ln2:>4} | {content}")
                    elif prefix == "- ":
                        console.print(
                            f"{ln1:>4} | {' ' * 4} |", Text(content, style="bold red")
                        )
                    elif prefix == "+ ":
                        console.print(
                            f"{' ' * 4} | {ln2:>4} |", Text(content, style="bold green")
                        )
            output_buffer.clear()
            show_diff = False
