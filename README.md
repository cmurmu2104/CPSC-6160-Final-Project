# CPSC-6160-Final-Project
## Chandni Murmu and Alex Schlesener
---------------------------------------------------------

![Alt text](Stuff/images/progress_pics/2D-Game-Design.png)
 
 ** Important: to run game, use candyLand.py **
----------------------------------------------------------
### Changes to Game and Development Design
- Game Gimmicks: As such there are no changes to the game gimmicks, however, anticipating the time and effort required we may reduce the number of types of allies and enemies.
- Game Mechanics: There might be reduction in different types of ally and enemy movement depending on, if we have to, dropped ally and enemy.
- Game Architecture: No change in this.
- User Interface: No change in this.
- Game Engine: No change in this.

### How has your game evolved since you started working on it?
- Game Architecture:
    - The game architecture consists of two separate entities: background and characters. 
        - Background:
            - The landing screen is set and working, where the player presses any key to start the game.
            - The initial setting of the background with the initial treasure point is done, which appears when the player starts the game.
        - Character:
            - Our hero, Candy Boy, character now appears in the display and is able to move forward (right arrow), backward (left arrow), up (up arrow) and down (down arrow).
        - Ally character, Ice-cream in a jar, appears in  the display with a bouncing movement.
        - Enemy character, Celery, appears in  the display with a bouncing movement.

- User Interface
    - The implemented user interface that is controlled by the user is mostly keyboard inputs:
        - Game start: Any key, except the “Esc” key.
        - Game stop: “Esc” key.
        - Hero movements: Forward (right arrow key), backward (left arrow key), up (up arrow key) and down (down arrow key). Combination of these keys can be pressed together.

- Game Engine
    - The components covered for the Game Engine consists of three main components: model, view, and control.
        - Model: Game start, Game stop, Treasure Points, Game display update, Hero, Ally and Enemy definitions and state updates.
        - View: Game display definition
        - Control: Game loop with player inputs and game updates happening according to those inputs.

### An updated version of our project timeline
- Updated Project Timeline: 
    - Milestone 2: April 12
        - Milestone tasks
            - Alex: 
                - Complete the remaining hero character movement and animation.
                - Complete collision animation and movement design.
            - Chandni: 
                - Complete ally and enemy movement with collision impact and scoreboard updates. Integrate images into the game.
                - Finish character images and animation. Make sure the game runs smoothly.
            - Both: Update Game Document
    - Final Game Submission: April 26
        - Both: Completed and polished game
        - Both: Completed Game Document game

### What tasks have been postponed or moved up?
- Ally: Collision. collision impact and randomization.
- Enemy: Collision, collision impact and randomization.
- Treasure Points: points collection and update .
- Environment: Illusion of a long environment until the hero finds the key to the next level.

### Any technical challenges you and your team have encountered:
- FPS value was causing display blinking (Resolved)
- Previous frame was not getting removed (Resolved using blit)

### How will these challenges impact your development timeline?
Previous challenges have been resolved. However, we anticipate that we may face new challenges as our game becomes more complex. Then we will make modifications accordingly, if necessary, but will make sure that the core of the game design is met.

### Will your final game design need to change?
We feel that our game development is making good progress and the final game design could remain as it was defined in Milestone 1.



