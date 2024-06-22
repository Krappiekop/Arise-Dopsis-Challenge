# Project Overview


## Initial Attempts with Pre-trained Models
Description: Initially, pre-trained models like YOLO-V8 were used. However, these models were not effective as they misclassified objects (e.g., identifying a vase or baseball bat instead of insects).

1. Training a CNN Model
   - Notebook: C2.0 CNN Model.ipynb
   - Description: A basic Convolutional Neural Network (CNN) model was trained but showed poor accuracy in classifying insect images.
3. Training a VGG16 Model with Deepest Name
   - Notebook: C3.0 VGG16 Model Alleen DeepestName.ipynb
   - Description: This notebook involves training a VGG16 model using only the deepest name labels extracted from Data/Input/classification_labels.csv. The VGG16 model significantly improved the classification accuracy compared to the initial CNN model.
5. Incorporating Family Trees in the VGG16 Model
   - Notebook: C3.1 VGG16 Model Met Stamboom.ipynb
   - Description: An attempt was made to enhance the VGG16 model by incorporating family trees. The family tree data was sourced from Data/Input/name_to_ancestors.xlsx. This approach aimed to leverage hierarchical relationships between insect species, but the results were not as successful as expected.
