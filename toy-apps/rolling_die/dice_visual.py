import pygal
import numpy as np

from die import Die

def main():
    die_1 = Die()
    die_2 = Die()

    results = []
    num_rolling = 1000

    for i in range(num_rolling):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # 결과, 빈도수를 분석
    side, freq = np.unique(results, return_counts=True)

    hist = pygal.Bar()
    hist.title = "Results of rolling two D6 dice for 1000 times"
    hist.x_labels =  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add('two D6', freq)
    hist.render_to_file('two_D6_visual.svg')

if __name__ == '__main__':
    main()

