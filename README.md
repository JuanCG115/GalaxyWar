Galaxy's War: A Space Shooter Game with Pygame

This Python script creates a classic space shooter game called "Galaxy's War" using the Pygame library. The player controls a spaceship at the bottom of the screen, shooting down a fleet of enemy aliens that move back and forth and descend toward them. It's a great example of a simple game loop, handling user input, managing game objects, and detecting collisions.

Key Features

- Real-time Gameplay: The main game loop continuously updates the screen, processing player actions and enemy movements for a fluid experience.

- Object Management: The game handles a list of enemies and player projectiles (missiles), dynamically creating and removing them as they are shot or go off-screen. This is more efficient than managing a fixed number of objects.

- Collision Detection: It uses the Pythagorean theorem (via math.sqrt) to calculate the distance between the player's missile and an enemy to check for collisions.

- Dynamic Difficulty: The enemies' horizontal speed gradually increases as the game progresses, making it more challenging over time.

- Sound and Music: The game includes background music and sound effects for missile launches and enemy explosions, enhancing the player's experience.

- User Interface: It displays the current score and a "GAME OVER" message when the player loses.

How to Run the Game

1. Dependencies: Make sure you have Python 3 and the Pygame library installed. You can install Pygame by running:

        Bash
        
        pip install pygame

2. Assets: This game requires several external files (images and sounds). The following files must be in the same directory as the script:

  - Icono.png (game icon)

  - Fondo.png (background image)

  - nave-espacial.png (player's spaceship)

  - astronave.png (enemy spaceship)

  - misil.png (missile)

  - fondo_music.mp3 (background music)

  - disparo.mp3 (missile sound effect)

  - golpe.mp3 (collision sound effect)

  - FreeSansBold.ttf (font file)

3. Run the script: Navigate to the directory in your terminal and execute the script.

        Bash
        
        python your_script_name.py

Gameplay Controls

- Left Arrow Key (K_LEFT): Moves the player's spaceship to the left.

- Right Arrow Key (K_RIGHT): Moves the player's spaceship to the right.

- Spacebar (K_SPACE): Fires a missile.

Code Details

- Initialization: pygame.init() is called at the beginning to initialize all required Pygame modules.

- Game Window: pygame.display.set_mode((800, 600)) creates a window with dimensions of 800x600 pixels.

- Main Loop: The while ejecucion: loop is the heart of the game. It continuously listens for events, updates the game state, and redraws the screen.

- Game Over: The game ends when any enemy reaches a certain vertical position (enemigo_y > 470), causing all enemies to disappear and the "GAME OVER" text to be displayed.

- Function colision_detectada: This function is crucial for gameplay. It uses the math.sqrt() function to calculate the Euclidean distance between two points (the enemy and the missile). If this distance is less than a certain threshold, a collision is registered.
