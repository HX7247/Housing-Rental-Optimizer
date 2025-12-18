import unittest
import pandas as pd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for testing
import matplotlib.pyplot as plt


class TestPriceElasticityGraphs(unittest.TestCase):
    """Unit tests for price elasticity graph generation and data analysis"""
    
    @classmethod
    def setUpClass(cls):
        """Load data once for all tests"""
        cls.data_path = 'data/Housing_Rent_Price_Volume.csv'
        cls.df = pd.read_csv(cls.data_path)
        cls.df['Average Price (£)'] = cls.df['Average Price (£)'].str.replace(',', '').astype(float)
        cls.df['Counts of Rents'] = cls.df['Counts of Rents'].str.replace(',', '').astype(float)
    
    def test_data_file_exists(self):
        """Test that the data file exists"""
        self.assertTrue(os.path.exists(self.data_path), "Data file not found")
    
    def test_data_loaded_successfully(self):
        """Test that data is loaded and not empty"""
        self.assertIsNotNone(self.df, "DataFrame is None")
        self.assertGreater(len(self.df), 0, "DataFrame is empty")
    
    def test_required_columns_exist(self):
        """Test that all required columns are present"""
        required_columns = [
            'Boroughs',
            'Average Monthly Rent (£)',
            'Counts of Rents',
            'Average Price (£)',
            'Average Sales Volume ',
            'Gross Yield (%)'
        ]
        for col in required_columns:
            self.assertIn(col, self.df.columns, f"Column '{col}' not found")
    
    def test_data_types(self):
        """Test that numeric columns have correct data types"""
        self.assertTrue(pd.api.types.is_numeric_dtype(self.df['Average Monthly Rent (£)']),
                       "Average Monthly Rent should be numeric")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.df['Average Price (£)']),
                       "Average Price should be numeric")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.df['Counts of Rents']),
                       "Counts of Rents should be numeric")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.df['Average Sales Volume ']),
                       "Average Sales Volume should be numeric")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.df['Gross Yield (%)']),
                       "Gross Yield should be numeric")
    
    def test_no_missing_values(self):
        """Test that there are no missing values in key columns"""
        key_columns = ['Boroughs', 'Average Monthly Rent (£)', 'Average Price (£)', 
                      'Counts of Rents', 'Average Sales Volume ', 'Gross Yield (%)']
        for col in key_columns:
            self.assertEqual(self.df[col].isna().sum(), 0, 
                           f"Column '{col}' has missing values")
    
    def test_positive_values(self):
        """Test that all numeric values are positive"""
        self.assertTrue((self.df['Average Monthly Rent (£)'] > 0).all(),
                       "All rent values should be positive")
        self.assertTrue((self.df['Average Price (£)'] > 0).all(),
                       "All price values should be positive")
        self.assertTrue((self.df['Counts of Rents'] >= 0).all(),
                       "All rent counts should be non-negative")
        self.assertTrue((self.df['Average Sales Volume '] >= 0).all(),
                       "All sales volumes should be non-negative")
        self.assertTrue((self.df['Gross Yield (%)'] > 0).all(),
                       "All gross yields should be positive")
    
    def test_median_calculations(self):
        """Test that median calculations work correctly"""
        median_rent = self.df['Average Monthly Rent (£)'].median()
        median_sales = self.df['Average Sales Volume '].median()
        median_price = self.df['Average Price (£)'].median()
        median_renters = self.df['Counts of Rents'].median()
        
        self.assertIsInstance(median_rent, (int, float, np.number))
        self.assertIsInstance(median_sales, (int, float, np.number))
        self.assertIsInstance(median_price, (int, float, np.number))
        self.assertIsInstance(median_renters, (int, float, np.number))
        
        self.assertGreater(median_rent, 0)
        self.assertGreater(median_sales, 0)
        self.assertGreater(median_price, 0)
        self.assertGreater(median_renters, 0)
    
    def test_trend_line_calculation_plot1(self):
        """Test trend line calculation for Plot 1 (Rent vs Sales Volume)"""
        x = self.df['Average Monthly Rent (£)']
        y = self.df['Average Sales Volume ']
        z = np.polyfit(x, y, 1)
        
        self.assertEqual(len(z), 2, "Polyfit should return 2 coefficients")
        self.assertTrue(np.isfinite(z[0]), "Slope should be finite")
        self.assertTrue(np.isfinite(z[1]), "Intercept should be finite")
    
    def test_trend_line_calculation_plot2(self):
        """Test trend line calculation for Plot 2 (Price vs Renters)"""
        x = self.df['Average Price (£)']
        y = self.df['Counts of Rents']
        z = np.polyfit(x, y, 1)
        
        self.assertEqual(len(z), 2, "Polyfit should return 2 coefficients")
        self.assertTrue(np.isfinite(z[0]), "Slope should be finite")
        self.assertTrue(np.isfinite(z[1]), "Intercept should be finite")
    
    def test_trend_line_calculation_plot3(self):
        """Test trend line calculation for Plot 3 (Price vs Sales Volume)"""
        x = self.df['Average Price (£)']
        y = self.df['Average Sales Volume ']
        z = np.polyfit(x, y, 1)
        
        self.assertEqual(len(z), 2, "Polyfit should return 2 coefficients")
        self.assertTrue(np.isfinite(z[0]), "Slope should be finite")
        self.assertTrue(np.isfinite(z[1]), "Intercept should be finite")
    
    def test_trend_line_calculation_plot4(self):
        """Test trend line calculation for Plot 4 (Rent vs Renters)"""
        x = self.df['Average Monthly Rent (£)']
        y = self.df['Counts of Rents']
        z = np.polyfit(x, y, 1)
        
        self.assertEqual(len(z), 2, "Polyfit should return 2 coefficients")
        self.assertTrue(np.isfinite(z[0]), "Slope should be finite")
        self.assertTrue(np.isfinite(z[1]), "Intercept should be finite")
    
    def test_borough_count(self):
        """Test that we have the expected number of London boroughs"""
        # London has 33 boroughs including City of London
        self.assertEqual(len(self.df), 33, "Expected 33 London boroughs")
    
    def test_scatter_plot_generation(self):
        """Test that scatter plots can be generated without errors"""
        try:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(self.df['Average Monthly Rent (£)'], 
                      self.df['Average Sales Volume '],
                      s=100, alpha=0.7)
            plt.close(fig)
            success = True
        except Exception as e:
            success = False
            print(f"Scatter plot generation failed: {e}")
        
        self.assertTrue(success, "Scatter plot generation failed")
    
    def test_colormap_values_valid(self):
        """Test that gross yield values are valid for colormap"""
        gross_yield = self.df['Gross Yield (%)']
        self.assertTrue((gross_yield >= 0).all(), "Gross yield should be non-negative")
        self.assertTrue((gross_yield <= 100).all(), "Gross yield should be <= 100%")
    
    def test_annotation_threshold_logic(self):
        """Test that annotation thresholds correctly identify boroughs"""
        # Plot 1 thresholds
        plot1_annotated = self.df[
            (self.df['Average Monthly Rent (£)'] > 2500) | 
            (self.df['Average Sales Volume '] > 350)
        ]
        self.assertGreater(len(plot1_annotated), 0, "Should have boroughs to annotate in Plot 1")
        
        # Plot 2 thresholds
        plot2_annotated = self.df[
            (self.df['Counts of Rents'] > 3500) | 
            (self.df['Average Price (£)'] > 1200000)
        ]
        self.assertGreater(len(plot2_annotated), 0, "Should have boroughs to annotate in Plot 2")
        
        # Plot 3 thresholds
        plot3_annotated = self.df[
            (self.df['Average Sales Volume '] > 350) | 
            (self.df['Average Price (£)'] > 1200000)
        ]
        self.assertGreater(len(plot3_annotated), 0, "Should have boroughs to annotate in Plot 3")
        
        # Plot 4 thresholds
        plot4_annotated = self.df[
            (self.df['Counts of Rents'] > 3500) | 
            (self.df['Average Monthly Rent (£)'] > 2800)
        ]
        self.assertGreater(len(plot4_annotated), 0, "Should have boroughs to annotate in Plot 4")
    
    def test_quadrant_classification(self):
        """Test that quadrant classification logic works"""
        median_rent = self.df['Average Monthly Rent (£)'].median()
        median_sales = self.df['Average Sales Volume '].median()
        
        # Count boroughs in each quadrant
        q1 = len(self.df[(self.df['Average Monthly Rent (£)'] <= median_rent) & 
                        (self.df['Average Sales Volume '] > median_sales)])
        q2 = len(self.df[(self.df['Average Monthly Rent (£)'] > median_rent) & 
                        (self.df['Average Sales Volume '] > median_sales)])
        q3 = len(self.df[(self.df['Average Monthly Rent (£)'] > median_rent) & 
                        (self.df['Average Sales Volume '] <= median_sales)])
        q4 = len(self.df[(self.df['Average Monthly Rent (£)'] <= median_rent) & 
                        (self.df['Average Sales Volume '] <= median_sales)])
        
        # Total should equal number of boroughs
        total_classified = q1 + q2 + q3 + q4
        self.assertEqual(total_classified, len(self.df), 
                        "All boroughs should be classified into quadrants")
    
    def test_data_ranges_realistic(self):
        """Test that data values are within realistic ranges for London"""
        # Rent should be between £500 and £5000 per month
        self.assertTrue((self.df['Average Monthly Rent (£)'] >= 500).all(),
                       "Rent values seem too low")
        self.assertTrue((self.df['Average Monthly Rent (£)'] <= 5000).all(),
                       "Rent values seem too high")
        
        # Price should be between £100,000 and £2,000,000
        self.assertTrue((self.df['Average Price (£)'] >= 100000).all(),
                       "Price values seem too low")
        self.assertTrue((self.df['Average Price (£)'] <= 2000000).all(),
                       "Price values seem too high")
        
        # Gross yield should be between 1% and 10%
        self.assertTrue((self.df['Gross Yield (%)'] >= 1).all(),
                       "Gross yield seems too low")
        self.assertTrue((self.df['Gross Yield (%)'] <= 10).all(),
                       "Gross yield seems too high")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
