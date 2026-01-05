# CPSC-6160-Final-Project
## Chandni Murmu and Alex Schlesener
---------------------------------------------------------

![Alt text](Stuff/images/progress_pics/2D-Game-Design.png)

----------------------------------------------------------
### Instructions
- Download the "zip" folder of this repository.
- To run the game, make sure that Python (3.10.11) and Pygame are installed on your computer.
- Run "candyLand.py"

----------------------------------------------------------
### Game Controls
- Game start: Any key, except the “Esc” key.
- Game stop: “Esc” key.
- Hero movements: Forward (right arrow key), backward (left arrow key), up (up arrow key) and down (down arrow key). Combination of these keys can be pressed together.
 - Hero on collision with the Ally character gains treasure points.
 - Hero on collision with an Enemy character loses treasure points.
 - Hero can jump onto the floating platforms; once the platform ends, the hero falls back to the ground.

----------------------------------------------------------
### Game Design
#### Mechanics and Technology
- What is the gameplay loop of your game?*
 - File name: candyGameLoop.py
 - Display update
 - Candboy movement and background scroll as per his movement
 - Floating block generation and randomization (sprite)
 - Allies (Chocolate, Candy and Ice-cream) generation and randomization (sprite)
 - Enemy (Celery, Tomato, Pumpkin and Bottle Gourd) generation and randomization (sprite)
 - Level score, Total score and Level tracking and updating
 - Collision checks for Candyboy with Allies, Enemies and Level Key and making them disappear from the scene
 - Game music and enemy collision sound effect
- What are the core mechanics of your game, and how do they contribute to the gameplay loop?
 - Candyboy can move up, down, front and back. It contributes 50% of the gameplay loop as most of the game aspects depend on the Candyboy’s position.
 - Floating blocks appear in the scene at random time and random height. Candyboy can move up and land on it, walk on it and if it stays still, it will fall off the edge of the block once the block moves away. It contributes 20% of the gameplay loop as it is the base on which the randomization of allies and enemies has been done. Also, it enables the player to make strategic decisions.
 - Allies and enemies appear randomly on the block and on the ground with their respective animations. If the Candyboy collides with an ally he collects a treasure point and if he collides with an enemy, there is a sound effect, and he loses a treasure point. This contributes 20% of the gameplay loop as it makes the game interesting and challenging.
 - The treasure point represents the treasure (allies) collected and maintained in a level. There is both increment - from allies, and decrement  - from enemies, system to the treasure point, so maintaining it is the challenge. Once the level requirement is met a key appears in the scene. If the Candyboy collects the key before it disappears from the scene he will move to the next level else he will have to wait for another key to appear.
- What is your game’s gimmick and how does it contribute to your game?*
 - Gimmick: This game’s gimmick is the wide range of characters that our hero will interact with throughout the level. These characters are split into two different groups: enemies and allies. The enemies are various types of vegetables. Upon collision with the vegetables (Celery, Tomato, Pumpkin and Bottle Gourd) the user loses treasure points. The allies are various types of sweet things: Ice-cream, Candy and Chocolate. Upon collision with the allies, the user gains treasure points.
 - Contribution: The game’s gimmick contributed as a guide for stepwise design and development of the game which was very helpful in organizing the game aspects into control, view, and model concepts of the 2D game engine construction.
- How does your game differ from other games in the same genre?*
 - Our game differs from other games in the same genre in the following aspects:
  - Characters, Visual, Animations, Score and Level Controls, and Music and sound effects.
- How does your game utilize the strengths of the game engine you're working with?
 - Our game utilize the strengths of the game engine (pygame) in the following ways:
  - We used pygame.init() to initialize all imported pygame modules
  - Used pygame’s time modules for monitoring time and time related triggers. Below are the specific modules used:
   - pygame.time.Clock
   - pygame.time.get_ticks
  - For monitoring interactions with events and queues we used the pygame.event.get module and pygame.KEYDOWN/K_UP/K_DOWN/K_LEFT/K_RIGHT/KEYUP/QUIT/K_ESCAPE for managing various events.
  - For managing and controlling our generative and degenerative characters we used pygame.sprite.GroupSingle and pygame.sprite.Group
  - For handling our music and sound effect content we used modules in pygame.mixer: pygame.mixer.music.load/play/pause/Sound/unpause
  - To control the closing or exiting of the game we used pygame.quit

