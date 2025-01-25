# Machine Learning & Neural Network Classes Repository

Welcome to the **Machine Learning & Neural Network Classes Repository**! This repository contains various notebooks, datasets, and resources for learning and applying machine learning and neural network concepts. It is designed to cover a wide range of topics, from basic ML algorithms to advanced deep learning techniques.

---

## **Current Project: Transfer Learning with Image Classification**

This project demonstrates the implementation of **Transfer Learning** for image classification. The specific example involves classifying images of ducks and geese. The project uses pre-trained models to fine-tune on a custom dataset.

### **Key Features:**
- Uses TensorFlow's `image_dataset_from_directory` to load and preprocess the dataset.
- Implements transfer learning with a pre-trained MobileNetV2 model.
- Visualizes validation loss and accuracy to evaluate model performance.
- Dataset: Custom folders containing images of ducks and geese.

---

## **Dataset Setup**
The dataset contains two folders, each representing a class:
- `ducks/`: Contains images of ducks.
- `goose/`: Contains images of goose.

### **Steps to Use the Dataset:**
1. The dataset is zipped and stored in the repository as `dataset.zip`.
2. The notebook includes code to download and extract the dataset automatically:
   ```python
   # Download the dataset from GitHub
   !curl -L -o dataset.zip https://github.com/<your_username>/<repo_name>/raw/main/dataset.zip
   !unzip -q dataset.zip -d /content
   ```
3. After extraction, the folder structure will look like:
   ```
   /content/
       ducks_v2/
           image1.jpg
           image2.jpg
           ...
       goose/
           image1.jpg
           image2.jpg
           ...
   ```

---

## **How to Run the Notebook**
1. Open the notebook in Google Colab.
2. Run all the cells sequentially.
3. The dataset will be downloaded and extracted automatically.
4. Train the model, evaluate performance, and visualize results.

---

## **Repository Structure**
The repository is organized into the following sections:

- **`datasets/`**: Contains datasets used in various projects.
  - Example: `dataset.zip` for the current project.
- **`notebooks/`**: Contains Jupyter/Colab notebooks for each class or project.
  - Example: `transfer_learning_ducks_geese.ipynb`.
- **`README.md`**: Project documentation and repository overview.

---

## **Planned Topics and Classes**
This repository will be expanded with more classes and projects, covering topics like:

- **Machine Learning Fundamentals**:
  - Supervised and unsupervised learning.
  - Regression and classification algorithms.

- **Deep Learning**:
  - Feedforward neural networks.
  - Convolutional Neural Networks (CNNs).
  - Recurrent Neural Networks (RNNs).
  - Transfer learning and pre-trained models.

- **Advanced Topics**:
  - Generative Adversarial Networks (GANs).
  - Natural Language Processing (NLP).
  - Reinforcement Learning (RL).

---

## **Getting Started**

1. Clone the repository:
   ```bash
   git clone https://github.com/MatheusDSantossi/transfer-learning-project-DIO
   ```

2. Navigate to the desired project folder (e.g., `notebooks/transfer_learning_ducks_geese.ipynb`).

3. Open the notebook in Google Colab or Jupyter Notebook.

4. Follow the instructions in the notebook to run the project.

---

## **Dependencies**
To run the projects in this repository, you will need:

- Python 3.x
- TensorFlow
- Matplotlib
- NumPy
- Pandas

Install dependencies using:
```bash
pip install tensorflow matplotlib numpy pandas
```

---

## **Contributing**
Contributions are welcome! If you want to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

---


## **Acknowledgments**
Special thanks to the contributors of open-source datasets and frameworks that make these projects possible!
