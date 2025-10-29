import random

# Define lists of AI/ML class components
topics = [
    "Supervised Learning", 
    "Unsupervised Learning", 
    "Neural Networks", 
    "Natural Language Processing", 
    "Computer Vision", 
    "Reinforcement Learning",
    "Model Evaluation",
    "Feature Engineering"
]

subtopics = {
    "Supervised Learning": ["Linear Regression", "Logistic Regression", "Decision Trees"],
    "Unsupervised Learning": ["K-Means Clustering", "PCA", "Anomaly Detection"],
    "Neural Networks": ["Feedforward Networks", "Backpropagation", "CNNs", "RNNs"],
    "Natural Language Processing": ["Text Classification", "Word Embeddings", "Transformers"],
    "Computer Vision": ["Image Classification", "Object Detection", "Image Segmentation"],
    "Reinforcement Learning": ["Q-Learning", "Policy Gradients", "Deep Q-Networks"],
    "Model Evaluation": ["Cross Validation", "Precision-Recall", "ROC Curves"],
    "Feature Engineering": ["Normalization", "One-Hot Encoding", "Dimensionality Reduction"]
}

activities = [
    "Lecture and slides",
    "Hands-on coding exercise",
    "Group discussion",
    "Mini project demo",
    "Quiz and review",
    "Case study presentation"
]

# Randomly select components
topic = random.choice(topics)
subtopic = random.choice(subtopics[topic])
activity = random.choice(activities)

# Print random lecture plan
print("🎓 AI/ML Class Lecture Plan 🎓")
print(f"Topic: {topic}")
print(f"Subtopic: {subtopic}")
print(f"Activity: {activity}")
