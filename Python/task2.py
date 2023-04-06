def solution(in_str: str) -> str:
    stack = []                              # Воспользуемся стеком для отслеживания символов
    for symbol in in_str:
        if symbol in ['(', '{', '[']:       # Если скобка открывающая, закидываем её в стек
            stack.append(symbol)
        elif symbol in [')', '}', ']']:     # Если закрывающая...
            if len(stack) == 0:             # Проверяем, что стек имеет ненулевую длину (кол-во открытых скобок >= кол-ва закрытых)
                return "Bruh"
            last_symbol = stack.pop()       # Достаём из стека последний символ
            if last_symbol == "(" and symbol != ")":    # тут можно было воспользоваться (сравнительно) новой фишкой Питона: case match, но я решил не рисковать и интерпретатором
                return "Bruh"
            if last_symbol == "{" and symbol != "}":
                return "Bruh"
            if last_symbol == "[" and symbol != "]":
                return "Bruh"
    if len(stack) != 0:                     # Если в конце строки в стеке что-то осталось, значит кол-во открытых скобок осталось больше, чем кол-во закрытых. Нехорошо
        return "Bruh"
    return "Nice"

if __name__ == "__main__":
    print(solution(input()))
