#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LEN 256

void camel_to_snake(int size, char* in_str, char** out_str)
{
    int A_ascii = 'A', 
        Z_ascii = 'Z', 
        shift = 'a' - 'A';  // переменная хранит сдвиг по ascii таблице между строчными и заглавными буквами
    int counter = 1;        // переменная, которая покажет, сколько памяти нужно для выходной строки
                            // изначально равна 1, т.к. strlen не считает терминальный символ.
    char *c_inp, *c_out;
    for (c_inp = in_str; (*c_inp)!='\0' && (*c_inp)!='\n'; ++c_inp)
        if (A_ascii <= (*c_inp) && (*c_inp) <= Z_ascii)
            counter++;
    (*out_str) = (char*)malloc(size+counter);
    if (counter == 1)       // Проверим, не находится ли строка в формате snake 
    {
        strncpy((*out_str), in_str, size+1);    // Если находится, то копируем одно в другое и покидаем функцию
        return;
    }
    for (c_inp = in_str, c_out=(*out_str); c_inp - in_str != size; c_inp++, c_out++)    // иначе проходим циклом 
    {
        if ((*c_inp) == '\n' || (*c_inp) == '\0') 
        {
            *c_out = '\0';
            return;
        }
        if (A_ascii <= (*c_inp) && (*c_inp) <= Z_ascii) // Если в исходной строке встречается символ заглавной буквы, то
        {
            *c_out = '_';                                   // Добавляем символ '_'
            c_out++;                                        // Сдвигаем указатель
            *c_out = (*c_inp) + shift;                      // заменяем заглавный символ на строчной
        }
        else *c_out = *c_inp;                           // иначе копируем как есть
    }
    return;
    /*
        Изначально я планировал использовать функции стандартной библиотеки, 
        но решил, что в условиях экзамена могу потеряться в индексах, и сделал
        работающий вариант на указателях, к которым привык чуть больше
    */
}

int main()
{
    char *input_str, *out_str;
    
    input_str = (char*)malloc(MAX_LEN);
    if (input_str)          // проверим, что память выделилась корректно
    {
        fgets(input_str, MAX_LEN, stdin);   // scanf, кажется, менее безопасный, чем fgets (не говоря уже о gets)
        camel_to_snake(strlen(input_str), input_str, &out_str);
        printf("%s\n", out_str);
        free(input_str);        // Освободим память, мы ведь приличные люди
        free(out_str);
    }
    return 0;
}