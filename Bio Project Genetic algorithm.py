import random

hair_colors = ['Black', 'Brown', 'Blonde']
ear_lobe_attachments = ['Attached', 'Detached']
eye_colors = ['Brown', 'Blue', 'Green']
genders = ['Male', 'Female']

male_names = ["Liam", "Noah", "Ethan", "Lucas", "Mason", "Oliver", "Benjamin", "Logan", "William", "Alexander", "Elijah", "James", "Gabriel", "Michael", "Daniel", "Anthony", "Christopher", "Joshua", "Andrew", "Samuel", "Julian", "Kevin", "Tyler", "Austin", "Bryson", "Cameron", "Cooper", "Dominic", "Evan", "Gavin", "Harrison", "Henry", "Isaac", "Jaxon", "Landon", "Micah", "Nathan", "Parker", "Patrick", "Peter", "Ryder", "Ryan", "Seth", "Theodore", "Thomas", "Timothy", "Victor", "Wesley", "Xavier", "Zachary"]
female_names = ["Emma", "Olivia", "Ava", "Sophia", "Mia", "Isabella", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Lily", "Madison", "Victoria", "Jessica", "Samantha", "Avery", "Riley", "Zoey", "Natalie", "Grace", "Hannah", "Aubrey", "Elizabeth", "Taylor", "Kayla", "Gabriella", "Jasmine", "Julia", "Morgan", "Sydney", "Gianna", "Brianna", "Alexandra", "Savannah", "Annabelle", "Mackenzie", "Addison", "Brooklyn", "Everley", "Lilah", "Paige", "Sara", "Adeline", "Danielle", "Valerie", "Yvette", "Zoe"]

def generate_unique_names(num_names, name_list):
    if num_names > len(name_list):
        raise ValueError("Not enough unique names available")
    return random.sample(name_list, num_names)

def generate_individuals(num_individuals):
    num_males = num_individuals // 2
    num_females = num_individuals - num_males
    males = generate_unique_names(num_males, male_names)
    females = generate_unique_names(num_females, female_names)
    individuals = []
    for name in males:
        individual = {
            'Name': name,
            'Gender': 'Male',
            'Hair Color': random.choice(hair_colors),
            'Ear Lobe Attachment': random.choice(ear_lobe_attachments),
            'Height': 'Tall' if random.uniform(150, 200) >= 175 else 'Short',
            'Eye Color': random.choice(eye_colors),
            'Mutation': 'Yes' if random.random() < 0.1 else 'No'
        }
        individuals.append(individual)
    for name in females:
        individual = {
            'Name': name,
            'Gender': 'Female',
            'Hair Color': random.choice(hair_colors),
            'Ear Lobe Attachment': random.choice(ear_lobe_attachments),
            'Height': 'Tall' if random.uniform(150, 200) >= 175 else 'Short',
            'Eye Color': random.choice(eye_colors),
            'Mutation': 'Yes' if random.random() < 0.1 else 'No'
        }
        individuals.append(individual)
    random.shuffle(individuals)
    return individuals

def calculate_suitability_score(individual):
    score = 0
    if individual['Hair Color'] == 'Black':
        score += 3
    elif individual['Hair Color'] == 'Brown':
        score += 2
    elif individual['Hair Color'] == 'Blonde':
        score += 1
    if individual['Ear Lobe Attachment'] == 'Attached':
        score += 1
    elif individual['Ear Lobe Attachment'] == 'Detached':
        score += 2
    if individual['Height'] == 'Tall':
        score += 2
    else:
        score += 1
    if individual['Eye Color'] == 'Brown':
        score += 3
    elif individual['Eye Color'] == 'Blue':
        score += 2
    elif individual['Eye Color'] == 'Green':
        score += 1
    return score

def select_top_individuals(individuals, top_n):
    scored_individuals = [(individual, calculate_suitability_score(individual)) for individual in individuals]
    scored_individuals.sort(key=lambda x: x[1], reverse=True)
    males = [(individual, score) for individual, score in scored_individuals if individual['Gender'] == 'Male']
    females = [(individual, score) for individual, score in scored_individuals if individual['Gender'] == 'Female']
    
    top_males = [(individual, score) for individual, score in males if individual['Mutation'] == 'No'][:5]
    top_females = [(individual, score) for individual, score in females if individual['Mutation'] == 'No'][:5]
    
    top_individuals = top_males + top_females
    
    return top_individuals

num_individuals = 50
top_n = 10

individuals = generate_individuals(num_individuals)

for i, individual in enumerate(individuals, 1):
    print(f"\nIndividual {i}: {individual}")

top_individuals = select_top_individuals(individuals, top_n)

print("\nTop 10 Individuals by Suitability Score:")
print("\nMales : ")
for i, (individual, score) in enumerate(top_individuals, 1):
    if i != 5 :
        print(f"\n{i}. {individual['Name']} (Score: {score})")
    else :
        print(f"\n{i}. {individual['Name']} (Score: {score})")
        print("\nFemales : ")