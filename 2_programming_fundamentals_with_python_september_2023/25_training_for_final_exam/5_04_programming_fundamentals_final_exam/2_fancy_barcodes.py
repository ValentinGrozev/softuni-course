import re

barcodes_to_check = int(input())

for barcode in range(barcodes_to_check):
    current_barcode = input()
    pattern = r"(@#+)(([A-Z])([a-z0-9A-Z]{4,})([A-Z]))(@#+)"
    matches = re.findall(pattern, current_barcode)
    if matches:
        for match in matches:
            exact_match = match[1]
            pattern = r"\d+"
            product_group = re.findall(pattern, exact_match)
            if product_group:
                product_group = "".join(product_group)
                print(f"Product group: {product_group}")
            else:
                print("Product group: 00")
    else:
        print("Invalid barcode")
