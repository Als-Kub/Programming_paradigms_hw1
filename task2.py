# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers

print(f"Declarative proceedure -> {sort_list_declarative([92, 18, 2, 3, -30, 20, 8, 31])}")