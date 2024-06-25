import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Function to read the stats.txt file
def read_stats(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [float(item.strip()) for item in data if item.strip()]

# Function to create the graph
def create_graph(data):
    last_thirty_items = data[-30:]
    day = datetime.now()
    labels = [f'{(day - timedelta(30-i)).strftime('%b')} {(day - timedelta(30-i)).strftime('%d')}th' for i in range(len(last_thirty_items))]
    
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(labels, last_thirty_items, marker='o', markersize=12)
    for i, value in enumerate(last_thirty_items):
        x = i
        y = value
        text = str(int(value))
        bbox_props = dict(boxstyle="circle,pad=0.2", lw=0)
        ax.text(x, y, text, ha="center", va="center", size=10,color='white',fontweight='bold',
                bbox=bbox_props)
    ax.set_title('Df classic players month stats')
    ax.set_xlabel('Days')
    ax.set_ylabel('Players')
    ax.grid(True)
    
    plt.savefig('graph2.png')
    plt.show()

filename = 'stats/stats.txt'
data = read_stats(filename)
create_graph(data)
