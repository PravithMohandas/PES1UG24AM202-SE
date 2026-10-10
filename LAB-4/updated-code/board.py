class Board:
    SIZE = 6

    def __init__(self):
        # Each ship has its own identity and set of occupied cells.
        self._ships = {}
        self.shots = set()
        self.hits = set()
        self._next_ship_id = 1

    @property
    def ships(self):
        """Return all occupied cells, preserving the original Board interface."""
        return set().union(*self._ships.values()) if self._ships else set()

    @property
    def ship_count(self):
        """Number of distinct ships on this board."""
        return len(self._ships)

    @property
    def sunk_ships(self):
        """Names of ships whose every cell has been hit."""
        return {
            name for name, cells in self._ships.items()
            if cells <= self.hits
        }

    def place_ship(self, cells, name=None):
        """Place a distinct ship, rejecting empty or overlapping placements."""
        cells = set(cells)
        if not cells:
            raise ValueError("A ship must occupy at least one cell.")
        if not all(
            isinstance(pos, tuple) and len(pos) == 2
            and all(isinstance(value, int) for value in pos)
            and 0 <= pos[0] < self.SIZE and 0 <= pos[1] < self.SIZE
            for pos in cells
        ):
            raise ValueError("Ship cells must be valid zero-based (row, column) coordinates.")
        if cells & self.ships:
            raise ValueError("Ships cannot overlap.")

        if name is None:
            name = f"Ship {self._next_ship_id}"
            self._next_ship_id += 1
        elif name in self._ships:
            raise ValueError(f"A ship named {name!r} already exists.")

        self._ships[name] = cells
        return name

    def fire(self, pos):
        """Fire once at a valid cell; True=hit, False=miss, None=repeated."""
        if not (
            isinstance(pos, tuple) and len(pos) == 2
            and all(isinstance(value, int) and not isinstance(value, bool) for value in pos)
            and 0 <= pos[0] < self.SIZE
            and 0 <= pos[1] < self.SIZE
        ):
            raise ValueError("Shot must use a valid zero-based (row, column) coordinate.")

        if pos in self.shots:
            return None

        self.shots.add(pos)
        if pos in self.ships:
            self.hits.add(pos)
            return True
        return False

    def ship_sunk_at(self, pos):
        """Return the name of the ship sunk by this shot, or None."""
        for name, cells in self._ships.items():
            if pos in cells and cells <= self.hits:
                return name
        return None

    def all_sunk(self):
        """Return True only when a non-empty fleet has been completely sunk."""
        return bool(self._ships) and len(self.sunk_ships) == len(self._ships)
