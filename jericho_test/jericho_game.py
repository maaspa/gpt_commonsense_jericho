import openai
from jericho import FrotzEnv

openai.api_key = ""


def get_action_from_gpt(observation, valid_actions):
    prompt = f"""
You are playing Zork. Here's what you see:

{observation.strip()}

You can choose from these actions:
{', '.join(valid_actions)}

What is the best next action to take? Just respond with the action.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=20,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Initialize environment
env = FrotzEnv("z-machine-games-master/jericho-game-suite/zork1.z5")
observation, info = env.reset()
done = False

# Game loop
while not done:
    valid = env.get_valid_actions()
    print(f"\nObservation:\n{observation.strip()}")
    print(f"Valid actions: {valid}")
    
    action = get_action_from_gpt(observation, valid)
    print(f"\n>>> GPT Action: {action}")
    
    observation, reward, done, info = env.step(action)
    print(f"Reward: {reward}, Score: {info['score']}, Moves: {info['moves']}")

print(f"\nFinal Score: {info['score']} out of {env.get_max_score()}")
