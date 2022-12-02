import sys
import os


def find_max_calories(input: list) -> tuple[int, int]:
    max_calorie_elf = -1
    max_calorie = 0
    for i, elf_inventory in enumerate(input):
        current_cal = 0
        for cal_count in elf_inventory:
            current_cal += cal_count
        if max_calorie < current_cal:
            max_calorie = current_cal
            max_calorie_elf = i

    if max_calorie_elf == -1:
        print("No elves found")

    return max_calorie_elf, max_calorie


def find_calories_per_elf(input: list) -> list:
    elf_inventories = []
    for i, elf_inventory in enumerate(input):
        current_cal = 0
        for cal_count in elf_inventory:
            current_cal += cal_count
        elf_inventories.append(current_cal)

    return elf_inventories


def parse_file(file_path: str) -> list:
    outfile = open(file_path, "r")
    data = outfile.readlines()
    outfile.close()

    elf_inventories = []
    current_elf_inventory = []
    for line in data:
        if line.strip() == "":
            # end of elf inventoriy
            elf_inventories.append(current_elf_inventory)
            current_elf_inventory = []
        else:
            int_val = int(line)
            current_elf_inventory.append(int_val)

    elf_inventories.append(current_elf_inventory)

    return elf_inventories


# MAIN
for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])

file_name = sys.argv[1]
path = os.path.join(file_name)

input = parse_file(path)

elf_inventories = find_calories_per_elf(input)
elf_inventories.sort(reverse=True)

print(elf_inventories[0] + elf_inventories[1] + elf_inventories[2])

