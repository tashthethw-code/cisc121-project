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
User Input → Parse Data → Merge Sort → Output Sorted Playlist

---

## Steps to Run Locally
1. Install dependencies:
   pip install gradio

2. Run:
   python app.py

3. Open the local URL shown in terminal

---

## Hugging Face Link
(Add your Hugging Face link here)

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
Your Name

## Acknowledgment
Used AI (ChatGPT) to assist with debugging and understanding structure. Final code was reviewed and modified manually.
