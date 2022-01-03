import io

from dataclasses import dataclass
from functools import reduce

INPUT = 'input1.txt'

SUITE = {
    'C200B40A82': 3,
    '04005AC33890': 54,
    '880086C3E88112': 7,
    'CE00C43D881120': 9,
    'D8005AC2A8F0': 1,
    'F600BC2D8F': 0,
    '9C005AC2F8F0': 0,
    '9C0141080250320F1802104A08': 1
}

PACKET_SUM = 0
PACKET_PRODUCT = 1
PACKET_MINIMUM = 2
PACKET_MAXIMUM = 3
PACKET_LITERAL = 4
PACKET_GT = 5
PACKET_LT = 6
PACKET_EQ = 7

def product(a):
    return reduce(lambda x, y: x*y, a)

def less_than(a):
    assert len(a) == 2
    return int(a[0] < a[1])

def greater_than(a):
    assert len(a) == 2
    return int(a[0] > a[1])

def equal_to(a):
    assert len(a) == 2
    return int(a[0] == a[1])

OPERATIONS = {
    PACKET_SUM: sum,
    PACKET_PRODUCT: product,
    PACKET_MAXIMUM: max,
    PACKET_MINIMUM: min,
    PACKET_GT: greater_than,
    PACKET_LT: less_than,
    PACKET_EQ: equal_to
}

# ------------------------------------------------------
# Classes

@dataclass
class LiteralPacket:
    version: int
    typeid: int
    value: int

    def solution1(self):
        return self.version

    def solution2(self):
        return self.value

@dataclass
class OperatorPacket:
    version: int
    typeid: int
    subpackets: list

    def solution1(self):
        total = self.version
        for p in self.subpackets:
            total += p.solution1()
        return total

    def solution2(self):
        sub_val = [p.solution2() for p in self.subpackets]
        return OPERATIONS[self.typeid](sub_val)



# ------------------------------------------------------
# Load

def load():
    s = ''
    with io.open(INPUT,'r', encoding='utf-8') as f:
        f.seek(0, io.SEEK_END)
        last = f.tell() - 1
        f.seek(0)
        while f.tell() < last:
            nibble = f.read(8)
            s += hex2raw(nibble)

    return s

# ------------------------------------------------------
#

def bin(s):
   return str(s) if s<=1 else bin(s>>1) + str(s&1)

def hex2raw(h):
    raw = bin(int(h, base=16))
    frame = len(h) * 4
    return raw.zfill(frame)

def get_packet_header(buffer):
    oper = buffer.read(3)
    typeid = buffer.read(3)
    return int(oper, 2), int(typeid, 2)

def parse(buffer):
    version, typeid = get_packet_header(buffer)
    if typeid == PACKET_LITERAL:
        return read_literal(version, typeid, buffer)
    else:
        return read_operator(version, typeid, buffer)

def read_literal(version, typeid, buffer):
    parsing = True
    accum = 0

    while parsing:
        chunk = buffer.read(5)
        parsing &= int(chunk[0])
        accum = (accum << 4) + int(chunk[1:], 2)
        # print('\t', chunk, accum)

    return LiteralPacket(version, typeid, accum)

def read_operator(version, typeid, buffer):
    subs = []

    if buffer.read(1) == '0':
        sub_len = int(buffer.read(15), 2)
        sub_buffer = io.StringIO(buffer.read(sub_len))
        while sub_buffer.tell() < sub_len:
            subs.append(parse(sub_buffer))

    else:
        sub_len = int(buffer.read(11), 2)
        subs = [parse(buffer) for _ in range(sub_len)]

    return OperatorPacket(version, typeid, subs)

# ------------------------------------------------------
# Main

def main():
    packets = []

    # for s, v in SUITE.items():
    #     print(s)
    #     buffer = io.StringIO(hex2raw(s))
    #     head = parse(buffer)
    #     print(head)
    #     print('\t', head.solution2(), v)

    buffer = io.StringIO(load())
    head = parse(buffer)
    print('\t', head.solution2()) # 873

if __name__ == '__main__':
    main()
