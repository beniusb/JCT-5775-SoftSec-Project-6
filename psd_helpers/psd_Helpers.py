import string

jump_instructions = ['call','jmp', 'jo', 'jno', 'js', 'jns', 'je', 'jz', 'jne', 'jnz', 'jb', 'jnae', 'jc', 'jnb', 'jae', 'jnc', 'jbe', 'jna', 'ja', 'jnbe', 'jl', 'jnge', 'jge', 'jnl', 'jle', 'jng', 'jg', 'jnle', 'jp', 'jpe', 'jnp', 'jpo', 'jcxz', 'jecxz']

def ask_yes_no(str_prompt):
    answer=""
    while answer not in ["y", "n"]:
        answer=raw_input(str_prompt+" (y/n)")
    return answer

def strip_non_printable(dirty_str):
    """
    :param str: string to stripped out of non printable bytes
    :return: returns string that conatins only printable bytes
    """
    return ''.join(filter(string.printable.__contains__, dirty_str))

def is_jmp_instruction(nemonic_str):
    return  nemonic_str in jump_instructions
