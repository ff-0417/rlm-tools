import sys

def read_header(path):
    with open(path, "rb") as f:
        return f.read(16)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: parser.py <file>")
        raise SystemExit(1)

    print(read_header(sys.argv[1]).hex())
