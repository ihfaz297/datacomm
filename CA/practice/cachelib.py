# cachelib.py — tiny cache simulator used by the drills' checkers.
# You can also use it directly to check ANY trace from a question:
#
#   python CA/practice/cachelib.py
#
# and edit the demo at the bottom. Don't open this before you've tried the drills by hand.

_score = [0, 0]


def check(name, got, expected, tol=0.01):
    """PASS/FAIL printer for drills. Blank answers (None / ...) are skipped, not spoiled."""
    _score[1] += 1
    if got is None or got is ...:
        print(f"[ TODO ] {name}")
        return
    if isinstance(expected, float) or isinstance(got, float):
        ok = abs(float(got) - float(expected)) <= tol * max(1.0, abs(float(expected)))
    elif isinstance(expected, str):
        ok = str(got).strip().lower() == expected.lower()
    else:
        ok = got == expected
    if ok:
        _score[0] += 1
        print(f"[ PASS ] {name}")
    else:
        print(f"[ FAIL ] {name}: you said {got!r}, expected {expected!r}")


def score():
    print(f"\n{_score[0]}/{_score[1]} correct")


def split(addr, offset_bits, index_bits):
    """Return (tag, index, offset) of a byte/word address."""
    offset = addr & ((1 << offset_bits) - 1)
    index = (addr >> offset_bits) & ((1 << index_bits) - 1)
    tag = addr >> (offset_bits + index_bits)
    return tag, index, offset


def simulate(addrs, n_blocks, block_size=1, ways=1, initial=None):
    """Set-associative cache with LRU. ways=1 -> direct mapped, ways=n_blocks -> fully associative.
    addrs are in the same unit as block_size (bytes if block_size is in bytes).
    initial: dict {set_index: [tag, ...]} (LRU order: oldest first).
    Returns list of (addr, block_addr, set, tag, 'hit'/'miss', evicted_block_or_None) and final sets."""
    n_sets = n_blocks // ways
    sets = {s: list((initial or {}).get(s, [])) for s in range(n_sets)}
    log = []
    for a in addrs:
        blk = a // block_size
        s = blk % n_sets
        tag = blk // n_sets
        lines = sets[s]
        if tag in lines:
            lines.remove(tag); lines.append(tag)
            log.append((a, blk, s, tag, "hit", None))
        else:
            ev = None
            if len(lines) == ways:
                old = lines.pop(0)
                ev = old * n_sets + s
            lines.append(tag)
            log.append((a, blk, s, tag, "miss", ev))
    return log, sets


def write_policy(ops, allocate):
    """Fully associative, 'many entries' (never evicts), starts empty unless ops says otherwise.
    ops: list of ('R'|'W', addr). Reads always allocate. Writes allocate only if allocate=True."""
    cache, out = set(), []
    for op, a in ops:
        if a in cache:
            out.append("hit")
        else:
            out.append("miss")
            if op == "R" or allocate:
                cache.add(a)
    return out


if __name__ == "__main__":
    # Demo: textbook Fig 5.6 trace (8-block direct-mapped, 1-word blocks)
    log, _ = simulate([22, 26, 22, 26, 16, 3, 16, 18, 16], n_blocks=8)
    for a, blk, s, tag, hm, ev in log:
        print(f"{a:3d} = {a:05b}  index={s:03b} tag={tag:02b}  {hm}" + (f"  (evicts block {ev})" if ev is not None else ""))
