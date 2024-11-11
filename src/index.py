import sys
from utility import read_file, highlight_diff

def main():
    """
    Main function to handle command-line arguments and perform diff.
    """
    if len(sys.argv) != 3:
        print("Usage: dt <file1> <file2>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    print(file1_path)
    print(file2_path)
    file1_content = read_file(file1_path)
    file2_content = read_file(file2_path)

    highlight_diff(file1_content, file2_content)


if __name__ == "__main__":
    main()
