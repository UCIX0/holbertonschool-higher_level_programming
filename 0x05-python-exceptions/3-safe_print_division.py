#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resulta = a/b
    except (TypeError, ZeroDivisionError):
        resulta = None
    finally:
        print("Inside result: {}".format(resulta))
        return resulta
