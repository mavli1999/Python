import csv
from datetime import datetime

filepath = '/Users/maverickli/Desktop/Daily/daily.csv'
date_of_comparison = "2024-12-16"

def process_revenue():
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        
        # Data structures
        revenue_data = {}  # Nested dict: {site: {creative_type: {date: revenue}}}
        yesterday_revenue = {}  # Nested dict: {site: {creative_type: revenue}}
        
        for row in reader:
            site = row["Site"]
            creative_type = row["Creative_Type"]
            date = row["Dimension_DATE"]
            revenue = float(row["Revenue"])
            
            # Initialize nested structure
            revenue_data.setdefault(site, {}).setdefault(creative_type, {})
            yesterday_revenue.setdefault(site, {}).setdefault(creative_type, 0)
            
            # Populate revenue data
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            revenue_data[site][creative_type][date_obj] = (
                revenue_data[site][creative_type].get(date_obj, 0) + revenue
            )
            
            # Track yesterday's revenue
            if date == date_of_comparison:
                yesterday_revenue[site][creative_type] += revenue
        
        # Sort revenues by date
        for site in revenue_data:
            for creative_type in revenue_data[site]:
                revenue_data[site][creative_type] = dict(
                    sorted(revenue_data[site][creative_type].items(), key=lambda x: x[0], reverse=True)
                )
        
        return revenue_data, yesterday_revenue


def analyze_revenue(revenue_data, yesterday_revenue):
    results = {}  # To store results by site and creative type
    
    for site, creative_types in revenue_data.items():
        results[site] = {}
        for creative_type, revenues in creative_types.items():
            yesterday_rev = yesterday_revenue[site][creative_type]
            for date, daily_rev in revenues.items():
                if daily_rev > yesterday_rev:
                    results[site][creative_type] = (yesterday_rev, date, daily_rev)
                    break
            else:
                # If yesterday's revenue was the best ever
                results[site][creative_type] = (yesterday_rev, "Best Ever", yesterday_rev)
    
    return results


def display_results(results):
    for site, creative_results in results.items():
        print(f"Site: {site}")
        for creative_type, (yesterday_rev, result_date, result_rev) in creative_results.items():
            if result_date == "Best Ever":
                print(f"  {creative_type}: {date_of_comparison}'s revenue of ${round(yesterday_rev / 1000)}K was the best ever!")
            else:
                print(
                    f"  {creative_type}: {date_of_comparison}'s revenue was ${round(yesterday_rev / 1000)}K. "
                    f"Best since {result_date} which had ${round(result_rev / 1000)}K."
                )


def main():
    revenue_data, yesterday_revenue = process_revenue()
    results = analyze_revenue(revenue_data, yesterday_revenue)
    display_results(results)


main()
