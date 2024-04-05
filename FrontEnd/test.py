import json

def generate_fallacies_json(fallacies_found, **fallacies_info):
    # Create a dictionary to hold the fallacies information
    fallacies_dict = {"Fallacies_found": fallacies_found}

    # Add individual fallacies information to the dictionary
    for i in range(1, fallacies_found + 1):
        fallacy_name = fallacies_info.get(f"fallacy_{i}_name", "")
        fallacy_info = fallacies_info.get(f"fallacy_{i}_info", "")
        fallacy_mitigation = fallacies_info.get(f"fallacy_{i}_mitigation", "")
        fallacy_degree = fallacies_info.get(f"fallacy_{i}_degree", "")
        fallacies_dict[f"fallacy_{i}"] = {
            "name": fallacy_name,
            "info": fallacy_info,
            "mitigation": fallacy_mitigation,
            "degree": fallacy_degree
        }

    # Convert the dictionary to JSON format
    json_data = json.dumps(fallacies_dict, indent=4)
    
    return json_data

# Example usage:
fallacies_json = generate_fallacies_json(
    2,
    fallacy_1_name="Ad Hominem",
    fallacy_1_info="Attacking the person making the argument rather than the argument itself.",
    fallacy_1_mitigation="Focus on the argument itself and provide evidence and reasoning.",
    fallacy_1_degree="Low",
    fallacy_2_name="Straw Man",
    fallacy_2_info="Misrepresenting someone's argument to make it easier to attack.",
    fallacy_2_mitigation="Address the actual argument being made and avoid misrepresentation.",
    fallacy_2_degree="Medium"
)
print(fallacies_json)
