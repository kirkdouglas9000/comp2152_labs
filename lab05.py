# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions_lab05

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collect Loot
    def collect_loot(x, y):
        print("!!You find a loot bag!! You look inside to find 2 items:")
        input("Roll for first item (Press enter)")
        lootRoll = random.choice(range(1, len(loot_options) + 1))
        loot = x.pop(lootRoll - 1)
        y.append(loot)
        print("Your belt: ", y)

    collect_loot(loot_options,belt)

    # Second time Collecting Loot
    input("Roll for second item (Press enter)")
    lootRoll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(lootRoll - 1)
    belt.append(loot)
    print("Your belt: ", belt)

    # Organize Belt
    print("You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("Your belt: ", belt)

    # Use Loot
    def use_loot(x):
        print("!!You see a monster in the distance! So you quickly use your first item:")
        first_item = belt.pop(0)
        if first_item in good_loot_options:
            x = min(6, (x + 2))
            print("You used " + first_item + " to up your health to " + str(x))
        elif first_item in bad_loot_options:
            x = max(0, (x - 2))
            print("You used " + first_item + " to hurt your health to " + str(x))
        else:
            print("You used " + first_item + " but it's not helpful")
    use_loot(health_points)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")


    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        m_combat_strength) + " using the " + power_roll + " magic power")

    # Fight Sequence
    def hero_attacks(combat_strength, m_health_points):
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                   @@@@@@          @@  @    
                @@       @@        @ @@     
               @%         @     @@@ @       
                @        @@     @@@@@     
                   @@@@@        @@       
                   @    @@@@                
              @@@ @@                        
           @@     @                         
       @@*       @                          
       @        @@                          
               @@                                                    
             @   @@@@@@@                    
            @            @                  
          @              @                  

      """
        print(ascii_image)
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
        if combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            m_health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(m_health_points))
        return m_health_points


    # Monster's Attack Function
    def monster_attacks(m_combat_strength, health_points):
        ascii_image2 = """                                                                 
               @@@@ @                           
          (     @*&@  ,                         
        @               %                       
         &#(@(@%@@@@@*   /                      
          @@@@@.                                
                   @       /                    
                    %         @                 
                ,(@(*/           %              
                   @ (  .@#                 @   
                              @           .@@. @
                       @         ,              
                          @       @ .@          
                                 @              
                              *(*  *      
                 """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if m_combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("    |    Player is dead")

        else:
            # Monster only damaged the player
            health_points -= m_combat_strength
            print("    |    The monster has reduced Player's health to: " + str(health_points))
        return health_points


    # Loop while the monster and the player are alive. Call fight sequence functions
    print("You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:

        attack_roll = random.randint(1, 6)  # Simulating a six-sided dice roll
        print(f"Attack Roll: {attack_roll}")

        if attack_roll in [1, 3, 5]:  # Hero goes first
            health_points=hero_attacks(combat_strength, m_health_points)
            m_health_points=monster_attacks(m_combat_strength, health_points)
        else:  # Monster goes first
            m_health_points=monster_attacks(m_combat_strength, health_points)
            health_points=hero_attacks(combat_strength, m_health_points)


    while True:
        hero_name = input("Enter your Hero's name (in two words): ").strip()
        name_parts = hero_name.split()

        # Ensure exactly two words are entered
        if len(name_parts) != 2:
            print("Please enter exactly two words.")
            continue

        first_name, second_name = name_parts

        # Ensure both names contain only alphabetical characters
        if not (first_name.isalpha() and second_name.isalpha()):
            print("Both parts of the name should only contain alphabetical characters.")
            continue

        # Create the short name using string slicing
        short_name = first_name[:2] + second_name[:1]

        print(f"Hero Name: {hero_name}")
        print(f"Short Name: {short_name}")
        break

    stars = "*" * num_stars
    print("Hero " + short_name + " gets <" + stars + " > stars")