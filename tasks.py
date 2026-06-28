"""
AI Assignment 05 — Task Definitions
20 structured tasks the agent must solve, grouped by difficulty.
DO NOT MODIFY THIS FILE.
"""

TASKS = [
    # ══════════════════════════════════════════════════════════════════════
    #  GROUP 1 — Simple Lookups (4 tasks)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "T01",
        "dataset": "countries",
        "goal": "Find the capital of France",
        "steps_hint": ["search", "get_field"],
        "params": {
            "search_field": "name",
            "search_value": "France",
            "target_field": "capital",
        },
        "answer_type": "string",
        "expected": "Paris",
    },
    {
        "id": "T02",
        "dataset": "countries",
        "goal": "Find the population of Japan",
        "steps_hint": ["search", "get_field"],
        "params": {
            "search_field": "name",
            "search_value": "Japan",
            "target_field": "population",
        },
        "answer_type": "integer",
        "expected": 125700000,
    },
    {
        "id": "T03",
        "dataset": "products",
        "goal": "Find the price of GameStation 6",
        "steps_hint": ["search", "get_field"],
        "params": {
            "search_field": "name",
            "search_value": "GameStation 6",
            "target_field": "price",
        },
        "answer_type": "number",
        "expected": 499.99,
    },
    {
        "id": "T04",
        "dataset": "countries",
        "goal": "Find the official language of Brazil",
        "steps_hint": ["search", "get_field"],
        "params": {
            "search_field": "name",
            "search_value": "Brazil",
            "target_field": "official_language",
        },
        "answer_type": "string",
        "expected": "Portuguese",
    },

    # ══════════════════════════════════════════════════════════════════════
    #  GROUP 2 — Filtered Queries (4 tasks)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "T05",
        "dataset": "countries",
        "goal": "Find European countries with population greater than 50 million, sorted by population descending",
        "steps_hint": ["search", "filter_records", "sort_records"],
        "params": {
            "search_field": "continent",
            "search_value": "Europe",
            "filter_field": "population",
            "filter_op": "gt",
            "filter_value": 50000000,
            "sort_field": "population",
            "sort_asc": False,
            "target_field": "name",
        },
        "answer_type": "list",
        "expected": ["Russia", "Germany", "United Kingdom", "France", "Italy"],
    },
    {
        "id": "T06",
        "dataset": "products",
        "goal": "Find Electronics products with rating >= 4.5, sorted by price ascending",
        "steps_hint": ["search", "filter_records", "sort_records"],
        "params": {
            "search_field": "category",
            "search_value": "Electronics",
            "filter_field": "rating",
            "filter_op": "gte",
            "filter_value": 4.5,
            "sort_field": "price",
            "sort_asc": True,
            "target_field": "name",
        },
        "answer_type": "list",
        "expected": ["NoiseFree Buds", "GameStation 6", "UltraPhone Pro", "TurboLaptop 16"],
    },
    {
        "id": "T07",
        "dataset": "countries",
        "goal": "Find Asian countries with GDP per capita less than 5000, sorted by name ascending",
        "steps_hint": ["search", "filter_records", "sort_records"],
        "params": {
            "search_field": "continent",
            "search_value": "Asia",
            "filter_field": "gdp_per_capita",
            "filter_op": "lt",
            "filter_value": 5000,
            "sort_field": "name",
            "sort_asc": True,
            "target_field": "name",
        },
        "answer_type": "list",
        "expected": ["Bangladesh", "India", "Indonesia", "Pakistan", "Philippines", "Vietnam"],
    },
    {
        "id": "T08",
        "dataset": "products",
        "goal": "Find products with revenue greater than 500000, sorted by revenue descending",
        "steps_hint": ["filter_records", "sort_records"],
        "params": {
            "filter_field": "revenue",
            "filter_op": "gt",
            "filter_value": 500000,
            "sort_field": "revenue",
            "sort_asc": False,
            "target_field": "name",
        },
        "answer_type": "list",
        "expected": ["TurboLaptop 16", "GameStation 6", "SuperProtein Bar", "UltraPhone Pro", "RunnerShoe Elite", "NoiseFree Buds", "SkinCare Luxe Set", "FitTracker Band"],
    },

    # ══════════════════════════════════════════════════════════════════════
    #  GROUP 3 — Aggregations (4 tasks)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "T09",
        "dataset": "countries",
        "goal": "What is the total population of European countries?",
        "steps_hint": ["search", "aggregate"],
        "params": {
            "search_field": "continent",
            "search_value": "Europe",
            "agg_field": "population",
            "agg_op": "sum",
        },
        "answer_type": "number",
        "expected": 504755000.0,
    },
    {
        "id": "T10",
        "dataset": "products",
        "goal": "What is the average rating of Electronics products?",
        "steps_hint": ["search", "aggregate"],
        "params": {
            "search_field": "category",
            "search_value": "Electronics",
            "agg_field": "rating",
            "agg_op": "mean",
        },
        "answer_type": "number",
        "expected": 4.36,
    },
    {
        "id": "T11",
        "dataset": "countries",
        "goal": "What is the maximum GDP (in billions) among African countries?",
        "steps_hint": ["search", "aggregate"],
        "params": {
            "search_field": "continent",
            "search_value": "Africa",
            "agg_field": "gdp_billion",
            "agg_op": "max",
        },
        "answer_type": "number",
        "expected": 477.0,
    },
    {
        "id": "T12",
        "dataset": "products",
        "goal": "How many Sports products are there?",
        "steps_hint": ["search", "aggregate"],
        "params": {
            "search_field": "category",
            "search_value": "Sports",
            "agg_field": "name",
            "agg_op": "count",
        },
        "answer_type": "integer",
        "expected": 8,
    },

    # ══════════════════════════════════════════════════════════════════════
    #  GROUP 4 — Computed Arguments (4 tasks)
    #  These require using the output of one step as input to the next.
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "T13",
        "dataset": "countries",
        "goal": "Find European countries with GDP per capita above the European average, sorted descending",
        "steps_hint": ["search", "aggregate", "filter_records", "sort_records"],
        "params": {
            "search_field": "continent",
            "search_value": "Europe",
            "agg_field": "gdp_per_capita",
            "agg_op": "mean",
            "filter_field": "gdp_per_capita",
            "filter_op": "gt",
            "filter_value": "$agg_result",
            "sort_field": "gdp_per_capita",
            "sort_asc": False,
            "target_field": "name",
        },
        "answer_type": "list",
        "expected": ["Luxembourg", "Ireland", "Switzerland", "Norway", "Denmark", "Netherlands", "Sweden", "Canada"],
    },
    {
        "id": "T14",
        "dataset": "products",
        "goal": "Find products with price above average product price, sorted by price descending",
        "steps_hint": ["aggregate", "filter_records", "sort_records"],
        "params": {
            "agg_field": "price",
            "agg_op": "mean",
            "filter_field": "price",
            "filter_op": "gt",
            "filter_value": "$agg_result",
            "sort_field": "price",
            "sort_asc": False,
            "target_field": "name",
        },
        "answer_type": "list",
        "expected": ["WindTurbine Home", "TurboLaptop 16", "MountainBike X7", "UltraPhone Pro", "SolarPanel Kit", "DroneFlyer X2", "GameStation 6", "SmartWatch X3", "TennisPro Racket"],
    },
    {
        "id": "T15",
        "dataset": "countries",
        "goal": "Which Asian country has the highest GDP per capita?",
        "steps_hint": ["search", "sort_records", "get_field"],
        "params": {
            "search_field": "continent",
            "search_value": "Asia",
            "sort_field": "gdp_per_capita",
            "sort_asc": False,
            "target_field": "name",
        },
        "answer_type": "string",
        "expected": "Singapore",
    },
    {
        "id": "T16",
        "dataset": "countries",
        "goal": "How many countries have a population above the global average?",
        "steps_hint": ["aggregate", "filter_records", "aggregate"],
        "params": {
            "agg_field": "population",
            "agg_op": "mean",
            "filter_field": "population",
            "filter_op": "gt",
            "filter_value": "$agg_result",
            "count_field": "name",
            "count_op": "count",
        },
        "answer_type": "integer",
        "expected": 14,
    },

    # ══════════════════════════════════════════════════════════════════════
    #  GROUP 5 — Cross-Dataset + Error Handling (4 tasks)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "T17",
        "dataset": "products",
        "goal": "What is the total revenue of products originating from the United States?",
        "steps_hint": ["search", "aggregate"],
        "params": {
            "search_field": "origin_country",
            "search_value": "United States",
            "agg_field": "revenue",
            "agg_op": "sum",
        },
        "answer_type": "number",
        "expected": 3410000.0,
    },
    {
        "id": "T18",
        "dataset": "countries",
        "goal": "Find the name of the largest country by area in Asia, then look up products from that country",
        "steps_hint": ["search", "sort_records", "get_field"],
        "params": {
            "search_field": "continent",
            "search_value": "Asia",
            "sort_field": "area_km2",
            "sort_asc": False,
            "target_field": "name",
            "cross_dataset": "products",
            "cross_search_field": "origin_country",
            "cross_target_field": "name",
        },
        "answer_type": "string",
        "expected": "China",
    },
    {
        "id": "T19",
        "dataset": "products",
        "goal": "Find total revenue of Beauty products from France",
        "steps_hint": ["search", "filter_records", "aggregate"],
        "params": {
            "search_field": "category",
            "search_value": "Beauty",
            "filter_field": "origin_country",
            "filter_op": "eq",
            "filter_value": "France",
            "agg_field": "revenue",
            "agg_op": "sum",
        },
        "answer_type": "number",
        "expected": 950000.0,
    },
    {
        "id": "T20",
        "dataset": "products",
        "goal": "Find the average price of products in the nonexistent_field category",
        "steps_hint": ["search", "aggregate"],
        "params": {
            "search_field": "nonexistent_field",
            "search_value": "Test",
            "agg_field": "price",
            "agg_op": "mean",
        },
        "answer_type": "number",
        "expected": None,
    },
]
