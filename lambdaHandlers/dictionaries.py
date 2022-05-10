"""
    Auto DM

    Jeremy L Thompson

    This file provides dictionaries for random modules
"""
# ------------------------------------------------------------------------------
# Dictionary of Monsters
# ------------------------------------------------------------------------------
ALL_MONSTERS = [  # Monster Manual
    {
        "Name":
        "commoner",
        "CR":
        "0",
        "Env": [
            "arctic", "coastal", "desert", "forest", "grassland", "hill",
            "urban"
        ]
    },
    {
        "Name": "Owl",
        "CR": "0",
        "Env": ["arctic", "forest"]
    },
    {
        "Name": "bandit",
        "CR": "1/8",
        "Env": ["arctic", "costal", "desert", "forest", "hill", "urban"]
    },
    {
        "Name": "blood hawk",
        "CR": "1/8",
        "Env":
        ["arctic", "coastal", "forest", "grassland", "hill", "mountain"]
    },
    {
        "Name":
        "kobold",
        "CR":
        "1/8",
        "Env": [
            "arctic", "coastal", "desert", "forest", "hill", "mountain",
            "swamp", "underdark", "urban"
        ]
    },
    {
        "Name":
        "tribal warrior",
        "CR":
        "1/8",
        "Env": [
            "arctic", "coastal", "desert", "forest", "grassland", "hill",
            "mountain", "swamp", "underdark"
        ]
    },
    {
        "Name": "giant owl",
        "CR": "1/4",
        "Env": ["arctic"]
    },
    {
        "Name":
        "winged kobold",
        "CR":
        "1/4",
        "Env": [
            "arctic", "coastal", "desert", "forest", "hill", "mountain",
            "swamp", "underdark", "urban"
        ]
    },
    {
        "Name": "ice mephit",
        "CR": "1/2",
        "Env": ["arctic"]
    },
    {
        "Name":
        "orc",
        "CR":
        "1/2",
        "Env": [
            "arctic", "forest", "grassland", "hill", "mountain", "swamp",
            "underdark"
        ]
    },
    {
        "Name":
        "scout",
        "CR":
        "1/2",
        "Env": [
            "arctic", "coastal", "desert", "forest", "grassland", "hill",
            "mountain", "swamp", "underdark"
        ]
    },
    {
        "Name": "brown bear",
        "CR": "1",
        "Env": ["arctic", "forest", "hill"]
    },
    {
        "Name": "half ogre",
        "CR": "1",
        "Env": ["arctic", "forest", "hill", "mountain", "underdark", "urban"]
    },
    {
        "Name": "crab",
        "CR": "0",
        "Env": ["coastal"]
    },
    {
        "Name": "eagle",
        "CR": "0",
        "Env": ["coastal", "grassland", "hill", "mountain"]
    },
    {
        "Name": "giant crab",
        "CR": "1/8",
        "Env": ["coastal"]
    },
    {
        "Name":
        "guard",
        "CR":
        "1/8",
        "Env": [
            "coastal", "desert", "forest", "grassland", "hill", "mountain",
            "urban"
        ]
    },
    {
        "Name": "merfolk",
        "CR": "1/8",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "poisonous snake",
        "CR": "1/8",
        "Env": ["coastal", "desert", "forest", "grassland", "hill", "swamp"]
    },
    {
        "Name":
        "stirge",
        "CR":
        "1/8",
        "Env": [
            "coastal", "desert", "forest", "grassland", "hill", "mountain",
            "swamp", "underdark", "urban"
        ]
    },
    {
        "Name": "giant lizard",
        "CR": "1/4",
        "Env": ["coastal", "desert", "forest", "swamp", "underdark"]
    },
    {
        "Name": "giant wolf spider",
        "CR": "1/4",
        "Env": ["coastal", "desert", "forest", "grassland", "hill"]
    },
    {
        "Name": "pseudodragon",
        "CR": "1/4",
        "Env": ["coastal", "desert", "forest", "hill", "mountain", "urban"]
    },
    {
        "Name": "pteranodon",
        "CR": "1/4",
        "Env": ["coastal", "grassland", "mountain"]
    },
    {
        "Name": "sahuagin",
        "CR": "1/2",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "giant eagle",
        "CR": "1",
        "Env": ["coastal", "grassland", "hill", "mountain"]
    },
    {
        "Name": "giant toad",
        "CR": "1",
        "Env": ["coastal", "desert", "forest", "swamp", "underdark"]
    },
    {
        "Name": "harpy",
        "CR": "1",
        "Env": ["coastal", "forest", "hill", "mountain"]
    },
    {
        "Name": "cat",
        "CR": "0",
        "Env": ["desert", "forest", "grassland", "urban"]
    },
    {
        "Name": "hyena",
        "CR": "0",
        "Env": ["desert", "forest", "grassland", "hill"]
    },
    {
        "Name": "jackal",
        "CR": "0",
        "Env": ["desert", "grassland"]
    },
    {
        "Name": "scorpion",
        "CR": "0",
        "Env": ["desert"]
    },
    {
        "Name": "vulture",
        "CR": "0",
        "Env": ["desert", "grassland", "hill"]
    },
    {
        "Name": "camel",
        "CR": "1/8",
        "Env": ["desert"]
    },
    {
        "Name": "flying snake",
        "CR": "1/8",
        "Env": ["desert", "forest", "grassland", "urban"]
    },
    {
        "Name": "mule",
        "CR": "1/8",
        "Env": ["desert", "hill", "urban"]
    },
    {
        "Name": "constrictor snake",
        "CR": "1/4",
        "Env": ["desert", "forest", "underwater"]
    },
    {
        "Name": "giant poisonous snake",
        "CR": "1/4",
        "Env": ["desert", "forest", "grassland", "underdark", "urban"]
    },
    {
        "Name": "dust mephit",
        "CR": "1/2",
        "Env": ["desert"]
    },
    {
        "Name": "gnoll",
        "CR": "1/2",
        "Env": ["desert", "forest", "grassland", "hill"]
    },
    {
        "Name": "hobgoblin",
        "CR": "1/2",
        "Env": ["desert", "forest", "grassland", "hill", "underdark"]
    },
    {
        "Name": "jackalwere",
        "CR": "1/2",
        "Env": ["desert", "grassland"]
    },
    {
        "Name":
        "swarm of insects",
        "CR":
        "1/2",
        "Env": [
            "desert", "forest", "grassland", "hill", "swamp", "underdark",
            "urban"
        ]
    },
    {
        "Name": "death dog",
        "CR": "1",
        "Env": ["desert"]
    },
    {
        "Name": "giant hyena",
        "CR": "1",
        "Env": ["desert", "forest", "grassland", "hill"]
    },
    {
        "Name": "giant spider",
        "CR": "1",
        "Env": ["desert", "forest", "underdark", "urban"]
    },
    {
        "Name": "giant vulture",
        "CR": "1",
        "Env": ["desert", "grassland"]
    },
    {
        "Name": "lion",
        "CR": "1",
        "Env": ["desert", "grassland", "hill", "mountain"]
    },
    {
        "Name": "thri-keen",
        "CR": "1",
        "Env": ["desert", "grassland"]
    },
    {
        "Name": "yuan-ti pureblood",
        "CR": "1",
        "Env": ["desert", "forest", "swamp", "urban"]
    },
    {
        "Name": "awakened shrub",
        "CR": "0",
        "Env": ["forest"]
    },
    {
        "Name": "baboon",
        "CR": "0",
        "Env": ["forest", "hill"]
    },
    {
        "Name": "badger",
        "CR": "0",
        "Env": ["forest"]
    },
    {
        "Name": "deer",
        "CR": "0",
        "Env": ["forest", "grassland"]
    },
    {
        "Name": "giant rat",
        "CR": "1/8",
        "Env": ["forest", "swamp", "underdark", "urban"]
    },
    {
        "Name": "giant weasel",
        "CR": "1/8",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "mastiff",
        "CR": "1/8",
        "Env": ["forest", "hill", "urban"]
    },
    {
        "Name": "twig blight",
        "CR": "1/8",
        "Env": ["forest"]
    },
    {
        "Name": "blink dog",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "boar",
        "CR": "1/4",
        "Env": ["forest", "grassland"]
    },
    {
        "Name": "elk",
        "CR": "1/4",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "giant badger",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "giant frog",
        "CR": "1/4",
        "Env": ["forest", "swamp"]
    },
    {
        "Name": "giant owl",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "goblin",
        "CR": "1/4",
        "Env": ["forest", "grassland", "hill", "underdark"]
    },
    {
        "Name": "kenku",
        "CR": "1/4",
        "Env": ["forest", "urban"]
    },
    {
        "Name": "needle blight",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "panther",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "pixie",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "sprite",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "swarm of ravens",
        "CR": "1/4",
        "Env": ["forest", "hill", "swamp", "urban"]
    },
    {
        "Name": "wolf",
        "CR": "1/4",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "ape",
        "CR": "1/2",
        "Env": ["forest"]
    },
    {
        "Name": "black bear",
        "CR": "1/2",
        "Env": ["forest"]
    },
    {
        "Name": "giant wasp",
        "CR": "1/2",
        "Env": ["forest", "grassland", "urban"]
    },
    {
        "Name": "lizardfolk",
        "CR": "1/2",
        "Env": ["forest", "swamp"]
    },
    {
        "Name": "satyr",
        "CR": "1/2",
        "Env": ["forest"]
    },
    {
        "Name": "vine blight",
        "CR": "1/2",
        "Env": ["forest"]
    },
    {
        "Name": "worg",
        "CR": "1/2",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "bugbear",
        "CR": "1",
        "Env": ["forest", "grassland", "underdark"]
    },
    {
        "Name": "dire wolf",
        "CR": "1",
        "Env": ["forest", "hill"]
    },
    {
        "Name": "dryad",
        "CR": "1",
        "Env": ["forest"]
    },
    {
        "Name": "faerie dragon yellow or younger",
        "CR": "1",
        "Env": ["forest"]
    },
    {
        "Name": "goblin boss",
        "CR": "1",
        "Env": ["forest", "grassland", "hill", "underdark"]
    },
    {
        "Name": "harpy",
        "CR": "1",
        "Env": ["forest", "hill", "mountain"]
    },
    {
        "Name": "tiger",
        "CR": "1",
        "Env": ["forest", "grassland"]
    },
    {
        "Name": "goat",
        "CR": "0",
        "Env": ["grassland", "hill", "mountain", "urban"]
    },
    {
        "Name": "axe beak",
        "CR": "1/4",
        "Env": ["grassland", "hill"]
    },
    {
        "Name": "riding horse",
        "CR": "1/4",
        "Env": ["grassland", "urban"]
    },
    {
        "Name": "cockatrice",
        "CR": "1/2",
        "Env": ["grassland"]
    },
    {
        "Name": "giant goat",
        "CR": "1/2",
        "Env": ["grassland", "hill"]
    },
    {
        "Name": "hippogriff",
        "CR": "1",
        "Env": ["grassland", "hill", "mountain"]
    },
    {
        "Name": "scarecrow",
        "CR": "1",
        "Env": ["grassland"]
    },
    {
        "Name": "raven",
        "CR": "0",
        "Env": ["hill", "swamp", "urban"]
    },
    {
        "Name": "swarm of bats",
        "CR": "1/4",
        "Env": ["hill", "mountain", "underdark", "urban"]
    },
    {
        "Name": "aarakocra",
        "CR": "1/4",
        "Env": ["mountain"]
    },
    {
        "Name": "rat",
        "CR": "0",
        "Env": ["swamp", "urban"]
    },
    {
        "Name": "bullywug",
        "CR": "1/8",
        "Env": ["swamp"]
    },
    {
        "Name": "mud mephit",
        "CR": "1/8",
        "Env": ["swamp"]
    },
    {
        "Name": "crocodile",
        "CR": "1/2",
        "Env": ["swamp", "urban"]
    },
    {
        "Name": "ghoul",
        "CR": "1",
        "Env": ["swamp", "underdark", "urban"]
    },
    {
        "Name": "giant fire beetle",
        "CR": "0",
        "Env": ["underdark"]
    },
    {
        "Name": "shrieker",
        "CR": "0",
        "Env": ["underdark"]
    },
    {
        "Name": "myconid sprout",
        "CR": "0",
        "Env": ["underdark"]
    },
    {
        "Name": "flumph",
        "CR": "1/8",
        "Env": ["underdark"]
    },
    {
        "Name": "drow",
        "CR": "1/4",
        "Env": ["underdark"]
    },
    {
        "Name": "giant bat",
        "CR": "1/4",
        "Env": ["underdark"]
    },
    {
        "Name": "giant centipede",
        "CR": "1/4",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "grimlock",
        "CR": "1/4",
        "Env": ["underdark"]
    },
    {
        "Name": "kuo-toa",
        "CR": "1/4",
        "Env": ["underdark"]
    },
    {
        "Name": "troglodyte",
        "CR": "1/4",
        "Env": ["underdark"]
    },
    {
        "Name": "violet fungus",
        "CR": "1/4",
        "Env": ["underdark"]
    },
    {
        "Name": "darkmantle",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "deep gnome",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "gas spore",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "gray ooze",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "magma mephit",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "myconid adult",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "piercer",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "rust monster",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "shadow",
        "CR": "1/2",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "duergar",
        "CR": "1",
        "Env": ["underdark"]
    },
    {
        "Name": "fire snake",
        "CR": "1",
        "Env": ["underdark"]
    },
    {
        "Name": "kuo-toa whip",
        "CR": "1",
        "Env": ["underdark"]
    },
    {
        "Name": "quaggoth spore servant",
        "CR": "1",
        "Env": ["underdark"]
    },
    {
        "Name": "specter",
        "CR": "1",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "quipper",
        "CR": "0",
        "Env": ["underwater"]
    },
    {
        "Name": "steam mephit",
        "CR": "1/4",
        "Env": ["underwater"]
    },
    {
        "Name": "giant sea horse",
        "CR": "1/2",
        "Env": ["underwater"]
    },
    {
        "Name": "reef shark",
        "CR": "1/2",
        "Env": ["underwater"]
    },
    {
        "Name": "giant octopus",
        "CR": "1",
        "Env": ["underwater"]
    },
    {
        "Name": "swarm of quippers",
        "CR": "1",
        "Env": ["underwater"]
    },
    {
        "Name": "cultist",
        "CR": "1/8",
        "Env": ["urban"]
    },
    {
        "Name": "noble",
        "CR": "1/8",
        "Env": ["urban"]
    },
    {
        "Name": "pony",
        "CR": "1/8",
        "Env": ["urban"]
    },
    {
        "Name": "acolyte",
        "CR": "1/4",
        "Env": ["urban"]
    },
    {
        "Name": "draft horse",
        "CR": "1/4",
        "Env": ["urban"]
    },
    {
        "Name": "skeleton",
        "CR": "1/4",
        "Env": ["urban"]
    },
    {
        "Name": "smoke mephit",
        "CR": "1/4",
        "Env": ["urban"]
    },
    {
        "Name": "swarm of rats",
        "CR": "1/4",
        "Env": ["urban"]
    },
    {
        "Name": "zombie",
        "CR": "1/4",
        "Env": ["urban"]
    },
    {
        "Name": "thug",
        "CR": "1/2",
        "Env": ["urban"]
    },
    {
        "Name": "warhorse",
        "CR": "1/2",
        "Env": ["urban"]
    },
    {
        "Name": "bandit captain",
        "CR": "2",
        "Env": ["arctic", "coastal", "desert", "forest", "hill", "urban"],
        "NPC": True
    },
    {
        "Name": "berserker",
        "CR": "2",
        "Env": ["arctic", "coastal", "desert", "forest", "hill", "mountain"],
        "NPC": True
    },
    {
        "Name":
        "druid",
        "CR":
        "2",
        "Env": [
            "arctic", "coastal", "desert", "forest", "grassland", "hill",
            "mountain", "swamp", "underdark"
        ],
        "NPC":
        True
    },
    {
        "Name": "griffon",
        "CR": "2",
        "Env": ["arctic", "coastal", "grassland", "hill", "mountain"]
    },
    {
        "Name":
        "ogre",
        "CR":
        "2",
        "Env": [
            "arctic", "coastal", "desert", "forest", "grassland", "hill",
            "mountain", "swamp", "underdark"
        ]
    },
    {
        "Name":
        "orc Eye of Gruumsh",
        "CR":
        "2",
        "Env": [
            "arctic", "forest", "grassland", "hill", "mountain", "swamp",
            "underdark"
        ]
    },
    {
        "Name": "orog",
        "CR": "2",
        "Env":
        ["arctic", "forest", "grassland", "hill", "mountain", "underdark"]
    },
    {
        "Name": "polar bear",
        "CR": "2",
        "Env": ["arctic", "underdark"]
    },
    {
        "Name": "saber toothed tiger",
        "CR": "2",
        "Env": ["arctic", "mountain"]
    },
    {
        "Name": "manticore",
        "CR": "3",
        "Env": ["arctic", "coastal", "hill", "mountain"]
    },
    {
        "Name":
        "veteran",
        "CR":
        "3",
        "Env": [
            "arctic", "coastal", "forest", "grassland", "hill", "mountain",
            "underdark", "urban"
        ],
        "NPC":
        True
    },
    {
        "Name": "winter wolf",
        "CR": "3",
        "Env": ["arctic"]
    },
    {
        "Name": "yeti",
        "CR": "3",
        "Env": ["arctic"]
    },
    {
        "Name": "revenant",
        "CR": "5",
        "Env": ["arctic", "desert", "forest", "hill", "swamp", "urban"]
    },
    {
        "Name": "merrow",
        "CR": "2",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "plesiosaurus",
        "CR": "2",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "sahuagin priestess",
        "CR": "2",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "sea hag",
        "CR": "2",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "banshee",
        "CR": "4",
        "Env": ["coastal", "forest"]
    },
    {
        "Name": "sahuagin baron",
        "CR": "5",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "water elemental",
        "CR": "5",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "giant constrictor snake",
        "CR": "2",
        "Env": ["desert", "forest", "swamp", "underdark"]
    },
    {
        "Name": "gnoll pack lord",
        "CR": "2",
        "Env": ["desert", "forest", "grassland", "hill"],
        "NPC": True
    },
    {
        "Name": "giant scorpion",
        "CR": "3",
        "Env": ["desert"]
    },
    {
        "Name": "hobgoblin captain",
        "CR": "3",
        "Env": ["desert", "forest", "grassland", "hill", "underdark"],
        "NPC": True
    },
    {
        "Name": "mummy",
        "CR": "3",
        "Env": ["desert"]
    },
    {
        "Name": "phase spider",
        "CR": "3",
        "Env": ["desert", "forest", "grassland", "hill", "underdark", "urban"]
    },
    {
        "Name": "wight",
        "CR": "3",
        "Env": ["desert", "swamp", "underdark", "urban"]
    },
    {
        "Name": "yuan-ti malison",
        "CR": "3",
        "Env": ["desert", "forest", "swamp"]
    },
    {
        "Name": "couatl",
        "CR": "4",
        "Env": ["desert", "forest", "grassland", "urban"]
    },
    {
        "Name": "gnoll hand of Yeenoghu",
        "CR": "4",
        "Env": ["desert", "forest", "grassland", "hill"]
    },
    {
        "Name": "lamia",
        "CR": "4",
        "Env": ["desert"]
    },
    {
        "Name": "weretiger",
        "CR": "4",
        "Env": ["desert", "forest", "grassland"]
    },
    {
        "Name": "air elemental",
        "CR": "5",
        "Env": ["desert", "mountain"]
    },
    {
        "Name": "fire elemental",
        "CR": "5",
        "Env": ["desert"]
    },
    {
        "Name": "revenant",
        "CR": "5",
        "Env": ["desert", "hill", "swamp"]
    },
    {
        "Name": "ankheg",
        "CR": "2",
        "Env": ["forest"]
    },
    {
        "Name": "awakened tree",
        "CR": "2",
        "Env": ["forest"]
    },
    {
        "Name": "centaur",
        "CR": "2",
        "Env": ["forest", "grassland"],
        "NPC": True
    },
    {
        "Name": "ettercap",
        "CR": "2",
        "Env": ["forest"]
    },
    {
        "Name": "faerie dragon green or older",
        "CR": "2",
        "Env": ["forest"]
    },
    {
        "Name": "giant boar",
        "CR": "2",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "giant elk",
        "CR": "2",
        "Env": ["forest", "grassland", "hill", "mountain"]
    },
    {
        "Name": "grick",
        "CR": "2",
        "Env": ["forest", "underdark"]
    },
    {
        "Name": "lizardfolk shaman",
        "CR": "2",
        "Env": ["forest"]
    },
    {
        "Name": "pegasus",
        "CR": "2",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "swarm of poisonous snakes",
        "CR": "2",
        "Env": ["forest", "swamp"]
    },
    {
        "Name": "wererat",
        "CR": "2",
        "Env": ["forest", "urban"]
    },
    {
        "Name": "will-o-wisp",
        "CR": "2",
        "Env": ["forest", "swamp", "urban"]
    },
    {
        "Name": "displacer beast",
        "CR": "3",
        "Env": ["forest"]
    },
    {
        "Name": "green hag",
        "CR": "3",
        "Env": ["forest", "hill", "swamp"],
        "NPC": True
    },
    {
        "Name": "owlbear",
        "CR": "3",
        "Env": ["forest"]
    },
    {
        "Name": "werewolf",
        "CR": "3",
        "Env": ["forest", "hill"]
    },
    {
        "Name": "wereboar",
        "CR": "4",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "gorgon",
        "CR": "5",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "shambling mound",
        "CR": "5",
        "Env": ["forest", "swamp"]
    },
    {
        "Name": "troll",
        "CR": "5",
        "Env": ["forest", "hill", "mountain", "swamp", "underdark"]
    },
    {
        "Name": "unicorn",
        "CR": "5",
        "Env": ["forest"]
    },
    {
        "Name": "allosaurus",
        "CR": "2",
        "Env": ["grassland"]
    },
    {
        "Name": "ankheg",
        "CR": "2",
        "Env": ["grassland"]
    },
    {
        "Name": "rhinoceros",
        "CR": "2",
        "Env": ["grassland"]
    },
    {
        "Name": "ankylosaurus",
        "CR": "3",
        "Env": ["grassland"]
    },
    {
        "Name": "bulette",
        "CR": "5",
        "Env": ["grassland", "hill", "mountain"]
    },
    {
        "Name": "triceratops",
        "CR": "5",
        "Env": ["grassland"]
    },
    {
        "Name": "ettin",
        "CR": "4",
        "Env": ["hill", "mountain", "underdark"]
    },
    {
        "Name": "hill giant",
        "CR": "5",
        "Env": ["hill"]
    },
    {
        "Name": "basilisk",
        "CR": "3",
        "Env": ["mountain"]
    },
    {
        "Name": "hell hound",
        "CR": "3",
        "Env": ["mountain", "underdark"]
    },
    {
        "Name": "ghast",
        "CR": "2",
        "Env": ["swamp", "underdark"]
    },
    {
        "Name": "giant crocodile",
        "CR": "5",
        "Env": ["swamp"]
    },
    {
        "Name": "carrion crawler",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "gargoyle",
        "CR": "2",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "gelatinous cube",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "gibbering mouther",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "intellect devourer",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "mimic",
        "CR": "2",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "minotaur skeleton",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "nothic",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "ochre jelly",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "quaggoth",
        "CR": "2",
        "Env": ["underdark"]
    },
    {
        "Name": "doppelganger",
        "CR": "3",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "grell",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "hook horror",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "kuo-toa monitor",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "minotaur",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "quaggoth thonot",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "spectator",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "water weird",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "black pudding",
        "CR": "4",
        "Env": ["underdark"]
    },
    {
        "Name": "bone naga",
        "CR": "4",
        "Env": ["underdark"]
    },
    {
        "Name": "chuul",
        "CR": "4",
        "Env": ["underdark"]
    },
    {
        "Name": "flameskull",
        "CR": "4",
        "Env": ["underdark"]
    },
    {
        "Name": "ghost",
        "CR": "4",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "beholder zombie",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "drow elite warrior",
        "CR": "5",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "earth elemental",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "otyugh",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "roper",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "salamander",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "umber hulk",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "vampire spawn",
        "CR": "5",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "wraith",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "xorn",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "hunter shark",
        "CR": "2",
        "Env": ["underwater"]
    },
    {
        "Name": "killer whale",
        "CR": "3",
        "Env": ["underwater"]
    },
    {
        "Name": "giant shark",
        "CR": "5",
        "Env": ["underwater"]
    },
    {
        "Name": "cult fanatic",
        "CR": "2",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "priest",
        "CR": "2",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "knight",
        "CR": "3",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "succubus",
        "CR": "4",
        "Env": ["urban"]
    },
    {
        "Name": "incubus",
        "CR": "4",
        "Env": ["urban"]
    },
    {
        "Name": "cambion",
        "CR": "5",
        "Env": ["urban"]
    },
    {
        "Name": "gladiator",
        "CR": "5",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "mammoth",
        "CR": "6",
        "Env": ["arctic"]
    },
    {
        "Name": "young white dragon",
        "CR": "6",
        "Env": ["arctic"]
    },
    {
        "Name": "frost giant",
        "CR": "8",
        "Env": ["arctic", "mountain"]
    },
    {
        "Name": "abominable yeti",
        "CR": "9",
        "Env": ["arctic"]
    },
    {
        "Name": "remorhaz",
        "CR": "11",
        "Env": ["arctic"]
    },
    {
        "Name": "roc",
        "CR": "11",
        "Env": ["arctic", "coastal", "desert", "hill", "mountain"]
    },
    {
        "Name": "adult white dragon",
        "CR": "13",
        "Env": ["arctic"],
        "NPC": True
    },
    {
        "Name": "ancient white dragon",
        "CR": "20",
        "Env": ["arctic"],
        "NPC": True
    },
    {
        "Name": "cyclops",
        "CR": "6",
        "Env":
        ["coastal", "desert", "grassland", "hill", "mountain", "underdark"]
    },
    {
        "Name": "young bronze dragon",
        "CR": "8",
        "Env": ["coastal"]
    },
    {
        "Name": "young blue dragon",
        "CR": "9",
        "Env": ["coastal", "desert"]
    },
    {
        "Name": "djinni",
        "CR": "11",
        "Env": ["coastal"],
        "NPC": True
    },
    {
        "Name": "marid",
        "CR": "11",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "storm giant",
        "CR": "13",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "adult bronze dragon",
        "CR": "15",
        "Env": ["coastal"],
        "NPC": True
    },
    {
        "Name": "adult blue dragon",
        "CR": "16",
        "Env": ["coastal", "desert"],
        "NPC": True
    },
    {
        "Name": "dragon turtle",
        "CR": "17",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "ancient bronze dragon",
        "CR": "22",
        "Env": ["coastal"],
        "NPC": True
    },
    {
        "Name": "ancient blue dragon",
        "CR": "23",
        "Env": ["coastal", "desert"],
        "NPC": True
    },
    {
        "Name": "medusa",
        "CR": "6",
        "Env": ["desert"]
    },
    {
        "Name": "young brass dragon",
        "CR": "6",
        "Env": ["desert"]
    },
    {
        "Name": "yuan-ti abomination",
        "CR": "7",
        "Env": ["desert", "forest", "swamp"],
        "NPC": True
    },
    {
        "Name": "gaurdian naga",
        "CR": "10",
        "Env": ["desert", "forest"]
    },
    {
        "Name": "efreeti",
        "CR": "11",
        "Env": ["desert"]
    },
    {
        "Name": "gynosphinx",
        "CR": "11",
        "Env": ["desert"]
    },
    {
        "Name": "adult brass dragon",
        "CR": "13",
        "Env": ["desert"],
        "NPC": True
    },
    {
        "Name": "mummy lord",
        "CR": "15",
        "Env": ["desert"]
    },
    {
        "Name": "purple worm",
        "CR": "15",
        "Env": ["desert"]
    },
    {
        "Name": "adult blue dracolich",
        "CR": "17",
        "Env": ["desert"],
        "NPC": True
    },
    {
        "Name": "androsphinx",
        "CR": "17",
        "Env": ["desert"]
    },
    {
        "Name": "ancient brass dragon",
        "CR": "20",
        "Env": ["desert"],
        "NPC": True
    },
    {
        "Name": "giant ape",
        "CR": "7",
        "Env": ["forest"]
    },
    {
        "Name": "grick alpha",
        "CR": "7",
        "Env": ["forest", "underdark"]
    },
    {
        "Name": "oni",
        "CR": "7",
        "Env": ["forest", "urban"]
    },
    {
        "Name": "young green dragon",
        "CR": "8",
        "Env": ["forest"]
    },
    {
        "Name": "treant",
        "CR": "9",
        "Env": ["forest"]
    },
    {
        "Name": "guardian naga",
        "CR": "10",
        "Env": ["forest"]
    },
    {
        "Name": "young gold dragon",
        "CR": "10",
        "Env": ["forest", "grassland"]
    },
    {
        "Name": "adult green dragon",
        "CR": "15",
        "Env": ["forest"],
        "NPC": True
    },
    {
        "Name": "adult gold dragon",
        "CR": "17",
        "Env": ["forest", "grassland"],
        "NPC": True
    },
    {
        "Name": "ancient green dragon",
        "CR": "22",
        "Env": ["forest"],
        "NPC": True
    },
    {
        "Name": "ancient gold dragon",
        "CR": "24",
        "Env": ["forest", "grassland"],
        "NPC": True
    },
    {
        "Name": "chimera",
        "CR": "6",
        "Env": ["grassland", "hill", "mountain", "underdark"]
    },
    {
        "Name": "tyrannosaurus rex",
        "CR": "8",
        "Env": ["grassland"]
    },
    {
        "Name": "galeb duhr",
        "CR": "6",
        "Env": ["hill", "mountain"]
    },
    {
        "Name": "wyvern",
        "CR": "6",
        "Env": ["hill", "mountain"]
    },
    {
        "Name": "stone giant",
        "CR": "7",
        "Env": ["hill", "mountain", "underdark"]
    },
    {
        "Name": "young copper dragon",
        "CR": "7",
        "Env": ["hill"]
    },
    {
        "Name": "young red dragon",
        "CR": "10",
        "Env": ["hill", "mountain"]
    },
    {
        "Name": "adult copper dragon",
        "CR": "14",
        "Env": ["hill"],
        "NPC": True
    },
    {
        "Name": "adult red dragon",
        "CR": "17",
        "Env": ["hill", "mountain"],
        "NPC": True
    },
    {
        "Name": "ancient copper dragon",
        "CR": "21",
        "Env": ["hill"],
        "NPC": True
    },
    {
        "Name": "ancient red dragon",
        "CR": "24",
        "Env": ["hill", "mountain"],
        "NPC": True
    },
    {
        "Name": "cloud giant",
        "CR": "9",
        "Env": ["mountain"]
    },
    {
        "Name": "fire giant",
        "CR": "9",
        "Env": ["mountain", "underdark"]
    },
    {
        "Name": "young silver dragon",
        "CR": "9",
        "Env": ["mountain"]
    },
    {
        "Name": "adult silver dragon",
        "CR": "16",
        "Env": ["mountain"],
        "NPC": True
    },
    {
        "Name": "ancient silver dragon",
        "CR": "23",
        "Env": ["mountain"],
        "NPC": True
    },
    {
        "Name": "young black dragon",
        "CR": "7",
        "Env": ["swamp"]
    },
    {
        "Name": "hydra",
        "CR": "8",
        "Env": ["swamp"]
    },
    {
        "Name": "adult black dragon",
        "CR": "14",
        "Env": ["swamp"],
        "NPC": True
    },
    {
        "Name": "ancient black dragon",
        "CR": "21",
        "Env": ["swamp"],
        "NPC": True
    },
    {
        "Name": "drider",
        "CR": "6",
        "Env": ["underdark"]
    },
    {
        "Name": "drow mage",
        "CR": "7",
        "Env": ["underdark"]
    },
    {
        "Name": "mind flayer",
        "CR": "8",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "arcanist",
        "CR": "8",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "spirit naga",
        "CR": "8",
        "Env": ["underdark"]
    },
    {
        "Name": "aboleth",
        "CR": "10",
        "Env": ["underdark"]
    },
    {
        "Name": "behir",
        "CR": "11",
        "Env": ["underdark"]
    },
    {
        "Name": "dao",
        "CR": "11",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "beholder",
        "CR": "13",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "young red shadow dragon",
        "CR": "13",
        "Env": ["underdark"]
    },
    {
        "Name": "death tyrant",
        "CR": "14",
        "Env": ["underdark"]
    },
    {
        "Name": "purple worm",
        "CR": "15",
        "Env": ["underdark"]
    },
    {
        "Name": "kraken",
        "CR": "23",
        "Env": ["underwater"]
    },
    {
        "Name": "invisible stalker",
        "CR": "6",
        "Env": ["urban"]
    },
    {
        "Name": "mage",
        "CR": "6",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "shield guardian",
        "CR": "7",
        "Env": ["urban"]
    },
    {
        "Name": "assassin",
        "CR": "8",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "gray slaad",
        "CR": "9",
        "Env": ["urban"]
    },
    {
        "Name": "young silver dragon",
        "CR": "9",
        "Env": ["urban"]
    },
    {
        "Name": "archmage",
        "CR": "12",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "rakshasa",
        "CR": "13",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "vampire",
        "CR": "13",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "spellcaster vampire",
        "CR": "15",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "warrior vampire",
        "CR": "15",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "adult silver dragon",
        "CR": "16",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "ancient silver dragon",
        "CR": "23",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "tarrasque",
        "CR": "30",
        "Env": ["urban"]
    },
    {
        "Name": "ice devil",
        "CR": "14",
        "Env": []
    },
    {
        "Name": "adult blue dracolich",
        "CR": "17",
        "Env": [],
        "NPC": True
    },
    {
        "Name": "death knight",
        "CR": "17",
        "Env": [],
        "NPC": True
    },
    {
        "Name": "goristro",
        "CR": "17",
        "Env": []
    },
    {
        "Name": "demilich not in lair",
        "CR": "18",
        "Env": [],
        "NPC": True
    },
    {
        "Name": "balor",
        "CR": "19",
        "Env": []
    },
    {
        "Name": "demilich in lair",
        "CR": "20",
        "Env": [],
        "NPC": True
    },
    {
        "Name": "pit fiend",
        "CR": "20",
        "Env": []
    },
    {
        "Name": "lich not in lair",
        "CR": "21",
        "Env": []
    },
    {
        "Name": "solar",
        "CR": "21",
        "Env": [],
        "NPC": True
    },
    {
        "Name": "lich in lair",
        "CR": "22",
        "Env": []
    },
    {
        "Name": "Empyrean",
        "CR": "23",
        "Env": []
    },
    # Volo's Guide to Monsters
    {
        "Name": "gnoll witherling",
        "CR": "1/4",
        "Env": ["arctic", "forest", "grassland", "hill"]
    },
    {
        "Name": "gnoll hunter",
        "CR": "1/2",
        "Env": ["arctic", "forest", "grassland", "hill"]
    },
    {
        "Name": "gnolll flesh gnawer",
        "CR": "1",
        "Env": ["arctic", "forest", "grassland", "hill"]
    },
    {
        "Name": "guard drake white",
        "CR": "2",
        "Env": ["arctic", "urban"]
    },
    {
        "Name": "warlock of the archfey",
        "CR": "4",
        "Env": ["arctic", "swamp", "urban"],
        "NPC": True
    },
    {
        "Name": "warlock of the great old one",
        "CR": "6",
        "Env": ["arctic", "hill", "mountain", "urban"],
        "NPC": True
    },
    {
        "Name": "bheur hag",
        "CR": "7",
        "Env": ["arctic"],
        "NPC": True
    },
    {
        "Name": "warlock of the fiend",
        "CR": "7",
        "Env": ["arctic", "desert", "underdark", "urban"],
        "NPC": True
    },
    {
        "Name": "shoosuva",
        "CR": "8",
        "Env": ["arctic", "forest", "grassland", "hill"]
    },
    {
        "Name": "flind",
        "CR": "9",
        "Env": ["arctic", "forest", "grassland", "hill"]
    },
    {
        "Name": "frost giant everlasting one",
        "CR": "12",
        "Env": ["arctic", "coastal"]
    },
    {
        "Name": "storm giant quintessent",
        "CR": "16",
        "Env": ["arctic", "coastal", "underwater"]
    },
    {
        "Name": "dolphin",
        "CR": "1/8",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "dimetrodon",
        "CR": "1/4",
        "Env": ["coastal", "swamp"]
    },
    {
        "Name": "sea spawn",
        "CR": "1",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "quetzalcoatlus",
        "CR": "2",
        "Env": ["coastal", "hill"]
    },
    {
        "Name": "deep scion",
        "CR": "3",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "swashbuckler",
        "CR": "3",
        "Env": ["coastal", "urban"]
    },
    {
        "Name": "kraken priest",
        "CR": "5",
        "Env": ["coastal", "underwater"],
        "NPC": True
    },
    {
        "Name": "stone giant dreamwalker",
        "CR": "10",
        "Env": ["coastal", "hill", "mountain"]
    },
    {
        "Name": "morkoth",
        "CR": "11",
        "Env": ["coastal", "underwater"]
    },
    {
        "Name": "ki-rin",
        "CR": "12",
        "Env": ["coastal", "grassland", "mountain"]
    },
    {
        "Name": "firenewt",
        "CR": "1/2",
        "Env": ["desert", "hill", "mountain", "underdark"]
    },
    {
        "Name": "vargouille",
        "CR": "1",
        "Env": ["desert", "swamp", "underdark"]
    },
    {
        "Name": "guard drake blue",
        "CR": "2",
        "Env": ["desert", "urban"]
    },
    {
        "Name": "yuan-ti broodguard",
        "CR": "2",
        "Env": ["desert", "forest", "underdark"]
    },
    {
        "Name": "leucrotta",
        "CR": "3",
        "Env": ["desert", "grassland"]
    },
    {
        "Name": "yuan-ti mind whisperer",
        "CR": "4",
        "Env": ["desert", "forest", "underdark"]
    },
    {
        "Name": "yuan-ti nightmare speaker",
        "CR": "4",
        "Env": ["desert", "forest", "underdark"]
    },
    {
        "Name": "spawn of Kyuss",
        "CR": "5",
        "Env": ["desert", "underdark"]
    },
    {
        "Name": "tlincalli",
        "CR": "5",
        "Env": ["desert"]
    },
    {
        "Name": "yuan-ti pit master",
        "CR": "5",
        "Env": ["desert", "forest", "underdark"]
    },
    {
        "Name": "champion",
        "CR": "9",
        "Env": ["desert", "urban"]
    },
    {
        "Name": "necromancer",
        "CR": "9",
        "Env": ["desert", "urban"],
        "NPC": True
    },
    {
        "Name": "war priest",
        "CR": "9",
        "Env": ["desert", "urban"],
        "NPC": True
    },
    {
        "Name": "yuan-ti anathema",
        "CR": "12",
        "Env": ["desert", "forest", "underdark"]
    },
    {
        "Name": "boggle",
        "CR": "1/8",
        "Env": ["forest", "hill", "underdark", "urban"]
    },
    {
        "Name": "grung",
        "CR": "1/4",
        "Env": ["forest"]
    },
    {
        "Name": "kobold inventor",
        "CR": "1/4",
        "Env": ["forest", "hill", "mountain", "underdark", "inventor"]
    },
    {
        "Name": "vegepygmy",
        "CR": "1/4",
        "Env": ["forest", "swamp"]
    },
    {
        "Name": "velociraptor",
        "CR": "1/4",
        "Env": ["forest", "grassland"]
    },
    {
        "Name": "darkling",
        "CR": "1/2",
        "Env": ["forest", "swamp", "underdark", "urban"]
    },
    {
        "Name": "orc nurtured one of yurtrus",
        "CR": "1/2",
        "Env": ["forest", "grassland", "hill", "mountain", "underdark"]
    },
    {
        "Name": "deinonychus",
        "CR": "1",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "grung wildling",
        "CR": "1",
        "Env": ["forest"]
    },
    {
        "Name": "kobold dragonshield",
        "CR": "1",
        "Env": ["forest", "hill", "mountain", "underdark"]
    },
    {
        "Name": "kobold scale sorcerer",
        "CR": "1",
        "Env": ["forest", "hill", "mountain", "underdark", "urban"]
    },
    {
        "Name": "nilbog",
        "CR": "1",
        "Env": ["forest", "hill", "underdark"]
    },
    {
        "Name": "quickling",
        "CR": "1",
        "Env": ["forest"]
    },
    {
        "Name": "thorny",
        "CR": "1",
        "Env": ["forest", "swamp"]
    },
    {
        "Name": "darkling elder",
        "CR": "2",
        "Env": ["forest", "swamp", "underdark"]
    },
    {
        "Name": "grung elite warrior",
        "CR": "2",
        "Env": ["forest"]
    },
    {
        "Name": "guard drake green",
        "CR": "2",
        "Env": ["forest", "urban"]
    },
    {
        "Name": "hobgoblin iron shadow",
        "CR": "2",
        "Env": ["forest", "grassland", "hill"],
        "NPC": True
    },
    {
        "Name": "meenlock",
        "CR": "2",
        "Env": ["forest", "swamp", "urban"]
    },
    {
        "Name": "orc hand of yurtrus",
        "CR": "2",
        "Env": ["forest", "grassland", "hill", "mountain", "underdark"]
    },
    {
        "Name": "shadow mastiff",
        "CR": "2",
        "Env": ["forest", "hill", "swamp"]
    },
    {
        "Name": "vegepygmy chief",
        "CR": "2",
        "Env": ["forest", "swamp"],
        "NPC": True
    },
    {
        "Name": "archer",
        "CR": "3",
        "Env": ["forest", "urban"]
    },
    {
        "Name": "flail snail",
        "CR": "3",
        "Env": ["forest", "swamp", "underdark"]
    },
    {
        "Name": "orc red fang of shargaas",
        "CR": "3",
        "Env": ["forest", "hill", "mountain", "underdark", "urban"]
    },
    {
        "Name": "redcap",
        "CR": "3",
        "Env": ["forest", "hill", "swamp"]
    },
    {
        "Name": "barghest",
        "CR": "4",
        "Env": ["forest", "grassland", "hill", "mountain", "underdark"]
    },
    {
        "Name": "girallon",
        "CR": "4",
        "Env": ["forest"]
    },
    {
        "Name": "hobgoblin devastator",
        "CR": "4",
        "Env": ["forest", "grassland", "hill"],
        "NPC": True
    },
    {
        "Name": "orc blade of ilneval",
        "CR": "4",
        "Env": ["forest", "grassland", "hill", "mountain", "underdark"]
    },
    {
        "Name": "stegosaurus",
        "CR": "4",
        "Env": ["forest", "grassland"]
    },
    {
        "Name": "yeth hound",
        "CR": "4",
        "Env": ["forest", "grassland", "hill"]
    },
    {
        "Name": "brontosaurus",
        "CR": "5",
        "Env": ["forest", "grassland"]
    },
    {
        "Name": "wood woad",
        "CR": "5",
        "Env": ["forest"]
    },
    {
        "Name": "korred",
        "CR": "7",
        "Env": ["forest"]
    },
    {
        "Name": "archdruid",
        "CR": "12",
        "Env": ["forest", "mountain", "swamp", "underwater"],
        "NPC": True
    },
    {
        "Name": "cow",
        "CR": "1/4",
        "Env": ["grassland", "underdark", "urban"]
    },
    {
        "Name": "hadrosaurus",
        "CR": "1/4",
        "Env": ["grassland"]
    },
    {
        "Name": "aurochs",
        "CR": "2",
        "Env": ["grassland", "hill", "mountain"]
    },
    {
        "Name": "stegosaurus",
        "CR": "3",
        "Env": ["grassland"]
    },
    {
        "Name": "mouth of grolantor",
        "CR": "6",
        "Env": ["grassland", "hill"]
    },
    {
        "Name": "neogi hatchling",
        "CR": "1/8",
        "Env": ["hill", "underdark"]
    },
    {
        "Name": "xvart",
        "CR": "1/8",
        "Env": ["hill", "underdark"]
    },
    {
        "Name": "firenewt warlock of imix",
        "CR": "1",
        "Env": ["hill", "mountain", "underdark"]
    },
    {
        "Name": "giant strider",
        "CR": "1",
        "Env": ["hill", "mountain", "underdark"]
    },
    {
        "Name": "xvart marlock of raxivort",
        "CR": "1",
        "Env": ["hill", "underdark"]
    },
    {
        "Name": "quetzalcoatlus",
        "CR": "2",
        "Env": ["hill", "mountain"]
    },
    {
        "Name": "neogi",
        "CR": "3",
        "Env": ["hill", "underdark"]
    },
    {
        "Name": "neogi master",
        "CR": "4",
        "Env": ["hill", "underdark"]
    },
    {
        "Name": "tanarukk",
        "CR": "5",
        "Env": ["hill", "mountain", "underdark"]
    },
    {
        "Name": "annis hag",
        "CR": "6",
        "Env": ["hill", "mountain"],
        "NPC": True
    },
    {
        "Name": "guard drake red",
        "CR": "2",
        "Env": ["mountain", "underdark", "urban"]
    },
    {
        "Name": "cloud giant smiling one",
        "CR": "11",
        "Env": ["mountain"]
    },
    {
        "Name": "fire giant dreadnought",
        "CR": "14",
        "Env": ["mountain", "underdark"]
    },
    {
        "Name": "dimetrodon",
        "CR": "1/4",
        "Env": ["swamp"]
    },
    {
        "Name": "swarm of rot grubs",
        "CR": "1/2",
        "Env": ["swamp", "underdark"]
    },
    {
        "Name": "vargouille",
        "CR": "1",
        "Env": ["swamp", "underdark"]
    },
    {
        "Name": "guard drake black",
        "CR": "2",
        "Env": ["swamp", "urban"]
    },
    {
        "Name": "catoblepas",
        "CR": "5",
        "Env": ["swamp"]
    },
    {
        "Name": "froghemoth",
        "CR": "10",
        "Env": ["swamp", "underdark"]
    },
    {
        "Name": "cranium rat",
        "CR": "0",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "chitine",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "gazer",
        "CR": "1/2",
        "Env": ["underdark"]
    },
    {
        "Name": "cave fisher",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "choldrith",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "neogi",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "slithering tracker",
        "CR": "3",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "trapper",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "babau",
        "CR": "4",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "mindwitness",
        "CR": "5",
        "Env": ["underdark"]
    },
    {
        "Name": "swarm of cranium rats",
        "CR": "5",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "draegloth",
        "CR": "7",
        "Env": ["underdark"]
    },
    {
        "Name": "blackguard",
        "CR": "8",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "ulithharid",
        "CR": "9",
        "Env": ["underdark"]
    },
    {
        "Name": "ashoon",
        "CR": "10",
        "Env": ["underdark"]
    },
    {
        "Name": "death kiss",
        "CR": "10",
        "Env": ["underdark"]
    },
    {
        "Name": "devourer",
        "CR": "13",
        "Env": ["underdark"]
    },
    {
        "Name": "neothelid",
        "CR": "13",
        "Env": ["underdark"]
    },
    {
        "Name": "elder brain",
        "CR": "14",
        "Env": ["underdark"]
    },
    {
        "Name": "mind flayer lich",
        "CR": "22",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "apprentice",
        "CR": "1/8",
        "Env": ["urban"]
    },
    {
        "Name": "bard",
        "CR": "2",
        "Env": ["urban"]
    },
    {
        "Name": "illusionist",
        "CR": "3",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "martial arts adept",
        "CR": "3",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "banderhobb",
        "CR": "5",
        "Env": ["urban"]
    },
    {
        "Name": "enchanter",
        "CR": "5",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "master thief",
        "CR": "5",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "transmuter",
        "CR": "5",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "bodak",
        "CR": "6",
        "Env": ["urban"]
    },
    {
        "Name": "conjurer",
        "CR": "6",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "diviner",
        "CR": "8",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "abjurer",
        "CR": "9",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "evoker",
        "CR": "9",
        "Env": ["urban"],
        "NPC": True
    },
    {
        "Name": "warlord",
        "CR": "12",
        "Env": ["urban"],
        "NPC": True
    },
    # Mordenkainen's Tome of Foes
    {
        "Name":
        "vampiric mist",
        "CR":
        "3",
        "Env": [
            "arctic", "coastal", "forest", "grassland", "mountain", "swamp",
            "underdark", "urban"
        ]
    },
    {
        "Name":
        "the lost",
        "CR":
        "7",
        "Env": [
            "arctic", "desert", "forest", "mountain", "swamp", "underdark",
            "urban"
        ]
    },
    {
        "Name": "frost salamander",
        "CR": "9",
        "Env": ["arctic"]
    },
    {
        "Name": "winter eladrin",
        "CR": "10",
        "Env": ["arctic", "forest"],
        "NPC": True
    },
    {
        "Name": "boneclaw",
        "CR": "12",
        "Env": ["arctic", "desert", "urban"]
    },
    {
        "Name": "dire troll",
        "CR": "13",
        "Env": ["arctic", "forest", "hill", "mountain", "underdark"]
    },
    {
        "Name": "nightwalker",
        "CR": "20",
        "Env": ["arctic", "desert", "swamp", "underdark"]
    },
    {
        "Name": "elder tempest",
        "CR": "23",
        "Env": ["arctic", "grassland", "hill", "mountain"]
    },
    {
        "Name": "tortle",
        "CR": "1/4",
        "Env": ["coastal"]
    },
    {
        "Name": "skulk",
        "CR": "1/2",
        "Env": ["coastal", "forest", "swamp", "underdark", "urban"]
    },
    {
        "Name": "tortle druid",
        "CR": "2",
        "Env": ["coastal"]
    },
    {
        "Name": "merrenoloth",
        "CR": "3",
        "Env": ["coastal"]
    },
    {
        "Name": "canoloth",
        "CR": "8",
        "Env": ["coastal", "underdark", "urban"]
    },
    {
        "Name": "balhannoth",
        "CR": "11",
        "Env": ["coastal", "mountain", "underdark"]
    },
    {
        "Name": "spirit troll",
        "CR": "11",
        "Env": ["coastal", "forest", "swamp", "underdark"]
    },
    {
        "Name": "eidolon",
        "CR": "12",
        "Env": ["coastal", "desert", "forest", "mountain", "urban"]
    },
    {
        "Name": "wastrilith",
        "CR": "13",
        "Env": ["coastal", "swamp", "underdark"]
    },
    {
        "Name": "blue abishai",
        "CR": "17",
        "Env": ["coastal", "urban"]
    },
    {
        "Name": "nagpa",
        "CR": "17",
        "Env": ["coastal", "desert", "forest", "swamp", "underdark", "urban"]
    },
    {
        "Name": "levithan",
        "CR": "20",
        "Env": ["cosatal", "underwater"]
    },
    {
        "Name": "elder tempest",
        "CR": "23",
        "Env": ["coastal", "grassland", "hill", "mountain"]
    },
    {
        "Name": "young kruthik",
        "CR": "1/8",
        "Env": ["desert", "mountain", "underdark"]
    },
    {
        "Name":
        "meazel",
        "CR":
        "1",
        "Env": [
            "desert", "forest", "grassland", "hill", "mountain", "swamp",
            "underdark", "urban"
        ]
    },
    {
        "Name": "stone cursed",
        "CR": "1",
        "Env": ["desert", "mountain", "urban"]
    },
    {
        "Name": "adult kruthik",
        "CR": "2",
        "Env": ["desert", "mountain", "underdark"]
    },
    {
        "Name": "berbalang",
        "CR": "2",
        "Env": ["desert"]
    },
    {
        "Name": "dybbuk",
        "CR": "4",
        "Env": ["desert", "urban"]
    },
    {
        "Name": "kruthik hive lord",
        "CR": "5",
        "Env": ["desert", "mountain", "underdark"]
    },
    {
        "Name": "howler",
        "CR": "8",
        "Env": ["desert", "grassland", "hill", "underdark"]
    },
    {
        "Name": "rot troll",
        "CR": "9",
        "Env": ["desert", "forest", "swamp", "underdark"]
    },
    {
        "Name": "the lonely",
        "CR": "9",
        "Env": ["desert", "mountain", "underdark", "urban"]
    },
    {
        "Name": "githyanki gish",
        "CR": "10",
        "Env": ["desert", "mountain", "urban"],
        "NPC": True
    },
    {
        "Name": "githzerai enlightened",
        "CR": "10",
        "Env": ["desert", "mountain", "urban"],
        "NPC": True
    },
    {
        "Name": "orthon",
        "CR": "10",
        "Env": ["desert", "underdark", "urban"]
    },
    {
        "Name": "summer eladrin",
        "CR": "10",
        "Env": ["desert", "forest"],
        "NPC": True
    },
    {
        "Name": "githyanki kith'rak",
        "CR": "12",
        "Env": ["desert", "mountain", "urban"],
        "NPC": True
    },
    {
        "Name": "oinoloth",
        "CR": "12",
        "Env": ["desert", "underdark"]
    },
    {
        "Name": "githyanki supreme commander",
        "CR": "14",
        "Env": ["desert", "mountain", "urban"],
        "NPC": True
    },
    {
        "Name": "retriever",
        "CR": "14",
        "Env": ["desert", "forest", "underdark"]
    },
    {
        "Name": "skull lord",
        "CR": "15",
        "Env": ["desert", "swamp", "underdark"]
    },
    {
        "Name": "phoenix",
        "CR": "16",
        "Env": ["desert", "mountain"]
    },
    {
        "Name": "zaratan",
        "CR": "22",
        "Env": ["desert", "forest", "hill", "mountain", "underdark"]
    },
    {
        "Name": "bronze scout",
        "CR": "1",
        "Env": ["forest", "grassland", "mountain"]
    },
    {
        "Name": "choker",
        "CR": "1",
        "Env": ["forest", "mountain", "underdark"]
    },
    {
        "Name": "iron cobra",
        "CR": "4",
        "Env": ["forest", "grassland", "hill", "mountain"]
    },
    {
        "Name": "stone defender",
        "CR": "4",
        "Env": ["forest", "grassland", "hill", "mountain"]
    },
    {
        "Name": "oaken bolter",
        "CR": "5",
        "Env": ["forest", "grassland", "hill", "mountain"]
    },
    {
        "Name": "shadow dancer",
        "CR": "7",
        "Env": ["forest", "underdark", "urban"]
    },
    {
        "Name": "venom troll",
        "CR": "7",
        "Env": ["forest", "swamp", "underdark"]
    },
    {
        "Name": "corpse flower",
        "CR": "8",
        "Env": ["forest", "swamp", "urban"]
    },
    {
        "Name": "autumn eladrin",
        "CR": "10",
        "Env": ["forest"],
        "NPC": True
    },
    {
        "Name": "ogre bolt launcher",
        "CR": "2",
        "Env": ["grassland", "hill", "mountain"]
    },
    {
        "Name": "ogre howdah",
        "CR": "2",
        "Env": ["grassland", "hill", "mountain"]
    },
    {
        "Name": "ogre chain brute",
        "CR": "3",
        "Env": ["grassland", "hill", "mountain"]
    },
    {
        "Name": "sword wraith warrior",
        "CR": "3",
        "Env": ["grassland", "swamp"]
    },
    {
        "Name": "ogre battering ram",
        "CR": "4",
        "Env": ["grassland", "hill", "mountain"]
    },
    {
        "Name": "sword wraith commander",
        "CR": "8",
        "Env": ["grassland", "swamp"],
        "NPC": True
    },
    {
        "Name": "spring eladrin",
        "CR": "10",
        "Env": ["grassland", "forest"]
    },
    {
        "Name": "cadaver collector",
        "CR": "14",
        "Env": ["grassland"]
    },
    {
        "Name": "gray render",
        "CR": "12",
        "Env": ["hill"]
    },
    {
        "Name": "derro",
        "CR": "1/4",
        "Env": ["mountain", "underdark"]
    },
    {
        "Name": "stap spawn grue",
        "CR": "1/4",
        "Env": ["mountain", "swamp"]
    },
    {
        "Name": "duergar soulblade",
        "CR": "1",
        "Env": ["mountain", "underdark"]
    },
    {
        "Name": "duergar hammerer",
        "CR": "2",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "duergar kavalrachni",
        "CR": "2",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "duergar mind master",
        "CR": "2",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "duergar stone guard",
        "CR": "2",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "duergar xarrorn",
        "CR": "2",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "duergar screamer",
        "CR": "3",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "duergar warlord",
        "CR": "6",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "duergar despot",
        "CR": "12",
        "Env": ["mountain", "underdark"],
        "NPC": True
    },
    {
        "Name": "star spawn seer",
        "CR": "13",
        "Env": ["mountain", "swamp", "urban"]
    },
    {
        "Name": "star spawn larva mage",
        "CR": "16",
        "Env": ["mountain"]
    },
    {
        "Name": "red abishai",
        "CR": "19",
        "Env": ["mountain", "urban"]
    },
    {
        "Name": "oblex spawn",
        "CR": "1/4",
        "Env": ["swamp", "underdark", "urban"]
    },
    {
        "Name": "the wretched",
        "CR": "1/4",
        "Env": ["swamp", "underdark", "urban"]
    },
    {
        "Name": "adult oblex",
        "CR": "5",
        "Env": ["swamp", "underdark", "urban"]
    },
    {
        "Name": "allip",
        "CR": "5",
        "Env": ["swamp", "urban"]
    },
    {
        "Name": "maurezhi",
        "CR": "7",
        "Env": ["swamp", "urban"]
    },
    {
        "Name": "elder oblex",
        "CR": "10",
        "Env": ["swamp", "urban"]
    },
    {
        "Name": "male steeder",
        "CR": "1/4",
        "Env": ["underdark"]
    },
    {
        "Name": "female steeder",
        "CR": "1",
        "Env": ["underdark"]
    },
    {
        "Name": "derro savant",
        "CR": "3",
        "Env": ["underdark"]
    },
    {
        "Name": "armanite",
        "CR": "7",
        "Env": ["underdark"]
    },
    {
        "Name": "dhergoloth",
        "CR": "7",
        "Env": ["underdark"]
    },
    {
        "Name": "drow house captain",
        "CR": "9",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "gloom weaver",
        "CR": "9",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "alkilith",
        "CR": "11",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "drow shadowblade",
        "CR": "11",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "soul monger",
        "CR": "11",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "drow arachnomancer",
        "CR": "13",
        "Env": ["underdark"]
    },
    {
        "Name": "the angry",
        "CR": "13",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "drow inquisitor",
        "CR": "14",
        "Env": ["underdark"]
    },
    {
        "Name": "nabassu",
        "CR": "14",
        "Env": ["underdark", "urban"]
    },
    {
        "Name": "drow favored consort",
        "CR": "18",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "sibriex",
        "CR": "18",
        "Env": ["underdark"]
    },
    {
        "Name": "drow matron mother",
        "CR": "20",
        "Env": ["underdark"],
        "NPC": True
    },
    {
        "Name": "giff",
        "CR": "3",
        "Env": ["urban"]
    },
    {
        "Name": "deathlock",
        "CR": "4",
        "Env": ["urban"]
    },
    {
        "Name": "white abishai",
        "CR": "6",
        "Env": ["urban"]
    },
    {
        "Name": "black abishai",
        "CR": "7",
        "Env": ["urban"]
    },
    {
        "Name": "deathlock mastermind",
        "CR": "8",
        "Env": ["urban"]
    },
    {
        "Name": "yagnoloth",
        "CR": "11",
        "Env": ["urban"]
    },
    {
        "Name": "green abishai",
        "CR": "15",
        "Env": ["urban"]
    },
    {
        "Name": "steel predator",
        "CR": "16",
        "Env": ["urban"]
    },
    {
        "Name": "blue abishai",
        "CR": "17",
        "Env": ["urban"]
    },
    {
        "Name": "red abishai",
        "CR": "19",
        "Env": ["urban"]
    },
    {
        "Name": "baphomet",
        "CR": "23",
        "Env": []
    },
    {
        "Name": "fraz urb'luu",
        "CR": "23",
        "Env": []
    },
    {
        "Name": "juiblex",
        "CR": "23",
        "Env": []
    },
    {
        "Name": "zuggtmoy",
        "CR": "23",
        "Env": []
    },
    {
        "Name": "graz'zt",
        "CR": "23",
        "Env": []
    },
    {
        "Name": "yeenoghu",
        "CR": "24",
        "Env": []
    },
    {
        "Name": "marut",
        "CR": "25",
        "Env": []
    },
    {
        "Name": "demogorgon",
        "CR": "26",
        "Env": []
    },
    {
        "Name": "orcus",
        "CR": "26",
        "Env": []
    },
    {
        "Name": "zariel",
        "CR": "26",
        "Env": []
    },
    {
        "Name": "rutterkin",
        "CR": "2",
        "Env": []
    },
    {
        "Name": "abyssal wretch",
        "CR": "1/4",
        "Env": []
    },
    {
        "Name": "molydeus",
        "CR": "21",
        "Env": []
    },
    {
        "Name": "bael",
        "CR": "19",
        "Env": []
    },
    {
        "Name": "amnizu",
        "CR": "18",
        "Env": []
    },
    {
        "Name": "githzerai anarch",
        "CR": "16",
        "Env": []
    }
]

