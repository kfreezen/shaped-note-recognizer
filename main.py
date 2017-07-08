import network
import training_data_loader

net = network.Network([33*26, 30, 7])
data = training_data_loader.load_notes_data("./training_data", "training.txt", 7)

print data[0]