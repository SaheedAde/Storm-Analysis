from django.shortcuts import render

#Import datascience library
import pandas as pd

# Create your views here.

def data_analysis(request):

    # read file
    # filename = 'stormdata/Storm Events Database - 2008.xlsx'
    # data = pd.ExcelFile(filename)
    #
    # # First dataframe
    # df1 = pd.read_excel(data, 'Details')
    #
    # # Second dataframe
    # df2 = pd.read_excel(data, 'Fatalities')

    # USING CSV BECAUSE IT LOADS FASTER
    # Details = 'stormdata/Details.csv'
    Fatalities = 'stormdata/Fatalities.csv'
    #
    # df1 = pd.read_csv(Details, encoding="ISO-8859-1")
    df2 = pd.read_csv(Fatalities, encoding="ISO-8859-1")

    Det11 = pd.read_csv('stormdata/Det11.csv', encoding="ISO-8859-1")
    Det12 = pd.read_csv('stormdata/Det12.csv', encoding="ISO-8859-1")
    Det21 = pd.read_csv('stormdata/Det22a.csv',encoding="ISO-8859-1")
    Det22 = pd.read_csv('stormdata/Det22b.csv', encoding="ISO-8859-1")

    df1=pd.concat([Det11, Det12, Det21, Det22], ignore_index=True, sort=True)


    # state frequency-----------------------------------------------------------------------------
    # STATES WITH MOST FREQUENT STORM
    state_freq = df1['STATE'].value_counts()
    state_freq = state_freq.rename('Frequency of storm by state').to_frame().reset_index()

    #To get my y plot list
    y_state_freq = state_freq['Frequency of storm by state'].tolist()

    #To get my x plot list
    x_state_freq = state_freq['index'].tolist()



    # EVENT TYPE frequency---------------------------------------------------------------------
    # STORM EVENTS WITH MOST FREQUENT STORM
    storm_type_freq = df1['EVENT_TYPE'].value_counts()
    storm_type_freq = storm_type_freq.rename('Frequency of storm by storm type').to_frame().reset_index()

    # To get my y plot list
    y_storm_type_freq = storm_type_freq['Frequency of storm by storm type'].tolist()

    # To get my x plot list
    x_storm_type_freq = storm_type_freq['index'].tolist()


    #STORM FREQUENCY OF MONTH--------------------------------------------------------------------
    month_freq = df1['MONTH_NAME'].value_counts(sort=False)
    month_freq = month_freq.rename('Frequency of storm by month').to_frame().reset_index()

    # To get my y plot list
    y_month_freq = month_freq['Frequency of storm by month'].tolist()

    # To get my x plot list
    x_month_freq = month_freq['index'].tolist()

    # FATALITY BY GENDER--------------------------------------------------------------------
    fatal_sex = df2['FATALITY_SEX'].value_counts().head()
    fatal_sex = fatal_sex.rename('Fatality Sex').to_frame().reset_index()

    # To get my y plot list
    y_fatal_sex = fatal_sex['Fatality Sex'].tolist()

    # To get my x plot list
    x_fatal_sex = fatal_sex['index'].tolist()



    # #--------------------- JOINING THE 2 DATAFRAMES BY EVENT ID TO FORM A THIRD DATAFRAME-------------------------------
    df3 = df1.join(df2.set_index('EVENT_ID'), on='EVENT_ID')

    # # FATALITIES AGAINST EVENT TYPE---------------------------------------------
    #### DIRECT FATALITIES AGAINST EVENT TYPE
    event_direct_death = df3.groupby('EVENT_TYPE')['DEATHS_DIRECT'].sum()
    event_direct_death = event_direct_death.rename('Direct Death').to_frame().reset_index().sort_values(by=['Direct Death'], ascending=False)

    # To get my y plot list
    y_direct = event_direct_death['Direct Death'].tolist()

    # To get my x plot list
    x_direct = event_direct_death['EVENT_TYPE'].tolist()

    #### INDIRECT FATALITIES AGAINST EVENT TYPE
    event_indirect_death = df3.groupby('EVENT_TYPE')['DEATHS_INDIRECT'].sum()
    event_indirect_death = event_indirect_death.rename('Indirect Death').to_frame().reset_index().sort_values(by=['Indirect Death'], ascending=False)

    # To get my y plot list
    y_indirect = event_indirect_death['Indirect Death'].tolist()

    # To get my x plot list
    x_indirect = event_indirect_death['EVENT_TYPE'].tolist()

    # FATALITIES AGAINST STATES------------------------------------------------------------
    #### DIRECT FATALITIES AGAINST STATES
    state_direct_death = df3.groupby('STATE')['DEATHS_DIRECT'].sum()
    state_direct_death = state_direct_death.rename('Direct Death').to_frame().reset_index().sort_values(by=['Direct Death'], ascending=False)

    # To get my y plot list
    y_direct_state = state_direct_death['Direct Death'].tolist()

    # To get my x plot list
    x_direct_state = state_direct_death['STATE'].tolist()

    #### INDIRECT FATALITIES AGAINST STATES
    state_indirect_death = df3.groupby('STATE')['DEATHS_INDIRECT'].sum()
    state_indirect_death = state_indirect_death.rename('Indirect Death').to_frame().reset_index().sort_values(by=['Indirect Death'], ascending=False)

    # To get my y plot list
    y_indirect_state = state_indirect_death['Indirect Death'].tolist()

    # To get my x plot list
    x_indirect_state = state_indirect_death['STATE'].tolist()

    # DIRECT FATALITIES AGAINST STATES HEATMAP---------------------------------------------------------------------------------
    death_heat = df3.groupby('STATE')['DEATHS_DIRECT'].sum().sort_values(ascending=False).head(10)
    death_heat = death_heat.rename('Death Heat').to_frame().reset_index()

    # To get my y plot list
    y_death_heat = death_heat['Death Heat'].tolist()

    # To get my x plot list
    x_death_heat = death_heat['STATE'].tolist()




    context = {
        'x_state_freq':x_state_freq, 'y_state_freq': y_state_freq,
        'x_storm_type_freq': x_storm_type_freq, 'y_storm_type_freq': y_storm_type_freq,
        'x_month_freq': x_month_freq, 'y_month_freq': y_month_freq,
        'x_fatal_sex': x_fatal_sex, 'y_fatal_sex': y_fatal_sex,
        'x_direct':x_direct, 'y_direct': y_direct,
        'x_indirect': x_indirect, 'y_indirect': y_indirect,
        'x_direct_state': x_direct_state, 'y_direct_state': y_direct_state,
        'x_indirect_state': x_indirect_state, 'y_indirect_state': y_indirect_state,
        'x_death_heat': x_death_heat, 'y_death_heat': y_death_heat,
               }
    return render(request, 'stormdata/index.html', context)