----------------------------------------------------------
#### Story
- Does your game have a story or theme? What are they?
 - Candyland’s theme is, as expressed in its title, Candy! The story takes place in a land made of candy, where the good guys are made of processed sugars and the bad guys are vegetables. 
- Who is the protagonist of your game, and what is their motivation?
 - That game’s narrative is set from the perspective of our hero character, Candyboy. The hero’s objective is to cross through Candy Land while gathering treasure points from his allies and avoiding interactions with any enemies! Once enough points have been secured, the Candyboy will collect his key and unlock the Candy Shop!
Who or what is the antagonist of your game, and what are their goals?
The antagonists of the game are the vegetables, whose main goal is to remove treasure points from our hero, and keep him from the Candy Shop. 

#### Player Experience
- What emotions do you want the player to experience while playing your game?
 - Ideally, the player will have a lot of fun while playing our game – the graphics are intentionally playful and cute, which will hopefully bring lots of joy to our players.
- What kind of challenges will the player face, and how will they be overcome?*
 - As the levels progress, more and more enemies will enter the scene. In order to avoid the vegetables, the Hero must run through the space and jump onto moving platforms. This process will be tricky for most players, considering it takes some skill to perfectly time these actions. Additionally, while avoiding the vegetables, the Hero character can collide with different candies to gain points and inevitably reach the finish line!
- What kind of rewards will the player receive for progressing through the game?*
 - The rewards system is based on the accumulation of treasure points, which are attained by colliding with Ally characters (i.e. ice cream, lollipops, and chocolate). Once the player has gathered enough points, they can grab the key and go to the next level! After the second level is completed, the player has officially unlocked the Candy Shop, and wins the game!
- What kind of feedback will the player receive while playing the game?*
 - Five different scoreboards are placed on the screen and update throughout the game. The tracked scores include the current level, total score, treasure points, ally appearance, and enemy appearance. The current level is, as suggested by the name, the level that the player is in, at present. The total score incorporates the treasure points across all levels, while the treasure points score is just within the current level. The ally and enemy appearance scores track how many allies/enemies have entered the scene, throughout all levels. 
- What kind of audio and visual elements will enhance the player's experience?*
 - Audio:
  - Background Music:The background music plays throughout the entire game, giving the player an idea of the game’s overall vibe and also creating a highly engaging experience. 
  - Sound Effects: Every time that the player collides with an enemy character, a sound effect will be played. This auditory cue tells the player that they made contact with the enemy and have now lost a point. 
 - Visual: 
  - Animation: All characters in the game have animations, which enhance the player’s experience within the game. All allies hop along, showing that they are currently trapped inside of their candy jar. The enemy characters have different animations based on their type: tall or short. Tall enemies (celery and gourds) hop, whereas short enemies roll. 
  - Scoreboard: The scoreboards frequently update throughout gameplay, alerting the player of their current progress. This feature provides the player with knowledgeable information about their current status, thus enhancing their experience. 
 
----------------------------------------------------------
#### Game Design Changes
This game’s gimmick is the wide range of characters that our hero will interact with throughout the level. These characters are split into two different groups: enemies and allies. The enemies are various types of vegetables, each with their own ways to deplete the hero’s strength. Upon collision with the user, tall vegetables (i.e. Okra, Cucumber, Celery, and Bottle Gourd) knock the user over onto their side. After a couple of seconds, the user is able to get back onto their feet and continue walking. Short vegetables (i.e. Brussel Sprouts, Tomatoes, Potatoes, and Pumpkin.), reduce the user to half speed for a couple of seconds. Additionally, the user has different ways to avoid each of these enemy groups. The hero can squat down to avoid tall vegetables, and jump over short vegetables. 

