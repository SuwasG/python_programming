def madlib():
    # Story template with placeholders
    story_template = """
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}. Every day, the {noun1} would {verb1} in the {place1}.
    One day, the {noun1} met a {adjective2} {noun2}. They became friends and decided to {verb2} together.
    They had the most {adjective3} adventures, and they always {verb3} happily ever after.
    """

    # Prompts for user input
    prompts = {
        'adjective1': "Enter an adjective: ",
        'noun1': "Enter a noun: ",
        'verb1': "Enter a verb: ",
        'place1': "Enter a place: ",
        'adjective2': "Enter another adjective: ",
        'noun2': "Enter another noun: ",
        'verb2': "Enter another verb: ",
        'adjective3': "Enter yet another adjective: ",
        'verb3': "Enter a final verb: ",
    }

    # Collect user inputs
    user_inputs = {}
    for placeholder, prompt in prompts.items():
        user_inputs[placeholder] = input(prompt)

    # Fill in the story template with user inputs
    story = story_template.format(**user_inputs)

    # Print the completed story
    print("\nHere is your Madlib story:\n")
    print(story)

if __name__ == "__main__":
    madlib()
