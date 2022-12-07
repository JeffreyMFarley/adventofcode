import io
from dataclasses import dataclass

INPUT = "input1.txt"

# ------------------------------------------------------
# Classes


class OS(object):
    def __init__(self, raw: str) -> None:
        self.root = OS_Dir("/")
        self._cwd = None

        cmds = list(map(str.lstrip, raw.split("$")))
        for cmd in cmds:
            self.parse(cmd)

    def __repr__(self) -> str:
        return repr(self.root)

    # --------------------------------------------------

    def parse(self, s: str) -> None:
        if not s:
            return

        cmd_line, *output = s.splitlines()
        cmd, *args = cmd_line.split()
        if cmd == "cd":
            self._change_dir(args[0])
        elif cmd == "ls":
            self._parse_ls_output(output)
        else:
            raise NotImplementedError(f"Unknown command {cmd}")

    def dfs(self):
        q = [self.root]
        while len(q):
            curr = q.pop(0)
            yield curr
            q.extend(curr.dirs())

    # --------------------------------------------------

    def _change_dir(self, to_dir: str) -> None:
        if to_dir == "/":
            self._cwd = self.root
        elif to_dir == "..":
            self._cwd = self._cwd.parent
        else:
            self._cwd = self._cwd.children[to_dir]

    def _parse_ls_output(self, output: list[str]) -> None:
        for a1, a2 in map(str.split, output):
            if a1 == "dir":
                self._cwd.add_dir(a2)
            else:
                self._cwd.add_file(int(a1), a2)


class OS_Dir(object):
    def __init__(self, name: str) -> None:
        self.children = {}
        self.files = []
        self.name = name
        self.parent = None

    def __repr__(self) -> str:
        d = "\n   ".join([repr(x) for x in self.dirs()])
        f = "\n   ".join([repr(x) for x in self.files])

        output = f"+- {self.name}"
        if d:
            output += f"\n   {d}"
        if f:
            output += f"\n   {f}"
        return output

    def dirs(self):
        for d in self.children.values():
            yield d

    def add_dir(self, name: str):
        r = OS_Dir(name)
        self.children[name] = r
        r.parent = self

    def add_file(self, size: int, name: str):
        self.files.append(OS_File(size, name))

    def size(self) -> int:
        r = sum([x.size() for x in self.children.values()])
        r += sum([x.size for x in self.files])
        return r


@dataclass
class OS_File:
    size: int
    name: str

    def __repr__(self) -> str:
        return f"{self.name}\t({self.size})"


# ------------------------------------------------------
# Load


def load():
    with io.open(INPUT, "r", encoding="utf-8") as f:
        return f.read()


# ------------------------------------------------------
# Functions


def under_100K(i: int) -> bool:
    return i < 100000


# ------------------------------------------------------
# Main

TOTAL_SPACE = 70000000
FREE_NEEDED = 30000000


def main():
    drive = OS(load())
    sizes = sorted([d.size() for d in drive.dfs()])
    print(f"Solution 1: {sum(filter(under_100K, sizes)):,}")

    curr_size = drive.root.size()
    unused = TOTAL_SPACE - curr_size
    needed = FREE_NEEDED - unused

    candidate = min(filter(lambda x: x > needed, sizes))
    print(f"Solution 2: {candidate:,}")


if __name__ == "__main__":
    main()
