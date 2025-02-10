# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []
bad_loot_options = ["Poison Potion"]
good_loot_options = ["Health Potion", "Leather Boots"]
big_dice_options = list(range(1, 21))
health_points = random.choice(big_dice_options)

def use_loot(x):
    print("!!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(6, (x + 2))
        print("You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (x - 2))
        print("You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("You used " + first_item + " but it's not helpful")

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")



def collect_loot(x=loot_options, y=belt):
    print("!!You find a loot bag!! You look inside to find 2 items:")
    input("Roll for first item (Press enter)")
    lootRoll = random.choice(range(1, len(loot_options) + 1))
    loot = x.pop(lootRoll - 1)
    y.append(loot)
    print("Your belt: ", belt)



# Hero's Attack Function
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
