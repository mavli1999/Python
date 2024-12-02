import csv
from datetime import datetime
filepath = '/Users/maverickli/Desktop/Daily/daily.csv'

def display_imps_results():
    with open(filepath, 'r') as display_file:
        reader = csv.DictReader(display_file)

        yesterday_display_imps = 0
        display_imps_by_date = {}  # Create a dict that's like date: imps for getting daily impressions

        for row in reader:
            # Get yesterday's impressions
            if row["Dimension_DATE"] == "2024-11-26" and row["Creative_Type"] == "Display":
                yesterday_display_imps += float(row["Impressions"])

            # Get daily impressions for all dates
            date = row["Dimension_DATE"]
            date = datetime.strptime(date, "%Y-%m-%d").date()
            daily_imps = float(row["Impressions"])

            if row["Creative_Type"] == "Display":
                display_imps_by_date[date] = display_imps_by_date.get(date, 0) + daily_imps
                # get(date, 0) default 0, get the value of the key, date

    display_imps_by_date = dict(sorted(display_imps_by_date.items(), key=lambda x: x[0], reverse=True))  # Sort dict descending by date

    for display_date in display_imps_by_date:  # Get display's result
        if display_imps_by_date[display_date] > yesterday_display_imps:
            return round(yesterday_display_imps / 1000000,1), display_date, round(display_imps_by_date[display_date] / 1000000,1)
        
    #if yesterday was best ever
    return round(yesterday_display_imps / 1000), "Best Ever", round(yesterday_display_imps / 1000)

def video_imps_results():
    with open(filepath, 'r') as video_file:
        reader = csv.DictReader(video_file)

        yesterday_video_imps = 0
        video_imps_by_date = {}  # Create a dict that's like date: imps for getting daily impressions

        for row in reader:
            # Get yesterday's impressions
            if row["Dimension_DATE"] == "2024-11-26" and row["Creative_Type"] == "Pre Roll":
                yesterday_video_imps += float(row["Impressions"])

            # Get daily impressions for all dates
            date = row["Dimension_DATE"]
            date = datetime.strptime(date, "%Y-%m-%d").date()
            daily_imps = float(row["Impressions"])

            if row["Creative_Type"] == "Pre Roll":
                video_imps_by_date[date] = video_imps_by_date.get(date, 0) + daily_imps
                # get(date, 0) default 0, get the value of the key, date

    video_imps_by_date = dict(sorted(video_imps_by_date.items(), key=lambda x: x[0], reverse=True))  # Sort dict descending

    for video_date in video_imps_by_date:  # Get video's result
        if video_imps_by_date[video_date] > yesterday_video_imps:
            return round(yesterday_video_imps / 1000000,1), video_date, round(video_imps_by_date[video_date] / 1000000,1)
    
    #if yesterday was best ever
    return round(yesterday_video_imps / 1000), "Best Ever", round(yesterday_video_imps / 1000)

def main_imps():
    yesterday_display, result_display_date, result_display_imps = display_imps_results()
    yesterday_video, result_video_date, result_video_imps = video_imps_results()

    if result_display_date == "Best Ever":
        print(f"Yesterday's display imps of {yesterday_display}M were the best ever!")
    else:
        print(f"Yesterday's display impressions were {yesterday_display}M. Best since {result_display_date} which had {result_display_imps}M")
    
    if result_video_date == "Best Ever":
        print(f"Yesterday's video imps of {yesterday_video}M were the best ever!")
    else:
        print(f"Yesterday's video impressions were {yesterday_video}M. Best since {result_video_date} which had {result_video_imps}M")

main_imps()
