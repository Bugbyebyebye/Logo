import math
import random
import turtle

# 初始化 Turtle 画笔
pen = turtle.Turtle()
pen.speed('fastest')
pen.hideturtle()
pen.penup()
pen.setposition(0, 0)
pen.pendown()

# 全局状态
variables = {'h':100,'s':'fdkfdjk'}
functions = {}


def lexer(program):
    tokens = []
    pos = 0
    keywords = [
        'fd', 'bk', 'lt', 'rt', 'ct', 'pu', 'pd', 'ht', 'dt',
        'setpensize', 'setpencolor', 'home', 'label', 'setxy',
        'make', 'print', 'repeat', 'while', 'if', 'else', 'end',
        'random', 'sqrt', 'power', 'ln', 'log10', 'exp', 'to', 'stop'
    ]

    while pos < len(program):
        if program[pos].isdigit():
            num = ''
            while pos < len(program) and program[pos].isdigit():
                num += program[pos]
                pos += 1
            tokens.append(('num', int(num)))
        elif program[pos].isalpha() or program[pos] == '_':
            identifier = ''
            while pos < len(program) and (program[pos].isalnum() or program[pos] == '_'):
                identifier += program[pos]
                pos += 1
            if identifier in keywords:
                tokens.append((identifier, None))
            else:
                tokens.append(('id', identifier))
        elif program[pos] == '"':
            pos += 1
            string = ''
            while pos < len(program) and program[pos] != '"':
                string += program[pos]
                pos += 1
            tokens.append(('str', string))
            pos += 1  # skip closing double quote
        elif program[pos] in ['+', '-', '*', '/', '=', '<', '>']:
            tokens.append((program[pos], None))
            pos += 1
        elif program[pos] in ['(', ')', '[', ']', ',', ':']:
            tokens.append((program[pos], None))
            pos += 1
        elif program[pos] in [' ', '\t', '\r', '\n']:
            pos += 1
        else:
            pos += 1  # skip unknown character

    tokens.append(('eof', None))
    return tokens


def parser(tokens):
    pos = 0
    current_token = tokens[pos]

    def next_token():
        nonlocal pos, current_token
        pos += 1
        current_token = tokens[pos]

    def match(token_type):
        nonlocal current_token
        if current_token[0] == token_type:
            next_token()
        else:
            raise SyntaxError(f"Expected {token_type}, found {current_token[0]}")

    def program():
        commands = []
        while current_token[0] != 'eof':
            commands.append(statement())
        return 'program', commands

    def statement():
        if current_token[0] == 'fd':
            next_token()
            return 'fd', expr()
        elif current_token[0] == 'bk':
            next_token()
            return 'bk', expr()
        elif current_token[0] == 'lt':
            next_token()
            return 'lt', expr()
        elif current_token[0] == 'rt':
            next_token()
            return 'rt', expr()
        elif current_token[0] == 'ct':
            next_token()
            return 'ct', None
        elif current_token[0] == 'pu':
            next_token()
            return 'pu', None
        elif current_token[0] == 'pd':
            next_token()
            return 'pd', None
        elif current_token[0] == 'ht':
            next_token()
            return 'ht', None
        elif current_token[0] == 'dt':
            next_token()
            return 'dt', None
        elif current_token[0] == 'setpensize':
            next_token()
            return 'setpensize', expr()
        elif current_token[0] == 'setpencolor':
            next_token()
            return 'setpencolor', expr()
        elif current_token[0] == 'home':
            next_token()
            return 'home', None
        elif current_token[0] == 'label':
            next_token()
            return 'label', expr()
        elif current_token[0] == 'setxy':
            next_token()
            x = expr()
            match(',')
            y = expr()
            return 'setxy', (x, y)
        elif current_token[0] == 'make':
            next_token()
            var_name = current_token[1]
            next_token()
            var_value = expr()
            return 'make', (var_name, var_value)
        elif current_token[0] == 'print':
            next_token()
            if current_token[0] == ':':
                next_token()
            value = current_token[1]
            next_token()
            return 'print', value
        elif current_token[0] == 'repeat':
            next_token()
            n = expr()
            match('[')  # 这里可能需要注意方括号的匹配问题
            commands = []
            while current_token[0] != ']':
                commands.append(statement())
            match(']')
            return 'repeat', (n, commands)
        elif current_token[0] == 'while':
            next_token()
            cond = expr()
            match('[')  # 这里可能需要注意方括号的匹配问题
            commands = []
            while current_token[0] != ']':
                commands.append(statement())
            match(']')
            return 'while', (cond, commands)
        elif current_token[0] == 'if':
            next_token()
            cond = []
            while current_token[0] != '[':
                cond.append(current_token)
                next_token()

            match('[')  # 这里可能需要注意方括号的匹配问题
            true_commands = []
            while current_token[0] != ']':
                true_commands.append(statement())
            match(']')
            if current_token[0] == 'else':
                next_token()
                match('[')  # 这里可能需要注意方括号的匹配问题
                false_commands = []
                while current_token[0] != ']':
                    false_commands.append(statement())
                match(']')
                return 'if', (cond, true_commands, false_commands)
            else:
                return 'if', (cond, true_commands, [])
        elif current_token[0] == 'to':
            next_token()
            func_name = current_token[1]
            next_token()
            args = []
            while current_token[0] == 'id':
                args.append(current_token[1])
                next_token()
            commands = []
            while current_token[0] != 'end':
                commands.append(statement())
                if current_token[0] == 'eof':
                    raise SyntaxError("Expected 'end' keyword")
            next_token()  # consume 'end'
            functions[func_name] = (args, commands)
            return 'function', (func_name, args, commands)
        elif current_token[0] == 'random':
            next_token()
            value = current_token[1]
            next_token()
            return 'random', value
        elif current_token[0] == 'sqrt':
            next_token()
            arg = expr()
            return 'sqrt', arg
        elif current_token[0] == 'power':
            next_token()
            base = expr()
            exp = expr()
            return 'power', base, exp
        elif current_token[0] == 'ln':
            next_token()
            arg = expr()
            return 'ln', arg
        elif current_token[0] == 'log10':
            next_token()
            arg = expr()
            return 'log10', arg
        elif current_token[0] == 'exp':
            next_token()
            arg = expr()
            return 'exp', arg
        elif current_token[0] == ':':
            next_token()
            if current_token[0] == 'id':
                result = variables[current_token[1]]
                next_token()
                return 'variable', result
        elif current_token[0] == 'stop':
            next_token()
            return 'stop', None
        else:
            raise SyntaxError(f"Unexpected token: {current_token}")

    def expr():
        if current_token[0] == 'num':
            num = current_token[1]
            next_token()
            return 'num', num
        elif current_token[0] == 'str':
            str = current_token[1]
            next_token()
            return 'str', str
        elif current_token[0] == 'id':
            result = variables[current_token[1]]
            next_token()
            if type(result) == "":
                return 'str',result
            else:
                return 'num',result
        elif current_token[0] == ':':
            next_token()
            arg = expr()
            return arg
        else:
            raise SyntaxError(f"Unexpected token: {current_token}")

    tree = program()
    return tree


