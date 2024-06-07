import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to read the stats.txt file
def read_stats(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [float(item.strip()) for item in data if item.strip()]

# Function to create the graph
def create_graph(data):
    last_seven_items = data[-7:]
    day = datetime.now()
    labels = [f'{(day + timedelta(i)).strftime('%A')}' for i in range(len(last_seven_items))]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(labels, last_seven_items, marker='o', markersize=12)
    for i, value in enumerate(last_seven_items):
        x = i
        y = value
        text = str(int(value))
        bbox_props = dict(boxstyle="circle,pad=0.2", lw=0)
        ax.text(x, y, text, ha="center", va="center", size=10,color='white',fontweight='bold',
                bbox=bbox_props)
    ax.set_title('Df classic players week stats')
    ax.set_xlabel('Days')
    ax.set_ylabel('Players')
    ax.grid(True)
    
    plt.savefig('graph.png')
    plt.show()

filename = 'stats/stats.txt'
data = read_stats(filename)
create_graph(data)
