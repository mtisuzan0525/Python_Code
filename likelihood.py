from model import model

# Calculate probability for a given observation
probability = model.probability([["heavy", "yes", "delayed", "attend"]])

print(probability)