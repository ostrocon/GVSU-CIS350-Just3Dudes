# Overview

This document contains lists of requirements which are specifications of what we want to be implemented in our game. Our requirements describe how the system should behave and what attributes it will have. Here we have listed function requirements which are behavioral requirements that the user can preform while playing the game. The non-functional requirements describe qualities that the system should have and contraints that are implemented

# Software Requirements

The functional requirements are first and they all have a unique id with FR1, FR2, etc. Then the Non-functional requirements are also labled uniquely with NFR1, NFR2, etc. Both sections have a feature that is followed by five requirements.  

## Functional Requirements

### Player Movement
| ID | Requirement |
| :-------------: | :----------: |
| FR1 | The player shall move forward when the user presses the  w key. |
| FR2 | The player shall move left when the user presses the a key. |
| FR3 | The player shall move right when the user presses the d key. |
| FR4 | The player shall move backwards when the user presses the s key. |
| FR5 | The player shall look left and right when the user moves their cursor left and right respectively. |

### Interface
| ID | Requirement |
| :-------------: | :----------: |
| FR6 | The game shall show players current health at the top left of the game screen. |
| FR7 | The game shall have a starting menu that starts when the up arrow key is clicked. |
| FR8 | The game shall show a You Win screen when all the enemies are defeated. |
| FR9 | The game shall show a Game Over Screen when the player is defeated. |
| FR10 | The game shall show a score on the you win screen that is equal to the number of enemies defeated. |

### Terrain
| ID | Requirement |
| :-------------: | :----------: |
| FR11 | The player shall not be able to shoot through walls. |
| FR12 | The player shall be able to walk through sprites like lamps but not walls. |
| FR13 | The enemies shall not be able to shoot through walls. |
| FR14 | When the player walks over a health pack it shall disappear and be used. |
| FR15 | When the player walks over a weapon they shall pick it up. |

## Non-Functional Requirements

### Sprites
| ID | Requirement |
| :-------------: | :----------: |
| NFR1 | The sprite scale shall be below 3 to maintain stable frames. |
| NFR2 | The pickup sprites like guns and medkit shall have specific ground level, height, and render distance variables to keep fps stable. |
| NFR3 | The random sprite placement shall not spawn out of bounds. |
| NFR4 | The random sprites placement shall not fill entire row and column range. |
| NFR5 | The spirtes shall be oriented towards the player to prevent having to render 3d objects. |

### Performance
| ID | Requirement |
| :-------------: | :----------: |
| NFR6 | The game resolution shall be 1600x900. |
| NFR7 | The game shall run at a minimum of 50 frames per second. |
| NFR8 | The game shall keep stable fps when the player faces right against the wall. |
| NFR9 | The depth of the game shall be 40 to maintain stable frames.|
| NFR10 | The intro slide shall not drop below 50 frames per second while generating the flame visuals. |

### NPC Attributes
| ID | Requirement |
| :-------------: | :----------: |
| NFR11 | The 'guy' NPC type shall have 500 health when spawned. |
| NFR12 | The 'guy' NPC type shall be the slowest with a speed of 0.05 |
| NFR13 | The 'CyberDemon' NPC type shall have a speed of 0.055 to be the fastest|
| NFR14 | The 'Soldier' NPC type shall have the least health with a starting value of 100 |
| NFR15 | The 'CacoDemon' NPC type shall have an attack distance of 1.0 |

# Software Artifacts

This section contains artifacts that our team has compilied throughout the semester. This will include things like use case diagrams, project plans and links to other material we used for this project.

* [Use Case 1](UseCase1.jpg)
* [Use Case 2](useCase2.jpg)
* [Use Case 3](UseCase3.jpg)

