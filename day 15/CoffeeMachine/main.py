from typing import List


def generate_user_prompt(options: List):
    user_prompt = f"What would you like? "
    if len(options) > 0:
        user_prompt += "("
        for i, current_option in enumerate(options):
            user_prompt += f"{current_option}"
            if i < len(options) - 1:
                user_prompt += "/"
        user_prompt += "): "
    else:
        user_prompt += "(no available options): "
    return user_prompt


if __name__ == '__main__':
    available_options = ["espresso", "latte", "cappuccino"]
    user_selection = input(f"{generate_user_prompt(available_options)}")
