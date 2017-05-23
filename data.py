# Data format: each data point is comprised of a list of integers 
# between 0 and 255.

def load_data(filename):
    with open(filename) as f:
        header = f.readline()
        labels = []
        points = []
        for line in f.readlines():
            data = line.split(',')
            labels.append(int(data[0]))
            points.append([int(x) for x in data[1:]])
        return points, labels

