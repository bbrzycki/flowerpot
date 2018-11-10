import json
import matplotlib.pyplot as plt
import numpy as np


def plot_organism_field(time, organism_paths, world_paths, field):
    image = []
    for i in range(time + 1):
        with open(organism_paths[i], 'r') as f:
            organism_list = json.load(f)
        with open(world_paths[i], 'r') as f:
            world = json.load(f)

        matching_organisms = []
        for organism_dict in organism_list:
            if field == 'alive' and organism_dict['alive'] \
                    or field == 'old_age' \
                        and organism_dict['cause_of_death'] == 'old_age' \
                    or field == 'thirst' \
                        and organism_dict['cause_of_death'] == 'thirst' \
                    or field == 'hunger' \
                        and organism_dict['cause_of_death'] == 'hunger' \
                    or field == 'births' \
                        and organism_dict['age'] == 0:
                matching_organisms.append(organism_dict['position'])

        frequency_weights = np.zeros(world['world_size'][0])
        for position in matching_organisms:
            index = position[0]
            frequency_weights[index] += 1

        image.append(frequency_weights)

    plt.imshow(image, aspect='auto')
    plt.colorbar()

    if field == 'alive':
        title = 'Living Organisms'
    elif field == 'old_age':
        title = 'Deaths from Old Age'
    elif field == 'thirst':
        title = 'Deaths from Thirst'
    elif field == 'hunger':
        title = 'Deaths from Hunger'
    elif field == 'births':
        title = 'Organism Births'
    else:
        title = field
    plt.title('%s' % title)


def plot_world_field(time, world_paths, field):
    image = []
    for i in range(time + 1):
        with open(world_paths[i], 'r') as f:
            world = json.load(f)

        image.append(world[field])

    plt.imshow(image, aspect='auto')
    plt.colorbar()

    if field == 'water':
        title = 'Water Supply'
    elif field == 'food':
        title = 'Food Supply'
    elif field == 'obstacles':
        title = 'Obstacles'
    else:
        title = field
    plt.title('%s' % title)
