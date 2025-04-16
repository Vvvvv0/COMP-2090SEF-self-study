import matplotlib.pyplot as plt
import heapq

class BattleVisualizer: # Visualization of battle results using matplotlib
    @staticmethod
    def show_results(players, boss=None):
        if boss: # Display battle result as bar charts for boss battle
            plt.figure(figsize=(10, 5))

            # Sort players by HP using max_HP
            hp_heap = [(-p.character.HP, p.name) for p in players] # Make the arrangement of player(higher HP) be lower
            heapq.heapify(hp_heap)
            sorted_players = []
            while hp_heap:
                hp, name = heapq.heappop(hp_heap) # Remove the upper player, then know who is winner
                sorted_players.append((name, -hp))
            
            # Plot player HP status
            player_hp = [p[1] for p in sorted_players]
            player_names = [p[0] for p in sorted_players]
            plt.subplot(1, 2, 1)
            plt.bar(player_names, player_hp, color=['green' if hp > 0 else 'red' for hp in player_hp])
            plt.title("Team HP Status")
            plt.ylabel("Remaining HP")
            
            plt.subplot(1, 2, 2)
            boss_hp = boss.HP
            plt.bar(["Boss"], [boss_hp], color='green' if boss_hp > 0 else 'orange')
            plt.title("Boss HP Status")
            plt.ylabel("Remaining HP")
            
            plt.suptitle("Boss Battle Results", y=1.05)
            plt.tight_layout()
            plt.show()
        else: # Player vs player
            hp_values = [p.character.HP for p in players]
            damage_values = [p.total_damage for p in players]
            names = [p.name for p in players]
            
            plt.figure(figsize=(12, 5))
            
            plt.subplot(1, 2, 1)
            hp_bars = plt.bar(names, hp_values, color=['lightgreen' if hp > 0 else 'salmon' for hp in hp_values])
            plt.title("Final HP Comparison")
            plt.ylabel("Remaining HP")
            
            for bar in hp_bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height)}',
                        ha='center', va='bottom')
            
            plt.subplot(1, 2, 2)
            damage_bars = plt.bar(names, damage_values, color=['skyblue', 'goldenrod'])
            plt.title("Total Damage Dealt")
            plt.ylabel("Damage Points")
            
            for bar in damage_bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height)}',
                        ha='center', va='bottom')
            
            winner = heapq.nlargest(1, [(p.character.HP, p.name) for p in players], key=lambda x: x[0])[0]
            result = "Draw!" if winner[0] <= 0 else f"{winner[1]} wins!"
            plt.suptitle(f"Battle Result: {result}", y=1.05, fontsize=14)
            plt.tight_layout()
            plt.show()
