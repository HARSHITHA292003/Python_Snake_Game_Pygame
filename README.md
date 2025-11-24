# Python_Snake_Game
A classic Snake Game implemented using Python and Pygame. The player controls a snake that moves around the screen, eats food to grow longer, and must avoid hitting the walls or itself. The game increases in length as you eat more food, and ends when the snake crashes.

## 🔧 Software Components
| Component | Description |
|----------|-------------|
| Python 3.x | Programming language used |
| Pygame Module | Used for graphics, input, and game loop |
| snake_game.py | Main game script |
| Terminal / Pygame Window | Game interface |

## 🧠 Working Principle

### Snake Movement
The snake moves in fixed-size blocks (10x10). The player controls direction using:
- Arrow Keys → Move Up, Down, Left, Right

### Food Generation
Food appears at random positions on the screen.  
When the snake reaches the food:
- Snake length increases  
- New food is generated  

### Collision Detection
Game ends when:
- Snake hits screen border  
- Snake hits itself  

### Display
- Snake → Green blocks  
- Food → White block  
- Background → Black  
- Game Over Screen → Message with Q/Quit or C/Restart  

## 📂 Project Structure
| File | Description |
|------|-------------|
| snake_game.py | Python code for the Snake game |
| README.md | Documentation file |

## 📝 Game Loop Summary
The Python script:
- Handles user keyboard input  
- Moves snake based on direction  
- Checks for collisions  
- Generates food positions  
- Updates snake length  
- Renders game using Pygame  

## 🔌 How to Run
Install pygame if not installed:
pip install pygame



Run the game:
<img width="945" height="471" alt="SNAKE_GAME" src="https://github.com/user-attachments/assets/0b103db0-8e43-40b8-a8d6-ddadf91867c4" />


## 🚀 Future Enhancements
- Add score display  
- Add increasing speed  
- Add sound effects  
- Improve graphics with images  
- Add pause/resume feature  

## 👩‍💻 Author
Developed by **HARSHITHA ARUNACHALA**  
Undergraduate Student, B.E. Electronics and Communication Engineering (ECE)  
GitHub: **@HARSHITHA292003**

