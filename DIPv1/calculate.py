"""
Example of prediciton array
prediction = [
    [1, 0.3474264705882353, 0.5130718954248366, 0.4056372549019608, 0.4738562091503268],
    [0, 0.8952205882352942, 0.7165032679738562, 0.1409313725490196, 0.18137254901960784]]
"""

REAL_COIN_HEIGHT = 15
REAL_COIN_WIDTH = 15


def calcuate_dim(prediction, img_size):
    obj_dim = []
    coin_width = 0
    coin_height = 0
    for i in range(len(prediction)):
        if i == 0:
            coin_width = prediction[i][3] * img_size[0]
            coin_height = prediction[i][4] * img_size[1]
        else:
            obj_dim.append(
                [
                    prediction[i][3] * img_size[0],
                    prediction[i][4] * img_size[1],
                    prediction[i][0],
                ]
            )

    for i in range(len(obj_dim)):
        obj_dim[i][0] = (obj_dim[i][0] / coin_width) * REAL_COIN_WIDTH
        obj_dim[i][1] = (obj_dim[i][1] / coin_height) * REAL_COIN_HEIGHT

    return obj_dim

#print(calcuate_dim(prediction, (125, 125)))