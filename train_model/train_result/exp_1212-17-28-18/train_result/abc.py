import pickle

# Specify the file path
file_path = 'train_result.pkl'

# Open the file in binary mode
with open(file_path, 'r') as file:
    # Load the object from the file
    loaded_object = pickle.load(file)
    print(loaded_object)