import random

random_words = ["vater", "mach", "scheisse", "toten", "katze", "dick", "behindert", "gefurzed", "schwul", "schwanz", "schwarz"]

message = ""
sentence_length = random.randint(0, len(random_words))
for i in range(sentence_length):
    random_index = random.randint(0, sentence_length)
    message += random_words[random_index] + " "

print(message)