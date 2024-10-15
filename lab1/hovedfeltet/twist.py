ant_personer = int(input('Hvor mange er dere på laget?\n'))
ant_twist = input('Hvor mange twist er det i posen dere vant?\n')

# ant_personer = int(ant_personer)
ant_twist = int(ant_twist)

til_hver = ant_twist // ant_personer
til_overs = ant_twist % ant_personer

print(f'Det blir {til_hver} twist til hver, og det blir {til_overs} twist til overs.')