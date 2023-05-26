import pandas as pd
import random
import math
import numpy as np

data = pd.read_excel(r'C:\Users\kramal361\Downloads\masking-input (2).xlsx')


def mask_gps_data(gps_data, precision=2, perturbation_range=0.001):
    
    # Remove degree symbol and extract latitude value
    latitude = float(gps_data.split('°')[0])
    
    # Apply random perturbation
    latitude += random.uniform(-perturbation_range, perturbation_range)
    
    # Round to the desired precision
    latitude = round(latitude, precision)
    
    # Format the masked GPS data
    masked_gps_data = f"{latitude}° N"
    
    return masked_gps_data


def gps_data(gps_data, precision=4, perturbation_range=0.001):
    # Generate random perturbation values within the specified range
    perturbation_lat = random.uniform(-perturbation_range, perturbation_range)
    perturbation_lon = random.uniform(-perturbation_range, perturbation_range)
    
    # Extract latitude and direction values
    latitude, direction = gps_data.split('°')
    latitude = float(latitude)
    
    # Apply random perturbation to latitude
    masked_latitude = latitude + perturbation_lat
    
    # Round latitude to the desired precision
    masked_latitude = round(masked_latitude, precision)
    
    # Format the masked GPS data
    masked_gps_data = f"{masked_latitude}° {direction}"
    
    return masked_gps_data

def laplace_noise(scale):
    return np.random.laplace(scale=scale)

def latitude_data(gps_data):
    # Set the privacy parameters
    epsilon = 1.0
    sensitivity = 0.01
    # Extract latitude and direction values
    latitude, direction = gps_data.split('°')
    latitude = float(latitude)
    
    # Calculate the privacy budget
    scale = sensitivity / epsilon
    
    # Add Laplace noise to the latitude
    masked_latitude = latitude + laplace_noise(scale)
    
    # Round the masked latitude to 6 decimal places
    masked_latitude = round(masked_latitude, 6)
    
    # Format the masked GPS data
    masked_gps_data = f"{masked_latitude}° {direction}"
    
    return masked_gps_data



# Apply Laplace noise addition to the GPS data
data['GPS'] = data['GPS'].apply(latitude_data)

print(data['GPS'])

