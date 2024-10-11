def transpose(data: list[list[str]]) -> list[list[str]]:
    return [list(row) for row in zip(*data)]


def remove_redundant_lines_in_the_end(data: list[list[str]]) -> list[list[str]]:
    for i in range(len(data)):
        if data[i][0] not in '+-=':
            return data[:i]
    return data


def read_data(path: str) -> list[list[str]]:
    with open(path, 'r') as file:
        raw_lines = file.readlines()
    lines = [line.split() for line in raw_lines]
    data = remove_redundant_lines_in_the_end(lines)

    return transpose(data)


def main():
    data = read_data('examples/1.txt')

    trans = {
        "+": 1,
        "-": 0,
        "=": -1,
    }

    data = [[trans[v] for v in d[::-1]] for d in data]
    values = [
        (i + 1, data[i]) for i in range(len(data))
    ]

    values.sort(key=lambda x: x[1], reverse=True)

    for i, v in values:
        print(f"{i}: {v}")


if __name__ == '__main__':
    main()
