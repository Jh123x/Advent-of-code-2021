
with open('input.txt') as f:
    input_data = list(map(int, f.read().split()))

prev = 10000
count = 0
window_size = 3

for index in range(len(input_data) - window_size + 1):
    s = 0
    for i in range(index, index + window_size):
        s += input_data[i]
    if prev < s:
        count += 1

    prev = s
print(count)