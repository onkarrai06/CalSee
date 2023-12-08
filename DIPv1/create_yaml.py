import yaml

def yaml_create():
    classes = {}
    with open("classes.txt", "r") as file:
        i = 0
        for line in file:
            i += 1
            classes[i] = line.strip()  # [classid, name]

    data = {
        "path": "../dataset", 
        "train": "images/train", 
        "val": "images/valdiation",
        "test": "images/test",
        "names": classes
    }

    # Write the data to the YAML file
    with open("data.yaml", 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)
