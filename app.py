import gradio as gr

def parse_input(text):
    songs = []
    lines = text.strip().split("\n")

    if text.strip() == "":
        return None, "Input is empty."

    for i, line in enumerate(lines):
        parts = line.split(",")

        if len(parts) != 4:
            return None, f"Line {i+1} is invalid."

        title = parts[0].strip()
        artist = parts[1].strip()

        try:
            energy = int(parts[2].strip())
            duration = int(parts[3].strip())
        except:
            return None, f"Line {i+1} has invalid numbers."

        songs.append({
            "title": title,
            "artist": artist,
            "energy": energy,
            "duration": duration
        })

    return songs, None


def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def format_output(songs):
    text = ""
    for i, s in enumerate(songs, 1):
        text += f"{i}. {s['title']} - {s['artist']} | Energy: {s['energy']} | Duration: {s['duration']}\n"
    return text


def run_sort(input_text, key):
    songs, error = parse_input(input_text)
    if error:
        return error

    sorted_songs = merge_sort(songs, key)
    return format_output(sorted_songs)


demo = gr.Interface(
    fn=run_sort,
    inputs=[
        gr.Textbox(lines=8, label="Enter songs: title, artist, energy, duration"),
        gr.Radio(["energy", "duration"], label="Sort by", value="energy")
    ],
    outputs=gr.Textbox(label="Sorted Playlist"),
    title="Playlist Sorter (Merge Sort)"
)

demo.launch()