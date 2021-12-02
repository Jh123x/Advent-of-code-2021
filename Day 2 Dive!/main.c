#include <stdio.h>

long long int getCount(char *buffer, size_t length)
{
    long long int index = 0;
    // Get the last string
    while (buffer[index] != ' ')
    {
        ++index;
    }
    ++index;
    long long int acc = 0;
    for (long long int i = 0; i < length; ++i)
    {
        acc *= 10;
        acc += buffer[index + i] - '0';
    }
    return acc;
}

int main()
{
    long long int x = 0, y = 0, a = 0;
    size_t read;
    size_t len = 0;
    char *line = NULL;

    // Read the file line by line
    FILE *fp = fopen("./input.txt", "r");
    if (fp == NULL)
    {
        printf("Error opening file\n");
        return 1;
    }
    while (read = getline(&line, &len, fp) != -1)
    {
        // Process each line
        long long int count = getCount(line, read);
        if (line[0] == 'f')
        {
            x += count;
            y += a * count;
        }
        else if (line[0] == 'd')
        {
            // y += count;
            a += count;
        }
        else if (line[0] == 'u')
        {
            // y -= count;
            a -= count;
        }
        printf("X: %lld Y: %lld Aim: %lld\n", x, y, a);
    }
    printf("Final Sum: %lld\n", x * y);
    fclose(fp);
    return 0;
}