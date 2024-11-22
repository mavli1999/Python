import csv
from datetime import datetime
filepath = '/Users/maverickli/Desktop/Daily/table.csv'

def display_rev_results():
    with open(filepath, 'r') as display_file:
        reader = csv.DictReader(display_file)

        yesterday_display_revenue = 0
        display_revenue_by_date = {} #create a dict thats like date: rev for getting daily rev

        for row in reader:
            #get yesterday's revenue
            if row["Dimension_DATE"] == "2024-11-18" and row["Creative_Type"] == "Display":
                yesterday_display_revenue += float(row["Revenue"])

            #get daily rev for all dates
            date = row["Dimension_DATE"]
            date = datetime.strptime(date, "%Y-%m-%d").date()
            daily_revenue = float(row["Revenue"]) 

            if row["Creative_Type"] == "Display":
                display_revenue_by_date[date] = display_revenue_by_date.get(date, 0) + daily_revenue
                #get(date, 0) default 0, get the value of the key, date

    display_revenue_by_date = dict(sorted(display_revenue_by_date.items(), key=lambda x: x[0], reverse=True)) #sort dict descending

    for display_date in display_revenue_by_date: #get display's result
        if display_revenue_by_date[display_date] > yesterday_display_revenue:
            return round(yesterday_display_revenue / 1000), display_date, round(display_revenue_by_date[display_date] / 1000)

def video_rev_results():
    with open(filepath, 'r') as video_file:
        reader = csv.DictReader(video_file)

        yesterday_video_revenue = 0
        video_revenue_by_date = {} #create a dict thats like date: rev for getting daily rev

        for row in reader:
            #get yesterday's revenue
            if row["Dimension_DATE"] == "2024-11-18" and row["Creative_Type"] == "Pre Roll":
                yesterday_video_revenue += float(row["Revenue"])

            #get daily rev for all dates
            date = row["Dimension_DATE"]
            date = datetime.strptime(date, "%Y-%m-%d").date()
            daily_revenue = float(row["Revenue"]) 

            if row["Creative_Type"] == "Pre Roll":
                video_revenue_by_date[date] = video_revenue_by_date.get(date, 0) + daily_revenue
                #get(date, 0) default 0, get the value of the key, date

    video_revenue_by_date = dict(sorted(video_revenue_by_date.items(), key=lambda x: x[0], reverse=True)) #sort dict descending

    for video_date in video_revenue_by_date: #get video's result
        if video_revenue_by_date[video_date] > yesterday_video_revenue:
            return round(yesterday_video_revenue / 1000), video_date, round(video_revenue_by_date[video_date] / 1000)

def main_rev():
    yesterday_display, result_display_date, result_display_revenue = display_rev_results()
    yesterday_video, result_video_date, result_video_revenue = video_rev_results()
    print(f"Yesterday's display revenue was ${yesterday_display}K. Best since {result_display_date} which had ${result_display_revenue}K")
    print(f"Yesterday's video revenue was ${yesterday_video}K. Best since {result_video_date} which had ${result_video_revenue}K")

main_rev()