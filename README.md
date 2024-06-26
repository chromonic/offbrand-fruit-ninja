### README

# Fruit Ninja Clone

This project is a simple clone of the popular game Fruit Ninja, developed using Python and the Pygame library. The game allows you to slice fruits by clicking on them as they appear on the screen.

## Table of Contents
- [Fruit Ninja Clone](#fruit-ninja-clone)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Files](#files)
    - [`fruit.py`](#fruitpy)
    - [`fruit_slice.py`](#fruit_slicepy)
    - [`main.py`](#mainpy)
  - [Gameplay](#gameplay)
    - [Controls](#controls)
  - [Contributing](#contributing)
    - [Guidelines](#guidelines)
  - [License](#license)

## Installation

### Prerequisites
- Python 3.x
- Pygame

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fruit-ninja-clone.git
    cd fruit-ninja-clone
    ```
2. Install Pygame:
    ```bash
    pip install pygame
    ```

## Usage

To run the game, simply execute the `main.py` file:

```bash
python main.py
```

The game window will open, and you can start playing by slicing fruits with your mouse.

## Files

### `fruit.py`
Defines the `Fruit` class responsible for handling fruit objects, including their positions, velocities, and rendering.

Key methods:
- `__init__`: Initializes the fruit with position, size, and image.
- `update`: Updates the position based on velocity and gravity.
- `render`: Renders the fruit on the provided surface.

### `fruit_slice.py`
Defines the `FruitSlice` class that manages the sliced fruit pieces.

Key methods:
- `__init__`: Initializes the sliced fruit with position, size, and velocity.
- `update`: Updates the position and velocity of the slice.
- `render`: Renders the sliced fruit piece on the provided surface.

### `main.py`
Contains the main application logic, including the game loop.

Key components:
- `App` class: Initializes the game, handles fruit creation, manages game entities, and updates the display.
- `mainloop`: The main game loop that keeps the game running, manages events, updates game state, and renders the frame.

## Gameplay

The objective of the game is to slice as many fruits as possible without missing them. Points are awarded for each fruit you slice. 

### Controls
- Use the left mouse button to slice fruits.
- Avoid missing fruits, as you will lose points or face game-over conditions in future updates.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements. 

### Guidelines
- Follow the PEP 8 coding style.
- Ensure that any new features or changes are well-documented.
- Test your changes thoroughly.

## License

This project is licensed under the MIT License.

---

Enjoy slicing fruits!

---

Feel free to reach out if you have any questions or suggestions. You can contact me at adamabbouatta@google.com.

---

**Note:** Future updates may include additional features such as bombs, different fruit types, and enhanced gameplay mechanics. Stay tuned!

---

**Screenshots and additional gameplay instructions will be added soon.**
