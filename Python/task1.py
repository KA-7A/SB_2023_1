import sys
import copy

DEFAULT  = "default"
FUNCTION = "function"
functions = {}

class Interprer:
    def parse_functions_code(self): # должен вернуть список списков формата [str, []]
        instructions = []
        while True:
            tokens = input().strip().split()
            instructions.append([tokens[0], tokens[1:]])
            if tokens[0] in ["return", "end_program"]:
                break
        return instructions


    def local_executor(self, instruction, args, variables, mode=DEFAULT):
        if instruction ==  "init":
                if args[1] in variables:
                    variables[args[0]] = variables[args[1]]
                else:
                    variables[args[0]] = int(args[1])
        elif instruction ==  "function":
                if mode == FUNCTION:
                    return (-1, "err")
                else:
                    f = self.Function(args[0], args[1:])
                    f.body = self.parse_functions_code()
                    functions[f.name] = f
        elif instruction == "end_program":
                exit(0)
        elif instruction ==  "return":      # тут у нас какой-то бардак, давайте разбираться..
                
                return_value = 0
                if args[0] in variables:
                    return_value = variables[args[0]]
                elif args[0].isnumeric():
                    return_value = int(args[0])
                else:
                    return (-1, "err")
                # print(f"Here, [return_value] = {[return_value]}")
                return [return_value]
            
        elif instruction ==  "add": # instruction = ["add", ["left_operand", "right_operand"]] ; left_operand -- имя локальной переменной, right_operand -- имя локальной переменной либо число
                if args[1] in variables:
                    variables[args[0]] += variables[args[1]]
                elif args[1].isnumeric():
                    variables[args[0]] += int(args[1])
                else:
                    return (-1, "err")
        elif instruction ==  "sub": # instruction = ["sub", ["left_operand", "right_operand"]]
                if args[1] in variables:
                    variables[args[0]] -= variables[args[1]]
                elif args[1].isnumeric():
                    variables[args[0]] -= int(args[1])
                else:
                    return (-1, "err")
        elif instruction ==  "mul": # instruction = ["mul", ["left_operand", "right_operand"]]
                if args[1] in variables:
                    variables[args[0]] *= variables[args[1]]
                elif args[1].isnumeric():
                    variables[args[0]] *= int(args[1])
                else:
                    return (-1, "err")
        elif instruction ==  "div": # instruction = ["div", ["left_operand", "right_operand"]]
                if args[1] in variables:
                    variables[args[0]] //= variables[args[1]]
                elif args[1].isnumeric():
                    variables[args[0]] //= int(args[1])
                else:
                    return (-1, "err")
            
        else:     # обрабатываем случай, когда вызывается другая функция
                if instruction in functions:
                    # print(f"Function {instruction} call received!")
                    tmp_list = copy.copy(args)
                    to_func_args = []
                    for arg in args:
                        to_func_args.append(variables[arg])
                    # print(f"to_func_args = {to_func_args}")
                    code = functions[instruction].execute(to_func_args) 
                    if code == (-1, "err"):
                        return (-1, "err")
                    else:
                        # print(f"Here 2: code = {code}, to_func_args = {to_func_args}")
                        variables[tmp_list[0]] = code[0]
                else:
                    return (-1, "err")
        

    class Function:
        def __init__(self, name, args) -> None:
            self.name = name
            self.args = args    # пойдет в список локальных переменных нах
            self.body = []      # dict(instruction_name, args = dict())

        def execute(self, args: list()):
            local_variables = {}
            for name, value in zip(self.args, args):
                local_variables[name] = value
            # print(f"local_variables : {local_variables}")
            for instruction in self.body:
                # print(f"instruction = {instruction}")
                # print(f"variables p = {local_variables}")
                tmp_executor = Interprer()
                return_value = tmp_executor.local_executor(instruction = instruction[0], args = instruction[1], variables = local_variables, mode=FUNCTION)
                # print(f"variables c = {local_variables}")
                # print("--------------------------------")
                if instruction[0] == "return":
                    return return_value



    class Parser:
        def __init__(self, f_in, f_out) -> None:
            self.f_in = f_in
            self.f_out = f_out
            self.variables = {}

        def parse(self):
            while True:
                print("-------------------------")
                print(f"variables : {self.variables}")
                print(f"functions : {functions}")
                print("-------------------------")
                tokens_string = input().strip()
                if not len(tokens_string):
                    continue
                tokens = tokens_string.split()
                tmp_executor = Interprer()
                code = tmp_executor.local_executor(tokens[0], tokens[1:], self.variables)
                if tokens[0] == "return" and (len(code) >= 2 and [1] != "err" or len(code) == 1):
                    print(code[0])
                    break
                if tokens[0] == "end_program":
                    exit(0)


def solve(f_in, f_out):
    p = Interprer.Parser(f_in, f_out)
    p.parse()
    return
            
        

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)