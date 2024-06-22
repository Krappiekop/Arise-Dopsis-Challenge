# Arise-Dopsis Detection Challenge

This repository contains the work for the Arise-Dopsis Challenge, which involves training models for insect detection and annotation using machine learning techniques. The project is divided into several stages, each documented in individual Jupyter Notebooks.

## Project Overview
1. Training a Small YOLO Model
   - Notebook: D4.1.1 Active Learning Model_Yolo-V8s.ipynb
   - Description: In this notebook, a small YOLO model was initially trained on 100 manually annotated images. Subsequently, 50 more images were manually annotated and added to the training data, repeating this process twice to enhance the dataset incrementally.
3. Automated Annotation of Insect Dataset
   - Notebook: D4.1.2 Dataset Annoteren Alles.ipynb
   - Description: Using the trained YOLO model from the previous step, this notebook automates the annotation process for 40,000 insect images. The annotations are saved in a CSV file named D4.1.2_auto_annotations.csv.
5. Training the VGG16 Model
   - Notebook: D4.1.3 Model trainen insect herkennen.ipynb
   - Description: This notebook describes the training of a VGG16 model on the dataset annotated by the YOLO model. The goal is to improve insect recognition accuracy.
7. Processing Large Images
   - Notebook: D4.1.4 Grote afbeelding.ipynb
   - Description: In this final notebook, the trained VGG16 model is used to process large images containing many insects. The model detects and highlights insects with bounding boxes.
