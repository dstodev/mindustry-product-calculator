from . import recipe

BOOST = 1.6

RECIPES = {
    "graphite": [
        recipe.Recipe("graphite", 1, 1.5, "Graphite Press", [
            ("coal", 2)
        ]),
        recipe.Recipe("graphite", 2, 0.5, "Multi-Press", [
            ("coal", 3),
            ("water", 3)
        ])
    ],
    "silicon": [
        recipe.Recipe("silicon", 1, 0.67, "Silicon Smelter", [
            ("coal", 1),
            ("sand", 2)
        ])
    ],
    "metaglass": [
        recipe.Recipe("metaglass", 1, 0.5, "Kiln", [
            ("lead", 1),
            ("sand", 1)
        ])
    ],
    "plastanium": [
        recipe.Recipe("plastanium", 1, 1, "Plastanium Compressor", [
            ("titanium", 2),
            ("oil", 15)
        ])
    ],
    "phase_fabric": [
        recipe.Recipe("phase_fabric", 1, 2, "Phase Weaver", [
            ("thorium", 4),
            ("sand", 10)
        ])
    ],
    "surge_alloy": [
        recipe.Recipe("surge_alloy", 1, 1.25, "Alloy Smelter", [
            ("titanium", 2),
            ("lead", 4),
            ("silicon", 3),
            ("copper", 3)
        ])
    ],
    "cryofluid": [
        recipe.Recipe("cryofluid", 24, 2, "Cryofluid Mixer", [
            ("titanium", 1),
            ("water", 24)
        ])
    ],
    "blast_compound": [
        recipe.Recipe("blast_compound", 1, 1.33, "Blast Mixer", [
            ("pyratite", 1),
            ("spore_pod", 1)
        ])
    ],
    "pyratite": [
        recipe.Recipe("pyratite", 1, 1.33, "Pyratite Mixer", [
            ("coal", 1),
            ("lead", 2),
            ("sand", 2)
        ])
    ],
    "slag": [
        recipe.Recipe("slag", 2, 0.17, "Melter", [
            ("scrap", 1)
        ])
    ],
    "oil": [
        recipe.Recipe("oil", 6, 0.33, "Spore Press", [
            ("spore_pod", 1)
        ]),
        recipe.Recipe("oil", 25.05, 1.67, "Oil Extractor", [
            ("sand", 1),
            ("water", 15.03)
        ])
    ],
    "sand": [
        recipe.Recipe("sand", 1, 0.67, "Pulverizer", [
            ("scrap", 1)
        ])
    ],
    "coal": [
        recipe.Recipe("coal", 1, 0.5, "Coal Centrifuge", [
            ("oil", 2.7)
        ])
    ],
    "water": [
        recipe.Recipe("water", 7.8, 1, "Water Extractor", []),
        recipe.Recipe("water", 6, 1, "Mechanical Pump", []),
        recipe.Recipe("water", 48, 1, "Rotary Pump", [])
    ],
    "spore_pod": [
        recipe.Recipe("spore_pod", 1, 2.33, "Cultivator", [
            ("water", 25.2)
        ])
    ]
}
