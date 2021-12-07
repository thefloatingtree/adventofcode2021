from time import perf_counter
import pprint

FISH_DEFAULT = 6
NEW_FISH_DEFAULT = 8

num_fish_after_days_memo = {}
def num_fish_after_days(fish):

    # Memoize
    global num_fish_after_days_memo
    if fish in num_fish_after_days_memo:
        return num_fish_after_days_memo[fish]

    f, days = fish

    offspring = 0
    new_fish = []

    for day in range(days):
        if f == 0:
            f = FISH_DEFAULT
            new_fish.append((NEW_FISH_DEFAULT, days - (day + 1)))
        else:
            f -= 1

    offspring += len(new_fish)
    for temp_fish in new_fish:
        offspring += num_fish_after_days(temp_fish)

    # Memoize
    num_fish_after_days_memo[fish] = offspring

    return offspring

def main():
    global num_fish_after_days_memo
    with open("day6_input.txt") as f:
        fish = list(map(lambda x: int(x), f.readlines()[0].split(',')))

        start = perf_counter()
        fish_counts = list(map(lambda f: num_fish_after_days((f, 256)) + 1, fish))

        # pprint.pprint(num_fish_after_days_memo)
        
        print(f"Ran in {perf_counter() - start:0.5f} seconds")
        print(sum(fish_counts))

main()