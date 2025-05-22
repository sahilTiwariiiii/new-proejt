import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from preswald import text, plotly, table

# Load Dataa which was in Origina data file

df = pd.read_csv("data/Original_data.csv")


# 1. Gender Distribution 
fig1 = px.pie(df, names='GENDER', title='Gender Distribution')
plotly(fig1)

# 2. Age Distributio n 
fig2 = px.histogram(df, x='AGE', nbins=10, title='Age Distribution')
plotly(fig2)

# 3. Investment Avenue Preferencee
fig3 = px.pie(df, names='Do you invest in Investment Avenues?', title='Do You Invest in Investment Avenues?')
plotly(fig3)

# 4. Investment in Stck Market
fig4 = px.pie(df, names='Do you invest in Stock Market?', title='Do You Invest in Stock Market?')
plotly(fig4)

# 5. Top Preferred Investment Option
top_avenue = df['Which investment avenue do you mostly invest in?'].value_counts().reset_index()
top_avenue.columns = ['Investment Avenue', 'Count']
fig5 = px.bar(top_avenue, x='Investment Avenue', y='Count', title='Most Preferred Investment Avenue', color='Investment Avenue')
plotly(fig5)

# 6. Expected Return Preferences
fig6 = px.histogram(df, x='How much return do you expect from any investment instrument?',
                    title='Expected Return Ranges', color='How much return do you expect from any investment instrument?')
plotly(fig6)

# 7. Investment Purpose Distribution
purpose_counts = df['What is your purpose behind investment?'].value_counts().reset_index()
purpose_counts.columns = ['Purpose', 'Count']
fig7 = px.bar(purpose_counts, x='Purpose', y='Count', title='Purpose Behind Investment')
plotly(fig7)

# 8. Savings Objective
savings_counts = df['What are your savings objectives?'].value_counts().reset_index()
savings_counts.columns = ['Savings Objective', 'Count']
fig8 = px.bar(savings_counts, x='Savings Objective', y='Count', title='Savings Objectives')
plotly(fig8)

# 9. Time Horizon
fig9 = px.pie(df, names='How long do you prefer to keep your money in any investment instrument?',
              title='Investment Time Horizon')
plotly(fig9)

# 10. Monitoring Frequency
fig10 = px.pie(df, names='How often do you monitor your investment?',
               title='Investment Monitoring Frequency')
plotly(fig10)

# Text insight
text("### Key Insights Summary")
text("- Majority of participants are in the age range of 20-35.")
text("- A large number prefer investing in Mutual Funds and Equity.")
text("- 20%-30% return is the most expected range.")
text("- Most investors save for Retirement and Health Care.")
text("- Safe investments and better returns are strong motivators.")

# it is not necessary it was Optional: Show table if needed
table(df.head(), title="Sample Data Preview")
