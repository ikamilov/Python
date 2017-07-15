def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing Model: " + current_design)
		completed_models.append(current_design)
def show_completed(completed_models):
	print("\nThe Following Models have been printed: ")
	for completed_model in completed_models:
		print("\t" + completed_model)
