def get_game_data():
    """Return the game data structure with all scenes, choices, and character information."""
    return {
        "characters": {
            "jedi": {
                "id": "jedi",
                "name": "Jedi Padawan",
                "description": "Strong with the Force, but much to learn you have.",
                "image": "static/images/padawan.png",
                "first_scene": "jedi_start"
            },
            "rebel": {
                "id": "rebel",
                "name": "Rebel Pilot",
                "description": "Skilled in combat and navigation, ready to fight the Empire.",
                "image": "static/images/rebel_pilot.png",
                "first_scene": "rebel_start"
            },
            "bounty_hunter": {
                "id": "bounty_hunter",
                "name": "Bounty Hunter",
                "description": "No allegiance but to credits, hunting targets across the galaxy.",
                "image": "static/images/bounty_hunter.jpg",
                "first_scene": "bounty_hunter_start"
            }
        },
        "scenes": {
            # Jedi Padawan storyline
            "jedi_start": {
                "title": "The Hidden Temple",
                "description": [
                    "You are a Jedi Padawan training at the hidden temple on Dantooine.",
                    "The Empire has been hunting down the remaining Jedi for years.",
                    "Your master, a wise Twi'lek named Kora Vess, has been teaching you the ways of the Force.",
                    "One day, during your meditation, you sense a dark presence approaching the temple..."
                ],
                "background": "static/images/jedi_temple.jpg",
                "choices": [
                    {
                        "text": "Alert Master Kora immediately",
                        "next_scene": "jedi_alert_master"
                    },
                    {
                        "text": "Investigate the presence yourself",
                        "next_scene": "jedi_investigate"
                    },
                    {
                        "text": "Prepare the temple's defenses",
                        "next_scene": "jedi_prepare_defenses"
                    }
                ]
            },
            "jedi_alert_master": {
                "title": "Warning the Master",
                "description": [
                    "You rush to find Master Kora in the training grounds.",
                    "'Master, I sense a dark presence approaching the temple,' you say, trying to remain calm.",
                    "Master Kora closes her eyes, reaching out with the Force.",
                    "'You have sensed correctly, my Padawan. Imperial Inquisitors have found us.'",
                    "'We must act quickly. The future of the Jedi Order may depend on our next move.'"
                ],
                "background": "static/images/jedi_master.jpg",
                "choices": [
                    {
                        "text": "Suggest evacuating the temple",
                        "next_scene": "jedi_evacuate"
                    },
                    {
                        "text": "Propose standing and fighting",
                        "next_scene": "jedi_stand_fight"
                    },
                    {
                        "text": "Recommend hiding and letting them pass",
                        "next_scene": "jedi_hide"
                    }
                ]
            },
            "jedi_evacuate": {
                "title": "Evacuation",
                "description": [
                    "'We should evacuate, Master. We cannot risk losing the younglings or the ancient texts.'",
                    "Master Kora nods. 'Wise choice. Our survival is more important than this place.'",
                    "You help gather the younglings and the most precious Jedi artifacts.",
                    "As you board the hidden escape ships, you hear the sound of Imperial shuttles landing.",
                    "Master Kora hands you a holocron. 'Take this to Alderaan. Find Senator Organa.'",
                    "'But what about you, Master?' you ask, sensing her intentions.",
                    "'I will delay them. This is your first solo mission, Padawan.'"
                ],
                "background": "static/images/jedi_evacuation.jpg",
                "choices": [
                    {
                        "text": "Accept the mission and leave",
                        "next_scene": "jedi_accept_mission"
                    },
                    {
                        "text": "Refuse to leave without your Master",
                        "next_scene": "jedi_refuse_to_leave"
                    },
                    {
                        "text": "Suggest an alternative plan",
                        "next_scene": "jedi_alternative_plan"
                    }
                ]
            },
            "jedi_accept_mission": {
                "title": "A New Journey",
                "description": [
                    "With a heavy heart, you accept the holocron and board the ship with the younglings.",
                    "As your ship lifts off, you see Master Kora ignite her lightsaber to face the approaching Inquisitors.",
                    "The journey to Alderaan is long, but you successfully deliver the holocron to Senator Organa.",
                    "Though you mourn Master Kora's sacrifice, you continue your Jedi training.",
                    "Years later, you help rebuild the Jedi Order from the ashes of the Empire."
                ],
                "background": "static/images/jedi_alderaan.jpg",
                "ending": "You successfully escape with the younglings and the holocron. Though you mourn Master Kora's sacrifice, you continue your Jedi training and eventually help rebuild the Jedi Order."
            },
            "jedi_refuse_to_leave": {
                "title": "The Last Stand",
                "description": [
                    "'I will not leave you, Master,' you say, igniting your lightsaber.",
                    "Master Kora looks at you with pride. 'Then we stand together.'",
                    "You help the younglings escape while preparing for battle.",
                    "When the Inquisitors arrive, you and Master Kora fight with everything you have.",
                    "Though you both fall in battle, your sacrifice allows the younglings to escape with the sacred knowledge."
                ],
                "background": "static/images/jedi_battle.jpg",
                "ending": "You refuse to leave, and together with Master Kora, you make a valiant stand against the Inquisitors. Though you both perish, your sacrifice allows the younglings to escape and preserve the Jedi legacy."
            },
            "jedi_alternative_plan": {
                "title": "The Decoy",
                "description": [
                    "You suggest using decoys to confuse the Inquisitors while you escape with the real holocron.",
                    "The plan works partially - you and Master Kora escape, but the Inquisitors capture one of the decoy holocrons.",
                    "Now you must recover the real artifact while evading the Empire's forces.",
                    "Your journey continues as you and Master Kora become hunted across the galaxy."
                ],
                "background": "static/images/jedi_escape.jpg",
                "ending": "Your alternative plan to use decoys works partially. You escape with Master Kora, but the Inquisitors capture the holocron. Your journey continues as you try to recover the lost artifact while evading the Empire."
            },
            
            # More Jedi scenes...
            "jedi_investigate": {
                "title": "Into the Forest",
                "description": [
                    "You decide to investigate the presence yourself, trusting in your training.",
                    "Moving silently through the forest surrounding the temple, you follow your Force senses.",
                    "Soon, you spot an Imperial shuttle landing in a clearing ahead.",
                    "Two figures in black emerge - Imperial Inquisitors, former Jedi turned to the dark side.",
                    "They haven't spotted you yet, but they're heading toward the temple."
                ],
                "background": "static/images/forest.jpg",
                "choices": [
                    {
                        "text": "Return to the temple to warn everyone",
                        "next_scene": "jedi_return_warn"
                    },
                    {
                        "text": "Try to distract the Inquisitors away from the temple",
                        "next_scene": "jedi_distract"
                    },
                    {
                        "text": "Attempt to listen to their plans",
                        "next_scene": "jedi_listen_plans"
                    }
                ]
            },
            "jedi_return_warn": {
                "title": "Warning the Temple",
                "description": [
                    "You sprint back to the temple, using the Force to enhance your speed.",
                    "You arrive just in time to warn Master Kora and the others.",
                    "With the advance notice, Master Kora organizes a successful evacuation.",
                    "You escape with the other Jedi, continuing your training in hiding."
                ],
                "background": "static/images/jedi_warning.jpg",
                "ending": "You return to warn the temple. With the advance notice, Master Kora organizes a successful evacuation. You escape with the other Jedi, continuing your training in hiding."
            },
            
            # Rebel Pilot storyline
            "rebel_start": {
                "title": "Echo Base",
                "description": [
                    "You are a skilled pilot for the Rebel Alliance, stationed on the ice planet Hoth.",
                    "The Empire has been hunting rebel bases across the galaxy, and tensions are high.",
                    "During a routine patrol, your scanners detect an unidentified ship approaching the system.",
                    "It's not broadcasting any codes - friendly or Imperial."
                ],
                "background": "static/images/hoth.jpg",
                "choices": [
                    {
                        "text": "Report to base and request instructions",
                        "next_scene": "rebel_report_base"
                    },
                    {
                        "text": "Approach the ship to investigate",
                        "next_scene": "rebel_approach_ship"
                    },
                    {
                        "text": "Hide and observe the ship's actions",
                        "next_scene": "rebel_observe_ship"
                    }
                ]
            },
            "rebel_report_base": {
                "title": "Command Decision",
                "description": [
                    "You immediately contact Echo Base. 'Command, this is Rogue Seven. Unidentified vessel in sector four.'",
                    "'Copy Rogue Seven. Maintain distance and stand by,' responds the controller.",
                    "After a tense wait, Command responds: 'Rogue Seven, intelligence suggests it might be a smuggler with vital supplies.'",
                    "'However, we can't rule out an Imperial trap. Proceed with caution.'"
                ],
                "background": "static/images/rebel_base.jpg",
                "choices": [
                    {
                        "text": "Escort the ship to a safe distance from the base",
                        "next_scene": "rebel_escort_ship"
                    },
                    {
                        "text": "Attempt to make contact with the ship",
                        "next_scene": "rebel_contact_ship"
                    },
                    {
                        "text": "Request backup before approaching",
                        "next_scene": "rebel_request_backup"
                    }
                ]
            },
            "rebel_escort_ship": {
                "title": "Unexpected Ally",
                "description": [
                    "You decide to escort the ship to a safe rendezvous point away from the base.",
                    "The ship follows your instructions without resistance.",
                    "When you finally make contact, you're surprised to find Han Solo and Chewbacca aboard the Millennium Falcon.",
                    "They've brought a shipment of shield generators that will be crucial for the base's defenses.",
                    "Your caution is commended by Alliance leadership."
                ],
                "background": "static/images/millennium_falcon.jpg",
                "ending": "The ship follows your escort instructions. It turns out to be Han Solo with a shipment of shield generators. Your caution is commended by Alliance leadership."
            },
            
            # Bounty Hunter storyline
            "bounty_hunter_start": {
                "title": "The Contract",
                "description": [
                    "You are a notorious bounty hunter, known across the Outer Rim for always catching your target.",
                    "Your ship, the Crimson Viper, is docked at Mos Eisley spaceport on Tatooine.",
                    "You've just received a mysterious transmission offering a job with payment that could set you up for life.",
                    "The message is encrypted, but you recognize the Imperial insignia."
                ],
                "background": "static/images/mos_eisley.jpg",
                "choices": [
                    {
                        "text": "Accept the Imperial contract",
                        "next_scene": "bounty_hunter_accept"
                    },
                    {
                        "text": "Ignore it - Imperial entanglements are trouble",
                        "next_scene": "bounty_hunter_ignore"
                    },
                    {
                        "text": "Try to trace the message source",
                        "next_scene": "bounty_hunter_trace"
                    }
                ]
            },
            "bounty_hunter_accept": {
                "title": "The Hunt Begins",
                "description": [
                    "You decide to accept the contract. Credits are credits, after all.",
                    "The encrypted details reveal your target: a former Imperial officer who defected to the Rebellion.",
                    "Last seen in the Anoat system, the bounty is five million credits - alive only.",
                    "As you prepare your ship, a Rodian approaches. 'I hear you're hunting Verik Tarn.'",
                    "'The Rebellion will pay double what the Empire's offering to keep him safe.'"
                ],
                "background": "static/images/bounty_hunter_ship.jpg",
                "choices": [
                    {
                        "text": "Stick with the Imperial contract",
                        "next_scene": "bounty_hunter_imperial"
                    },
                    {
                        "text": "Switch to the Rebellion's offer",
                        "next_scene": "bounty_hunter_rebellion"
                    },
                    {
                        "text": "Play both sides against each other",
                        "next_scene": "bounty_hunter_double_cross"
                    }
                ]
            },
            "bounty_hunter_imperial": {
                "title": "Imperial Service",
                "description": [
                    "You decide to honor your agreement with the Empire.",
                    "After a challenging hunt across several systems, you finally capture Verik Tarn.",
                    "The Empire pays you handsomely, and your reputation soars among Imperial clients.",
                    "This leads to more lucrative but increasingly dangerous work for the Empire.",
                    "You become one of their most valued assets in the hunt for rebel sympathizers."
                ],
                "background": "static/images/star_destroyer.jpg",
                "ending": "You complete the Imperial contract, delivering the defector. Your reputation soars among Imperial clients, leading to more lucrative but increasingly dangerous work for the Empire."
            }
            
            # More scenes would be added here...
        }
    } 