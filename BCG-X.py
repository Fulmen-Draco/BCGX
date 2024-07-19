import pandas as pd
import streamlit as st

# Load data
final_report = pd.read_csv('bcg.csv')
summary_report = pd.read_csv('summ.csv')

def financial_chatbot(user_query, fiscal_year, company_input):
    if user_query == "What is the total revenue?":
        revenue = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Revenue'].values[0]
        return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
    
    elif user_query == "What is the Net Income?":
        net_income  = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income'].values[0]
        return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
    
    elif user_query == "What is the sum of total assets?":
        total_assets  = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Assets'].values[0]
        return f"The sum of Total Assets for {company_input} for fiscal year {fiscal_year} is $ {total_assets}"
    
    elif user_query == "What is the sum of total liabilities?":
        total_liabilities  = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Liabilities'].values[0]
        return f"The sum of Total Liabilities for {company_input} for fiscal year {fiscal_year} is $ {total_liabilities}"
    
    elif user_query == "What is cash flow from operating activities?":
        cash_ops = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Cash Flow from Operating Activities'].values[0]
        return f"The Cash Flow from Operating Activities for {company_input} for fiscal year {fiscal_year} is $ {cash_ops}"
    
    elif user_query == "What is the revenue growth(%) ?":
        revenue_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
        return f"The Revenue Growth(%) for {company_input} for fiscal year {fiscal_year} is {revenue_growth}(%)"
    
    elif user_query == "What is the net income growth(%) ?":
        net_income_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
        return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {net_income_growth}(%)"
    
    elif user_query == "What is the assets growth(%) ?":
        assets_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
        return f"The Assets Growth(%) for {company_input} for fiscal year {fiscal_year} is {assets_growth}(%)"
    
    elif user_query == "What is the liabilities growth(%) ?":
        liabilities_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
        return f"The Liabilities Growth(%) for {company_input} for fiscal year {fiscal_year} is {liabilities_growth}(%)"
    
    elif user_query == "What is the cash flow from operations growth(%) ?":
        cash_ops_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
        return f"The Cash Flow from Operations Growth(%) for {company_input} for fiscal year {fiscal_year} is {cash_ops_growth}(%)"
    
    elif user_query == "What is the year by year average revenue growth rate(%)?":
        year_avg_revenue_growth = summary_report[(summary_report['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_revenue_growth}(%)"
     
    elif user_query == "What is the year by year average net income growth rate(%)?":
        year_avg_net_income_growth = summary_report[(summary_report['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
        return f"The Year By Year Net Income Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_net_income_growth}(%)"
    
    elif user_query == "What is the year by year average assets growth rate(%)?":
        year_avg_assets_growth = summary_report[(summary_report['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Assets Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_assets_growth}(%)"
    
    elif user_query == "What is the year by year average liabilities growth rate(%)?":
        year_avg_liabilities_growth = summary_report[(summary_report['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Liabilities Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_liabilities_growth}(%)"
    
    elif user_query == "What is the year by year average cash flow from operations growth rate(%)?":
        year_avg_cash_ops_growth = summary_report[(summary_report['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
        return f"The Year By Year Average Cash Flow from Operations Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_cash_ops_growth}(%)" 
    
    else:
        return "Sorry, I can only provide information on the requested query."

# Streamlit app structure
st.title("AI Driven Financial Chatbot")

user_input = st.text_input("Enter 'Hi' to start the chatbot session, type 'exit' to quit:")

if user_input.lower() == "hi":
    st.write("Hello! Welcome to AI Driven Financial Chatbot!!!")
    st.write("I can help you with your financial queries.")
    st.write("Please select the company name from below:")
    st.write("1. Microsoft\n2. Tesla\n3. Apple")
    
    company_input = st.text_input("Enter company name: ").capitalize()
    if company_input not in ['Apple', 'Microsoft', 'Tesla']:
        st.write("Invalid Company Name. Please check and enter the correct company name.")
    else:
        st.write("The data for the fiscal year 2023, 2022, and 2021 is currently available.")
        fiscal_year = int(st.text_input("Enter the fiscal year for the selected company:"))
        if fiscal_year not in [2023, 2022, 2021]:
            st.write("Please enter a valid fiscal year.")
        else:
            query = st.text_input("Enter your query:")
            if query:
                response = financial_chatbot(query, fiscal_year, company_input)
                st.write(response)
elif user_input.lower() == "exit":
    st.write("Goodbye!")
else:
    st.write("Please enter 'Hi' to start the chatbot session.")
