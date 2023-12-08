# Overview

<Describe the purpose of this document in 1 paragraph of less ... hint: it isyour SRS>

# Software Requirements

<Describe the structure of this section>

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

### game controls
| ID | Requirement |
| :-------------: | :----------: |
| NFR1 | the game shall have a simple control system |
| NFR2 | the game shall have responsive inputs |
| NFR3 | the game shall start after the intro menu when a key is pressed|
| NFR4 | the game shall exit after the escape key it pressed |
| NFR5 | the game shall allow for the player to use a keypad or mouse to aim |

### Performence
| ID | Requirement |
| :-------------: | :----------: |
| NFR6 | The game resolution shall be 1600x900 |
| NFR7 | The game shall run at a minimum of 50 frames per second. |
| NFR8 | The players health shall be changed when fighting an NPC. |
| NFR9 | The players health shall increase after picking up a med kit.|
| NFR10 | The intro slide shall not drop below 50 frames per second while generating the flame visuals. |

### NPC attributes
| ID | Requirement |
| :-------------: | :----------: |
| NFR11 | The 'guy' NPC type shall 500 health when spawned |
| NFR12 | The 'guy' NPC type shall be the slowest with a speed of 0.05 |
| NFR13 | The 'CyberDemon' NPC type shall have a speed of 0.055 to be the fastest|
| NFR14 | The 'Soldier' NPC type shall have the least health with a starting value of 100 |
| NFR15 | The 'CacoDemon' NPC type shall have an attack distance of 1.0 |

# Software Artifacts

This section contains artifacts that our team has compilied throughout the semester. This will include things like use case diagrams, project plans and links to other material we used for this project.

* [Use Case 1](UseCase1.jpg)
* [Use Case 2](useCase2.jpg)
* [Use Case 3](UseCase3.jpg)