# ------------------------------------------------------------------------------
# Dictionary of NPCs
# ------------------------------------------------------------------------------
ALL_NPCs = [npc for npc in ALL_MONSTERS if npc.get("NPC")]

# ------------------------------------------------------------------------------
# Dictionaries of Monster Features
# ------------------------------------------------------------------------------
ALL_FEATURES = [
    "aggressive", "ambusher", "amorphous", "angelic weapons",
    "antimagic susceptibility", "avoidance", "blind senses", "blood frenzy",
    "breath weapon", "brute", "chameleon skin", "change shape", "charge",
    "charm", "constrict", "damage absorption", "damage transfer",
    "death burst", "devil sight", "dive attack", "echolocation",
    "elemental body", "enlarge", "ethearlness", "false appearance",
    "fey ancestry", "fiendish blessing", "flyby", "frightful presence",
    "grappler", "hold breath", "horrifying visage", "illumination",
    "illusory appearance", "immutable form", "incorporeal movement",
    "innate spellcasting", "inscrutable", "invisibility", "keen senses",
    "labyrinthine recall", "leadership", "legendary resistance", "life drain",
    "light sensitivity", "magic resistance", "magic weapons",
    "martial advantage", "mimicry", "nimble escape", "otherworldly perception",
    "pack tactics", "possession", "pounce", "psychic defense", "rampage",
    "read thoughts", "reckless", "redirect attack", "reel", "regeneration",
    "rejuvenation", "relentless", "shadow stealth", "shapechanger",
    "siege monster", "slippery", "spellcasting", "spider climb",
    "standing leap", "steadfast", "stench", "sunlight sensitivity",
    "superior invisibility", "sure footed", "surprise attack", "swallow",
    "teleport", "terrain camouflage", "tunneler", "turn resistance",
    "two heads", "undead fortitude", "web", "web sense", "web walker",
    "wounded fury"
]

