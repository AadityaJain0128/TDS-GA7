import marimo as mo
import pandas as pd
import numpy as np
import altair as alt

# Marimo notebook for interactive data analysis
# Author: Data Science Team
# Contact: 23f2003550@ds.study.iitm.ac.in

# Cell 1: Define the interactive widget
# This cell creates a slider to control the number of data points.
# It is an independent cell; other cells will depend on its value.
sample_size_slider = mo.ui.slider(
    start=10, stop=200, step=10, value=50, label="Number of data points:"
)


# Cell 2: Generate synthetic data
# This cell depends on the 'sample_size_slider' from Cell 1.
# When the slider's value changes, this cell will automatically rerun
# to generate a new DataFrame with the specified number of samples.
@mo.capture
def generate_data(sample_size_slider):
    # Data flow: sample_size_slider.value -> n_samples -> df
    n_samples = sample_size_slider.value
    np.random.seed(42)
    data = {
        'x': np.random.rand(n_samples) * 10,
        'y': 2.5 * np.random.rand(n_samples) * 10 + np.random.randn(n_samples) * 2,
        'category': np.random.choice(['A', 'B', 'C'], n_samples)
    }
    df = pd.DataFrame(data)
    return df


# Cell 3: Display the interactive slider and dynamic markdown
# This cell depends on 'sample_size_slider' from Cell 1.
# It renders the slider UI and markdown text that updates reactively.
mo.md(
    f"""
    ## Interactive Data Exploration
    Use the slider below to change the number of data points in the analysis.

    {sample_size_slider}

    **Current sample size:** `{sample_size_slider.value}` points are being generated.
    """
)


# Cell 4: Create and display the plot
# This cell depends on the 'df' DataFrame from Cell 2.
# When 'df' is regenerated, this cell reruns to draw a new chart.
@mo.capture
def create_plot(generate_data):
    df = generate_data.df
    # Data flow: df -> chart
    chart = alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X('x', title='Independent Variable'),
        y=alt.Y('y', title='Dependent Variable'),
        color='category',
        tooltip=['x', 'y', 'category']
    ).properties(
        title='Relationship between X and Y'
    ).interactive()
    return chart


# Cell 5: Display the generated data table
# This cell also depends on the 'df' from Cell 2.
# It provides a tabular view of the data, which updates with the slider.
mo.md(
    f"""
    ### Generated Data
    The following table contains the raw data used for the plot above.
    
    {generate_data.df.head()}
    """
)

# Cell 6: Display the plot created in Cell 4
create_plot.chart
