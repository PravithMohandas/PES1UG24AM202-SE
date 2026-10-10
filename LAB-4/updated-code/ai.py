import random


class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.hits = set()

    def choose(self):
        """Choose an untried cell, preferring neighbors of previous hits.

        Returns a zero-based (row, column) tuple, or None when no cells remain.
        The selected cell is immediately recorded in tried.
        """
        options = {
            (r, c)
            for r in range(self.size)
            for c in range(self.size)
            if (r, c) not in self.tried
        }
        if not options:
            return None

        adjacent = set()
        for r, c in self.hits:
            adjacent.update({
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            })

        # Keep only valid, untried orthogonal neighbors of known hits.
        targets = adjacent & options
        targets = {
            (r, c) for r, c in targets
            if 0 <= r < self.size and 0 <= c < self.size
        }

        pos = random.choice(sorted(targets or options))
        self.tried.add(pos)
        return pos

    def record_result(self, pos, hit):
        """Record a successful hit so the next choice can target its neighbors."""
        if hit:
            self.hits.add(pos)