ALL_CRs = [
    "0", "1/8", "1/4", "1/2", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21",
    "22", "23", "24", "25", "26", "27", "28", "29", "30"
]

ALL_PROFICIENCIES = {
    "0": "2",
    "1/8": "2",
    "1/4": "2",
    "1/2": "2",
    "1": "2",
    "2": "2",
    "3": "2",
    "4": "2",
    "5": "3",
    "6": "3",
    "7": "3",
    "8": "3",
    "9": "4",
    "10": "4",
    "11": "4",
    "12": "4",
    "13": "5",
    "14": "5",
    "15": "5",
    "16": "5",
    "17": "6",
    "18": "6",
    "19": "6",
    "20": "6",
    "21": "7",
    "22": "7",
    "23": "7",
    "24": "7",
    "25": "8",
    "26": "8",
    "27": "8",
    "28": "8",
    "29": "9",
    "30": "9"
}

ALL_ACs = {
    "0": "13",
    "1/8": "13",
    "1/4": "13",
    "1/2": "13",
    "1": "13",
    "2": "13",
    "3": "13",
    "4": "14",
    "5": "15",
    "6": "15",
    "7": "15",
    "8": "16",
    "9": "16",
    "10": "17",
    "11": "17",
    "12": "17",
    "13": "18",
    "14": "18",
    "15": "18",
    "16": "18",
    "17": "19",
    "18": "19",
    "19": "19",
    "20": "19",
    "21": "19",
    "22": "19",
    "23": "19",
    "24": "19",
    "25": "19",
    "26": "19",
    "27": "19",
    "28": "19",
    "29": "19",
    "30": "19"
}

