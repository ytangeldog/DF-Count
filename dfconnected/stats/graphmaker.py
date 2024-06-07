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
    
    plt.figure(figsize=(10, 5))
    plt.plot(labels, last_seven_items, marker='o')
    plt.gca().yaxis.set_major_formatter('{x:.0f}')
    plt.title('Df Connected players week stats')
    plt.xlabel('Days')
    plt.ylabel('Players')
    plt.grid(True)
    plt.savefig('dfconnected/graph.png')
    plt.show()


filename = 'dfconnected/stats/stats.txt'
data = read_stats(filename)
create_graph(data)
