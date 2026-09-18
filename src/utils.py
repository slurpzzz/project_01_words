import csv
import sys


def load_unigram(filename) -> dict[str, dict[int, int]]:
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            unigram = {}
            for row in reader:
                row[1] = int(row[1])
                row[2] = int(row[2])
                if row[0] not in unigram:
                    unigram[row[0]] = {row[1]: row[2]}
                elif row[1] not in unigram[row[0]]:
                    unigram[row[0]][row[1]] = row[2]
                else:
                    unigram[row[0]][row[1]] += row[2]
            return unigram
    except (FileNotFoundError, PermissionError):
        print(f'{filename} does not exist!', file=sys.stderr)
    sys.exit()
