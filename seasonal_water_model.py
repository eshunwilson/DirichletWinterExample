#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 13:10:56 2024

@author: mtn309
"""

import numpy as np
from scipy.stats import dirichlet
import matplotlib.pyplot as plt

# Define transition matrices for different seasons
# Example: Rows (current state), Columns (next state)
# [Vapor, Liquid, Ice]
summer_transition = np.array([
    [0.7, 0.25, 0.05],  # Vapor -> Vapor, Liquid, Ice
    [0.3, 0.6, 0.1],    # Liquid -> Vapor, Liquid, Ice
    [0.1, 0.4, 0.5]     # Ice -> Vapor, Liquid, Ice
])

winter_transition = np.array([
    [0.2, 0.3, 0.5],    # Vapor -> Vapor, Liquid, Ice
    [0.1, 0.4, 0.5],    # Liquid -> Vapor, Liquid, Ice
    [0.05, 0.2, 0.75]   # Ice -> Vapor, Liquid, Ice
])

spring_transition = np.array([
    [0.8, 0.1, 0.1],    # Vapor -> Vapor, Liquid, Ice
    [0.1, 0.4, 0.5],    # Liquid -> Vapor, Liquid, Ice
    [0.05, 0.2, 0.75]   # Ice -> Vapor, Liquid, Ice
])

# Function to calculate stationary distribution
def stationary_distribution(transition_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(transition_matrix.T)
    stationary = np.real(eigenvectors[:, np.isclose(eigenvalues, 1)])
    stationary = stationary / np.sum(stationary)
    return stationary.flatten()

# Compute stationary distributions
summer_stationary = stationary_distribution(summer_transition)
winter_stationary = stationary_distribution(winter_transition)
spring_stationary = stationary_distribution(spring_transition)

# Use Dirichlet distribution to simulate proportions
summer_proportions = dirichlet.rvs(summer_stationary, size=100)
winter_proportions = dirichlet.rvs(winter_stationary, size=100)
spring_proportions = dirichlet.rvs(spring_stationary, size=100)

# Plotting the results
def plot_proportions(proportions, title):
    phases = ['Vapor', 'Liquid', 'Ice']
    mean_proportions = np.mean(proportions, axis=0)
    plt.bar(phases, mean_proportions, color=['skyblue', 'blue', 'darkblue'])
    plt.title(title)
    plt.ylabel("Proportion")
    plt.ylim(0, 1)
    plt.show()

plot_proportions(summer_proportions, "Water Composition in Summer")
plot_proportions(winter_proportions, "Water Composition in Winter")
plot_proportions(spring_proportions, "Water composition in Spring")