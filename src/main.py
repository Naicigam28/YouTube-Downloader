from pytube import YouTube
import csv

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("./Downloads")
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def read_file(file):
    data = []
    
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            data.append(row)
    print(f"Processed {len(data)} lines.")

    return data
linkData=read_file("links.csv")


for row in linkData:
    link=row.get("Link")
    Download(link)