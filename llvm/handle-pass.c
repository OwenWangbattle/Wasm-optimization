#include <stdio.h>
#include <stdlib.h>

int main()
{
    char file_name[] = "c-pass.txt";
    char temp_file_name[] = "temp2.txt";
    FILE *file = fopen(file_name, "r");
    FILE *temp_file = fopen(temp_file_name, "w");

    if (file == NULL || temp_file == NULL)
    {
        perror("Error opening file");
        return 1;
    }

    char ch;
    while (fread(&ch, 1, 1, file) == 1)
    {
        if (ch == ' ')
        {
            fwrite("\n", 1, 1, temp_file);
        }
        else
        {
            fwrite(&ch, 1, 1, temp_file);
        }
    }

    fclose(file);
    fclose(temp_file);

    // 替换原文件

    return 0;
}