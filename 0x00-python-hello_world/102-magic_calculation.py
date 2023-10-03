import dis
def magic_calculation(a, b):
    result = 98
    result += a ** b
    return result
# Print the bytecode of the function for reference
dis.dis(magic_calculation)
