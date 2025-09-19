import pandas as pd  # for reading and writing CSV files

# Read the job listings from CSV
jobs = pd.read_csv("job.csv")

# Keywords that usually indicate scams
scam_keywords = [
    "advance payment",
    "urgent join",
    "free registration",
    "pay fee",
    "registration fee",
    "pay advance"
]

# Function to classify each job description
def check_scam(description):
    # Convert description to string to avoid AttributeError
    description = str(description).lower()
    for keyword in scam_keywords:
        if keyword in description:
            return "Scam"
    return "Legitimate"

# Apply the function to each row in Description column
jobs["Status"] = jobs["Description"].apply(check_scam)

# Save the results to a new CSV
jobs.to_csv("jobs_filtered.csv", index=False)

# Print the table on screen
print(jobs)
print("\nFiltered jobs saved to jobs_filtered.csv")
