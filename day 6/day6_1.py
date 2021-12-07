FISH_DEFAULT = 6
NEW_FISH_DEFAULT = 8

def main():
    with open("day6_input_test_test.txt") as f:
        fish = list(map(lambda x: int(x), f.readlines()[0].split(',')))

        for _ in range(80):
            print(_, fish)
            for index, f in enumerate(fish[:]):
                if f == 0:
                    fish[index] = FISH_DEFAULT
                    fish.append(NEW_FISH_DEFAULT)
                else:
                    fish[index] -= 1
        
        print(18, fish)
        print(len(fish))


main()