#!/usr/bin/env python3
"""
Scraper.py
Fetches the New York Times Hard Sudoku puzzle from
https://www.nytimes.com/puzzles/sudoku/hard and prints the grid.
Written with the help of ChatGPT 
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import sys

def scrape_hard_sudoku(url="https://www.nytimes.com/puzzles/sudoku/hard"):
    # 1. Download page
    resp = requests.get(url)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    script_tag = None
    for script in soup.find_all("script"):
        txt = (script.string or script.get_text() or "")
        if "window.gameData" in txt:
            script_tag = txt
            break
    if not script_tag:
        raise RuntimeError("Could not find the embedded gameData script.")

    # Extract the JSON blob...
    _, after_eq = script_tag.split("window.gameData", 1)
    json_str = after_eq.split("=", 1)[1].strip().rstrip(";")
    json_str = json_str[: json_str.rfind("}") + 1]

    game_data = json.loads(json_str)
    flat = game_data["hard"]["puzzle_data"]["puzzle"]
    if len(flat) != 81:
        raise RuntimeError(f"Expected 81 cells, found {len(flat)}")

    return [flat[i*9:(i+1)*9] for i in range(9)]


def print_grid(grid):
    for row in grid:
        # Use '.' for empty cells
        print(" ".join(str(v) if v != 0 else "." for v in row))

if __name__ == "__main__":
    try:
        grid = scrape_hard_sudoku()
        print_grid(grid)
    except Exception as e:
        sys.exit(f"Error: {e}")
