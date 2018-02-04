import pygal
import numpy as np

from die import Die

def main():
    die = Die()

    results = []
    num_rolling = 1000
    for i in range(num_rolling):
        result = die.roll()
        results.append(result)

    # 결과, 빈도수를 분석
    side, freq = np.unique(results, return_counts=True)

    hist = pygal.Bar()
    hist.title = "Results of rolling Die for 1000 times"
    hist.x_labels =  ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('D6', freq)
    hist.render_to_file('die_visual.svg')

if __name__ == '__main__':
    main()

