import matplotlib.pyplot as plt
import numpy as np

# Training data
data = [
    {'epoch': 1.06, 'loss': 0.0615, 'grad_norm': 0.1445, 'learning_rate': 1.829734e-5},
    {'epoch': 1.07, 'loss': 0.0622, 'grad_norm': 0.1414, 'learning_rate': 1.82795e-5},
    {'epoch': 1.07, 'loss': 0.0817, 'grad_norm': 0.1358, 'learning_rate': 1.82799e-5},
    {'epoch': 1.08, 'loss': 0.0656, 'grad_norm': 0.1573, 'learning_rate': 1.82624e-5},
    {'epoch': 1.08, 'loss': 0.0729, 'grad_norm': 0.1244, 'learning_rate': 1.82448e-5},
    {'epoch': 1.09, 'loss': 0.0666, 'grad_norm': 0.1093, 'learning_rate': 1.82271e-5},
    {'epoch': 1.09, 'loss': 0.0778, 'grad_norm': 0.1842, 'learning_rate': 1.82094e-5},
    {'epoch': 1.10, 'loss': 0.0703, 'grad_norm': 0.1042, 'learning_rate': 1.81915e-5},
    {'epoch': 1.11, 'loss': 0.0685, 'grad_norm': 0.1830, 'learning_rate': 1.81736e-5},
    {'epoch': 1.11, 'loss': 0.0593, 'grad_norm': 0.1091, 'learning_rate': 1.81556e-5},
    {'epoch': 1.12, 'loss': 0.0472, 'grad_norm': 0.0672, 'learning_rate': 1.81375e-5},
    {'epoch': 1.12, 'loss': 0.1301, 'grad_norm': 0.4128, 'learning_rate': 1.81194e-5},
    {'epoch': 1.13, 'loss': 0.0634, 'grad_norm': 0.0883, 'learning_rate': 1.81011e-5},
    {'epoch': 1.13, 'loss': 0.0717, 'grad_norm': 0.1987, 'learning_rate': 1.80828e-5},
    {'epoch': 1.14, 'loss': 0.0683, 'grad_norm': 0.1125, 'learning_rate': 1.80644e-5},
    {'epoch': 1.15, 'loss': 0.0638, 'grad_norm': 0.0952, 'learning_rate': 1.80460e-5},
    {'epoch': 1.16, 'loss': 0.0699, 'grad_norm': 0.2087, 'learning_rate': 1.80274e-5},
    {'epoch': 1.17, 'loss': 0.0598, 'grad_norm': 0.0980, 'learning_rate': 1.80088e-5},
    {'epoch': 1.17, 'loss': 0.0615, 'grad_norm': 0.1261, 'learning_rate': 1.79901e-5},
    {'epoch': 1.18, 'loss': 0.0603, 'grad_norm': 0.2007, 'learning_rate': 1.79713e-5},
    {'epoch': 1.18, 'loss': 0.0713, 'grad_norm': 0.1734, 'learning_rate': 1.79525e-5},
    {'epoch': 1.19, 'loss': 0.0563, 'grad_norm': 0.0973, 'learning_rate': 1.79336e-5},
    {'epoch': 1.19, 'loss': 0.0703, 'grad_norm': 0.2033, 'learning_rate': 1.79145e-5},
    {'epoch': 1.19, 'loss': 0.0574, 'grad_norm': 0.0774, 'learning_rate': 1.78954e-5},
    {'epoch': 1.19, 'loss': 0.0634, 'grad_norm': 0.0800, 'learning_rate': 1.78763e-5}
]

# Extract data into separate lists
epochs = [d['epoch'] for d in data]
losses = [d['loss'] for d in data]
grad_norms = [d['grad_norm'] for d in data]
learning_rates = [d['learning_rate'] for d in data]

# Create figure and axis objects with a single subplot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Set the style
plt.style.use('default')

# Plot loss and gradient norm on the first y-axis
color1 = '#8884d8'
color2 = '#82ca9d'
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss / Gradient Norm', color='black')
line1 = ax1.plot(epochs, losses, color=color1, label='Loss')
line2 = ax1.plot(epochs, grad_norms, color=color2, label='Gradient Norm')
ax1.tick_params(axis='y', labelcolor='black')

# Create a second y-axis for learning rate
ax2 = ax1.twinx()
color3 = '#ff7300'
ax2.set_ylabel('Learning Rate', color='black')
line3 = ax2.plot(epochs, learning_rates, color=color3, label='Learning Rate')
ax2.tick_params(axis='y', labelcolor='black')

# Add grid
ax1.grid(True, linestyle='--', alpha=0.7)

# Combine legends
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right')

# Add title
plt.title('Training Metrics Over Time')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show plot
plt.show()

# Optional: Save the plot
# plt.savefig('training_metrics.png', dpi=300, bbox_inches='tight')