import io

from dataclasses import dataclass

INPUT = 'input1.txt'

INPUTA = 'D2FE28'
INPUTB = '38006F45291200'
INPUTC = 'EE00D40C823060'
INPUTD = '8A004A801A8002F478'

SUITE = {
    '620080001611562C8802118E34': 16,
    'C0015000016115A2E0802F182340': 23,
    'A0016C880162017C3686B18A3D4780': 31
}

LITERAL_PACKET = 4

# ------------------------------------------------------
# Classes

@dataclass
class LiteralPacket:
    version: int
    typeid: int
    value: int

    def solution1(self):
        return self.version


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
    if typeid == LITERAL_PACKET:
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
    #     print('\t', head.solution1(), v)

    buffer = io.StringIO(load())
    head = parse(buffer)
    print('\t', head.solution1()) # 873

if __name__ == '__main__':
    main()
