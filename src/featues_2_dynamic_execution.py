# Executing code using exec()
def fun_exec1():
    code = """for i in range(1, 6): print(f'Number: {i}')"""

    local_scope = {}
    exec(code, {}, local_scope)
    print("Executed dynamic code with exec():\n")


fun_exec1()


# Executing code that defines a function using exec()
def fun_exec2():
    code = """def greet(name):
    return f'Hello, {name}!'"""

    local_scope = {}
    exec(code, {}, local_scope)
    res = local_scope["greet"]("World")

    print(f"{res}\n")

    return res


fun_exec2()


# Executing code using eval()
def fun_eval():
    expression = "3 * (4 + 5)"
    res = eval(expression)
    print(f"Evaluated expression '{expression}' with eval(): {res}\n")


fun_eval()


# Accesing exeisting code with eval()
def fun_eval2():
    expression = input("Enter an expression: ")
    res = eval(expression)  # Here you can type like fun_exec2()
    print(f"Result of '{expression}': {res}\n")


# fun_eval2()

#  How to use dynamic execution functions safely
# 1. Avoid executing untrusted code.
# 2. Use restricted scopes (as shown above).
# 3. Consider alternatives like ast.literal_eval() for simple expressions.
# 4. Sanitize and validate any input before execution.

# Example of safe usage


def fun_safe_eval():
    expression = input("Enter an expression: ")

    local_scope = {"a": 1, "b": 2, "c": 3}

    res = eval(expression, {}, local_scope)

    print(f"Safely evaluated expression '{expression}': {res}\n")

    return res


fun_safe_eval()
