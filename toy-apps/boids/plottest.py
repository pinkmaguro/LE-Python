import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


width, height = 600, 400

pos = np.array([[100,100]])

class Ball:
    def __init__(self,N):
        self.pos = self._random_pos(N, width, height)
        self.max_speed = 10
        self.vel = self._random_pos(N, self.max_speed, self.max_speed)
         
    def _random_pos(self, N, x_max, y_max):
        pos_x = x_max * np.random.rand(N,1)
        pos_y = y_max * np.random.rand(N,1)
        return np.hstack((pos_x, pos_y))

        
    def move(self, pts):
        self.pos[:,0] += self.vel[:,0]
        self.pos[:,1] += self.vel[:,1]
        self.applyBC()

        pts.set_data(self.pos[:,0], self.pos[:,1])

    def applyBC(self):
        delta = 10
        for p, v in zip(self.pos, self.vel):
            if p[0] < delta or p[0] > width - delta:
                v[0] = -v[0]
            if p[1] < delta or p[1] > height - delta:
                v[1] = -v[1]

    def buttonPress(self, event):
        if event.button is 1:
            self.pos = np.concatenate((self.pos, 
                                       np.array([[event.xdata, event.ydata]])), 
                                      axis=0)
            v = self.max_speed * np.random.rand(1,2)
            self.vel = np.concatenate((self.vel, v), 
                                      axis=0)

def run(frameNum, pts, ball):
    ball.move(pts)
    return pts

N = 10
ball = Ball(N)

fig = plt.figure()
ax = plt.axes(xlim=(0, width), ylim=(0, height))

pts, = ax.plot([], [], markersize=10, 
                c='k', marker='o', ls='None')

anim = animation.FuncAnimation(fig, run, fargs=(pts,ball,), 
                                 interval=50)

cid = fig.canvas.mpl_connect('button_press_event', ball.buttonPress)
plt.show()