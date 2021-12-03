def getfile(filename):
    with open(filename) as f:
        lines = tuple(
            map(
                lambda x: x.strip("\n"),
                filter(
                    lambda x: x != '',
                    f.readlines()
                )
            )
        )
    bit_len = len(lines[0])
    return lines, bit_len

def find_current_most_least(lines, index):
    z_count = 0
    o_count = 0
    for line in lines:
        if (line[index] == '0'):
            z_count += 1
        else:
            o_count += 1
    if (z_count < o_count):
        return '0', '1', z_count == o_count
    return '1', '0', z_count == o_count

def file_count(lines, bit_len):
    l_acc = []
    m_acc = []
    for i in range(bit_len):
        least, most, _ = find_current_most_least(lines, i)
        l_acc.append(least)
        m_acc.append(most)
    return l_acc, m_acc

def part_i(filename):
    lines, bit_len = getfile(filename)
    l_acc, m_acc = file_count(lines, bit_len)

    m_no = int(''.join(m_acc), base=2)
    l_no = int(''.join(l_acc), base=2)

    # Part i
    print("Part I: ", m_no * l_no)

def part_ii(filename):
    lines, bit_len = getfile(filename)
    m_lines = list(lines)
    l_lines = list(lines)
    for curr in range(bit_len):
        if(len(m_lines) > 1):
            _, most, eq = find_current_most_least(m_lines, curr)
            comp = '1' if eq else most
            m_lines = list(filter(lambda x: x[curr] == comp, m_lines))
        if (len(l_lines) > 1):
            least, _, eq = find_current_most_least(l_lines, curr)
            comp = '0' if eq else least
            l_lines = list(filter(lambda x: x[curr] == comp, l_lines))

    m_no = int(''.join(m_lines), base=2)
    l_no = int(''.join(l_lines), base=2)
    print("Part II: ", m_no * l_no)


if __name__ == '__main__':
    filename = './input.txt'
    part_i(filename)

    # Part ii
    part_ii(filename)
    


    