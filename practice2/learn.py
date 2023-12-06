import numpy as np
import cv2
from create_feature import *
from calorie_calc import *
import csv

svm_params = dict(kernel_type=cv2.ml.SVM_LINEAR, svm_type=cv2.ml.SVM_C_SVC, C=2.67, gamma=5.383)


def training():
    feature_mat = []
    response = []
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]:
        for i in range(1, 21):
            print("D:\Semester 5\Digital Image Processing\Project\image_processing\Calorie-estimation-from-food-images-OpenCV\images\All_Images\\" + str(j) + "_" + str(i) + ".jpg")
            fea, farea, skinarea, fcont, pix_to_cm = readFeatureImg(
                "D:\Semester 5\Digital Image Processing\Project\image_processing\Calorie-estimation-from-food-images-OpenCV\images\All_Images\\" + str(j) + "_" + str(i) + ".jpg"
            )
            feature_mat.append(fea)
            response.append(int(j))  # Convert response to integer

    trainData = np.float32(feature_mat).reshape(-1, 94)
    responses = np.array(response)  # Ensure responses are numpy array of float32

    svm = cv2.ml.SVM_create()
    svm.setKernel(cv2.ml.SVM_LINEAR)
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setC(2.67)
    svm.setGamma(5.383)

    svm.train(trainData, cv2.ml.ROW_SAMPLE, responses)
    svm.save('svm_data.dat')


def testing():
    svm_model = cv2.ml.SVM_load('svm_data.dat')
    feature_mat = []
    response = []
    image_names = []
    pix_cm = []
    fruit_contours = []
    fruit_areas = []
    fruit_volumes = []
    fruit_mass = []
    fruit_calories = []
    skin_areas = []
    fruit_calories_100grams = []
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]:
        for i in range(21, 26):
            img_path = "D:\Semester 5\Digital Image Processing\Project\image_processing\Calorie-estimation-from-food-images-OpenCV\images\Test_Images\\" + str(j) + "_" + str(i) + ".jpg"
            print(img_path)
            fea, farea, skinarea, fcont, pix_to_cm = readFeatureImg(img_path)
            pix_cm.append(pix_to_cm)
            fruit_contours.append(fcont)
            fruit_areas.append(farea)
            feature_mat.append(fea)
            skin_areas.append(skinarea)
            response.append([float(j)])
            image_names.append(img_path)

    testData = np.float32(feature_mat).reshape(-1, 94)
    responses = np.float32(response)
    _, result = svm_model.predict(testData)

    mask = result.flatten() == responses.flatten()

    # calculate calories
    for i in range(0, len(result)):
        volume = getVolume(result[i][0], fruit_areas[i], skin_areas[i], pix_cm[i], fruit_contours[i])
        mass, cal, cal_100 = getCalorie(result[i][0], volume)
        fruit_volumes.append(volume)
        fruit_calories.append(cal)
        fruit_calories_100grams.append(cal_100)
        fruit_mass.append(mass)

    # write into csv file
    with open('output.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        data = ["Image name", "Desired response", "Output label", "Volume (cm^3)", "Mass (grams)", "Calories for food item", "Calories per 100 grams"]
        writer.writerow(data)
        for i in range(0, len(result)):
            if fruit_volumes[i] is None:
                data = [str(image_names[i]), str(responses[i][0]), str(result[i][0]), "--", "--", "--",
                        str(fruit_calories_100grams[i])]
            else:
                data = [str(image_names[i]), str(responses[i][0]), str(result[i][0]), str(fruit_volumes[i]),
                        str(fruit_mass[i]), str(fruit_calories[i]), str(fruit_calories_100grams[i])]
            writer.writerow(data)

    for i in range(0, len(mask)):
        if not mask[i]:
            print("(Actual Reponse)", responses[i][0], "(Output)", result[i][0], image_names[i])

    correct = np.count_nonzero(mask)
    print(correct * 100.0 / result.size)


if __name__ == '__main__':
    training()
    testing()
