#include <stdlib.h>
#include <stdio.h>

unsigned int return_and(unsigned int a, unsigned int b)
{
    // Тут лучшее место, чтобы вставить проверку на то, что a <= b, но условие задачи такого не допускает
    unsigned int result = a;
    for (unsigned int i = a + 1; i <= b; ++i)
    {
        result = result & i;
        if (result == 0)        // Выйдем из цикла, если дальше его крутить бессмысленно.
            break;              // Условие можно было бы добавить в условие цикла for, но здесь получится нагляднее
    }
    return result;
}

int main()
{
    unsigned int a, b;
    scanf("%u %u", &a, &b);
    printf("%u\n", return_and(a, b));
    return 0;
}