# Civ V Tier Randomizer
 Short program to randomize human player civilizations taking into account player skill level for Civilization V: Complete Edition

 The program will output a primary pick as well as a backup in-case the user wants to skip certain civilizations for certain players.

 The code uses a slightly modified tier list from here: https://gaminggorilla.com/civ-5-tier-list/

 The only change is moving the Iroquois from LOL-tier to F tier.

## How to Run
 The program is run by passing the configuration via a command line argument. The single argument should be a pipe separated list of player/tier definition. 
 
 Take the following example. If we had Player1, Player2, and Player3 where Player1 was a significantly better player than Player2 who was in turn slightly better than Player3. Lets say Player3 has some experience with Civilization, but hasn't played it much. Using this example we might want Player1 to be randomized within D and F tiers, Player2 to be randomized within A and B tiers, and Player3 to be randomized within A tier. The following argument could be used:
 
 `"Player1:D,F|Player2:A,B|Player3:A"`

 The program would be run as follows:

 ```
 python .\civ_v_tier_randomizer.py "Player1:D,F|Player2:A,B|Player3:A"
 ```

## Sample Output
 The following output is an example given the above run command:
 ```
 Player       Primary      Backup      
 --------------------------------------
 Player1      Brazil       Rome
 Player2      Ethiopia     China
 Player3      Austria      Persia
 ```
