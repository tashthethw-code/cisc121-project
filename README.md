# Playlist Sorter (Merge Sort)

## Chosen Problem
This app sorts a playlist of songs based on either energy or duration. The goal is to help users organize music depending on mood (energy) or listening time (duration).

## Chosen Algorithm
Merge Sort was used because it is an efficient sorting algorithm with time complexity O(n log n). It works well for lists and allows clear step-by-step splitting and merging.

## Why it fits
The playlist is stored as a list of songs, and Merge Sort is ideal for sorting lists. It ensures consistent performance even for larger datasets.

---

## Problem Breakdown & Computational Thinking

### Decomposition
- Take user input (songs)
- Convert input into structured data
- Choose sorting key (energy or duration)
- Apply merge sort
- Display sorted playlist

### Pattern Recognition
- Repeated comparisons between elements
- Splitting lists into smaller parts
- Merging sorted lists together

### Abstraction
- Show only important data (title, artist, energy, duration)
- Hide internal sorting mechanics from user

### Algorithm Design
Input → Process → Output  
User enters songs → Merge Sort runs → Sorted playlist is displayed

---

## Flowchart
Start
↓
User enters playlist + chooses sort key (energy/duration)
↓
Parse input into list of songs
↓
Check: Is list size ≤ 1?
    ├── Yes → Return list (already sorted)
    └── No
         ↓
    Split list into left half and right half
         ↓
    Apply Merge Sort to left half
         ↓
    Apply Merge Sort to right half
         ↓
    Merge the two sorted halves:
         • Compare elements
         • Place smaller value first
         • Continue until merged
         ↓
Final sorted list created
↓
Display sorted playlist
↓
End

---

## Steps to Run Locally
1. Install dependencies:
   pip install gradio

2. Run:
   python app.py

3. Open the local URL shown in terminal

---

## Hugging Face Link
https://huggingface.co/spaces/Wafi1234/playlist-merge-sort 


---

## How to Use the App
1. Enter songs in this format:
   title, artist, energy, duration

2. Each song should be on a new line.

Example:
Song A, Drake, 80, 200  
Song B, Weeknd, 60, 180  

3. Choose a sorting option:
- energy
- duration

4. Click "Submit" to see the sorted playlist.

---

## Testing
Tested with:
- Normal input (multiple songs)
- Already sorted lists
- Reverse sorted lists
- Invalid input (missing values or wrong format)

All cases returned correct results or appropriate error messages.

---

## Author
Tashtheth Wafi

## Acknowledgment
Used AI to assist with debugging and understanding structure. Final code was reviewed and modified by myself
