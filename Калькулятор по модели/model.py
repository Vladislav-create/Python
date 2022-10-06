from logging import exception


def calculate(primer):
    try:
        return eval(primer)
    except Exception:
        return 'Error'


def converter_model(data):
    return data * 1000
