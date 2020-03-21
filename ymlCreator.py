# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:05:17 2020

@author: Chaitanya
"""

import haarCascade as hc

faces,faceID=hc.labels_for_training_data('trainingImages')
face_recognizer=hc.train_classifier(faces,faceID)
face_recognizer.write('trainingData.yml')