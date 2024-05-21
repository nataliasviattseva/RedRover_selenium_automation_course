def sort_list_price(lst: list, reverse_value):
    return sorted(lst, key=lambda i: float(i.replace("$", "")), reverse=reverse_value)


def sort_list_alphabetical(lst: list, reverse_value):
    return sorted(lst, reverse=reverse_value)
