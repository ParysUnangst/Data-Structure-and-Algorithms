def remove_discontinued_products(productCatalog, discontinuedID):
    # Initialize a pointer for the position to place non-discontinued products
    index = 0

    # Iterate over the productCatalog
    for product in productCatalog:
        if product != discontinuedID:
            # Place the non-discontinued product at the current index
            productCatalog[index] = product
            # Move the index to the next position
            index += 1

    # Return the count of non-discontinued products
    return index

# Example usage:
productCatalog1 = [1003, 1002, 1002, 1003]
discontinuedID1 = 1003
# Remove discontinued products and get the count of remaining products
remaining_count1 = remove_discontinued_products(productCatalog1, discontinuedID1)
# Print the output: count of remaining products and the modified product catalog
print(f"Output: {remaining_count1}, productCatalog = {productCatalog1[:remaining_count1]}")

productCatalog2 = [1000, 1001, 1002, 1002, 1003, 1000, 1004, 1002]
discontinuedID2 = 1002
# Remove discontinued products and get the count of remaining products
remaining_count2 = remove_discontinued_products(productCatalog2, discontinuedID2)
# Print the output: count of remaining products and the modified product catalog
print(f"Output: {remaining_count2}, productCatalog = {productCatalog2[:remaining_count2]}")
