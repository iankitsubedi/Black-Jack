# 🃏 Simple Blackjack Game (Python)

This is a simple text-based Blackjack game written in Python.  
It allows you to play against the computer with basic Blackjack rules.

---

## 🎮 Features

- Draw random cards from a deck.
- Ace card automatically counts as **11** if it doesn't bust your hand, otherwise as **1**.
- Player can:
  - Hit (draw a new card).
  - Pass (stand and end turn).
- Computer draws cards automatically after player passes.
- Score comparison at the end to determine the winner.
- Option to play multiple rounds.

---

## 📋 How To Play

1. Run the program.
2. You will receive two random cards.
3. Decide whether to:
   - `'y'` → Hit (get another card)
   - `'n'` → Pass (end your turn)
4. The computer will then draw cards.
5. Whoever gets closer to 21 without going over wins!

---

## 💡 Rules:
- Face cards (Jack, Queen, King) are worth 10.
- Ace counts as **11** unless it would cause you to bust (then it counts as 1).
- If you or the computer hits exactly 21, it's an automatic win for that hand.
- If both stand, higher score wins. Tie if both have the same score.
- Dealer draws cards until their total is at least 21.

---

## 🛠️ Requirements

- Python 3.x (no external libraries needed — uses `random` module).

---

## 📂 Files

- `blackjack.py` → Main game script.

---

## ✅ Notes

- This project is for fun and learning purposes.
- The game runs in the terminal/command prompt.
- You can customize or improve it further if you'd like!

---

## 🚀 How To Run

```bash
python blackjack.py
