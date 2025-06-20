# Secret_Auction_Project
A fun and interactive Python console app that simulates a secret auction. Users enter bids anonymously, and the program reveals the highest and lowest bidders at the end. Includes input validation, ASCII art banners, and loop-based control for multiple entries.

# 🕵️‍♂️ The Secret Auction Project

This is a beginner-friendly Python console application that simulates a **secret auction**. Participants enter their name and bid in secret. At the end, the program reveals the **highest** and **lowest** bidders. It's a fun way to practice loops, dictionaries, input handling, and basic logic in Python!

---

## 🎯 Features:

- Accepts multiple user bids in a loop
- Tracks all bidders and their amounts
- Identifies both **highest** and **lowest** bidder
- Validates user input (ensures bid is an integer)
- Uses ASCII art for a fun, polished terminal experience
- Cleans up the screen between entries to keep it secret

---

## 🚀 How to Run:

1. Make sure Python 3 is installed.
2. Clone this repository or download the `.py` file.
3. Open a terminal and run.

## 🧠 How It Works:

- Each bidder is prompted for their name and bid amount.
- After each entry, the screen clears (via blank lines) to simulate secrecy.
- When bidding ends, the app prints:
    - The highest bidder and their amount.
    - The lowest bidder and their amount.

## 💡 Sample Run:

1. What is your name?: Alice
2. What is your bid?: $150
3. Are there any other bidders? Type 'yes' or 'no':
4. yes

5. [screen clears]

6. What is your name?: Bob
7. What is your bid?: $200
8. Are there any other bidders? Type 'yes' or 'no':
9. no

10. The winner (highest bidder) is Bob with a bid of $200
11. The lowest bidder is Alice with a bid of $150
12. Goodbye!


## 🧰 Concepts Used:

- Loops and conditionals
- Dictionaries for data storage
- Input validation (try/except)
- Functions with parameters
- ASCII art for UI polish
