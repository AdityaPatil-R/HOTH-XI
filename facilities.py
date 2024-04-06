from datetime import datetime

# Function to convert time strings to datetime objects
def convert_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

# Define facilities with their respective information
facilities = {
    "John Wooden Center": {
        "Activities": {
            "Indoor Sports (e.g., Basketball)": {
                "SportCategory": "Basketball",
                "FitnessGoalCategory": ["Overall fitness", "sports training", "cardio"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "150-300"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.15-0.3"},
                "AvailableTime": {
                    "Monday": ["05:15", "21:30"],
                    "Tuesday": ["05:15", "21:30"],
                    "Wednesday": ["05:15", "21:30"],
                    "Thursday": ["05:15", "21:30"],
                    "Friday": ["05:15", "22:00"],
                    "Saturday": ["08:00", "21:30"],
                    "Sunday": ["08:00", "21:30"],
                },
            },
            "Cardiovascular Equipment (e.g., Treadmill)": {
                "SportCategory": "Cardio",
                "FitnessGoalCategory": ["Overall fitness", "muscle gain"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "150-300"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.15-0.3"},
                "AvailableTime": {
                    "Monday": ["05:15", "21:30"],
                    "Tuesday": ["05:15", "21:30"],
                    "Wednesday": ["05:15", "21:30"],
                    "Thursday": ["05:15", "21:30"],
                    "Friday": ["05:15", "22:00"],
                    "Saturday": ["08:00", "21:30"],
                    "Sunday": ["08:00", "21:30"],
                },
            },
            "Strength Training Equipment (e.g., Weightlifting Machines)": {
                "SportCategory": "Strength Training",
                "FitnessGoalCategory": ["Overall fitness", "muscle gain"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "50"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.1-0.2"},
                "AvailableTime": {
                    "Monday": ["05:15", "21:30"],
                    "Tuesday": ["05:15", "21:30"],
                    "Wednesday": ["05:15", "21:30"],
                    "Thursday": ["05:15", "21:30"],
                    "Friday": ["05:15", "22:00"],
                    "Saturday": ["08:00", "21:30"],
                    "Sunday": ["08:00", "21:30"],
                },
            },
            "Gymnastics": {
                "SportCategory": "Gymnastics",
                "FitnessGoalCategory": ["Overall fitness", "flexibility", "strength training"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "100-200"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.1-0.2"},
                "AvailableTime": {
                    "Monday – Friday": ["12:00", "21:30"],
                    "Saturday/Sunday": ["12:00", "21:30"],
                },
            },
            "Basketball": {
                "SportCategory": "Basketball",
                "FitnessGoalCategory": ["Overall fitness", "sports training", "cardio"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "150-300"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.15-0.3"},
                "AvailableTime": {
                    "Monday – Friday": ["08:00", "21:30"],
                    "Saturday/Sunday": ["09:00", "21:30"],
                },
            },
            "Rock Climbing": {
                "SportCategory": "Rock Climbing",
                "FitnessGoalCategory": ["Strength training", "adventure"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "200-400"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.2-0.4"},
                "AvailableTime": {
                    "Monday – Friday": ["10:00", "21:30"],
                    "Saturday/Sunday": ["10:00", "21:30"],
                },
            },
            # Add information for other activities
        },
    },
    "BruinFit": {
        "Activities": {
            "Cardiovascular Equipment (e.g., Treadmill)": {
                "SportCategory": "Cardio",
                "FitnessGoalCategory": ["Weight Loss", "overall fitness", "cardio"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "150-300"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.15-0.3"},
                "AvailableTime": {
                    "Monday": ["06:00", "21:30"],
                    "Tuesday": ["06:00", "21:30"],
                    "Wednesday": ["06:00", "21:30"],
                    "Thursday": ["06:00", "21:30"],
                    "Friday": ["06:00", "21:00"],
                    "Saturday": ["09:00", "18:00"],
                    "Sunday": ["09:00", "23:00"],
                },
            },
            "Strength Training Equipment (e.g., Weightlifting Machines)": {
                "SportCategory": "Strength Training",
                "FitnessGoalCategory": ["Overall fitness", "muscle gain"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "50"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.1-0.2"},
                "AvailableTime": {
                    "Monday": ["06:00", "21:30"],
                    "Tuesday": ["06:00", "21:30"],
                    "Wednesday": ["06:00", "21:30"],
                    "Thursday": ["06:00", "21:30"],
                    "Friday": ["06:00", "21:00"],
                    "Saturday": ["09:00", "18:00"],
                    "Sunday": ["09:00", "23:00"],
                },
            },
            # Add information for other activities
        },
    },
    "Drake Stadium Track": {
        "Activities": {
            "Running or walking": {
                "SportCategory": "Cardio",
                "FitnessGoalCategory": ["cardio", "sports training", "weight Loss"],
                "EnergyConsumption": {"unit": "minimal"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.001"},
                "AvailableTime": {
                    "Monday": ["06:00", "10:00", "17:00", "22:00"],
                    "Tuesday": ["06:00", "10:00", "17:00", "22:00"],
                    "Wednesday": ["06:00", "10:00", "17:00", "22:00"],
                    "Thursday": ["06:00", "10:00", "17:00", "22:00"],
                    "Friday": ["06:00", "10:00", "17:00", "22:00"],
                    "Saturday": ["09:00", "12:00"],
                    "Sunday": ["09:00", "20:00"],
                },
            },
            # Add information for other activities
        },
    },
    "Hitch Basketball Courts": {
        "Activities": {
            "Basketball": {
                "SportCategory": "Basketball",
                "FitnessGoalCategory": ["Overall fitness", "sports training", "cardio"],
                "EnergyConsumption": {"unit": "watts per hour", "value": "150-300"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.15-0.3"},
                "AvailableTime": {
                    "Monday": ["08:00", "21:30"],
                    "Tuesday": ["08:00", "21:30"],
                    "Wednesday": ["08:00", "21:30"],
                    "Thursday": ["08:00", "21:30"],
                    "Friday": ["08:00", "21:30"],
                    "Saturday": ["09:00", "21:30"],
                    "Sunday": ["09:00", "21:30"],
                },
            },
            # Add information for other activities
        },
    },
    "Intramural Field": {
        "Activities": {
            "Soccer": {
                "SportCategory": "Soccer",
                "FitnessGoalCategory": ["cardio", "weight Loss"],
                "EnergyConsumption": {"unit": "minimal"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.001"},
                "AvailableTime": {
                    "Monday": ["10:00", "22:00"],
                    "Tuesday": ["10:00", "22:00"],
                    "Wednesday": ["10:00", "22:00"],
                    "Thursday": ["10:00", "22:00"],
                    "Friday": ["09:00", "22:00"],
                    "Saturday": ["09:00", "20:00"],
                    "Sunday": ["09:00", "22:00"],
                },
            },
            # Add information for other activities
        },
    },
    "Los Angeles Tennis Courts": {
        "Activities": {
            "Tennis": {
                "SportCategory": "Tennis",
                "FitnessGoalCategory": ["cardio", "sports training", "weight Loss"],
                "EnergyConsumption": {"unit": "minimal"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.001"},
                "AvailableTime": {
                    "Monday": ["17:00", "19:00"],
                    "Tuesday": ["17:00", "19:00"],
                    "Wednesday": ["17:00", "19:00"],
                    "Thursday": ["17:00", "19:00"],
                    "Friday": ["17:00", "19:00"],
                    "Saturday": ["15:00", "22:00"],
                    "Sunday": ["15:00", "22:00"],
                },
            },
            # Add information for other activities
        },
    },
    "Sunset Canyon Recreation Center": {
        "Activities": {
            "Sand Volleyball": {
                "SportCategory": "Volleyball",
                "FitnessGoalCategory": ["cardio", "weight Loss"],
                "EnergyConsumption": {"unit": "minimal"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0"},
                "AvailableTime": {
                    "Monday": ["06:00", "21:00"],
                    "Tuesday": ["06:00", "21:00"],
                    "Wednesday": ["06:00", "21:00"],
                    "Thursday": ["06:00", "21:00"],
                    "Friday": ["06:00", "21:00"],
                    "Saturday": ["09:00", "18:00"],
                    "Sunday": ["09:00", "23:00"],
                },
            },
            "Swimming Pool": {
                "SportCategory": "Swimming",
                "FitnessGoalCategory": ["cardio", "weight Loss"],
                "EnergyConsumption": {"unit": "varies"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.2-0.4"},
                "AvailableTime": {
                    "Monday": ["06:00", "22:00"],
                    "Tuesday": ["06:00", "22:00"],
                    "Wednesday": ["06:00", "22:00"],
                    "Thursday": ["06:00", "22:00"],
                    "Friday": ["06:00", "22:00"],
                    "Saturday": ["09:00", "18:00"],
                    "Sunday": ["09:00", "23:00"],
                },
            },
            "Tennis Courts": {
                "SportCategory": "Tennis",
                "FitnessGoalCategory": ["cardio", "weight Loss"],
                "EnergyConsumption": {"unit": "minimal"},
                "CarbonFootprintEstimate": {"unit": "kg CO2e per hour", "value": "0.001"},
                "AvailableTime": {
                    "Monday": ["08:00", "19:00"],
                    "Tuesday": ["08:00", "19:00"],
                    "Wednesday": ["08:00", "19:00"],
                    "Thursday": ["08:00", "19:00"],
                    "Friday": ["08:00", "19:00"],
                    "Saturday": ["09:00", "19:00"],
                    "Sunday": ["09:00", "19:00"],
                },
            },
            # Add information for other activities
        },
    },
    # Add information for other facilities
}

# Print the facilities dictionary
print(facilities)