ALL_HP = {
    "0": [1, 6],
    "1/8": [7, 35],
    "1/4": [36, 49],
    "1/2": [50, 70],
    "1": [71, 85],
    "2": [86, 100],
    "3": [101, 115],
    "4": [116, 130],
    "5": [131, 145],
    "6": [146, 160],
    "7": [161, 175],
    "8": [176, 190],
    "9": [191, 205],
    "10": [206, 220],
    "11": [221, 235],
    "12": [236, 250],
    "13": [251, 265],
    "14": [266, 280],
    "15": [281, 295],
    "16": [296, 310],
    "17": [311, 325],
    "18": [326, 340],
    "19": [341, 355],
    "20": [356, 400],
    "21": [401, 445],
    "22": [446, 490],
    "23": [491, 535],
    "24": [536, 580],
    "25": [581, 625],
    "26": [626, 670],
    "27": [671, 715],
    "28": [716, 760],
    "29": [761, 805],
    "30": [806, 850]
}

ALL_ATTACK_BONUSES = {
    "0": "3",
    "1/8": "3",
    "1/4": "3",
    "1/2": "3",
    "1": "3",
    "2": "3",
    "3": "4",
    "4": "5",
    "5": "6",
    "6": "6",
    "7": "6",
    "8": "7",
    "9": "7",
    "10": "7",
    "11": "8",
    "12": "8",
    "13": "8",
    "14": "8",
    "15": "8",
    "16": "9",
    "17": "10",
    "18": "10",
    "19": "10",
    "20": "10",
    "21": "11",
    "22": "11",
    "23": "11",
    "24": "12",
    "25": "12",
    "26": "12",
    "27": "13",
    "28": "13",
    "29": "13",
    "30": "14"
}

