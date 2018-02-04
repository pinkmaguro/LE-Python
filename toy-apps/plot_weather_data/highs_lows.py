import csv
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def main():
    filename = 'sitka_weather_2014.csv'
    with open(filename, 'rt') as f:
        
        # csv.reader() 의 리턴은 iterator 이다. next()로 값을 얻는다.
        reader = csv.reader(f)
        header = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            dates.append(current_date)

            high = int(row[1])
            low = int(row[2])

            highs.append(high)
            lows.append(low)

    fig = plt.figure(figsize=(10,6), dpi=128)
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.title('Daily high temperatures, July 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # 날짜 레이블이 겹치지 않도록 대각선으로 표시한다.
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.savefig('../../static/images/weather_high_low.png')

    plt.show()
    
if __name__ == '__main__':
    main()