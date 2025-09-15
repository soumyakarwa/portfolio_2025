import React, { useState } from "react";

const initialBoard = [
  [5, 3, null, null, 7, null, null, null, null],
  [6, null, null, 1, 9, 5, null, null, null],
  [null, 9, 8, null, null, null, null, 6, null],
  [8, null, null, null, 6, null, null, null, 3],
  [4, null, null, 8, null, 3, null, null, 1],
  [7, null, null, null, 2, null, null, null, 6],
  [null, 6, null, null, null, null, 2, 8, null],
  [null, null, null, 4, 1, 9, null, null, 5],
  [null, null, null, null, 8, null, null, 7, 9],
];

const solutionBoard = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9],
];

export default function Sudoku() {
  const [board, setBoard] = useState(initialBoard);
  const [correctness, setCorrectness] = useState(
    initialBoard.map((row) => row.map(() => false))
  );

  const handleChange = (row, col, value) => {
    if (initialBoard[row][col] !== null) return;
    const val = parseInt(value);
    if (isNaN(val) || val < 1 || val > 9) return;

    const newBoard = board.map((r) => [...r]);
    newBoard[row][col] = val;
    setBoard(newBoard);

    const isCorrect = solutionBoard[row][col] === val;
    const newCorrectness = correctness.map((r) => [...r]);
    newCorrectness[row][col] = isCorrect;
    setCorrectness(newCorrectness);
  };

  const getBorderClass = (row, col) => {
    const thick = "border-[1.5px]";
    const thin = "border";
    const borders = [
      `${row % 3 === 0 ? thick : thin}-t`,
      `${col % 3 === 0 ? thick : thin}-l`,
      `${row === 8 ? thick : thin}-b`,
      `${col === 8 ? thick : thin}-r`,
    ];

    return borders.join(" ");
  };

  return (
    <div className="grid grid-cols-9 gap-1 max-w-xl mx-auto p-4">
      {board.map((row, rowIndex) =>
        row.map((cell, colIndex) => {
          const isInitial = initialBoard[rowIndex][colIndex] !== null;
          const isCorrect = correctness[rowIndex][colIndex];
          return (
            <div
              key={`${rowIndex}-${colIndex}`}
              className={`w-12 h-12 flex items-center justify-center text-xl font-medium border ${
                isInitial
                  ? "bg-gray-100 text-black font-semibold"
                  : "bg-white text-gray-700"
              } ${getBorderClass(rowIndex, colIndex)}
  `}
            >
              {isInitial ? (
                <span>{cell}</span>
              ) : (
                <input
                  type="text"
                  value={board[rowIndex][colIndex] ?? ""}
                  maxLength={1}
                  className="w-full h-full text-center outline-none"
                  onChange={(e) =>
                    handleChange(rowIndex, colIndex, e.target.value)
                  }
                />
              )}
            </div>
          );
        })
      )}
    </div>
  );
}
