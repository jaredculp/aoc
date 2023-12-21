from abc import ABC, abstractmethod
from collections import deque

DEBUG = 0


class Component(ABC):
    def __init__(self, name):
        self.name = name
        self.ins = []
        self.outs = []

    def connect_out(self, o):
        self.outs.append(o)
        o._connect_in(self)

    def _connect_in(self, o):
        self.ins.append(o)

    @abstractmethod
    def recv(self, in_=None, pulse=None):
        pass

    def _send(self, out, pulse):
        if DEBUG:
            pulse_str = {0: "low", 1: "high"}[pulse]
            print(f"{self} -{pulse_str}-> {out}")
        Q.append((self, out, pulse))

    def __repr__(self):
        return self.name


class Broadcaster(Component):
    def __init__(self):
        super().__init__("broadcaster")

    def recv(self, _, pulse):
        for o in self.outs:
            self._send(o, pulse)


class FlipFlop(Component):
    def __init__(self, name):
        super().__init__(name)
        self.state = 0

    def recv(self, _, pulse):
        if pulse == 0:
            self.state = ~(self.state ^ pulse) & 1
            for o in self.outs:
                self._send(o, self.state)


class Conjunction(Component):
    def __init__(self, name):
        super().__init__(name)
        self.in_states = {}

    def _connect_in(self, o):
        super()._connect_in(o)
        self.in_states[o] = 0

    def recv(self, in_, pulse):
        self.in_states[in_] = pulse
        for o in self.outs:
            pulse = ~all(self.in_states.values()) & 1
            self._send(o, pulse)


class Debug(Component):
    def __init__(self, name):
        super().__init__(name)

    def recv(self, *_):
        pass


N: dict[str, Component] = {}
input = [x.strip() for x in open("2023/inputs/20.txt").readlines()]

# first pass over input, create components
for line in input:
    module, _ = line.split(" -> ")
    match module[0], module[1:]:
        case "b", "roadcaster":
            module_type = Broadcaster()
        case "%", module:
            module_type = FlipFlop(module)
        case "&", module:
            module_type = Conjunction(module)
        case _:
            raise ValueError()

    N[module] = module_type

# second pass over input, connect components
for line in input:
    module, dst_modules = line.split(" -> ")
    if module != "broadcaster":
        module = module[1:]
    for dst_module in dst_modules.split(", "):
        if dst_module not in N:
            N[dst_module] = Debug(dst_module)
        N[module].connect_out(N[dst_module])

# run BFS on the network, recording low and high pulses
L = 0
H = 0
Q = deque()
for _ in range(1000):
    Q.append((None, N["broadcaster"], 0))
    while Q:
        in_, out, pulse = Q.popleft()
        if pulse == 0:
            L += 1
        if pulse == 1:
            H += 1
        N[out.name].recv(in_, pulse)

print(L, H, L * H)
