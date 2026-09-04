# 🚀 CIFAR-10 Image Classification using MobileNetV2

A Deep Learning project that performs image classification on the **CIFAR-10** dataset using **Transfer Learning** with **MobileNetV2** and TensorFlow/Keras.

---

## 📌 Project Overview

This project demonstrates how to use a pre-trained **MobileNetV2** model as a feature extractor for classifying images from the CIFAR-10 dataset.

The model leverages transfer learning to achieve faster convergence and better performance compared to training a CNN from scratch.

---

## 🧠 Features

* Uses the **CIFAR-10** dataset.
* Implements **Transfer Learning** with MobileNetV2.
* Built using **TensorFlow** and **Keras**.
* Image normalization for better training.
* Model training and evaluation.
* Predicts the class of unseen test images.

---

## 📂 Dataset

The project uses the built-in **CIFAR-10** dataset provided by TensorFlow.

It contains:

* **50,000** Training Images
* **10,000** Testing Images
* **10 Classes**

Classes include:

* ✈️ Airplane
* 🚗 Automobile
* 🐦 Bird
* 🐱 Cat
* 🦌 Deer
* 🐶 Dog
* 🐸 Frog
* 🐴 Horse
* 🚢 Ship
* 🚚 Truck

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* MobileNetV2
* NumPy

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cifar10-mobilenetv2.git
cd cifar10-mobilenetv2
```

Install the required packages:

```bash
pip install tensorflow numpy
```

---

## ▶️ Run the Project

Execute:

```bash
python main.py
```

The script will:

1. Load the CIFAR-10 dataset.
2. Normalize image pixel values.
3. Load the pre-trained MobileNetV2 model.
4. Train the classifier.
5. Evaluate the model.
6. Predict the class of a test image.

---

## 📁 Project Structure

```text
📦 CIFAR10-MobileNetV2
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🏗️ Model Architecture

```text
Input Image (32×32×3)
        │
        ▼
MobileNetV2 (Pre-trained)
        │
        ▼
Flatten Layer
        │
        ▼
Dense (64, ReLU)
        │
        ▼
Dense (10, Softmax)
```

---

## 📊 Training

Example configuration:

* Optimizer: Adam
* Loss: Sparse Categorical Crossentropy
* Epochs: 15
* Batch Size: 256

---

## 📈 Evaluation

After training, the model is evaluated using the testing dataset to measure classification accuracy.

Example:

```python
model.evaluate(x_test, y_test)
```

---

## 🔮 Prediction

Example:

```python
prediction = model.predict(x_test[0:1])
print(prediction)
```

---

## 🚀 Future Improvements

* Data Augmentation
* Early Stopping
* Learning Rate Scheduler
* Fine-tuning MobileNetV2
* Model Checkpointing
* Confusion Matrix Visualization
* TensorBoard Support

---

## 📚 Learning Outcomes

Through this project, you will learn:

* Transfer Learning
* Image Classification
* Deep Learning with TensorFlow
* Working with CIFAR-10
* Building Neural Networks using Keras
* Model Training and Evaluation

---

## 👨‍💻 Author

**Yash**

If you found this project useful, consider giving the repository a ⭐.

