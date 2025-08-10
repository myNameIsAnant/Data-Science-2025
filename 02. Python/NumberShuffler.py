import random
import pandas as pd

def generate_shuffled_table(rows, cols):
    # Create a list of numbers from 1 to rows*cols
    numbers = list(range(1, rows * cols + 1))
    # Shuffle the list randomly
    random.shuffle(numbers)
    # Build the table row by row
    table = []
    for r in range(rows):
        row = numbers[r * cols:(r + 1) * cols]
        table.append(row)
    return table

# Generate a 9x10 table
shuffled_table = generate_shuffled_table(9, 10)
df = pd.DataFrame(shuffled_table)
print(df)
# Print the table in a readable format
# for row in shuffled_table:
#     print('\t'.join(str(cell) for cell in row))

df.to_excel("shuffled_table.xlsx", index=False, header=False)
