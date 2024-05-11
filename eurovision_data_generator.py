import pandas as pd
import random
import numpy as np
import string

# Random seed for reproducibility
random.seed(42)

# Number of records for synthetic data
num_countries = 40
num_contests = 20
num_participants_per_contest = 26  # Average number of finalists
num_judges_per_contest = 10
num_sponsors_per_contest = 5
num_hosts_per_contest = 2

# Helper function to generate random strings
def random_string(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# 1. Countries Table
countries = pd.DataFrame({
    'country_id': [f"CTRY{str(i).zfill(3)}" for i in range(num_countries)],
    'country_name': [random_string(7) for _ in range(num_countries)],
    'country_code': [random_string(3) for _ in range(num_countries)],
    'region': [random.choice(['Western Europe', 'Eastern Europe', 'Northern Europe', 'Southern Europe']) for _ in range(num_countries)],
    'population': [random.randint(1000000, 100000000) for _ in range(num_countries)]
})

countries.to_csv('countries.csv', index=False)

# 2. Contests Table
contests = pd.DataFrame({
    'contest_id': [f"CONT{str(i).zfill(3)}" for i in range(num_contests)],
    'year': [2022 - i for i in range(num_contests)],
    'host_country': [random.choice(countries['country_id']) for _ in range(num_contests)],
    'venue': [random_string(10) for _ in range(num_contests)],
    'theme': [random.choice(['Unity', 'Diversity', 'Hope', 'Future', 'Love']) for _ in range(num_contests)]
})

contests.to_csv('contests.csv', index=False)

# 3. Participants Table
participants = pd.DataFrame({
    'participant_id': [f"PART{str(i).zfill(3)}" for i in range(num_contests * num_participants_per_contest)],
    'contest_id': [f"CONT{str(i // num_participants_per_contest).zfill(3)}" for i in range(num_contests * num_participants_per_contest)],
    'country_id': [random.choice(countries['country_id']) for _ in range(num_contests * num_participants_per_contest)],
    'artist_name': [random_string(10) for _ in range(num_contests * num_participants_per_contest)],
    'song_id': [f"SONG{str(i).zfill(3)}" for i in range(num_contests * num_participants_per_contest)],
    'is_finalist': [random.choice([True, False]) for _ in range(num_contests * num_participants_per_contest)]
})

participants.to_csv('participants.csv', index=False)

# 4. Songs Table
songs = pd.DataFrame({
    'song_id': [f"SONG{str(i).zfill(3)}" for i in range(num_contests * num_participants_per_contest)],
    'song_title': [random_string(15) for _ in range(num_contests * num_participants_per_contest)],
    'song_length_seconds': [random.randint(150, 300) for _ in range(num_contests * num_participants_per_contest)],
    'genre': [random.choice(['Pop', 'Rock', 'Folk', 'Jazz', 'Classical']) for _ in range(num_contests * num_participants_per_contest)],
    'language': [random.choice(['English', 'French', 'German', 'Spanish', 'Italian', 'Portuguese']) for _ in range(num_contests * num_participants_per_contest)]
})

songs.to_csv('songs.csv', index=False)

# 5. Judges Table
judges = pd.DataFrame({
    'judge_id': [f"JUDGE{str(i).zfill(3)}" for i in range(num_contests * num_judges_per_contest)],
    'contest_id': [f"CONT{str(i // num_judges_per_contest).zfill(3)}" for i in range(num_contests * num_judges_per_contest)],
    'name': [random_string(10) for _ in range(num_contests * num_judges_per_contest)],
    'country_id': [random.choice(countries['country_id']) for _ in range(num_contests * num_judges_per_contest)]
})

judges.to_csv('judges.csv', index=False)

# 6. Votes Table
votes = pd.DataFrame({
    'vote_id': [f"VOTE{str(i).zfill(3)}" for i in range(num_contests * num_participants_per_contest * 2)],  # Double points for public and jury votes
    'contest_id': [f"CONT{str(i // num_participants_per_contest // 2).zfill(3)}" for i in range(num_contests * num_participants_per_contest * 2)],
    'country_id': [random.choice(countries['country_id']) for _ in range(num_contests * num_participants_per_contest * 2)],
    'points': [random.randint(0, 12) for _ in range(num_contests * num_participants_per_contest * 2)],
    'voting_type': [random.choice(['Jury', 'Public']) for _ in range(num_contests * num_participants_per_contest * 2)],
    'participant_id': [random.choice(participants['participant_id']) for _ in range(num_contests * num_participants_per_contest * 2)]
})

votes.to_csv('votes.csv', index=False)

# 7. Results Table
results = pd.DataFrame({
    'result_id': [f"RESULT{str(i).zfill(3)}" for i in range(num_contests * num_participants_per_contest)],
    'contest_id': [f"CONT{str(i // num_participants_per_contest).zfill(3)}" for i in range(num_contests * num_participants_per_contest)],
    'country_id': [random.choice(countries['country_id']) for _ in range(num_contests * num_participants_per_contest)],
    'total_points': [random.randint(0, 200) for _ in range(num_contests * num_participants_per_contest)],
    'ranking': [random.randint(1, 26) for _ in range(num_contests * num_participants_per_contest)]
})

results.to_csv('results.csv', index=False)

# 8. Hosts Table
hosts = pd.DataFrame({
    'host_id': [f"HOST{str(i).zfill(3)}" for i in range(num_contests * num_hosts_per_contest)],
    'contest_id': [f"CONT{str(i // num_hosts_per_contest).zfill(3)}" for i in range(num_contests * num_hosts_per_contest)],
    'name': [random_string(10) for _ in range(num_contests * num_hosts_per_contest)],
    'country_id': [random.choice(countries['country_id']) for _ in range(num_contests * num_hosts_per_contest)]
})

hosts.to_csv('hosts.csv', index=False)

# 9. Sponsors Table
sponsors = pd.DataFrame({
    'sponsor_id': [f"SPONS{str(i).zfill(3)}" for i in range(num_contests * num_sponsors_per_contest)],
    'contest_id': [f"CONT{str(i // num_sponsors_per_contest).zfill(3)}" for i in range(num_contests * num_sponsors_per_contest)],
    'sponsor_name': [random_string(10) for _ in range(num_contests * num_sponsors_per_contest)],
    'contribution': [random.choice(['Funding', 'Logistics', 'Media', 'Production', 'Technical']) for _ in range(num_contests * num_sponsors_per_contest)]
})

sponsors.to_csv('sponsors.csv', index=False)

# 10. Venues Table
venues = pd.DataFrame({
    'venue_id': [f"VENUE{str(i).zfill(3)}" for i in range(num_contests)],
    'contest_id': [f"CONT{str(i).zfill(3)}" for i in range(num_contests)],
    'venue_name': [random_string(10) for _ in range(num_contests)],
    'city': [random_string(10) for _ in range(num_contests)],
    'capacity': [random.randint(5000, 20000) for _ in range(num_contests)]
})

venues.to_csv('venues.csv', index=False)
