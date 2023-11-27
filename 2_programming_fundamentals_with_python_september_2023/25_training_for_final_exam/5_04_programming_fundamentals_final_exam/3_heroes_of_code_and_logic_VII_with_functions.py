def cast_spell(heroes_stats, hero_name, mana_needed, spell_name):
    if heroes_stats[hero_name]['mana_points'] >= mana_needed:
        heroes_stats[hero_name]['mana_points'] -= mana_needed
        print(f"{hero_name} has successfully cast {spell_name} and "
              f"now has {heroes_stats[hero_name]['mana_points']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(heroes_stats, hero_name, damage, attacker):
    heroes_stats[hero_name]['hit_points'] -= damage
    if heroes_stats[hero_name]['hit_points'] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and "
              f"now has {heroes_stats[hero_name]['hit_points']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        heroes_stats.pop(hero_name)


def recharge(heroes_stats, hero_name, mana_recovered):
    current_mana = heroes_stats[hero_name]['mana_points']
    heroes_stats[hero_name]['mana_points'] += mana_recovered
    if heroes_stats[hero_name]['mana_points'] > 200:
        heroes_stats[hero_name]['mana_points'] = 200
        mana_added = 200 - current_mana
        print(f"{hero_name} recharged for {mana_added} MP!")
    else:
        print(f"{hero_name} recharged for {mana_recovered} MP!")


def heal(heroes_stats, hero_name, hit_points_recovered):
    current_hit_points = heroes_stats[hero_name]['hit_points']
    heroes_stats[hero_name]['hit_points'] += hit_points_recovered
    if heroes_stats[hero_name]['hit_points'] > 100:
        heroes_stats[hero_name]['hit_points'] = 100
        hit_points_added = 100 - current_hit_points
        print(f"{hero_name} healed for {hit_points_added} HP!")
    else:
        print(f"{hero_name} healed for {hit_points_recovered} HP!")


def main():
    number_of_party_members = int(input())
    heroes_stats = {}

    for current_member in range(number_of_party_members):
        heroes_and_stats = input().split(" ")
        hero_name = heroes_and_stats[0]
        hit_points = int(heroes_and_stats[1])
        mana_points = int(heroes_and_stats[2])
        if hero_name not in heroes_stats:
            heroes_stats[hero_name] = {'hit_points': 0, 'mana_points': 0}
        heroes_stats[hero_name]['hit_points'] += hit_points
        heroes_stats[hero_name]['mana_points'] += mana_points

    command = input().split(" - ")

    while command[0] != "End":
        action = command[0]
        if action == "CastSpell":
            hero_name = command[1]
            mana_needed = int(command[2])
            spell_name = command[3]
            cast_spell(heroes_stats, hero_name, mana_needed, spell_name)
        elif action == "TakeDamage":
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            take_damage(heroes_stats, hero_name, damage, attacker)
        elif action == "Recharge":
            hero_name = command[1]
            mana_recovered = int(command[2])
            recharge(heroes_stats, hero_name, mana_recovered)
        elif action == "Heal":
            hero_name = command[1]
            hit_points_recovered = int(command[2])
            heal(heroes_stats, hero_name, hit_points_recovered)

        command = input().split(" - ")

    for hero, hero_info in heroes_stats.items():
        print(f"{hero}\n  HP: {hero_info['hit_points']}\n  MP: {hero_info['mana_points']}")


main()
