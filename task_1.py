import random

scores=[random.randint(1,100)for_in range(7)]
print("исходные баллы:",scores)

min_score=min(score)
max_score=max(score)

filtered_scores=scores.copy()
filtered_scores.remove(min_score)
filtered_scores.remove(max_score)

average_rating=sum(filtered_scores)/len(filtered_scores)

print("средний рейтинг:",average_rating)