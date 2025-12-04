import io
from dataclasses import dataclass

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

@dataclass
class Range:
    start: int
    end: int

    def width(self):
        return max(len(str(self.start)), len(str(self.end)))

    def range_size(self):
        return self.end - self.start + 1

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield i

# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        raw = f.read()
    
    ranges = []
    for r in raw.split(","):
        a, b = r.split("-")
        rg = Range(int(a), int(b))
        ranges.append(rg)
    return ranges

# ------------------------------------------------------
#

def is_invalid(val: int) -> bool:
    s = str(val)
    length = len(s)
    if length == 1:
        return False
    if length == 2:
        return s[0] == s[1]
    mid = length // 2
    if length % 2 == 0:
        left = s[:mid]
        right = s[mid:]
        return left == right
    
     # odd lengths will only match if all digits are the same
    return False

# ------------------------------------------------------
# Main

def main():
    sum_invalid = 0

    ranges = load()
    for r in ranges:
        for value in r:
            if is_invalid(value):
                print(f"Invalid value found: {value}")
                sum_invalid += value


    print(f"Sum of invalid values: {sum_invalid}")

if __name__ == '__main__':
    main()