On the other hand, by breaking open the candy jar, heroes unlock new powers with the help of their allies. Depending on the ally’s type, the user will unlock various powers. Chocolate allies give the user an energy boost (double speed). Ice cream gives the user the ability to walk through enemies without collision. Lollipops restore the hero’s health bar. Each of these actions only last for a few seconds. If the hero is at full health (i.e. the health bar is at 100%), the user cannot use these powers, and will instead collect additional treasure points. 

As mentioned in the design question, most of the game’s gimmick has been implemented as it was proposed. The only change that happened was the diversity of interaction responses of the hero with allies and enemies got replaced by two generic responses: collect and lose treasure points. We decided to do so because we felt managing to complete the entire range of interaction responses in the short duration would be challenging. However, to compensate for that, we added a scoring system, level design and music, which was not in the proposal, in order to give an experience of a complete gameplay.

Even though we were able to implement almost every aspect of our initial game proposal, we did not have time to give each enemy/ally character a different type of interaction response with the hero character. This change was largely due to time constraints. Unfortunately, this implementation would have been a significant undertaking, so we opted out of including those features in the final game, to be able to complete the remaining sections of the game in time.

----------------------------------------------------------
#### Game Development and Documentation
- Main Classes and Major Functionality Methods
 - Classes: GameDisplay, CandyBoy, Block, Ally, Enemy, Topscore and LevelKey
 - Major methods: start_game(), stop_game(), game_loop(), load_*_frames(), *Animation(), draw(), update(), __init__(), currentScore(), allyScore(), enemyScore(), level_count(), totalScore()
[* indicates either ally, enemy or candyBoy]

- Include details on how your game:
 - receives player input (Controller): Through keyboard which are controlled and monitored by pygame modules: pygame.event.get and pygame.KEYDOWN/K_UP/K_DOWN/K_LEFT/K_RIGHT/KEYUP/QUIT/K_ESCAPE stores the state of the game (Model): Different variables are used to store the state of the game. They are:
  - screen: stores the screen’s state as per the game’s progress
  - SCORE: stores the treasure score as per the game scoring system
  - ALLY_COUNT: stores the number of ally sprites generated and appeared on the display
  - ENEMY_COUNT: stores the number of enemy sprites generated and appeared on the display
  - TOTAL_SCORE: stores the total treasure collected in the entire game, irrespective of the level.
  - block_count: keeps track of the block count based on which the allies and enemies appear on the block or on the ground.
  - block_sprites: stores the randomized blocks.
  - ally_sprite: stores the randomized allies.
  - enemy_sprite: stores the randomized enemies.
  - updates the screen/renderer (View): For managing, controlling and updating what would happen to our visual content below modules were used:
  - pygame.Surface: used for different scores display design
  - Pygame.image.load: used for loading all the required images for our characters and visual directions (start and end of the game).
  - Pygame.transform.scale: for scaling the characters as per the required size.
  - Pygame.transform.flip: to flip the images when needed.
  - Pygame.display.set_mode: for the defining and setting the main display.
  - Pygame.display.set_caption: to set the game caption on the display.
  - pygame.font.SysFont: for fonts used in various parts of the game.
  - pygame.Color: to define specific color for the game.
  - blit(): to draw images onto another as per the animation update or game state update.
  - Pygame.display.update: to update display as the game progresses.

- Are there any major bugs or flaws in your game we should be aware of? (Undocumented issues/bugs will result in a score deduction)
 - Level Loading Time: Every time that a new slew of enemy/ally characters and floating platforms are intended to enter the scene, there is a slight delay (30ms-1sec) in gameplay, in which the character and background movement freezes. We attempted troubleshooting this frustrating issue, but could not find an effective solution. 
 - Collision Size: The collision box on enemy characters is sometimes too large, so occasionally the hero character collides with the enemy, even when it has not made direct contact.
 - Flowing Platform Size: Due to inaccurate sizing of the randomized floating platform collision box, sometimes the hero character has the ability to stand slightly above, to the side of, or below the platform. 
 
We used GitHub to collaborate on the project code, and slack or texting to communicate with one another about the project timeline. 

----------------------------------------------------------
Demo Video: https://youtu.be/oP8YvShvUrY
