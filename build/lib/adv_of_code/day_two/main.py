import os
import sys
from adv_of_code.utils.file import read_file
from adv_of_code.day_two.models import parse_round, parse_round_by_letter


for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])

file_name = sys.argv[1]
path = os.path.join(file_name)

lines = read_file(path)

legacy_rounds = [parse_round_by_letter(line) for line in lines]

print(f"Legacy score: {sum([x.player_two_score for x in legacy_rounds])}")


rounds = [parse_round(line) for line in lines]

print(f"Score: {sum([x.player_two_score for x in rounds])}")
