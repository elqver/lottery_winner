from score import score


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
    values = [
        (i + 1, score(data[i])) for i in range(len(data))
    ]
    sorted_values = sorted(values, key=lambda x: x[1], reverse=True)
    for index, value in sorted_values:
        print(f'{index}: {value}: {data[index - 1][::-1]}')


if __name__ == '__main__':
    main()
