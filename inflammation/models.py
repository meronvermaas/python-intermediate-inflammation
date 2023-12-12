"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=",")


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    
   :param data: A 2D data array with inflammation data (each row
   contains measurements for a single patient across all days).
   :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    
    :param data: A 2D data array with inflammation data (each row
    contains measurements for a single patient across all days).
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    

   :param data: A 2D data array with inflammation data (each row
   contains measurements for a single patient across all days).
   :returns: An array of min values of measurements for each day.
    """
    return np.min(data, axis=0)

def daily_std(data):
    """Calculate the daily standard deviation of a 2D inflammation data array.
    

   :param data: A 2D data array with inflammation data (each row
   contains measurements for a single patient across all days).
   :returns: An array of std values of measurements for each day.
    """
    return np.std(data, axis=0)

class Person:
    "Basic Person class"
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)
        self.observations.append(new_observation)
        return new_observation

class Doctor(Person):
    """A Basic Doctor Class."""
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patient(self, new_patient):
        for patient in self.patients:
            if patient.name == new_patient.name:
                return
        self.patients.append(new_patient)