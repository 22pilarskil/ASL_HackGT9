from sklearn.neighbors import KNeighborsClassifier
import json
import pickle
import os
import math
import argparse

model = KNeighborsClassifier(n_neighbors=3)


data = []
labels = []

def unpack(world_landmarks):
    points = []
    for landmark in world_landmarks:
        point = []
        for det in landmark.landmark:
            point += [det.x, det.y, det.z, det.visibility]
        points.append(point)
    return len(world_landmarks), points


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="Data directory", type=str, default=None)
    parser.add_argument("--knn", help="Filename of pickled KNN", type=str, default=None)
    args = parser.parse_args()


    os.chdir(args.data)
    print(os.listdir("."))
    for filename in os.listdir('.'):
        if filename == ".DS_Store": continue
        print("Reading data from {}".format(filename))
        world_landmarks = pickle.load(open(filename, 'rb+'))
        length, points = unpack(world_landmarks)
        data += points
        labels += [filename for i in range(length)]

    os.chdir('../')


    model.fit(data,labels)

    if os.path.exists(args.knn): os.remove(args.knn)
    knn_file = open(args.knn, 'ab')
    pickle.dump(model, knn_file)
    knn_file.close()