from pathlib import Path
import time

with open(Path(__file__).parent / "test") as file:
    # Seeds
    line = file.readline().rstrip('\n').split(':')
    seeds = list(map(int, line[1].split()))
    file.readline()

    print(f"seeds: {seeds}")

    almanac = {}
    while True:
        label = file.readline().rstrip('\n').split()[0]
        almanac[label] = []
        while (line := file.readline()) and line != '\n':
            almanac[label].append(tuple(map(int, line.rstrip('\n').split())))

        almanac[label].sort(key=lambda x: x[1])
        print(f"{label}:")
        for val in almanac[label]:
            print(f"\t{val[0]:010} {val[1]:010} {val[2]:010}")
        if not line:
            break
    
    def search_almanac_mapping(mapping, index):
        for value in mapping:
            if index < value[1]:
                break
            elif index <= value[1] + value[2] - 1:
                return index + value[0] - value[1]
        return index

    start_time = time.time()

    seed_to_location = []
    for index in seeds:
        seed = index
        print(f"Seed: {seed}")
        for name, mapping in almanac.items():
            index = search_almanac_mapping(mapping, index)
            print(f"\t{name}: {index:03}")
        seed_to_location.append((seed, index))
    
    print(f"Time: {(((time.time() - start_time) / len(seeds)) * 1176123349) / 1000}")

    for mapping in sorted(seed_to_location, key=lambda x: x[1], reverse=True):
        print(f"Location: {mapping[1]}, Seed: {mapping[0]}")

    print(f"Lowest Location Number: {min(seed_to_location, key=lambda x: x[1])}")
        