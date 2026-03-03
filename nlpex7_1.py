

p1 = "The language learning platform helps users improve vocabulary."
p2 = "This system suggests synonyms to expand vocabulary."

set1,set2 = set(p1.lower().split()),set(p2.lower().split())
score =(p2.lower().split())
score = len(set1&set2) / len(set1 | set2)
level = "High" if score >= 0.75 else "Medium" if score >= 0.40 else "Low"

print("Joccard Score:", score)
print("Similarity Level:", level)
