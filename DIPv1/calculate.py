
REAL_COIN_HEIGHT = 25
REAL_COIN_WIDTH = 25


def calcuate_dim(prediction):
    obj_dim = []
    coin_width = 1
    coin_height = 1
    for i in range(len(prediction)):
        if prediction[i][0] == 0:
            coin_width = prediction[i][3]
            coin_height = prediction[i][4]
        else:
            obj_dim.append(
                [
                    prediction[i][0],
                    prediction[i][3],
                    prediction[i][4],
                ]
            )

    for i in range(len(obj_dim)):
        obj_dim[i][1] = (obj_dim[i][1] / coin_width) * REAL_COIN_WIDTH
        obj_dim[i][2] = (obj_dim[i][2] / coin_height) * REAL_COIN_HEIGHT

    return obj_dim
