
"""Manage scholarship grants, disbursements, and scheme statistics."""

import sqlite3

# In-memory database for scholarship records.
conn = sqlite3.connect(":memory:")

conn.execute(
    """
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        student TEXT,
        scheme TEXT,
        amount INTEGER,
        disbursed INTEGER
    )
    """
)

DISBURSED_TOTAL = 0


def grant(student, scheme, amount, audit=None):
    """Record a scholarship grant and update the audit list."""
    if audit is None:
        audit = []

    conn.execute(
        """
        INSERT INTO awards (student, scheme, amount, disbursed)
        VALUES (?, ?, ?, 0)
        """,
        (student, scheme, amount),
    )

    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse a scholarship and update the total amount."""
    global DISBURSED_TOTAL

    row = conn.execute(
        "SELECT amount FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()

    if row is not None:
        conn.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?",
            (award_id,),
        )
        DISBURSED_TOTAL += row[0]
        return row[0]

    return None


def archive():
    """Report that scholarship archiving has been requested."""
    print("Archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for a scholarship scheme."""
    if scheme is None:
        return 0

    return conn.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Demonstrate scholarship grants and disbursements."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)

    print(disburse(1), disburse(9))
    print(by_scheme_count("Merit"), DISBURSED_TOTAL)

    archive()


if __name__ == "__main__":
    main()
