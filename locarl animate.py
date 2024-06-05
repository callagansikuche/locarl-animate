import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


letters = ["L", "o", "c", "a", "r", "l"]
colors = ["red", "green", "blue", "purple", "orange", "violet" ]
duration = 7
num_frames = 30  

def animate(frame):
  plt.cla()


  positions = [i * (frame / (num_frames - 1)) for i in range(len(letters))]


  for i, letter in enumerate(letters):
    text = plt.text(positions[i], 0.5, letter, color=colors[i], fontsize=72)
    text.set_alpha(frame / num_frames)

  plt.xlim(0, len(letters))
  plt.ylim(0, 1)
  plt.axis("off")

fig, ax = plt.subplots()
animation = FuncAnimation(fig, animate, frames=num_frames, interval=duration * 800 / num_frames)

plt.show()




