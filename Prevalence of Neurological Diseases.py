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

plt.savefig('prevalence_neurological_diseases.png')
plt.show()
