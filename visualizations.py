import seaborn as sns
import matplotlib.pyplot as plt

def create_visualizations(data):
    """Create visualizations for the given data."""
    print("Creating visualizations...")
    
    # Extract x and y data
    x = data["Time"]
    y = data["XRP Price (USD)"]
    
    # Create the plot
    plt.plot(x, y)
    
    # Add labels and title
    plt.xlabel("Time")
    plt.ylabel("XRP Price (USD)")
    plt.title("XRP Price Over Time")

    # Customize appearance
    sns.set(style="whitegrid", font_scale=1.2, palette="muted")

    # Show the plot
    plt.show()
