import yaml

def yaml_create():
    classes = {}
    with open(".\DIPv1\classes.txt", "r") as file:
        i = 0
        for line in file:
            classes[i] = line.strip()  # [classid, name]
            i += 1

    data = {
        "path": "../dataset", 
        "train": "images/train", 
        "val": "images/validation",
        "test": "images/test",
        "names": classes
    }

    # Write the data to the YAML file
    with open("./DIPv1/yolo/data.yaml", 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)
