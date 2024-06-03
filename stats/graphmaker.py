import matplotlib.pyplot as plt

# Function to read the stats.txt file
def read_stats(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [float(item.strip()) for item in data if item.strip()]

# Function to create the graph
def create_graph(data):
    last_seven_items = data[-7:]
    labels = [f'day1 {i+1}' for i in range(len(last_seven_items))]
    
    plt.figure(figsize=(10, 5))
    plt.plot(labels, last_seven_items, marker='o')
    plt.title('Df classic players week stats')
    plt.xlabel('Days')
    plt.ylabel('Players')
    plt.grid(True)
    plt.savefig('graph.png')
    plt.show()


filename = 'stats.txt'
data = read_stats(filename)
create_graph(data)