ALL_DPR = {
    "0": [0, 1],
    "1/8": [2, 3],
    "1/4": [4, 5],
    "1/2": [6, 8],
    "1": [9, 14],
    "2": [15, 20],
    "3": [21, 26],
    "4": [27, 32],
    "5": [33, 38],
    "6": [39, 44],
    "7": [45, 50],
    "8": [51, 56],
    "9": [57, 62],
    "10": [63, 68],
    "11": [69, 74],
    "12": [75, 80],
    "13": [81, 86],
    "14": [87, 92],
    "15": [93, 98],
    "16": [99, 104],
    "17": [105, 110],
    "18": [111, 116],
    "19": [117, 122],
    "20": [123, 140],
    "21": [141, 158],
    "22": [159, 176],
    "23": [177, 194],
    "24": [195, 212],
    "25": [213, 230],
    "26": [231, 248],
    "27": [249, 266],
    "28": [267, 284],
    "29": [285, 302],
    "30": [303, 320]
}

ALL_DCs = {
    "0": "13",
    "1/8": "13",
    "1/4": "13",
    "1/2": "13",
    "1": "13",
    "2": "13",
    "3": "13",
    "4": "14",
    "5": "15",
    "6": "15",
    "7": "15",
    "8": "16",
    "9": "16",
    "10": "16",
    "11": "17",
    "12": "17",
    "13": "18",
    "14": "18",
    "15": "18",
    "16": "18",
    "17": "19",
    "18": "19",
    "19": "19",
    "20": "19",
    "21": "20",
    "22": "20",
    "23": "20",
    "24": "21",
    "25": "21",
    "26": "21",
    "27": "22",
    "28": "22",
    "29": "22",
    "30": "23"
}

