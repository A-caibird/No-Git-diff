# Diff Tool

A simple and efficient command-line utility to compare two text files and highlight the differences. Unlike `git diff`, this tool does not require a Git repository and can be used on any two plain text files. It is especially useful for quickly inspecting differences between two files, showing added and removed lines with context.

## 📝Features

- 🎈**Unnecessary Git**: Don't rely on git. 
- 🎓**Cross-Platform**: Supports macOS, Linux, and Windows.
- 😀**Easy Installation**: Available via Homebrew, Linuxbrew, or other package managers for seamless installation and updates.

- 🤖️**Highlight Changes**: 
  - Added lines (present in File B but not in File A) are displayed in **green**.
  - Removed lines (present in File A but not in File B) are displayed in **red**.
- 🤯**Line Numbers**: Each line is displayed with its corresponding line numbers from both files for easy reference.
- 🎃**Context Lines**: Shows up to 3 lines of context around changes for a clear understanding of modifications.
- 

## 🥢Usage

### Running the Tool

1. Make the script executable:
   ```bash
   chmod +x diff_tool.py
   ```

2. Run the tool with two file paths:
   ```bash
   python diff_tool.py <file1> <file2>
	```
   Example:
   ```bash
   python diff_tool.py ~/a.txt ~/b.txt
	```

### Example Output

Suppose `a.txt` contains:
```
Line 1
Line 2
Line 3
Line to remove
Line 5
```

And `b.txt` contains:
```
Line 1
Line 2
Line 3
Line added
Line 5
```

Running:
```bash
python diff_tool.py ~/a.txt ~/b.txt
```

Produces:
```
   1 |    1 | Line 1
   2 |    2 | Line 2
   3 |    3 | Line 3
      |    4 | Line added
-  4 |       | Line to remove
   5 |    5 | Line 5
```

### Notes on Differences

- **Added Lines**: Lines in File B but not in File A are considered "added" and highlighted in **green**.
- **Removed Lines**: Lines in File A but not in File B are considered "removed" and highlighted in **red**.

## Requirements

- Python 3.6 or higher
- `rich` library for colored terminal output:
  ```bash
  pip install rich
  ```

## Limitations

- This tool is intended for plain text files only. Binary files are not supported.
- The default context is 3 lines. If needed, you can modify the context in the code.

## Contributing

Feel free to submit issues or suggestions to improve this tool. Pull requests are welcome!

## License

This project is licensed under the MIT License.
