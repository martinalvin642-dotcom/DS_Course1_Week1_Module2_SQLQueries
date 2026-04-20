# Aviation Accident Safety Analysis

## Project Overview

This project analyzes commercial and passenger jet airline safety using NTSB aviation accident data from 1983–2023. The analysis was conducted for an airline/airplane insurer interested in identifying aircraft makes and models with the lowest rates of passenger injury and aircraft destruction.

## Business Problem

The client needs to understand:
- Which aircraft **makes** and **models** exhibit low serious/fatal injury rates and low destruction rates in accidents
- Separate recommendations for **small aircraft** (≤20 passengers) and **large aircraft** (>20 passengers)
- At least **two factors** that influence accident outcomes (injury / destruction risk)

## Repository Structure

```
├── Aviation_Accidents_Cleaning.ipynb   # Part 1: Data cleaning & feature engineering
├── Aviation_Accidents_Data_Analysis.ipynb  # Part 2: EDA, visualizations & recommendations
├── data/
│   ├── AviationData.csv               # Raw NTSB dataset
│   ├── USState_Codes.csv              # State codes reference
│   └── aviation_cleaned.csv          # Cleaned output from Part 1
└── README.md
```

## Data Source

NTSB Aviation Accident Database (1948–2023) — filtered to professional-build airplanes from 1983 onwards (40-year maximum model lifetime).

**Raw dataset:** 88,889 records × 31 columns  
**Cleaned dataset:** ~64,000 records × 23 columns

## Key Cleaning Steps

1. **Filtered** to accidents only (not incidents), professional builds (Amateur.Built == No), airplanes only, and events from 1983 onwards.
2. **Imputed** injury count NaNs to 0 (reasonable assumption: missing = not recorded because zero).
3. **Derived** `serious_fatal_fraction` = (fatal + serious injuries) / total onboard — the primary safety metric.
4. **Derived** `is_destroyed` binary column from `Aircraft.damage`.
5. **Standardized** `Make` column (case/whitespace normalization, alias resolution).
6. **Created** `make_model` unique identifier combining Make + Model.
7. **Standardized** categorical columns: Engine.Type, Weather.Condition, Purpose.of.flight, Broad.phase.of.flight.

## Key Findings

### Make-Level Recommendations

**Small Aircraft (≤20 onboard):**
- Top recommended makes: **Cessna**, **Piper**, **Beech**
- These manufacturers produce high-volume, well-tested designs with consistently low injury and destruction rates across large sample sizes.

**Large Aircraft (>20 onboard):**
- Top recommended makes: **Boeing**, **McDonnell Douglas**, **Embraer**
- Commercial jet manufacturers show very low mean injury fractions, supported by large incident counts.

### Model-Level Recommendations

**Small Aircraft:**
- **Cessna 172** — Most recorded incidents among small aircraft with one of the lowest injury rates; statistically the most confident recommendation.
- **Cessna 182** — Similar profile to the 172 with slightly larger capacity.
- **Piper PA-28 (Cherokee)** — Strong safety record with high incident count.

**Large Aircraft:**
- **Boeing 737** — Most recorded incidents among commercial jets; consistently low injury fractions.
- **Boeing 757 / 767** — Strong safety outcomes with significant incident data.

### Safety Factors

**Factor 1 — Weather Condition (VMC vs IMC):**
- Accidents in IMC (instrument meteorological conditions / low visibility) produce significantly higher injury fractions and destruction rates than VMC (clear conditions) accidents.
- IMC injury rates are roughly 2–4× higher than VMC, making weather exposure a critical risk pricing variable.

**Factor 2 — Phase of Flight:**
- Maneuvering and cruise-phase accidents are the most dangerous (highest injury fraction and destruction rate).
- Landing and takeoff accidents, while frequent, tend to be more survivable.
- Personal/instructional flight (high maneuvering exposure) carries greater injury risk than scheduled commercial operations.

## Visualizations

Key charts produced (saved in `data/`):
- `makes_injury_fraction.png` — Top 15 safest makes by injury fraction (small & large)
- `small_makes_violin.png` — Distribution of injury rates, top 10 small aircraft makes
- `large_makes_strip.png` — Distribution of injury rates, top 10 large aircraft makes
- `makes_destruction_rate.png` — Destruction rates by make
- `large_models_injury.png` / `small_models_injury.png` — Top safest models
- `weather_safety.png` / `weather_boxplot.png` — Weather condition analysis
- `phase_safety.png` / `phase_boxplot.png` — Phase of flight analysis

## Tools Used

- **Python 3** with Pandas, NumPy, Matplotlib, Seaborn
- Jupyter Notebooks
