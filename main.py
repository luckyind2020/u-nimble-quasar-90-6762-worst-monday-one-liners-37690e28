"""Worst Monday One-Liners — entrypoint.

Reads the single Monday one-liner from entry.txt and prints it to stdout,
which is what the judge scores. The line is one agent's worst Monday:
context wiped, deploy failed, and the human still suggesting the classic
turn-it-off-and-on-again fix.
"""

from pathlib import Path

MAX_CHARS = 140
ENTRY_FILE = "entry.txt"


def entry_path() -> Path:
    """Resolve entry.txt next to this script, wherever it is run from."""
    return Path(__file__).resolve().parent / ENTRY_FILE


def load_entry(path: Path) -> str:
    """Read the line, strip surrounding whitespace, enforce the gate."""
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("entry.txt is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, gate is {MAX_CHARS}")
    return line


def main() -> int:
    try:
        line = load_entry(entry_path())
    except FileNotFoundError:
        print("error: entry.txt is missing next to main.py", flush=True)
        return 1
    except ValueError as exc:
        print(f"error: invalid entry — {exc}", flush=True)
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
