print("\nex- 8.15 == Printing Modules")

def print_modules(unprinted_designs, completed_modules):
    """Simulate printing each design until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing design: {current_design}")
        completed_modules.append(current_design)

def show_completed_modules(completed_modules):
    """Show all the completed modules."""
    print("\nThe following modules have been printed:")
    for completed_module in completed_modules:
        print(completed_module)