def count_ones_and_zeros(data, index):
    ones_count = 0
    for line in data:
        ones_count += int(line[index])
    zeros_count = len(data) - ones_count
    return (zeros_count, ones_count)

def O2_rating(data):
    for index in range(len(data)):
        zeros, ones = count_ones_and_zeros(data, index)
        filter_by = '1' if ones >= zeros else '0'
        data = list(filter(lambda line: line[index] == filter_by, data))
        if len(data) == 1: return data[0]


def CO2_rating(data):
    for index in range(len(data)):
        zeros, ones = count_ones_and_zeros(data, index)
        filter_by = '1' if ones < zeros else '0'
        data = list(filter(lambda line: line[index] == filter_by, data))
        if len(data) == 1: return data[0]

with open('day3_input.txt') as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))

    print(int(O2_rating(lines), 2) * int(CO2_rating(lines), 2))