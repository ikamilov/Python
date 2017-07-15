# Start with the some designs that need to be printed
import printing_functions as printing
unprinted_designs = ['iphone case', 'robot robendant', 'dodecahedron']
completed_models = []

printing.print_models(unprinted_designs, completed_models)
printing.show_completed(completed_models)