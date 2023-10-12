# Overview

This document contains lists of requirements which are specifications of what we want to be implemented in our game. Our requirements describe how the system should behave and what attributes it will have. Here we have listed function requirements which are behavioral requirements that the user can preform while playing the game. The non-functional requirements describe qualities that the system should have and contraints that are implemented

# Functional Requirements

1. Player Movement
    1. The player shall move forward when the user presses w.
    2. The Player shall melee the enemey when the user presses E.

2. Interface
    1. The game shall have a scoreboard to track progress
    2. The game shall have a starting menu

3. In-game orientation
    1. The player's in-game orientation shall be synchronized with the position of the on-screen cursor controlled by the mouse.

4. Colliding
    1. The player shall not be able to walk through a live enemy.

5. Player Health
    1. The player shall regain health when walking over a health pack.
    2. When the player health hits zero the game shall restart.

# Non-Functional Requirements

1. Performance
    1. The game resoultion shall be 1600x900.
    2. The game shall run at 60FPS.
    3. The user controls shall be intuitive and easy to learn

2. Enviornment
    1. The game shall appear as a 3D enviornment
  
3. Health pack
    1. Walking over a health pack shall return 25-100% of the players current health back to them.

4. Enemy Collision
    1. Colliding with a live enemy shall cause the player to lose 25% of their current health.

5. Bullet Collision
    1. When the player shoots their gun and a bullet collides with a live enemy the enemy shall lose 50 health.
