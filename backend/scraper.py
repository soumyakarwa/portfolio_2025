#!/usr/bin/env python3
"""
Scraper.py

Fetches the New York Times Hard Sudoku puzzle from
https://www.nytimes.com/puzzles/sudoku/hard and
appends it as a JSON record to DailySudokus.jl.
Written with the help of ChatGPT
"""

import requests
from bs4 import BeautifulSoup
import json
import sys

NYT_URL = "https://www.nytimes.com/puzzles/sudoku/hard"
JL_PATH = "./data/DailySudokus.jl"

def scrape_hard_sudoku(url=NYT_URL):
    resp = requests.get(url)
    resp.raise_for_status()

    # find the <script> with window.gameData
    soup = BeautifulSoup(resp.text, "html.parser")
    script_tag = None
    for script in soup.find_all("script"):
        txt = (script.string or script.get_text() or "")
        if "window.gameData" in txt:
            script_tag = txt
            break
    if not script_tag:
        raise RuntimeError("Could not find the embedded gameData script.")

    # extract the JSON blob
    _, after_eq = script_tag.split("window.gameData", 1)
    json_str = after_eq.split("=", 1)[1].strip().rstrip(";")
    json_str = json_str[: json_str.rfind("}") + 1]

    data = json.loads(json_str)
    hard = data["hard"]
    # metadata
    date_str   = hard.get("print_date") or data.get("displayDate")
    difficulty = hard.get("difficulty", "hard").lower()

    flat = hard["puzzle_data"]["puzzle"]
    if len(flat) != 81:
        raise RuntimeError(f"Expected 81 cells, found {len(flat)}")

    return date_str, difficulty, flat

def record_exists(path, date_str, difficulty):
    """
    Returns True if DailySudokus.jl already has an entry
    for this date & difficulty.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("date") == date_str and rec.get("difficulty") == difficulty:
                    return True
    except FileNotFoundError:
        # no file yet => no record
        return False
    return False

def append_sudoku_record(path, date_str, difficulty, puzzle):
    record = {
        "date":       date_str,
        "difficulty": difficulty,
        "puzzle":     puzzle
    }
    # append one JSON object per line
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    try:
        date_str, difficulty, flat = scrape_hard_sudoku()
        if record_exists(JL_PATH, date_str, difficulty):
            print(f"{difficulty.capitalize()} puzzle for {date_str} is already in {JL_PATH}; skipping.")
            sys.exit(0)
        append_sudoku_record(JL_PATH, date_str, difficulty, flat)
        print(f"Appended {difficulty} puzzle for {date_str} to {JL_PATH}")
    except Exception as e:
        sys.exit(f"Error: {e}")

