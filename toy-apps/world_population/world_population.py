import json
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None


def main():
    # 데이터 읽기
    filename = 'population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)

        world_pop = {}
        for pop_dict in pop_data:
            if pop_dict['Year'] == '2010':
                country_name = pop_dict['Country Name']
                population = int(float(pop_dict['Value']))
                code = get_country_code(country_name)
                if code:
                    world_pop[code] = population

        # 인구의 크기에 따라 세 그룹으로 나눈다.
        pop_1, pop_2, pop_3 = {}, {}, {}
        for cc, pop in world_pop.items() :
            if pop < 10000000:
                pop_1[cc] = pop
            elif pop < 1000000000:
                pop_2[cc] = pop
            else:
                pop_3[cc] = pop

        # 그룹별 나라 갯수
        print(len(pop_1), len(pop_2), len(pop_3))  

        wm_style = RS('#336699', base_style=LCS)
        wm = World(style=wm_style)
        wm.title = 'World Population in 2010, by Country'
        wm.add('0-10m', pop_1)
        wm.add('10m-1bn', pop_2)
        wm.add('>1bn', pop_3)
            
        wm.render_to_file('world_population.svg')


if __name__ == '__main__':
    main()