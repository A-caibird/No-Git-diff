# No-Git-diff Tool

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

## Installation

### Script Install

1. For Mac Osx and Linx: 
2. For Window: 

### Package Install

`brew`

```shell
```

`apt`

```
```

`pacman`

```shell

```

### Manual install

## Usage

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
dt ~/a.txt ~/b.txt
```

Produces:

![nihao](https://github.com/A-caibird/picx-images-hosting/raw/master/GitHub/1.491alfljvq.webp)

### Notes on Differences

- **Added Lines**: Lines in File B but not in File A are considered "added" and highlighted in **green**.
- **Removed Lines**: Lines in File A but not in File B are considered "removed" and highlighted in **red**.

## Development Requirements

- Python 3.6 or higher
- `rich` library for colored terminal output:
  ```bash
  pip install -r requirements.txt
  ```

## Limitations

- This tool is intended for plain text files only.
- The default context is 3 lines. If needed, you can modify the context in the code,perform a manual compilation installation

## Contributing

Feel free to submit issues or suggestions to improve this tool. Pull requests are welcome!

## License

This project is licensed under the MIT License.
