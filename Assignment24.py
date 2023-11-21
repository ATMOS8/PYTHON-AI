def total_chocolates(child_ids, chocolates_received, extra_chocolates, given_child_id, extra):
    total = sum(chocolates_received)
    if extra < 1:
        return "Extra chocolates is less than 1"
    if given_child_id not in child_ids:
        return "Child id is invalid"
    index = child_ids.index(given_child_id)
    chocolates_received[index] += extra
    return chocolates_received
child_ids = (1, 2, 3, 4, 5)
chocolates_received = [10, 8, 12, 5, 6]
given_child_id = int(input("Enter the child ID: "))
extra = int(input("Enter the number of extra chocolates: "))
result = total_chocolates(child_ids, chocolates_received, extra, given_child_id, extra)
print("Total number of chocolates received by each child:", result)