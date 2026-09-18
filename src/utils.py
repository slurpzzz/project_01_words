import csv


def load_unigram(filename) -> dict[str, dict[int, int]] | None:
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            unigram = {}
            for row in reader:
                if row[0] not in unigram:
                    unigram[row[0]] = {row[1]: row[2]}
                else:
                    unigram[row[0]][row[1]] = row[2]
            return unigram
    except (FileNotFoundError, PermissionError):
        print(f'{filename} does not exist!')
    return None
