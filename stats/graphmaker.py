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
    ax.plot(labels, last_seven_items, marker='o')
    ax.yaxis.set_major_formatter('{x:.0f}')
    for i, value in enumerate(last_seven_items):
        ax.annotate(str(int(value)), (labels[i], value), xytext=(0, 5), textcoords="offset points")
    ax.set_title('Df classic players week stats')
    ax.set_xlabel('Days')
    ax.set_ylabel('Players')
    ax.grid(True)
    
    plt.savefig('graph.png')
    plt.show()

filename = 'stats/stats.txt'
data = read_stats(filename)
create_graph(data)
