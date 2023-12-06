import cv2
import numpy as np
import sys

# Density - gram / cm^3
density_dict = {1: 0.609, 2: 0.94, 3: 0.577, 4: 0.641, 5: 1.151, 6: 0.482, 7: 0.513, 8: 0.641, 9: 0.481, 10: 0.641, 11: 0.521, 12: 0.881, 13: 0.228, 14: 0.650}
# kcal
calorie_dict = {1: 52, 2: 89, 3: 92, 4: 41, 5: 360, 6: 47, 7: 40, 8: 158, 9: 18, 10: 16, 11: 50, 12: 61, 13: 31, 14: 30}
# Skin of photo to real multiplier
skin_multiplier = 5 * 2.3

def getCalorie(label, volume):  # volume in cm^3
    '''
    Inputs are the volume of the food item and the label of the food item
    so that the food item can be identified uniquely.
    The calorie content in the given volume of the food item is calculated.
    '''
    calorie = calorie_dict[int(label)]
    if volume is None:
        return None, None, calorie
    density = density_dict[int(label)]
    mass = volume * density * 1.0
    calorie_tot = (calorie / 100.0) * mass
    return mass, calorie_tot, calorie  # calorie per 100 grams

def getVolume(label, area, skin_area, pix_to_cm_multiplier, fruit_contour):
    '''
    Using calibration techniques, the volume of the food item is calculated using the
    area and contour of the food item by comparing the food item to standard geometric shapes.
    '''
    area_fruit = (area / skin_area) * skin_multiplier  # area in cm^2
    label = int(label)
    volume = 100
    if label == 1 or label == 9 or label == 7 or label == 6 or label == 12:  # sphere-apple,tomato,orange,kiwi,onion
        radius = np.sqrt(area_fruit / np.pi)
        volume = (4 / 3) * np.pi * radius * radius * radius
        print(area_fruit, radius, volume, skin_area)

    if label == 2 or label == 10 or (label == 4 and area_fruit > 30):  # cylinder like banana, cucumber, carrot
        fruit_rect = cv2.minAreaRect(fruit_contour)
        height = max(fruit_rect[1]) * pix_to_cm_multiplier
        radius = area_fruit / (2.0 * height)
        volume = np.pi * radius * radius * height

    if (label == 4 and area_fruit < 30) or (label == 5) or (label == 11):  # cheese, carrot, sauce
        volume = area_fruit * 0.5  # assuming width = 0.5 cm

    if (label == 8) or (label == 14) or (label == 3) or (label == 13):
        volume = None

    return volume

if __name__ == '__main__':
    # Example usage
    label = 1
    area = 50
    skin_area = 20
    pix_to_cm_multiplier = 2.0
    fruit_contour = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])  # Replace with the actual contour
    volume = getVolume(label, area, skin_area, pix_to_cm_multiplier, fruit_contour)
    mass, calorie_tot, calorie_per_100g = getCalorie(label, volume)
    print("Volume:", volume)
    print("Mass:", mass)
    print("Total Calories:", calorie_tot)
    print("Calories per 100g:", calorie_per_100g)
