import numpy as np
import matplotlib.pyplot as plt

# Data for AI benefits for investors
categories = ["Diagnostic Accuracy", "Treatment Efficacy", "Cost Reduction", "Research Speed"]
values = [90, 85, 70, 80]  # Percentage improvement in each area

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='gold', alpha=0.25)
ax.plot(angles, values, color='orange', linewidth=2)

ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

plt.title('Benefits of Using AI in Neurological Treatments')
plt.savefig('benefits_ai_investors.png')
plt.show()
