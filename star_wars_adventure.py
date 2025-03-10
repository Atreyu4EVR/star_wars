#!/usr/bin/env python3

import time
import random
import sys
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_title():
    """Display the game title."""
    title = """
    ███████╗████████╗ █████╗ ██████╗     ██╗    ██╗ █████╗ ██████╗ ███████╗
    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗    ██║    ██║██╔══██╗██╔══██╗██╔════╝
    ███████╗   ██║   ███████║██████╔╝    ██║ █╗ ██║███████║██████╔╝███████╗
    ╚════██║   ██║   ██╔══██║██╔══██╗    ██║███╗██║██╔══██║██╔══██╗╚════██║
    ███████║   ██║   ██║  ██║██║  ██║    ╚███╔███╔╝██║  ██║██║  ██║███████║
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                           
     █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
    ██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
    ███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  
    ██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  
    ██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
    ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """
    print(title)
    print("\n" + "=" * 80)
    typewriter_effect("A long time ago in a galaxy far, far away...", 0.05)
    print("=" * 80 + "\n")

def get_player_choice(options):
    """Get the player's choice from a list of options."""
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("\nEnter your choice (number): "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def game_over(ending):
    """Display game over message with the ending."""
    print("\n" + "=" * 80)
    typewriter_effect(f"GAME OVER: {ending}", 0.05)
    print("=" * 80)
    
    if input("\nPlay again? (y/n): ").lower().startswith('y'):
        start_game()
    else:
        typewriter_effect("Thank you for playing! May the Force be with you.", 0.05)
        sys.exit()

def start_game():
    """Start the adventure game."""
    clear_screen()
    display_title()
    
    # Character selection
    typewriter_effect("Before your adventure begins, you must choose your path in the galaxy...", 0.03)
    time.sleep(1)
    
    character_options = [
        "Jedi Padawan - Strong with the Force, but much to learn you have.",
        "Rebel Pilot - Skilled in combat and navigation, ready to fight the Empire.",
        "Bounty Hunter - No allegiance but to credits, hunting targets across the galaxy."
    ]
    
    print("\nChoose your character:")
    character_choice = get_player_choice(character_options)
    
    if character_choice == 1:
        jedi_path()
    elif character_choice == 2:
        rebel_path()
    else:
        bounty_hunter_path()

def jedi_path():
    """The Jedi Padawan storyline."""
    clear_screen()
    typewriter_effect("\nYou are a Jedi Padawan training at the hidden temple on Dantooine.", 0.03)
    typewriter_effect("The Empire has been hunting down the remaining Jedi for years.", 0.03)
    typewriter_effect("Your master, a wise Twi'lek named Kora Vess, has been teaching you the ways of the Force.", 0.03)
    typewriter_effect("One day, during your meditation, you sense a dark presence approaching the temple...", 0.03)
    
    options = [
        "Alert Master Kora immediately",
        "Investigate the presence yourself",
        "Prepare the temple's defenses"
    ]
    
    print("\nWhat do you do?")
    choice = get_player_choice(options)
    
    if choice == 1:
        jedi_alert_master()
    elif choice == 2:
        jedi_investigate()
    else:
        jedi_prepare_defenses()

def jedi_alert_master():
    """Alert the Jedi Master about the dark presence."""
    clear_screen()
    typewriter_effect("\nYou rush to find Master Kora in the training grounds.", 0.03)
    typewriter_effect("'Master, I sense a dark presence approaching the temple,' you say, trying to remain calm.", 0.03)
    typewriter_effect("Master Kora closes her eyes, reaching out with the Force.", 0.03)
    typewriter_effect("'You have sensed correctly, my Padawan. Imperial Inquisitors have found us.'", 0.03)
    typewriter_effect("'We must act quickly. The future of the Jedi Order may depend on our next move.'", 0.03)
    
    options = [
        "Suggest evacuating the temple",
        "Propose standing and fighting",
        "Recommend hiding and letting them pass"
    ]
    
    print("\nWhat do you suggest to Master Kora?")
    choice = get_player_choice(options)
    
    if choice == 1:
        jedi_evacuate()
    elif choice == 2:
        jedi_stand_fight()
    else:
        jedi_hide()

def jedi_evacuate():
    """Evacuate the Jedi temple."""
    clear_screen()
    typewriter_effect("\n'We should evacuate, Master. We cannot risk losing the younglings or the ancient texts.'", 0.03)
    typewriter_effect("Master Kora nods. 'Wise choice. Our survival is more important than this place.'", 0.03)
    typewriter_effect("You help gather the younglings and the most precious Jedi artifacts.", 0.03)
    typewriter_effect("As you board the hidden escape ships, you hear the sound of Imperial shuttles landing.", 0.03)
    typewriter_effect("Master Kora hands you a holocron. 'Take this to Alderaan. Find Senator Organa.'", 0.03)
    typewriter_effect("'But what about you, Master?' you ask, sensing her intentions.", 0.03)
    typewriter_effect("'I will delay them. This is your first solo mission, Padawan.'", 0.03)
    
    options = [
        "Accept the mission and leave",
        "Refuse to leave without your Master",
        "Suggest an alternative plan"
    ]
    
    print("\nWhat do you do?")
    choice = get_player_choice(options)
    
    if choice == 1:
        game_over("You successfully escape with the younglings and the holocron. Though you mourn Master Kora's sacrifice, you continue your Jedi training and eventually help rebuild the Jedi Order.")
    elif choice == 2:
        game_over("You refuse to leave, and together with Master Kora, you make a valiant stand against the Inquisitors. Though you both perish, your sacrifice allows the younglings to escape and preserve the Jedi legacy.")
    else:
        game_over("Your alternative plan to use decoys works partially. You escape with Master Kora, but the Inquisitors capture the holocron. Your journey continues as you try to recover the lost artifact while evading the Empire.")

def jedi_investigate():
    """Investigate the dark presence yourself."""
    clear_screen()
    typewriter_effect("\nYou decide to investigate the presence yourself, trusting in your training.", 0.03)
    typewriter_effect("Moving silently through the forest surrounding the temple, you follow your Force senses.", 0.03)
    typewriter_effect("Soon, you spot an Imperial shuttle landing in a clearing ahead.", 0.03)
    typewriter_effect("Two figures in black emerge - Imperial Inquisitors, former Jedi turned to the dark side.", 0.03)
    typewriter_effect("They haven't spotted you yet, but they're heading toward the temple.", 0.03)
    
    options = [
        "Return to the temple to warn everyone",
        "Try to distract the Inquisitors away from the temple",
        "Attempt to listen to their plans"
    ]
    
    print("\nWhat do you do?")
    choice = get_player_choice(options)
    
    if choice == 1:
        game_over("You return to warn the temple. With the advance notice, Master Kora organizes a successful evacuation. You escape with the other Jedi, continuing your training in hiding.")
    elif choice == 2:
        game_over("Your attempt to distract the Inquisitors draws their attention. Though you're captured after a fierce lightsaber duel, your sacrifice gives the temple time to evacuate. Years later, you're rescued by the Rebel Alliance.")
    else:
        game_over("You overhear the Inquisitors' plan to capture, not kill, the Jedi for interrogation. With this information, Master Kora devises a trap. The ambush is successful, and you help capture an Inquisitor, gaining valuable intelligence for the growing rebellion.")

def jedi_prepare_defenses():
    """Prepare the temple's defenses."""
    # Implementation left as an exercise
    game_over("You rally the other Padawans to prepare defenses. When the Inquisitors arrive, they're met with unexpected resistance. Though the battle is hard-fought, the temple defenders prevail, and you're recognized for your leadership.")

def jedi_stand_fight():
    """Stand and fight against the Inquisitors."""
    # Implementation left as an exercise
    game_over("You and Master Kora prepare for battle. The confrontation with the Inquisitors is legendary, and though the temple falls, your heroic last stand becomes a symbol of hope for Force users across the galaxy.")

def jedi_hide():
    """Hide from the Inquisitors."""
    # Implementation left as an exercise
    game_over("Your strategy to hide works initially, but the Inquisitors sense the Force users. In the ensuing chaos, you discover a secret passage leading to ancient Jedi ruins with knowledge that could turn the tide against the Empire.")

def rebel_path():
    """The Rebel Pilot storyline."""
    clear_screen()
    typewriter_effect("\nYou are a skilled pilot for the Rebel Alliance, stationed on the ice planet Hoth.", 0.03)
    typewriter_effect("The Empire has been hunting rebel bases across the galaxy, and tensions are high.", 0.03)
    typewriter_effect("During a routine patrol, your scanners detect an unidentified ship approaching the system.", 0.03)
    typewriter_effect("It's not broadcasting any codes - friendly or Imperial.", 0.03)
    
    options = [
        "Report to base and request instructions",
        "Approach the ship to investigate",
        "Hide and observe the ship's actions"
    ]
    
    print("\nWhat do you do?")
    choice = get_player_choice(options)
    
    if choice == 1:
        rebel_report_to_base()
    elif choice == 2:
        rebel_approach_ship()
    else:
        rebel_observe_ship()

def rebel_report_to_base():
    """Report the unidentified ship to rebel base."""
    clear_screen()
    typewriter_effect("\nYou immediately contact Echo Base. 'Command, this is Rogue Seven. Unidentified vessel in sector four.'", 0.03)
    typewriter_effect("'Copy Rogue Seven. Maintain distance and stand by,' responds the controller.", 0.03)
    typewriter_effect("After a tense wait, Command responds: 'Rogue Seven, intelligence suggests it might be a smuggler with vital supplies.'", 0.03)
    typewriter_effect("'However, we can't rule out an Imperial trap. Proceed with caution.'", 0.03)
    
    options = [
        "Escort the ship to a safe distance from the base",
        "Attempt to make contact with the ship",
        "Request backup before approaching"
    ]
    
    print("\nWhat's your next move?")
    choice = get_player_choice(options)
    
    if choice == 1:
        game_over("The ship follows your escort instructions. It turns out to be Han Solo with a shipment of shield generators. Your caution is commended by Alliance leadership.")
    elif choice == 2:
        game_over("You establish contact with the ship. It's a defecting Imperial officer with crucial Death Star plans. Your discovery accelerates the Alliance's victory at the Battle of Yavin.")
    else:
        game_over("Backup arrives, but the ship panics and tries to flee. After a brief pursuit, you discover it was a civilian freighter forced off course. They join the Rebellion after witnessing your professionalism.")

def rebel_approach_ship():
    """Approach the unidentified ship."""
    # Implementation left as an exercise
    game_over("As you approach, the ship identifies itself as a merchant vessel. However, your instincts prove correct when you discover it's smuggling weapons for the Rebellion. Your new alliance with the smuggler provides the base with much-needed supplies.")

def rebel_observe_ship():
    """Observe the unidentified ship's actions."""
    # Implementation left as an exercise
    game_over("Your patience reveals that the ship is being pursued by an Imperial Star Destroyer just outside the system. You warn the base in time, and your intelligence leads to a successful evacuation before the Empire arrives.")

def bounty_hunter_path():
    """The Bounty Hunter storyline."""
    clear_screen()
    typewriter_effect("\nYou are a notorious bounty hunter, known across the Outer Rim for always catching your target.", 0.03)
    typewriter_effect("Your ship, the Crimson Viper, is docked at Mos Eisley spaceport on Tatooine.", 0.03)
    typewriter_effect("You've just received a mysterious transmission offering a job with payment that could set you up for life.", 0.03)
    typewriter_effect("The message is encrypted, but you recognize the Imperial insignia.", 0.03)
    
    options = [
        "Accept the Imperial contract",
        "Ignore it - Imperial entanglements are trouble",
        "Try to trace the message source"
    ]
    
    print("\nWhat do you do?")
    choice = get_player_choice(options)
    
    if choice == 1:
        bounty_hunter_imperial_contract()
    elif choice == 2:
        bounty_hunter_ignore_contract()
    else:
        bounty_hunter_trace_message()

def bounty_hunter_imperial_contract():
    """Accept the Imperial contract."""
    clear_screen()
    typewriter_effect("\nYou decide to accept the contract. Credits are credits, after all.", 0.03)
    typewriter_effect("The encrypted details reveal your target: a former Imperial officer who defected to the Rebellion.", 0.03)
    typewriter_effect("Last seen in the Anoat system, the bounty is five million credits - alive only.", 0.03)
    typewriter_effect("As you prepare your ship, a Rodian approaches. 'I hear you're hunting Verik Tarn.'", 0.03)
    typewriter_effect("'The Rebellion will pay double what the Empire's offering to keep him safe.'", 0.03)
    
    options = [
        "Stick with the Imperial contract",
        "Switch to the Rebellion's offer",
        "Play both sides against each other"
    ]
    
    print("\nWhat do you do?")
    choice = get_player_choice(options)
    
    if choice == 1:
        game_over("You complete the Imperial contract, delivering the defector. Your reputation soars among Imperial clients, leading to more lucrative but increasingly dangerous work for the Empire.")
    elif choice == 2:
        game_over("You switch allegiances to the Rebellion. The defector helps the Alliance destroy a key Imperial shipyard. Though you're now wanted by the Empire, you find unexpected honor among the rebels.")
    else:
        game_over("Your attempt to double-cross both sides is initially successful, but word spreads of your treachery. With both Empire and Rebellion hunting you, you flee to the Unknown Regions, discovering an ancient Sith temple that changes your destiny forever.")

def bounty_hunter_ignore_contract():
    """Ignore the Imperial contract."""
    # Implementation left as an exercise
    game_over("Your instincts prove correct. The contract was a trap set by an old enemy using Imperial codes. Your caution saves your life, and you instead take on a job protecting a moisture farmer who turns out to be force-sensitive.")

def bounty_hunter_trace_message():
    """Trace the source of the mysterious message."""
    # Implementation left as an exercise
    game_over("The trace leads you to a Star Destroyer in orbit around Naboo. Curious, you infiltrate the ship and discover plans for a new superweapon. You sell this information to the highest bidder, making enough credits to retire comfortably.")

if __name__ == "__main__":
    try:
        start_game()
    except KeyboardInterrupt:
        print("\n\nGame terminated. May the Force be with you!")
