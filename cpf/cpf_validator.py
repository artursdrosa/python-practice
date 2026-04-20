def cpf_validation(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # Remove dots and dashes if present

    if not cpf.isdigit():
        return "Invalid input. Please enter only numbers."

    elif len(cpf) != 11:
        return "Invalid CPF. It must contain exactly 11 digits."
    
    return f"Your CPF is: {cpf} is valid."