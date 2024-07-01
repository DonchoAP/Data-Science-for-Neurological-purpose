import matplotlib.pyplot as plt

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

plt.show()
