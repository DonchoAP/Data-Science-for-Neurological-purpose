import matplotlib.pyplot as plt

# Data for the prevalence of neurological diseases
diseases = ["Dementia/Alzheimer's", "Stroke", "Multiple Sclerosis", "Epilepsy", "Parkinson's Disease", "ALS"]
prevalences = [50e6, 80e6, 2.8e6, 50e6, 10e6, 450e3]
percentages = [(p / 8e9) * 100 for p in prevalences]

# Plotting the prevalence chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(diseases, percentages, color='skyblue')
ax.set_xlabel('Percentage of Global Population (%)')
ax.set_title('Percentage of People with Neurological Diseases')

# Adding values on the bars
for index, value in enumerate(percentages):
    ax.text(value, index, f'{value:.4f}%')

plt.show()


# Data for the impact of AI
areas = ["Early Diagnosis", "Treatment Personalization", "Remote Monitoring", "R&D Acceleration"]
improvements = [85, 75, 80, 90]  # Percentage improvement in efficiency/cost

# Plotting the AI impact chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(areas, improvements, color='lightgreen')

ax.set_ylabel('Improvement (%)')
ax.set_title('Impact of AI on Neurological Disease Treatment')

# Adding labels on the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2 - 0.15, yval + 2, f'{yval}%', fontsize=12)

plt.savefig('impact_ai_neurological_treatment.png')
plt.show()