import csv
from datetime import datetime

filepath = '/Users/maverickli/Desktop/Daily/daily.csv'
date_of_comparison = "2024-12-16"

def format_number(value):
    """Format numbers into K (thousands) or M (millions)."""
    if value < 1_000_000:
        return f"{int(value / 1_000)}K"
    else:
        return f"{round(value / 1_000_000, 1)}M"

def process_impressions():
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        
        # Data structures
        impressions_data = {}  # Nested dict: {site: {creative_type: {date: impressions}}}
        yesterday_impressions = {}  # Nested dict: {site: {creative_type: impressions}}
        
        for row in reader:
            site = row["Site"]
            creative_type = row["Creative_Type"]
            date = row["Dimension_DATE"]
            impressions = float(row["Impressions"])
            
            # Initialize nested structure
            impressions_data.setdefault(site, {}).setdefault(creative_type, {})
            yesterday_impressions.setdefault(site, {}).setdefault(creative_type, 0)
            
            # Populate impressions data
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            impressions_data[site][creative_type][date_obj] = (
                impressions_data[site][creative_type].get(date_obj, 0) + impressions
            )
            
            # Track yesterday's impressions
            if date == date_of_comparison:
                yesterday_impressions[site][creative_type] += impressions
        
        # Sort impressions by date
        for site in impressions_data:
            for creative_type in impressions_data[site]:
                impressions_data[site][creative_type] = dict(
                    sorted(impressions_data[site][creative_type].items(), key=lambda x: x[0], reverse=True)
                )
        
        return impressions_data, yesterday_impressions


def analyze_impressions(impressions_data, yesterday_impressions):
    results = {}  # To store results by site and creative type
    
    for site, creative_types in impressions_data.items():
        results[site] = {}
        for creative_type, impressions in creative_types.items():
            yesterday_imps = yesterday_impressions[site][creative_type]
            for date, daily_imps in impressions.items():
                if daily_imps > yesterday_imps:
                    results[site][creative_type] = (format_number(yesterday_imps), date, format_number(daily_imps))
                    break
            else:
                # If yesterday's impressions were the best ever
                results[site][creative_type] = (format_number(yesterday_imps), "Best Ever", format_number(yesterday_imps))
    
    return results


def display_results(results):
    for site, creative_results in results.items():
        print(f"Site: {site}")
        for creative_type, (yesterday_imps, result_date, result_imps) in creative_results.items():
            if result_date == "Best Ever":
                print(f"  {creative_type}: {date_of_comparison}'s impressions of {yesterday_imps} were the best ever!")
            else:
                print(
                    f"  {creative_type}: {date_of_comparison}'s impressions were {yesterday_imps}. "
                    f"Best since {result_date} which had {result_imps}."
                )


def main():
    impressions_data, yesterday_impressions = process_impressions()
    results = analyze_impressions(impressions_data, yesterday_impressions)
    display_results(results)


main()
