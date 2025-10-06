# Brain Games

[![Actions Status](https://github.com/JulianaCarvajal/python-project-140/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/JulianaCarvajal/python-project-140/actions)
[![Maintainability](https://qlty.sh/gh/JulianaCarvajal/projects/python-project-140/maintainability.svg)](https://qlty.sh/gh/JulianaCarvajal/projects/python-project-140)

A collection of small **command-line brain games** to train logic, code comprehension, and terminal fluency.  
Built as the **first project** of the *Python Developer* course at **Códica** (Module 1).

---

## Games

- 🎲 **Calculator** — Solve simple arithmetic expressions.  
- 🎲 **Progression** — Find the missing number in an arithmetic progression.  
- 🎲 **Even** — Decide whether a number is even.  
- 🎲 **GCD** — Compute the greatest common divisor of two integers.  
- 🎲 **Prime** — Decide whether a number is prime.

---

## Minimum Requirements

- **Python**: 3.12
- **OS**: Linux, macOS, or Windows
- **Package manager**: [`uv`](https://github.com/astral-sh/uv)  

---

## Installation (with `uv`)

If you don’t have `uv`:

**macOS/Linux**
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**
```sh
irm https://astral.sh/uv/install.ps1 | iex
```

Clone and set up the environment:

```sh
git clone https://github.com/JulianaCarvajal/python-project-140.git
cd python-project-140
uv sync
```

This creates a local virtual environment and installs dependencies.

## Usage

You can run the console scripts directly (after `uv sync`):

```sh
uv run brain-games
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-prime
uv run brain-progression
```

### What each command does

* `brain-games` – welcome screen
* `brain-even` – answer “yes” if the shown number is even, otherwise “no”.
* `brain-calc` – compute the result of an arithmetic expression.
* `brain-gcd` – find the greatest common divisor of two integers.
* `brain-prime` – answer whether a number is prime.
* `brain-progression` – find the missing number in a progression.

## Demos (asciinema)

Each demo shows the flow of playing a game (with a success and a failure example)

### brain-even demo
[![asciicast](https://asciinema.org/a/47No2W25oifrtUCMEbSHsIzaZ.svg)](https://asciinema.org/a/47No2W25oifrtUCMEbSHsIzaZ)

### brain-calc demo
[![asciicast](https://asciinema.org/a/ZLri1bXO9Cq8JfXDpwWDugIOO.svg)](https://asciinema.org/a/ZLri1bXO9Cq8JfXDpwWDugIOO)

### brain-gcd demo
[![asciicast](https://asciinema.org/a/45zOPIzjOzZ31m40vHZ8mBJXK.svg)](https://asciinema.org/a/45zOPIzjOzZ31m40vHZ8mBJXK)

### brain-progression demo
[![asciicast](https://asciinema.org/a/TVgu7kz3qs2nicLQ112ZNO7mN.svg)](https://asciinema.org/a/TVgu7kz3qs2nicLQ112ZNO7mN)

### brain-prime demo
[![asciicast](https://asciinema.org/a/81ovNN6Q8M8YraVZwej0M3GKH.svg)](https://asciinema.org/a/81ovNN6Q8M8YraVZwej0M3GKH)

## Example (GCD)

```yaml
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!
Question: 100 52
Your answer: 4
Correct!
Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!
```

Failure case:

```
Question: 25 50
Your answer: 1
'1' is wrong answer ;(. Correct answer was '25'.
Let's try again, Sam!
```

## Project Structure

```
python-project-140/
├── brain_games/                
│   ├── __init__.py
│   ├── games/                  
│   │   ├── calc.py
│   │   ├── even.py
│   │   ├── gcd.py
│   │   ├── prime.py
│   │   └── progression.py
│   └── cli.py
├── scripts/                   
│   ├── brain-calc
│   ├── brain-even
│   ├── brain-games
│   ├── brain-gcd
│   ├── brain-prime
│   └── brain-progression
├── pyproject.toml              
├── ruff.toml                
├── .python-version           
├── .gitignore
├── Makefile
└── README.md
```
