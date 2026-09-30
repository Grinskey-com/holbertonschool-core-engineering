#!/usr/bin/env python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print(f"Inside result: {result}")
    return result
