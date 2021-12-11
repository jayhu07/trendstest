import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#cmd = ('SELECT customerName, orderNumber, YEAR(orderDate) AS year, SUM(quantityOrdered * priceEach) AS total ' +
#'FROM orders AS O ' +
#'JOIN customers AS C USING(customerNumber) ' +
#'JOIN orderdetails AS D USING(orderNumber) ' +
#'GROUP BY customerName, orderNumber, orderDate ' +
#'ORDER BY customerName;')


topCustomer = st.container()

with topCustomer:
    # select year period
    year = st.selectbox(label = 'Select the Year',
                        options = [2003, 2004, 2005])
    # select units, in dollars or in order amount
    measure = st.selectbox(label = 'Select Measurements',
                        options = ['orders count', 'total price'])

    # data cleaning
    df = pd.read_csv('topCustomers.csv')
    df = df.rename(columns={"total": "total price", "orderNumber": "orders count"})
    df1 = pd.DataFrame(df.groupby(['year', 'customerName'])['total price'].sum())
    df2 = pd.DataFrame(df.groupby(['year', 'customerName'])['orders count'].count())
    final = df1.merge(df2, left_index=True, right_index=True)
    final = final.loc[(year,)].sort_values(measure, ascending=False).head(10)

    # plot bar chart
    fig=final[measure].plot.bar()
    st.pyplot(fig)

