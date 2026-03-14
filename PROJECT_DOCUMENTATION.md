# Electricity Consumption Analysis Documentation

## Team Members
- Shivam Kumar
- Sumeet Kumar Yadav
- Vishal Kashyap
- Vishal Kumar

## Project Title
Electricity Consumption in India: Comparative Analysis (2019 vs 2020)

## Project Overview
This project presents an interactive Tableau-based analysis of electricity consumption in India and embeds the story and dashboards in a Flask web application.

The core goal is to compare electricity usage patterns across:
- 2019 (pre-COVID period)
- 2020 (COVID period)

This helps explain how demand changed during lockdowns and restricted industrial/commercial activity.

## Main Analysis Ideas

### 1. 2019 vs 2020 Electricity Comparison
- Compare month-wise electricity consumption between 2019 and 2020.
- Highlight the overall change in demand from pre-COVID to COVID year.
- Observe whether recovery happened in later months of 2020.

### 2. Electricity Consumption During COVID
- Focus on months affected by lockdown and movement restrictions.
- Identify visible drops in consumption during strict lockdown periods.
- Compare state-level and overall trends to find where impact was strongest.

### 3. Top N Months (Highest Consumption)
- Select value N (example: 3, 5, or 10).
- Rank months by total electricity consumption in descending order.
- Display top N months and compare if they belong mostly to 2019 or 2020.

### 4. Bottom N Months (Lowest Consumption)
- Use the same N value for fair comparison.
- Rank months by total electricity consumption in ascending order.
- Analyze whether low-demand months are concentrated in lockdown periods.

### 5. Highest Electricity Consumption Month
- Identify the single month with maximum total electricity consumption.
- Record year and month name.
- Use this month as a benchmark against all other months.

## Recommended Metrics and Views
- Total electricity consumption by month.
- Year-over-year percentage change for each month.
- State-wise consumption distribution.
- Contribution of residential vs industrial demand (if available in source data).

## Suggested Story Flow (Tableau)
1. Introduction to data and objective.
2. National trend line for 2019 vs 2020.
3. COVID-period impact highlights.
4. Top N months view.
5. Bottom N months view.
6. Highest-consumption month spotlight.
7. Conclusion and recommendations.

## Key Questions Answered by This Project
- How different was electricity consumption in 2020 compared to 2019?
- Which months had highest and lowest electricity usage?
- How strongly did COVID affect demand patterns?
- Which periods showed early recovery after lockdown?

## Application Pages
- Home: Project introduction.
- Story: Full Tableau narrative.
- Dashboards: Combined comparative dashboards.
- Conclusion: Summary and actionable insights.

## Tech Stack
- Python (Flask)
- Tableau Public embeds
- HTML/CSS templates
- Vercel deployment

## Future Enhancements
- Add direct KPI cards for top month, bottom month, and year-over-year change.
- Add parameter control for dynamic N in Top N and Bottom N analysis.
- Add downloadable CSV summary for monthly and yearly comparisons.
- Add a state-level drill-down page for deeper policy analysis.

## Notes
If you want, this document can be extended with exact month names and values for:
- Top N months
- Bottom N months
- Highest consumption month

These values can be filled directly from the current Tableau dashboard outputs.