# ------------------------------------------------------------------------------
# Dictionary of Names
# ------------------------------------------------------------------------------

ALL_NAMES = [  # Female Dragonborn
    "Akra",
    "Aasathra",
    "Antrara",
    "Arava",
    "Biri",
    "Blendaeth",
    "Burana",
    "Chassath",
    "Daar",
    "Dentratha",
    "Doudra",
    "Driindar",
    "Eggren",
    "Farideh",
    "Findex",
    "Furrele",
    "Gesrethe",
    "Gilkass",
    "Harann",
    "Havilar",
    "Hethress",
    "Hillanot",
    "Jaxi",
    "Jezean",
    "Jheri",
    "Kadana",
    "Kava",
    "Korinn",
    "Megren",
    "Mijira",
    "Mishann",
    "Nala",
    "Nuthra",
    "Perra",
    "Pogranix",
    "Pyxrin",
    "Quespa",
    "Raiann",
    "Rezena",
    "Ruloth",
    "Saphara",
    "Savaran",
    "Sora",
    "Surina",
    "Synthrin",
    "Tatyan",
    "Thava",
    "Uadjit",
    "Vezera",
    "Zykroff",
    # Male Dragonborn
    "Adrex",
    "Arjhan",
    "Azzakh",
    "Balasar",
    "Baradad",
    "Bharash",
    "Bidreked",
    "Dadalan",
    "Dazzazn",
    "Direcris",
    "Donaar",
    "Fax",
    "Gargax",
    "Ghesh",
    "Gorbundus",
    "Greethen",
    "Heskan",
    "Hirrathak",
    "Ildrex",
    "Kaladan",
    "Kerkad",
    "Kiirith",
    "Kriv",
    "Maagog",
    "Medrash",
    "Mehen",
    "Mozikth",
    "Mreksh",
    "Mugrunden",
    "Nadarr",
    "Nithther",
    "Norkruuth",
    "Nykkan",
    "Pandjed",
    "Patrin",
    "Pijjirik",
    "Quarethon",
    "Rathkran",
    "Rhogar",
    "Rivaan",
    "Sethrekar",
    "Shamash",
    "Shedinn",
    "Srorthen",
    "Tarhun",
    "Torinn",
    "Trynnicus",
    "Valorean",
    "Vrondiss",
    "Zedaar",
    # Female Dwarf
    "Anbera",
    "Artin",
    "Audhild",
    "Balifra",
    "Barbena",
    "Bardryn",
    "Bolhild",
    "Dagnal",
    "Dariff",
    "Delre",
    "Diesa",
    "Eldeth",
    "Eridred",
    "Falkrunn",
    "Fallthra",
    "Finellen",
    "Gillydd",
    "Gunnloda",
    "Gurdis",
    "Helgret",
    "Helja",
    "Hlin",
    "Ilde",
    "Jarana",
    "Kathra",
    "Kilia",
    "Kristryd",
    "Liftrasa",
    "Marastyr",
    "Mardred",
    "Morana",
    "Nalaed",
    "Nora",
    "Nurkara",
    "Oriff",
    "Ovina",
    "Riswynn",
    "Sannl",
    "Therlin",
    "Thodris",
    "Torbera",
    "Tordrid",
    "Torgga",
    "Urshar",
    "Valida",
    "Vistra",
    "Vonana",
    "Werydd",
    "Whurdred",
    "Yurgunn",
    # Male Dwarf
    "Adrik",
    "Alberich",
    "Baern",
    "Barendd",
    "Beloril",
    "Brottor",
    "Dain",
    "Dalgal",
    "Darrak",
    "Delg",
    "Duergath",
    "Dworic",
    "Eberk",
    "Einkil",
    "Elaim",
    "Erias",
    "Fallond",
    "Fargrim",
    "Gardain",
    "Gilthur",
    "Gimgen",
    "Gimurt",
    "Harbek",
    "Kildrak",
    "Kilvar",
    "Morgran",
    "Morkral",
    "Nalral",
    "Nordak",
    "Nuraval",
    "Oloric",
    "Olunt",
    "Orsik",
    "Oskar",
    "Rangrim",
    "Reirak",
    "Rurik",
    "Taklinn",
    "Thoradin",
    "Thorin",
    "Thradal",
    "Tordek",
    "Traubon",
    "Travok",
    "Ulfgar",
    "Uraim",
    "Veit",
    "Vonbin",
    "Vondal",
    "Whurbin",
    # Female Elf
    "Adrie",
    "Ahinar",
    "Althaea",
    "Anastrianna",
    "Andraste",
    "Antinua",
    "Arara",
    "Baelitae",
    "Bethrynna",
    "Birel",
    "Caelynn",
    "Chaedi",
    "Claira",
    "Dara",
    "Drusilia",
    "Elama",
    "Enna",
    "Faral",
    "Felosial",
    "Hatae",
    "Ielenia",
    "Ilanis",
    "Irann",
    "Jarsali",
    "Jelenneth",
    "Keyleth",
    "Leshanna",
    "Lia",
    "Maiathah",
    "Malquis",
    "Meriele",
    "Mialee",
    "Myathethil",
    "Naivara",
    "Quelenna",
    "Quillathe",
    "Ridaro",
    "Sariel",
    "Shanairla",
    "Shava",
    "Silaqui",
    "Sumnes",
    "Theirastra",
    "Thiala",
    "Tiaathque",
    "Traulam",
    "Vadania",
    "Valanthe",
    "Valna",
    "Xanaphia",
    # Male Elf
    "Adran",
    "Aelar",
    "Aerdeth",
    "Ahvain",
    "Aramil",
    "Arannis",
    "Aust",
    "Azaki",
    "Beiro",
    "Berrian",
    "Caeldrim",
    "Carric",
    "Dayereth",
    "Dreali",
    "Efferil",
    "Eiravel",
    "Enialis",
    "Erdan",
    "Erevan",
    "Fivin",
    "Galinndan",
    "Gennal",
    "Hadarai",
    "Halimath",
    "Heian",
    "Himo",
    "Immeral",
    "Ivellios",
    "Korfel",
    "Lamlis",
    "Laucian",
    "Lucan",
    "Mindartis",
    "Naal",
    "Nutae",
    "Paelias",
    "Peren",
    "Quarion",
    "Riardon",
    "Rolen",
    "Soveliss",
    "Suhnae",
    "Thamior",
    "Tharivol",
    "Theren",
    "Theriatis",
    "Thervan",
    "Uthemar",
    "Vanuath",
    "Varis",
    # Female Gnome
    "Abalaba",
    "Bimpnottin",
    "Breena",
    "Buvvie",
    "Callybon",
    "Caramip",
    "Carlin",
    "Cumpen",
    "Dalaba",
    "Donella",
    "Duvamil",
    "Ella",
    "Ellyjoybell",
    "Ellywick",
    "Enidda",
    "Lilli",
    "Loopmottin",
    "Lorilla",
    "Luthra",
    "Mardnab",
    "Meena",
    "Menny",
    "Mumpena",
    "Nissa",
    "Numba",
    "Nyx",
    "Oda",
    "Oppah",
    "Orla",
    "Panana",
    "Pyntle",
    "Quilla",
    "Ranala",
    "Reddlepop",
    "Roywyn",
    "Salanop",
    "Shamil",
    "Siffress",
    "Symma",
    "Tana",
    "Tenena",
    "Tervaround",
    "Tippletoe",
    "Ulla",
    "Unvera",
    "Veloptima",
    "Virra",
    "Waywocket",
    "Yebe",
    "Zanna",
    # Male Gnome
    "Alston",
    "Alvyn",
    "Anverth",
    "Arumawann",
    "Bilbron",
    "Boddynock",
    "Brocc",
    "Burgell",
    "Cockaby",
    "Crampernap",
    "Dabbledob",
    "Delebean",
    "Dimble",
    "Eberdeb",
    "Eldon",
    "Erky",
    "Fablen",
    "Fibblestib",
    "Fonkin",
    "Frouse",
    "Frug",
    "Gerbo",
    "Gimble",
    "Glim",
    "Igden",
    "Jabble",
    "Jebeddo",
    "Kellen",
    "Kipper",
    "Namfoodle",
    "Oppleby",
    "Orryn",
    "Paggen",
    "Pallabar",
    "Pog",
    "Qualen",
    "Ribbles",
    "Rimple",
    "Roondar",
    "Sapply",
    "Seebo",
    "Senteq",
    "Sindri",
    "Umpen",
    "Warryn",
    "Wiggens",
    "Wobbles",
    "Wrenn",
    "Zaffrab",
    "Zook",
    # Halfling Female
    "Alain",
    "Andry",
    "Anne",
    "Bella",
    "Blossom",
    "Bree",
    "Callie",
    "Chenna",
    "Cora",
    "Dee",
    "Dell",
    "Eida",
    "Eran",
    "Euphemia",
    "Georgina",
    "Gynnie",
    "Harriet",
    "Jasmine",
    "Jillian",
    "Jo",
    "Kithri",
    "Lavinia",
    "Lidda",
    "Maegan",
    "Marigold",
    "Merla",
    "Myria",
    "Nedda",
    "Nikki",
    "Nora",
    "Olivia",
    "Paela",
    "Pearl",
    "Pennie",
    "Philomena",
    "Portia",
    "Robbie",
    "Rose",
    "Saral",
    "Seraphina",
    "Shaena",
    "Stacee",
    "Tawna",
    "Thea",
    "Trym",
    "Tyna",
    "Vani",
    "Verna",
    "Wella",
    "Willow",
    # Male Halfling
    "Alton",
    "Ander",
    "Bernie",
    "Bobbin",
    "Cade",
    "Callus",
    "Corrin",
    "Dannad",
    "Danniel",
    "Eddie",
    "Egart",
    "Eldon",
    "Errich",
    "Fildo",
    "Finnan",
    "Franklin",
    "Garret",
    "Garth",
    "Gilbert",
    "Gob",
    "Harol",
    "Igor",
    "Jasper",
    "Keith",
    "Kevin",
    "Lazam",
    "Lerry",
    "Lindal",
    "Lyle",
    "Merric",
    "Mican",
    "Milo",
    "Morrin",
    "Nebin",
    "Nevil",
    "Osborn",
    "Ostran",
    "Oswalt",
    "Perrin",
    "Poppy",
    "Reed",
    "Roscoe",
    "Sam",
    "Shardon",
    "Tye",
    "Ulmo",
    "Wellby",
    "Wendel",
    "Wenner",
    "Wes",
    # Female Half-Orc
    "Arha",
    "Baggi",
    "Bendoo",
    "Bilga",
    "Brakka",
    "Creega",
    "Drenna",
    "Ekk",
    "Emen",
    "Engong",
    "Fistula",
    "Gaaki",
    "Gorga",
    "Grai",
    "Greeba",
    "Grigi",
    "Gynk",
    "Hrathy",
    "Huru",
    "Ilga",
    "Kabbarg",
    "Kansif",
    "Lagazi",
    "Lezre",
    "Murgen",
    "Murook",
    "Myev",
    "Nagrette",
    "Neega",
    "Nella",
    "Nogu",
    "Oolah",
    "Ootah",
    "Ovak",
    "Ownka",
    "Puyet",
    "Reeza",
    "Shautha",
    "Silgre",
    "Sutha",
    "Tagga",
    "Tawar",
    "Tomph",
    "Ubada",
    "Vanchu",
    "Vola",
    "Volen",
    "Vorka",
    "Yevelda",
    "Zagga",
    # Male Half-Orc
    "Argran",
    "Braak",
    "Brug",
    "Cagak",
    "Dench",
    "Dorn",
    "Dren",
    "Druuk",
    "Feng",
    "Gell",
    "Gnarsh",
    "Grumbar",
    "Gubrash",
    "Hagren",
    "Henk",
    "Hogar",
    "Holg",
    "Imsh",
    "Karash",
    "Karg",
    "Keth",
    "Korag",
    "Krusk",
    "Lubash",
    "Megged",
    "Mhurren",
    "Mord",
    "Morg",
    "Nil",
    "Nybarg",
    "Odorr",
    "Ohr",
    "Rendar",
    "Resh",
    "Ront",
    "Rrath",
    "Sark",
    "Scrag",
    "Sheggen",
    "Shump",
    "Tanglar",
    "Tarak",
    "Thar",
    "Thokk",
    "Trag",
    "Ugarth",
    "Varg",
    "Vilberg",
    "Yurk",
    "Zed",
    # Female Tiefling
    "Akta",
    "Anakis",
    "Armara",
    "Astaro",
    "Aym",
    "Azza",
    "Beleth",
    "Bryseis",
    "Bune",
    "Criella",
    "Damaia",
    "Decarabia",
    "Ea",
    "Gadreel",
    "Gomory",
    "Hecat",
    "Ishte",
    "Jezebeth",
    "Kali",
    "Kallista",
    "Kasdeya",
    "Lerissa",
    "Lilith",
    "Makaria",
    "Manea",
    "Markosian",
    "Mastema",
    "Naamah",
    "Nemeia",
    "Nija",
    "Orianna",
    "Osah",
    "Phelaia",
    "Prosperine",
    "Purah",
    "Pyra",
    "Rieta",
    "Ronobe",
    "Ronwe",
    "Seddit",
    "Seere",
    "Sekhmet",
    "Semyaza",
    "Shava",
    "Shax",
    "Sorath",
    "Uzza",
    "Vapula",
    "Vepar",
    "Verin",
    # Male Tiefling
    "Abad",
    "Ahrim",
    "Akmen",
    "Amnon",
    "Andram",
    "Astar",
    "Balam",
    "Barakas",
    "Bathin",
    "Caim",
    "Chem",
    "Cimer",
    "Cressel",
    "Damakos",
    "Ekemon",
    "Euron",
    "Fenriz",
    "Forcas",
    "Habor",
    "Iados",
    "Kairon",
    "Leucis",
    "Mamnen",
    "Mantus",
    "Marbas",
    "Melech",
    "Merihim",
    "Modean",
    "Mordai",
    "Mormo",
    "Morthos",
    "Nicor",
    "Nirgel",
    "Oriax",
    "Paymon",
    "Pelaios",
    "Purson",
    "Qemuel",
    "Raam",
    "Rimmon",
    "Sammal",
    "Skamos",
    "Tethren",
    "Thamuz",
    "Therai",
    "Valafar",
    "Vassago",
    "Xappan",
    "Zepar",
    "Zephan",
    # Female Human
    "Alfhild",
    "Arnbjorg",
    "Ase",
    "Aslog",
    "Astrid",
    "Auda",
    "Audhid",
    "Bergljot",
    "Birghild",
    "Bodil",
    "Brenna",
    "Brynhild",
    "Dagmar",
    "Eerika",
    "Eira",
    "Gudrun",
    "Gunborg",
    "Gunhild",
    "Gunvor",
    "Helga",
    "Hertha",
    "Hilde",
    "Hillevi",
    "Ingrid",
    "Iona",
    "Jorunn",
    "Kari",
    "Kenna",
    "Magnhild",
    "Nanna",
    "Olga",
    "Ragna",
    "Ragnhild",
    "Ranveig",
    "Runa",
    "Saga",
    "Sigfrid",
    "Signe",
    "Sigrid",
    "Sigrunn",
    "Solveg",
    "Svanhild",
    "Thora",
    "Torborg",
    "Torunn",
    "Tove",
    "Unn",
    "Vigdis",
    "Ylva",
    "Yngvild",
    "Adelaide",
    "Agatha",
    "Agnes",
    "Alice",
    "Aline",
    "Anne",
    "Avelina",
    "Avice",
    "Beatrice",
    "Cecily",
    "Egelina",
    "Eleanor",
    "Elizabeth",
    "Ella",
    "Eloise",
    "Elysande",
    "Emeny",
    "Emma",
    "Emmeline",
    "Ermina",
    "Eva",
    "Galiena",
    "Geva",
    "Giselle",
    "Griselda",
    "Hadwisa",
    "Helen",
    "Herleva",
    "Hugolina",
    "Ida",
    "Isabella",
    "Jacoba",
    "Jane",
    "Joan",
    "Juliana",
    "Katherine",
    "Margery",
    "Mary",
    "Matilda",
    "Maynild",
    "Millicent",
    "Oriel",
    "Rohesia",
    "Rosalind",
    "Rosamund",
    "Sarah",
    "Susannah",
    "Sybil",
    "Williamina",
    "Yvonne",
    "Aelia",
    "Aemilia",
    "Agrippina",
    "Alba",
    "Antonia",
    "Aquila",
    "Augusta",
    "Aurelia",
    "Balbina",
    "Blandina",
    "Caelia",
    "Camilla",
    "Casia",
    "Claudia",
    "Cloelia",
    "Domitia",
    "Drusa",
    "Fabia",
    "Fabricia",
    "Fausta",
    "Flavia",
    "Floriana",
    "Fulvia",
    "Germana",
    "Glaucia",
    "Gratiana",
    "Hadriana",
    "Hermina",
    "Horatia",
    "Hortensia",
    "Iovita",
    "Iulia",
    "Laelia",
    "Laurentia",
    "Livia",
    "Longina",
    "Lucilla",
    "Lucretia",
    "Marcella",
    "Marcia",
    "Maxima",
    "Nona",
    "Octavia",
    "Paulina",
    "Petronia",
    "Porcia",
    "Tacita",
    "Tullia",
    "Verginia",
    "Vita",
    # Male Human
    "Agni",
    "Alaric",
    "Anvindr",
    "Arvid",
    "Asger",
    "Asmund",
    "Bjarte",
    "Bjorg",
    "Bjorn",
    "Brandr",
    "Brandt",
    "Brynjar",
    "Calder",
    "Colborn",
    "Cuyler",
    "Egil",
    "Einar",
    "Eric",
    "Erland",
    "Fiske",
    "Folkvar",
    "Fritjof",
    "Frode",
    "Geir",
    "Halvar",
    "Hemming",
    "Hjalmar",
    "Hjortr",
    "Ingimarr",
    "Ivar",
    "Knud",
    "Leif",
    "Liufr",
    "Manning",
    "Oddr",
    "Olin",
    "Ormr",
    "Ove",
    "Rannulfr",
    "Sigurd",
    "Skari",
    "Snorri",
    "Sten",
    "Stigandr",
    "Stigr",
    "Sven",
    "Trygve",
    "Ulf",
    "Vali",
    "Vidar",
    "Adam",
    "Adelard",
    "Aldous",
    "Anselm",
    "Arnold",
    "Bernard",
    "Bertram",
    "Charles",
    "Clerebold",
    "Conrad",
    "Diggory",
    "Drogo",
    "Everard",
    "Frederick",
    "Geoffrey",
    "Gerald",
    "Gilbert",
    "Godfrey",
    "Gunter",
    "Guy",
    "Henry",
    "Heward",
    "Hubert",
    "Hugh",
    "Jocelyn",
    "John",
    "Lance",
    "Manfred",
    "Miles",
    "Nicholas",
    "Norman",
    "Odo",
    "Percival",
    "Peter",
    "Ralf",
    "Randal",
    "Raymond",
    "Reynard",
    "Richard",
    "Robert",
    "Roger",
    "Roland",
    "Rolf",
    "Simon",
    "Theobald",
    "Theodoric",
    "Thomas",
    "Timm",
    "William",
    "Wymar",
    "Aelius",
    "Aetius",
    "Agrippa",
    "Albanus",
    "Albus",
    "Antonius",
    "Appius",
    "Aquilinus",
    "Atilus",
    "Augustus",
    "Aurelius",
    "Avitus",
    "Balbus",
    "Blandus",
    "Blasius",
    "Brutus",
    "Caelius",
    "Caius",
    "Casian",
    "Cassius",
    "Cato",
    "Celsus",
    "Claudius",
    "Cloelius",
    "Cnaeus",
    "Crispus",
    "Cyprianus",
    "Diocletianus",
    "Egnatius",
    "Ennius",
    "Fabricius",
    "Faustus",
    "Gaius",
    "Germanus",
    "Gnaeus",
    "Horatius",
    "Iovianus",
    "Iulius",
    "Lucilius",
    "Manius",
    "Marcus",
    "Marius",
    "Maximus",
    "Octavius",
    "Paulus",
    "Quintilian",
    "Regulus",
    "Servius",
    "Tacitus",
    "Varius"
]

