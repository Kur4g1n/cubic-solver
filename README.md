# Polynomial Equation Solver

A Python package for solving polynomial equations up to 3rd degree with real roots support.

## Prerequisites

- Python 3.13 or higher. Download from [Python Official Downloads](https://www.python.org/downloads/).
- Windows users must use Windows Subsystem for Linux (WSL). Install WSL following the [Microsoft WSL Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install).

## Installation

### Installation on Windows using WSL

1. **Install WSL** following the [official guide](https://learn.microsoft.com/en-us/windows/wsl/install).
2. **Install Python 3.13+** in WSL:

   For Ubuntu-based distributions:

   ```bash
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install python3.13
   ```

3. **Install pip for Python 3.13**:

   ```bash
   curl -sS https://bootstrap.pypa.io/get-pip.py | python3.13
   ```

4. **Install Poetry** for Python 3.13:

   ```bash
   curl -sSL https://install.python-poetry.org | python3.13 -
   ```

   Ensure Poetry is in your PATH:

   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

5. **Clone the repository and install dependencies**:

   ```bash
   git clone https://github.com/kur4g1n/equation-solver.git
   cd equation-solver
   make install
   ```

### General Installation (Linux/macOS)

1. Install Poetry if not already installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Clone repository and install dependencies:

```bash
git clone https://github.com/kur4g1n/equation-solver.git
cd equation-solver
make install
```

## Usage

### Command Line Interface

Basic format:

```bash
A=<a> B=<b> C=<c> D=<d> N_DIGITS=<n_digits> DISPLAY_DIGITS=<display_digits> make run
```

or

```bash
poetry run python3 -m cubic_solver <a> <b> <c> <d> <n_digits> <display_digits>
```

Examples:

```bash
# Solve cubic equation x³ + 2x² + 3x + 4 = 0
poetry run python3 -m cubic_solver 1 2 3 4

# Solve quadratic equation 2x² - 4x + 2 = 0 with accuracy=1e-12
B=2 C=-4 D=2 N_DIGITS=12 DISPLAY_DIGITS=12 make run

# Solve linear equation 3x + 6 = 0
C=3 D=6 make run
```

### Programmatic Usage

```python
from equation_solver import SolverFactory

# Solve 2x² + 4x + 2 = 0
solver = SolverFactory.create_solver(0, 2, 4, 2)
solution = solver.solve()

print(f"Roots: {solution.roots}")  # Access raw roots
print(f"Formatted: {solution}")          # Get human-readable output
```

## Development

### Setup

1. Install development dependencies:

```bash
make install-dev
```

2. Run tests:

```bash
make tests
```

3. List of make commands:

```bash
make help
```