def interpreter(tree):
    if tree[0] == 'program':
        for statement in tree[1]:
            interpreter(statement)
    elif tree[0] == 'id':
        return variables[tree[1]]
    elif tree[0] == 'fd':
        pen.forward(interpreter_expr(tree[1]))
    elif tree[0] == 'bk':
        pen.backward(interpreter_expr(tree[1]))
    elif tree[0] == 'lt':
        pen.left(interpreter_expr(tree[1]))
    elif tree[0] == 'rt':
        pen.right(interpreter_expr(tree[1]))
    elif tree[0] == 'ct':
        pen.clear()
    elif tree[0] == 'pu':
        pen.penup()
    elif tree[0] == 'pd':
        pen.pendown()
    elif tree[0] == 'ht':
        pen.hideturtle()
    elif tree[0] == 'dt':
        pen.showturtle()
    elif tree[0] == 'setpensize':
        pen.pensize(interpreter_expr(tree[1]))
    elif tree[0] == 'setpencolor':
        pen.pencolor(*interpreter_expr(tree[1])) if isinstance(tree[1], tuple) else pen.pencolor(
            interpreter_expr(tree[1]))
    elif tree[0] == 'home':
        pen.home()
    elif tree[0] == 'label':
        pen.write(interpreter_expr(tree[1]), align='left')
    elif tree[0] == 'setxy':
        pen.setposition(interpreter_expr(tree[1][0]), interpreter_expr(tree[1][1]))
    elif tree[0] == 'make':
        arg = tree[1][1]
        variables[tree[1][0]] = interpreter_expr(arg)
        print(variables)
    elif tree[0] == 'print':

        if tree[1] in variables:
            print(variables[tree[1]])
        else:
            print(tree[1])

    elif tree[0] == 'repeat':
        n = interpreter_expr(tree[1][0])
        for _ in range(n):
            for statement in tree[1][1]:
                interpreter(statement)
    elif tree[0] == 'while':
        while interpreter_expr(tree[1][0]):
            for statement in tree[1][1]:
                interpreter(statement)
    elif tree[0] == 'if':
        if interpreter_expr(tree[1][0]):
            for statement in tree[1][1]:
                interpreter(statement)
        else:
            for statement in tree[1][2]:
                interpreter(statement)
    elif tree[0] == 'random':
        result = random.randint(0, tree[1])
        print(result)
        return result
    elif tree[0] == 'sqrt':
        result = math.sqrt(interpreter_expr(tree[1]))
        print(result)
        return result
    elif tree[0] == 'power':
        result = math.pow(interpreter_expr(tree[1]), interpreter_expr(tree[2]))
        print(result)
        return result
    elif tree[0] == 'ln':
        result = math.log(interpreter_expr(tree[1]))
        print(result)
        return result
    elif tree[0] == 'log10':
        result = math.log10(interpreter_expr(tree[1]))
        print(result)
        return result
    elif tree[0] == 'exp':
        result = math.exp(interpreter_expr(tree[1]))
        print(result)
        return result
    elif tree[0] == 'function':
        func_name = tree[1][0]
        args = tree[1][1]
        commands = tree[1][2]
        functions[func_name] = (args, commands)
    elif tree[0] == 'variable':
        value = tree[1]
        print(value)
        return value
    elif tree[0] == 'stop':
        return


def interpreter_expr(expr):
    if expr[0] == 'num':
        return expr[1]
    elif expr[0] == 'str':
        return expr[1]
    elif expr[0] == 'id':
        return variables[expr[0]]
    else:
        raise ValueError("Invalid expression type")


def run_logo_program(program):
    tokens = lexer(program)
    tree = parser(tokens)
    interpreter(tree)


if __name__ == '__main__':
    while True:
        command = input("Logo> ").strip()
        if command.lower() == "exit":
            break
        run_logo_program(command)