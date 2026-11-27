def process_file(filename):
    total = 0
    report = []
    rejected = []
    try:
        with open(filename, "r") as f:
            for line_no, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")
                    if len(parts) != 3:
                        raise ValueError("Invalid fields")
                    reg, name, amount = parts
                    amount = float(amount)
                    total += amount
                    report.append(f"{reg} {name} {amount}")
                except ValueError as e:
                    rejected.append((line_no, line.strip(), str(e)))
        print("\n".join(report))
        print("Total:", total)
        print("Rejected:", rejected)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
process_file("mess.txt")