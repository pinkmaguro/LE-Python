from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """ 랜덤워크를 구현
    """
    def __init__(self, num_pts=5000):
        self.num_pts = num_pts

        # 시작 위치 (0, 0)
        self.x_val = [0]
        self.y_val = [0]

    def fill_walk(self):

        while len(self.x_val) < self.num_pts:
            # 랜덤 워크의 이동 범위 -4 에서 +4 까지
            direction = [-1,1]
            distance = [0,1,2,3,4]

            x_step = self._get_step(direction, distance)
            y_step = self._get_step(direction, distance)

            # 제자리인 데이터는 사용하지 않는다.
            if x_step == 0 and y_step == 0:
                continue

            # 랜덤워크 한 위치
            x_next = self.x_val[-1] + x_step
            y_next = self.y_val[-1] + y_step

            # 새로운 위치 추가
            self.x_val.append(x_next)
            self.y_val.append(y_next)
    
    def _get_step(self, direction, distance):
        return choice(direction) * choice(distance)

def random_walk_visual(num_pts):
    rw = RandomWalk(num_pts)
    rw.fill_walk()

    point_idx = list(range(rw.num_pts))
    plt.scatter(rw.x_val, rw.y_val, c=point_idx,
                    cmap=plt.cm.Blues, edgecolor='none' ,s=10)
    plt.title('Random Walk')
    plt.show()

if __name__ == '__main__':
    random_walk_visual(5000)



