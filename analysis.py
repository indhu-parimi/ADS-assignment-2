#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the required libraries
import matplotlib.pyplot as mpl
import pandas as pf
import seaborn as sb


# In[2]:


def world_data(filedata):
    """
    Reads a CSV file and returns two dataframes.

    Parameters:
    -----------
    dataset : str
        The path to the CSV file.

    Returns:
    --------
    dt_name : pandas.DataFrame
        A dataframe with the country names as index and the columns as years.
    dt_data_country : pandas.DataFrame
        A dataframe with the country codes as index and the columns as years.
    """
    # read the CSV file and skip the first 4 rows of metadata
    info = pf.read_csv(filedata, skiprows=4)
    
    # drop unnecessary columns from the dataframe
    countries = info.drop(columns=['Country Code','Indicator Code','Unnamed: 66'], inplace=True)
    
    # set the index of the dataframe to 'Country Name' and transpose the dataframe
    countries = info.set_index('Country Name').T
    
    # set the index of the dataframe to 'Country Name' and reset the index
    df_name = info.set_index('Country Name').reset_index()
    return  df_name, countries


# In[3]:


# Reading the CSV file
df_name , countries = world_data("wbdata.csv")

# Displaying the first five rows of the df_name dataframe
df_name.head()


# In[4]:


countries.head()


# In[5]:


def attribute(indicators, info):
    """
    Returns a dataframe with the specified indicator.

    Parameters:
    -----------
    indicators : str
        The name of the indicator to select.
    dt : pandas.DataFrame
        The dataframe to select from.

    Returns:
    --------
    dt : pandas.DataFrame
        A dataframe with the specified indicator.
    """
    info = info[info['Indicator Name'].isin([indicators])]
    return info


# In[6]:


def choose_country(countries, info):
    """
    Returns a dataframe with the specified country.

    Parameters:
    -----------
    country : str
        The name of the country to select.
    dt : pandas.DataFrame
        The dataframe to select from.

    Returns:
    --------
    dt : pandas.DataFrame
        A dataframe with the specified country.
    """
    # Selecting data for the specified countries
    info = info[info['Country Name'].isin([countries])]
    
    # Dropping unnecessary column and setting index to Indicator Name
    info=info.set_index("Indicator Name")
    info=info.drop("Country Name",axis=1)
    
    # Transposing the dataframe
    info=info.T
    return info


# In[7]:


# Creating a list of countries
countries = ['United States', 'India', 'Australia', 'United Kingdom']

# Selecting data for these countries
t_pop = df_name[df_name['Country Name'].isin(countries)]

# Creating a line plot
mpl.plot(t_pop['Country Name'])

# Rotating x-axis labels
mpl.xticks(rotation=90)

# Setting y-axis label
mpl.ylabel('Countries')

# Setting title
mpl.title('Population in millions')

# Displaying plot
mpl.show()


# In[8]:


# Creating a list of countries
countries = ['Argentina', 'Belgium', 'Mexico', 'Italy']

# Selecting data for these countries
Foreign_invest = df_name[df_name['Country Name'].isin(countries)]

# Creating a bar plot
mpl.bar(Foreign_invest['Country Name'], Foreign_invest['2009'])

# Rotating x-axis labels
mpl.xticks(rotation=90)

# Setting y-axis label
mpl.ylabel('GDP %')

# Setting title
mpl.title('Foreign direct investment, net inflows (% of GDP)')

# Displaying plot
mpl.show()


# In[9]:


# Selecting data for a particular country using 'choose_country' function
elec_prod = choose_country('Austria', df_name)

# Selecting the relevant columns
percentage = elec_prod[['Electricity production from oil sources (% of total)',
'Electricity production from natural gas sources (% of total)',
'Electricity production from hydroelectric sources (% of total)',
'Electricity production from coal sources (% of total)']]

# Calculating the correlation matrix
correlation = percentage.corr()

# Creating a heatmap using seaborn library
sea = sb.heatmap(correlation, annot=True)


# In[22]:


import matplotlib.pyplot as plt

# Creating a list of countries
countries = ['United States', 'India', 'Australia', 'United Kingdom']

# Selecting data for these countries
mort_rate = df_name[df_name['Country Name'].isin(countries)]

# Creating a stem plot
plt.stem(mort_rate['Country Name'], mort_rate['2017'])

# Rotating x-axis labels
plt.xticks(rotation=90)

# Setting y-axis label
plt.ylabel('Mortality rate %')

# Setting title
plt.title('Mortality rate, under-5 (per 1,000 live births)')

# Displaying plot
plt.show()


# In[23]:


# Selecting data for a specific country
t_pop = choose_country('Australia', df_name)

# Selecting columns of interest
pop_percentage = t_pop[['Urban population (% of total population)',
'Urban population','Urban population growth (annual %)',
'Population, total','Population growth (annual %)']]

# Calculating correlation between the selected columns
pop_correlation = pop_percentage.corr()

# Creating a heatmap to visualize the correlation matrix
sea = sb.heatmap(pop_correlation, annot=True)


# In[ ]:




