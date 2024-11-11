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
        tuple[str, list[str]]: A tuple containing the file name and lines of the file content.
    """
    expanded_path = Path(file_path).expanduser()
    if not expanded_path.is_file():
        print(f"Error: File not found - {expanded_path}")
        sys.exit(1)
    with open(expanded_path, "r") as f:
        return expanded_path.name, f.readlines()


def highlight_diff(file1, file2):
    """
    Compare two files and output differences with clear file labels and custom highlighting.

    Args:
        file1 (tuple[str, list[str]]): Tuple containing the first file's name and content.
        file2 (tuple[str, list[str]]): Tuple containing the second file's name and content.
    """
    file_name1, file_content1 = file1
    file_name2, file_content2 = file2

    console = Console()
    d = Differ()

    diff = list(d.compare(file_content1, file_content2))
    line_number1 = 0
    line_number2 = 0
    temp_output = {"removed": None, "added": None, "line": None}
    pending_removal = False  # Flag to handle consecutive `-` lines

    for i, line in enumerate(diff):
        if line.startswith("  "):  # Unchanged line
            line_number1 += 1
            line_number2 += 1

            # Print accumulated changes if any
            if temp_output["removed"] or temp_output["added"]:
                console.print(f"in {temp_output['line']} line:")
                if temp_output["removed"]:
                    console.print(
                        Text("(-)", style="bold #f87171"),
                        f"{file_name1}: ",
                        Text(temp_output["removed"], style="bold #f87171"),
                        end="",
                    )
                if temp_output["added"]:
                    console.print(
                        Text("(+)", style="bold #a3e635"),
                        f"{file_name2}: ",
                        Text(temp_output["added"], style="bold #a3e635"),
                    )
                temp_output = {"removed": None, "added": None, "line": None}
                pending_removal = False

        elif line.startswith("- "):  # Removed line
            line_number1 += 1
            if temp_output["removed"]:
                # Print the previous removed line before handling the next
                console.print(f"in {temp_output['line']} line:")
                console.print(
                    Text("(-)", style="bold #f87171"),
                    f"{file_name1}: ",
                    Text(temp_output["removed"], style="bold #f87171"),
                )
            temp_output["removed"] = line[2:]
            temp_output["line"] = line_number1
            pending_removal = True  # Set the flag for consecutive `-` lines

        elif line.startswith("+ "):  # Added line
            line_number2 += 1
            if temp_output["removed"]:
                # If there's a removal, print both together
                console.print(f"in {temp_output['line']} line:")
                console.print(
                    Text("(-)", style="bold #f87171"),
                    f"{file_name1}: ",
                    Text(temp_output["removed"], style="bold #f87171"),
                    end="",
                )
                console.print(
                    Text("(+)", style="bold #a3e635"),
                    f"{file_name2}: ",
                    Text(line[2:], style="bold #a3e635"),
                )
                temp_output = {"removed": None, "added": None, "line": None}
                pending_removal = False
            else:
                # Otherwise, print added line separately
                console.print(f"in {line_number2} line:")
                console.print(
                    Text("(+)", style="bold #a3e635"),
                    f"{file_name2}: ",
                    Text(line[2:], style="bold #a3e635"),
                )

    # Handle any leftover changes after the loop
    if temp_output["removed"]:
        console.print(f"in {temp_output['line']} line:")
        console.print(
            Text("(-)", style="bold #f87171"),
            f"{file_name1}: ",
            Text(temp_output["removed"], style="bold #f87171"),
        )
    if temp_output["added"]:
        console.print(f"in {temp_output['line']} line:")
        console.print(
            Text("(+)", style="bold #a3e635"),
            f"{file_name2}: ",
            Text(temp_output["added"], style="bold #a3e635"),
        )
