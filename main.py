#!/usr/bin/env python3
"""Copy the checked-in poster to the grader's output directory.

Deterministic by design: a plain byte copy, so both sandbox runs write
identical files with no dependence on time, randomness, or the network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
