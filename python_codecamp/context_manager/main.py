from design import Connect

with Connect("pyserver") as server:
    # main action
    print("Installing Python ")
    print("Installing and updating more tools")

print("This is after __exit__")
