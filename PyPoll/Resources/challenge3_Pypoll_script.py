import os
import csv

# Set the file path for the election data
file_path = os.path.join(".", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file and iterate over each row
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    next(csvreader)
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1
        # Add the candidate to the candidates dictionary and increment their vote count
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Calculate the percentage of votes each candidate won
for candidate in candidates:
    vote_count = candidates[candidate]
    percentage = vote_count / total_votes * 100
    candidates[candidate] = {"vote_count": vote_count, "percentage": percentage}

# Determine the winner based on popular vote
winner = max(candidates, key=lambda x: candidates[x]["vote_count"])

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    vote_count = candidates[candidate]["vote_count"]
    percentage = candidates[candidate]["percentage"]
    print(f"{candidate}: {percentage:.3f}% ({vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the analysis to a text file
output_path = os.path.join(".", "election_results.txt")
with open(output_path, "w", newline="") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for candidate in candidates:
        vote_count = candidates[candidate]["vote_count"]
        percentage = candidates[candidate]["percentage"]
        textfile.write(f"{candidate}: {percentage:.3f}% ({vote_count})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")
