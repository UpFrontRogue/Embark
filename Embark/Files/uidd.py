from extras import *
from clasd import save_universe
from datetime import datetime, timedelta

class Quest:
    def __init__(self, name, uid, character, task, stages, reward, disc):
        self.name = name
        self.uid = uid
        self.character = character
        self.task = task
        self.stages = stages
        self.reward = reward
        self.disc = disc

def add_quest(uid = None):
    prints("Adding Quest to Universe")
    print()
    quest_name = inputs("Enter the name of the quest: ")

    quest_data = {
        "Task": inputs("Enter the task of the quest: "),
        "Stages": int(inputs("Enter the number of stages for the quest: ")),
        "Reward": inputs("Enter the reward for completing the quest: "),
        "Disc": inputs("Enter the quest description: ")
    }

    if not uid:
        prints(f"No universe with UID {uid} found.")
        return

    quests = universe_data[uid].get('Quests', {})
    quests[quest_name] = Quest(quest_name, uid, None, **quest_data)

    universe_data[uid]['Quests'] = quests

    save_universe(uid)

    prints(f"Quest '{quest_name}' has been added to Universe {uid}.")
    print()
    
def add_item(uid= None):
    prints("Adding Item to Universe")
    print()
    item_name = inputs("Enter the name of the item: ")

    item_data = {
        "Type": inputs("Enter the type of the item: "),
        "Description": inputs("Enter the description of the item: "),
        "Effect": inputs("Enter the effect of the item: ")
    }

    if not uid:
        prints(f"Universe: {uid} not found.")
        return

    items = universe_data[uid].get('Items', {})
    items[item_name] = item_data

    universe_data[uid]['Items'] = items

    save_universe(uid)

    prints(f"Item '{item_name}' has been added to Universe {uid}.")
    print()

def add_enemy(uid= None):
    prints("Adding Enemy to Universe")
    print()
    enemy_name = inputs("Enter the name of the enemy: ")

    enemy_data = {
        "Type": inputs("Enter the type of the enemy: "),
        "Description": inputs("Enter the description of the enemy: "),
        "Level": int(inputs("Enter the level of the enemy: "))
    }

    if not uid:
        prints(f"Universe: {uid} not found.")
        return

    enemies = universe_data[uid].get('Enemies', {})
    enemies[enemy_name] = enemy_data

    universe_data[uid]['Enemies'] = enemies

    save_universe(uid)

    prints(f"Enemy '{enemy_name}' has been added to Universe {uid}.")
    print()

def add_npc(uid=None):
    prints("Adding NPC to Universe")
    print()
    npc_name = inputs("Enter the name of the NPC: ")

    npc_data = {
        "Type": inputs("Enter the type of the NPC: "),
        "Description": inputs("Enter the description of the NPC: "),
        "Role": inputs("Enter the role of the NPC: ")
    }

    if not uid:
        prints(f"Universe: {uid} not found.")
        return

    npcs = universe_data[uid].get('NPCs', {})
    npcs[npc_name] = npc_data

    universe_data[uid]['NPCs'] = npcs

    save_universe(uid)

    prints(f"NPC '{npc_name}' has been added to Universe {uid}.")
    print()

def universe_quests(uid):
    if uid not in universe_data:
        prints(f"No universe with UID {uid} found.")
        return

    quests_data = universe_data[uid].get('Quests', {})

    daily_quests = []
    other_quests = []

    current_time = datetime.now()

    for quest_name, quest_obj in quests_data.items():
        if quest_obj.character is None:
            # Universe quests
            other_quests.append(quest_name)
        elif quest_obj.character == 'daily' and quest_obj.uid == uid:
            # Daily quests
            quest_start_time = quest_obj.task
            completion_time = quest_start_time + timedelta(hours=quest_obj.stages * 2)  # Varying time (18-24 hrs)
            min_completion_time = quest_start_time + timedelta(minutes=45)  # Minimum time after completion

            if current_time < quest_start_time:
                remaining_time = quest_start_time - current_time
                prints(f"Quest '{quest_name}' starts in {remaining_time}.")
            elif quest_start_time <= current_time < completion_time:
                remaining_time = completion_time - current_time
                prints(f"Quest '{quest_name}' is ongoing. Time remaining: {remaining_time}.")
            elif completion_time <= current_time < min_completion_time:
                prints(f"Quest '{quest_name}' completed. Waiting for minimum time before next attempt.")
            else:
                daily_quests.append(quest_name)

    prints("Daily Quests:")
    for i, quest_name in enumerate(daily_quests, start=1):
        prints(f"{i}. {quest_name}")

    prints("\nOther Universe Quests:")
    for i, quest_name in enumerate(other_quests, start=1):
        prints(f"{i}. {quest_name}")