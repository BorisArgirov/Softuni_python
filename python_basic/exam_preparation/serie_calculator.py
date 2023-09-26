movie_name = input()
seasons = int(input())
episodes = int(input())
time_per_episode = float(input())
time_episode_with_reclame = time_per_episode * 1.20
special_episode = seasons * 10

total_time = seasons * episodes * time_episode_with_reclame + special_episode
print(f"Total time needed to watch the {movie_name} series is {int(total_time)} minutes.")