# ------------------------------------------------------------------------------
# Dictionary of Plot Arcs
# ------------------------------------------------------------------------------

ALL_PLOTS = [
    "is searching for a powerful artifact", "wants to live forever",
    "wants revenge for the death of their family",
    "seeks to overthrow the government",
    "is trying to impress a love interest", "has kidnapped someone for ransom",
    "is searching for a missing person", "has lost a valuable item",
    "wants to acquire a legendary item to prolong life",
    "wants to ascend to godhood", "is trying to become undead",
    "is trying to obtain a younger body", "seeks to seize a position of power",
    "seeks to seize a title", "wants to win a contest",
    "wishes to win favor with a powerful individual",
    "is trying to place a pawn in a position of power",
    "wants to obtain an ancient artifact",
    "is trying to build a construct or magical device",
    "is carrying out a deity's wishes", "is offering sacrifices to a deity",
    "is trying to contact a lost deity or power",
    "wants to open a gate to another world",
    "is trying to fulfill an apocalyptic prophecy",
    "is enacting the vengeful will of a god",
    "is enacting the vengeful will of a patron",
    "is spreading a vile contagion", "wants to trigger a natural disaster",
    "seeks to utterly destroy a bloodline or clan",
    "wishes to prolong the life of a loved one",
    "wants to raise a dead loved one",
    "is destroying rivals for another person's affection",
    "wants to conquer a region", "is inciting a rebellion",
    "is trying to seize control of the army",
    "is working to become the power behind the throne",
    "seeks the favor of a ruler",
    "wants to avenge a past humiliation or insult",
    "wants to avenge a past imprisonment or injury",
    "seeks to recover stolen property and punish the thief",
    "wishes to control natural resources", "wishes to control trade",
    "is trying to marry into wealth", "is trying to plunder ancient ruins",
    "is stealing land", "is stealing goods", "is stealing money"
]

# ------------------------------------------------------------------------------
# Table of Difficulty Scaling
# ------------------------------------------------------------------------------

ALL_CR_SCALES = [(1, 1.0), (2, 1.5), (6, 2.0), (10, 2.5), (14, 3.0),
                 (100, 4.0)]

ALL_CR_SCALES.sort()

# ------------------------------------------------------------------------------
