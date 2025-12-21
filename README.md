# Housing Rental Optimizer

A comprehensive data analysis tool for analyzing London's housing rental market, providing insights into rental yields, price elasticity, market dynamics, and borough-level comparisons across all 33 London boroughs.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts Documentation](#scripts-documentation)
- [Data Requirements](#data-requirements)
- [Output Files](#output-files)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

This project analyzes 2018 housing data from London boroughs to provide actionable insights for:
- **Investors**: Identify high-yield investment opportunities
- **Renters**: Compare rental costs across boroughs
- **Policy Makers**: Understand housing affordability trends
- **Researchers**: Analyze market dynamics and price elasticity

The toolkit generates multiple visualizations including scatter plots with quadrant analysis, heat maps, histograms with KDE overlays, and ranked bar charts.

## Features

- **Price Elasticity Analysis**: Four comprehensive scatter plots analyzing relationships between rent, price, sales volume, and renter counts
- **Geographic Heat Map**: Interactive Folium map showing gross yield distribution across London boroughs
- **Statistical Analysis**: Regression analysis with confidence intervals, correlation coefficients, and p-values
- **Distribution Analysis**: Histogram with Kernel Density Estimation (KDE) for gross rental yield
- **Yield Ranking**: Horizontal bar chart ranking all boroughs by gross rental yield
- **Quadrant Analysis**: Market segmentation based on median values
- **Comprehensive Testing**: 18 unit tests ensuring data integrity and visualization accuracy

## Project Structure

```
Housing-Rental-Optimizer/
│
├── data/
│   └── Housing_Rent_Price_Volume.csv          # Source data (33 London boroughs)
│
├── price_elasticity_graph.py                   # 4 scatter plots analyzing market dynamics
├── rent+price_scatter_plot.py                  # Statistical regression analysis
├── heat_map_chart.py                           # Interactive geographic heat map
├── distribution_Gross_Rental_Yield_histogram.py # Yield distribution histogram
├── yield_ranking_barchart.py                   # Borough ranking by yield
├── price_elasticity_unit_test.py               # Unit tests (18 test cases)
├── requirements.txt                            # Python CircleCI dependencies
└── README.md                                   # This file
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone or download the repository**
   ```bash
   cd Housing-Rental-Optimizer
   ```

2. **Install required packages**
   ```bash
   pip install pandas numpy matplotlib scipy folium branca requests pytest
   ```

3. **Verify data file exists**
   Ensure `data/Housing_Rent_Price_Volume.csv` is present in the data directory.

## Usage

Run each script independently to generate specific visualizations:

### 1. Price Elasticity Analysis (4 Plots)

**Generates**: 4 interactive scatter plots with quadrant analysis
- Plot 1: Rent vs Sales Volume (Rental Market Strength)
- Plot 2: Price vs Renter Count (Affordability vs Demand)
- Plot 3: Price vs Sales Volume (Market Activity)
- Plot 4: Rent vs Renter Count (Rental Market Dynamics)

### 2. Statistical Regression Analysis

**Generates**: Scatter plot with regression line, 95% confidence interval, and detailed statistics

### 3. Interactive Heat Map

**Generates**: `london_gross_yield_heatmap.html` - Opens in browser automatically
**Features**: Hover tooltips with borough details, color-coded yield distribution

### 4. Gross Yield Distribution

**Generates**: `Appendix_Figure_Gross_Yield_Distribution.png` - Histogram with KDE overlay

### 5. Yield Ranking Chart

**Generates**: `Appendix_Figure_Yield_Ranking.png` - Horizontal bar chart ranking all boroughs

### 6. Run Unit Tests

**Runs**: 18 comprehensive unit tests validating data integrity and analysis logic

## Documentation

### 1. `price_elasticity_graph.py`

**Purpose**: Analyzes price elasticity through four different market perspectives.

**Key Features**:
- **Quadrant Analysis**: Divides data into four market segments using median values
- **Color Mapping**: Uses gross yield (%) or rent values for color intensity
- **Trend Lines**: Linear regression lines showing market trends
- **Smart Annotations**: Labels key boroughs based on threshold values
- **Professional Styling**: seaborn-v0_8-whitegrid style with custom colors

**Quadrant Interpretations**:

| Plot | X-Axis | Y-Axis | Purpose |
|------|--------|--------|---------|
| 1 | Monthly Rent | Sales Volume | Identify rental vs ownership markets |
| 2 | House Price | Renter Count | Analyze affordability impact |
| 3 | House Price | Sales Volume | Understand market activity |
| 4 | Monthly Rent | Renter Count | Examine rental demand dynamics |

**Technical Details**:
- Figure size: 12x8 inches
- Scatter point size: 150
- Color maps: RdYlGn (red-yellow-green), YlOrRd (yellow-orange-red)
- Annotation thresholds customized per plot to highlight outliers

---

### 2. `rent+price_scatter_plot.py`

**Purpose**: Statistical regression analysis of rent vs price relationship.

**Analysis Performed**:
- **Pearson Correlation**: Measures linear relationship strength
- **Linear Regression**: Calculates best-fit line (y = mx + b)
- **R-squared (R²)**: Explains variance percentage
- **P-value**: Statistical significance testing
- **95% Confidence Interval**: Uncertainty visualization
- **Standard Error**: Regression accuracy measure

**Output Statistics**:
```
Regression Equation: Price = {slope}x + {intercept}
R²: Percentage of variance explained
Correlation (r): Strength and direction
P-value: Statistical significance
Standard Error: Prediction accuracy
```

**Interpretation Example**:
"For every £1 increase in monthly rent, house price increases by approximately £{slope}"

---

### 3. `heat_map_chart.py`

**Purpose**: Interactive geographic visualization of gross rental yield across London.

**Key Features**:
- **Interactive Tooltips**: Hover to see borough details (yield, rent, price)
- **Custom Colormap**: Yellow-to-red gradient (9-color scale)
- **GeoJSON Integration**: Fetches London borough boundaries from GitHub
- **Auto-open Browser**: Automatically displays map after generation
- **Highlight Effect**: Borders darken on hover for emphasis

**Data Sources**:
- Borough boundaries: `radoi90/housequest-data` repository
- Housing data: Local CSV file

**Map Configuration**:
- Center: [51.5074, -0.1278] (London coordinates)
- Zoom: Level 10
- Tiles: CARTO Light basemap
- Fill opacity: 0.8 (80%)
- Border color: White

**Output**: `london_gross_yield_heatmap.html`

---

### 4. `distribution_Gross_Rental_Yield_histogram.py`

**Purpose**: Visualizes the distribution pattern of rental yields across boroughs.

**Statistical Components**:

1. **Histogram**:
   - Bins: 12
   - Color: Steel blue (#4C72B0)
   - Alpha: 0.65 (transparency)
   - Edge color: White

2. **KDE (Kernel Density Estimation)**:
   - Method: Gaussian kernel
   - Points: 200 interpolated values
   - Color: Red (#C44E52)
   - Shows smooth probability distribution

3. **Median Line**:
   - Style: Black dashed line
   - Label: Shows exact median value
   - Purpose: Reference point for yield comparison

**Styling**:
- Style: seaborn-v0_8-whitegrid
- Figure size: 10x6 inches
- Resolution: 300 DPI (publication quality)
- Font weights: Bold for labels and title

**Output**: `Appendix_Figure_Gross_Yield_Distribution.png`

---

### 5. `yield_ranking_barchart.py`

**Purpose**: Ranks all 33 London boroughs by gross rental yield in descending order.

**Features**:
- **Horizontal Bars**: Better readability for borough names
- **Value Annotations**: Exact yield percentage on each bar
- **Sorted Display**: Highest yield at top
- **Clean Design**: Minimal spines, subtle grid
- **Color**: Steel blue (#4C72B0) with 80% opacity

**Chart Configuration**:
- Figure size: 10x12 inches (tall for 33 boroughs)
- Inverted Y-axis: Best performing boroughs at top
- Grid: X-axis only, dashed, 20% opacity
- Text size: 9pt for annotations
- Resolution: 300 DPI

**Output**: `Appendix_Figure_Yield_Ranking.png`

---

### 6. `price_elasticity_unit_test.py`

**Purpose**: Comprehensive testing suite ensuring data quality and visualization accuracy.

**Test Categories**:

#### Data Integrity Tests (8 tests)
- `test_data_file_exists`: Verifies CSV file presence
- `test_data_loaded_successfully`: Checks DataFrame is not empty
- `test_required_columns_exist`: Validates all 6 required columns
- `test_data_types`: Ensures numeric columns are properly typed
- `test_no_missing_values`: Checks for NaN values
- `test_positive_values`: Validates all values are positive/non-negative
- `test_borough_count`: Confirms exactly 33 boroughs
- `test_data_ranges_realistic`: London-specific range validation

#### Statistical Tests (5 tests)
- `test_median_calculations`: Validates median calculations
- `test_trend_line_calculation_plot1-4`: Tests polynomial fits (4 tests)

#### Visualization Tests (5 tests)
- `test_scatter_plot_generation`: Ensures plots generate without errors
- `test_colormap_values_valid`: Validates color mapping values
- `test_annotation_threshold_logic`: Checks annotation selection
- `test_quadrant_classification`: Verifies all boroughs classified
- `test_data_ranges_realistic`: London-specific validation

**Validation Ranges**:
- Rent: £500 - £5,000/month
- Price: £100,000 - £2,000,000
- Gross Yield: 1% - 10%

**Expected Output**: All 18 tests pass
```
Ran 18 tests in {time}s
OK
```

## Data Requirements

### Input File: `data/Housing_Rent_Price_Volume.csv`

**Required Columns**:
1. `Boroughs` (string): Borough name
2. `Average Monthly Rent (£)` (float): Average monthly rental price
3. `Counts of Rents` (string/float): Number of rental properties (comma-formatted)
4. `Average Price (£)` (string/float): Average house price (comma-formatted)
5. `Average Sales Volume ` (float): Average number of property sales
6. `Gross Yield (%)` (float): Annual rental yield percentage

**Notes**:
- Price and count columns may contain commas (handled by scripts)
- Space after "Average Sales Volume " is intentional (matches CSV header)
- All 33 London boroughs must be included

## Output Files

| Script | Output File | Format | Description |
|--------|------------|--------|-------------|
| `price_elasticity_graph.py` | Interactive display | PNG/Screen | 4 scatter plots (not saved) |
| `rent+price_scatter_plot.py` | Interactive display | PNG/Screen | Regression plot + console stats |
| `heat_map_chart.py` | `london_gross_yield_heatmap.html` | HTML | Interactive map |
| `distribution_Gross_Rental_Yield_histogram.py` | `Appendix_Figure_Gross_Yield_Distribution.png` | PNG (300 DPI) | Histogram with KDE |
| `yield_ranking_barchart.py` | `Appendix_Figure_Yield_Ranking.png` | PNG (300 DPI) | Ranking chart |

**Note**: To save the price elasticity plots, modify the scripts to add `plt.savefig('filename.png', dpi=300)` before `plt.show()`.

## Testing

The project includes a comprehensive test suite covering:

- **Data validation**: File existence, completeness, data types
- **Statistical accuracy**: Median calculations, regression fits
- **Visualization integrity**: Plot generation, color mapping
- **Business logic**: Quadrant classification, annotation thresholds
- **Data quality**: Realistic value ranges for London market

## Dependencies

```
pandas          - Data manipulation and analysis
numpy           - Numerical computing and statistics
matplotlib      - Plotting and visualization
scipy           - Scientific computing (KDE, statistics)
folium          - Interactive mapping
branca          - Color mapping for Folium
requests        - HTTP library for GeoJSON fetching
pytest          - Testing framework (optional)
```

**Install all dependencies**:
```bash
pip install pandas numpy matplotlib scipy folium branca requests pytest
```

## Key Insights

The analysis reveals:

1. **High Yield Areas**: Boroughs with >5% gross yield (typically outer London)
2. **Rental Markets**: Areas with high rent but low sales (e.g., Westminster, Camden)
3. **Affordable Areas**: Low rent + high sales volume (outer boroughs)
4. **Investment Opportunities**: Quadrant analysis identifies best ROI locations
5. **Price Elasticity**: Positive correlation between rent and house prices (R² shown in regression)

## Usage Tips

1. **Customizing Plots**: Modify color schemes by changing `cmap` parameters
2. **Annotation Thresholds**: Adjust threshold values in price_elasticity_graph.py to highlight different boroughs
3. **Export Formats**: Add `plt.savefig()` calls to save plots as PNG, PDF, or SVG
4. **Data Updates**: Replace CSV file with new year data (maintain column structure)
5. **Additional Metrics**: Add new columns to CSV and modify scripts to visualize

