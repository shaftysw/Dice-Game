import random
import time
import os

# ---------- Utility Functions ----------

def roll_dice(sides=7):
    """Simulate rolling a multi-sided die."""
    return random.randint(1, sides)

def clear_screen():
    """Clear the terminal for readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------- Normal Mode ----------

def play_normal_mode():
    clear_screen()
    print("🎲 WELCOME TO THE DICE ROLL GAME! 🎲")
    player_name = input("Enter your name: ").strip() or "Player"
    score = 0
    goal = 50

    print("\n📜 RULES (Normal Mode):")
    print("- Reach 50 points to win.")
    print("- If you roll a 1 or 7, your score decreases by that number.")
    print("- Type 'n' when you want to stop.\n")

    while True:
        input(f"{player_name}, press Enter to roll the dice...")
        print("Rolling...", end="", flush=True)
        time.sleep(1)

        dice = roll_dice()
        print(f"\rYou rolled a {dice}!")

        # Scoring rule
        if dice in [1, 7]:
            score -= dice
            print(f"❌ Ouch! You lose {dice} points.")
        else:
            score += dice
            print(f"✅ You gain {dice} points.")

        print(f"🏆 Your current score: {score}")

        # Win/Lose conditions
        if score >= goal:
            print(f"\n🎉 Congratulations, {player_name}! You reached {goal} points and WON! 🏅")
            break
        elif score < 0:
            print(f"\n💀 Oh no, {player_name}! Your score dropped below 0. GAME OVER!")
            break

        choice = input("Roll again? (y/n): ").lower()
        if choice != "y":
            print(f"\nThanks for playing, {player_name}! Final score: {score}")
            break

# ---------- Hard Mode ----------

def play_hard_mode():
    clear_screen()
    print("💀 WELCOME TO THE ULTIMATE DICE ROLL CHALLENGE! 💀")
    player_name = input("Enter your name: ").strip() or "Player"
    score = 0
    goal = 100
    roll_count = 0
    last_roll = None

    print("\n📜 RULES (Hard Mode):")
    print("- Reach 100 points to win.")
    print("- Roll a 1 → your total score is HALVED!")
    print("- Roll a 7 → lose 7 points.")
    print("- Every 5th roll triggers a ⚠️ Risk Round.")
    print("- 15% chance of bad luck, 10% chance of lucky bonus.")
    print("- Rolling two high numbers (6 or 7) in a row gives a 🔥 combo bonus.")
    print("- You can 'bank' your score to quit safely.\n")

    while True:
        roll_count += 1
        input(f"{player_name}, press Enter to roll the dice...")
        print("🎲 Rolling...", end="", flush=True)
        time.sleep(1)

        dice = roll_dice()
        print(f"\rYou rolled a {dice}!")

        # Base scoring
        if dice == 1:
            score //= 2
            print("💀 CRITICAL FAIL! Your total score is HALVED!")
        elif dice == 7:
            score -= 7
            print("❌ Unlucky! You lose 7 points.")
        else:
            score += dice
            print(f"✅ You gain {dice} points.")

        # Combo bonus for consecutive high rolls
        if last_roll in [6, 7] and dice in [6, 7]:
            bonus = random.randint(5, 15)
            score += bonus
            print(f"🔥 COMBO! Consecutive high rolls! You gain {bonus} bonus points!")

        last_roll = dice

        # Risk round every 5th roll
        if roll_count % 5 == 0:
            print("\n⚠️ RISK ROUND! Something random happens...")
            time.sleep(1)
            event = random.choice(["bonus", "penalty", "nothing"])
            if event == "bonus":
                bonus = random.randint(5, 20)
                score += bonus
                print(f"💰 Lucky break! You gain {bonus} points!")
            elif event == "penalty":
                penalty = random.randint(10, 25)
                score -= penalty
                print(f"💣 Disaster strikes! You lose {penalty} points!")
            else:
                print("😅 You got lucky — nothing happens this time!")

        # Random events (10% good, 15% bad)
        event_chance = random.random()
        if event_chance < 0.10:
            bonus = random.randint(5, 10)
            score += bonus
            print(f"🍀 LUCKY EVENT! You gain {bonus} points!")
        elif event_chance > 0.85:
            penalty = random.randint(5, 15)
            score -= penalty
            print(f"💀 BAD LUCK! You lose {penalty} points!")

        print(f"🏆 Current score: {score}")

        # Win/Lose checks
        if score >= goal:
            print(f"\n🎉 EPIC WIN, {player_name}! You reached {goal} points and conquered Hard Mode! 🏅")
            break
        elif score < 0:
            print(f"\n☠️ GAME OVER, {player_name}! Your score dropped below 0!")
            break

        print("\nDo you want to:")
        print("1️⃣  Roll again (risk it all)")
        print("2️⃣  Bank your score and quit safely")
        choice = input("Choose 1 or 2: ").strip()

        if choice != "1":
            print(f"\n💰 You banked {score} points safely. Thanks for playing, {player_name}!")
            break

# ---------- Main Menu ----------

def main_menu():
    while True:
        clear_screen()
        print("🎲 DICE ROLL GAME MENU 🎲")
        print("========================")
        print("1️⃣  Play Normal Mode")
        print("2️⃣  Play Hard Mode")
        print("3️⃣  Exit Game")
        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            play_normal_mode()
        elif choice == "2":
            play_hard_mode()
        elif choice == "3":
            print("\n👋 Thanks for playing! See you next time!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")
            time.sleep(1)

        input("\nPress Enter to return to the main menu...")

# ---------- Run Game ----------
if __name__ == "__main__":
    main_menu()
