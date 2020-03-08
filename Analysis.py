import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html


#Data --------------------------------------------------------

# https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/5206.0Dec%202019?OpenDocument

df = pd.read_excel(f"https://www.abs.gov.au/ausstats/meisubs.nsf/log?openagent&5206006_industry_gva.xls&5206.0&Time%20Series%20Spreadsheet&13717EFC68459FA1CA258520000C2AA5&0&Dec%202019&04.03.2020&Latest",
sheet_name='Data1')

columns = ["Unnamed: 0",
"Agriculture, forestry and fishing (A) ;",
"Mining (B) ;",
"Manufacturing (C) ;",
"Electricity, gas, water and waste services (D) ;",
"Construction (E) ;",
"Wholesale trade (F) ;",
"Retail trade (G) ;",
"Accommodation and food services (H) ;",
"Transport, postal and warehousing (I) ;",
"Information media and telecommunications (J) ;",
"Financial and insurance services (K) ;",
"Rental, hiring and real estate services (L) ;",
"Professional, scientific and technical services (M) ;",
"Administrative and support services (N) ;",
"Public administration and safety (O) ;",
"Education and training (P) ;",
"Health care and social assistance (Q) ;",
"Arts and recreation services (R) ;",
"Other services (S) ;",
"Ownership of dwellings ;",
"Taxes less subsidies on products ;",
"Statistical discrepancy (P) ;"]

df.rename(columns={'Unnamed: 0': 'Criteria',
                   'Agriculture, forestry and fishing (A) ;':'Agriculture, forestry and fishing',
                  'Mining (B) ;': 'Mining',
                  'Manufacturing (C) ;': 'Manufacturing',
                  'Electricity, gas, water and waste services (D) ;': 'Electricity, gas, water & waste services',
                  'Construction (E) ;': 'Construction',
                   'Wholesale trade (F) ;': 'Wholesale trade',
                   'Retail trade (G) ;': 'Retail trade',
                   'Accommodation and food services (H) ;': 'Accommodation & food services',
                   'Transport, postal and warehousing (I) ;': 'Transport, postal & warehousing',
                   'Information media and telecommunications (J) ;': 'Information media & telecommunications',
                   'Financial and insurance services (K) ;':'Financial & insurance services',
                   'Rental, hiring and real estate services (L) ;':'Rental, hiring & real estate services',
                   'Professional, scientific and technical services (M) ;':'Professional, scientific & technical services',
                   'Administrative and support services (N) ;':'Administrative & support services',
                   'Public administration and safety (O) ;':'Public administration & safety',
                   'Education and training (P) ;': 'Education and training',
                   'Health care and social assistance (Q) ;': 'Health care & social assistance',
                   'Arts and recreation services (R) ;':'Arts & recreation services',
                   'Other services (S) ;': 'Other services',
                   'Ownership of dwellings ;':'Ownership of dwellings',
                  'Taxes less subsidies on products ;':'Taxes less subsidies on products',
                  'Statistical discrepancy (P) ;': 'Statistical discrepancy'}, inplace=True)


df.set_index('Criteria', inplace=True)

df.drop(['Unit', 'Series Type', 'Data Type','Frequency', 'Collection Month',
         'Series Start','Series End', 'No. Obs', 'Series ID'], inplace= True)

df.index = pd.to_datetime(df.index)
df.index.names = ['Date']

Prior_Year = df['2017-12-01' :'2018-12-01']
Current_Year = df['2019-01-01' :'2019-12-01']

# Prior Year Calculations
Agr_PY = Prior_Year['Agriculture, forestry and fishing'].sum() * 1000000
Mining_PY = Prior_Year['Mining'].sum() * 1000000
Manufact_PY = Prior_Year['Manufacturing'].sum() * 1000000
Elect_PY = Prior_Year['Electricity, gas, water & waste services'].sum() * 1000000
Construct_PY = Prior_Year['Construction'].sum() * 1000000
WholeTrade_PY = Prior_Year['Wholesale trade'].sum() * 1000000
RetailTrade_PY = Prior_Year['Retail trade'].sum() * 1000000
AccomFS_PY = Prior_Year['Accommodation & food services'].sum() * 1000000
Transport_PY = Prior_Year['Transport, postal & warehousing'].sum() * 1000000
Info_PY = Prior_Year['Information media & telecommunications'].sum() * 1000000
Financial_PY = Prior_Year['Financial & insurance services'].sum() * 1000000
Rental_PY = Prior_Year['Rental, hiring & real estate services'].sum() * 1000000
Professional_PY = Prior_Year['Professional, scientific & technical services'].sum() * 1000000
Admin_PY = Prior_Year['Administrative & support services'].sum() * 1000000
Public_PY = Prior_Year['Public administration & safety'].sum() * 1000000
Educate_PY = Prior_Year['Education and training'].sum() * 1000000
Health_PY = Prior_Year['Health care & social assistance'].sum() * 1000000
Arts_PY = Prior_Year['Arts & recreation services'].sum() * 1000000
Other_PY = Prior_Year['Other services'].sum() * 1000000
Owner_PY = Prior_Year['Ownership of dwellings'].sum() * 1000000
Taxes_PY = Prior_Year['Taxes less subsidies on products'].sum() * 1000000
Stats_PY = Prior_Year['Statistical discrepancy'].sum() * 1000000

Prior_Year_Sum = np.sum([Agr_PY, Mining_PY, Manufact_PY, Elect_PY, Construct_PY, WholeTrade_PY, RetailTrade_PY, AccomFS_PY,
                 Transport_PY, Info_PY, Financial_PY, Rental_PY, Professional_PY, Admin_PY, Public_PY,
                 Educate_PY, Health_PY, Arts_PY, Other_PY, Owner_PY, Taxes_PY, Stats_PY])

#This Year Calculations
Agr_CY = Current_Year['Agriculture, forestry and fishing'].sum() * 1000000
Mining_CY = Current_Year['Mining'].sum() * 1000000
Manufact_CY = Current_Year['Manufacturing'].sum() * 1000000
Elect_CY = Current_Year['Electricity, gas, water & waste services'].sum() * 1000000
Construct_CY = Current_Year['Construction'].sum() * 1000000
WholeTrade_CY = Current_Year['Wholesale trade'].sum() * 1000000
RetailTrade_CY = Current_Year['Retail trade'].sum() * 1000000
AccomFS_CY = Current_Year['Accommodation & food services'].sum() * 1000000
Transport_CY = Current_Year['Transport, postal & warehousing'].sum() * 1000000
Info_CY = Current_Year['Information media & telecommunications'].sum() * 1000000
Financial_CY = Current_Year['Financial & insurance services'].sum() * 1000000
Rental_CY = Current_Year['Rental, hiring & real estate services'].sum() * 1000000
Professional_CY = Current_Year['Professional, scientific & technical services'].sum() * 1000000
Admin_CY = Current_Year['Administrative & support services'].sum() * 1000000
Public_CY = Current_Year['Public administration & safety'].sum() * 1000000
Educate_CY = Current_Year['Education and training'].sum() * 1000000
Health_CY = Current_Year['Health care & social assistance'].sum() * 1000000
Arts_CY = Current_Year['Arts & recreation services'].sum() * 1000000
Other_CY = Current_Year['Other services'].sum() * 1000000
Owner_CY = Current_Year['Ownership of dwellings'].sum() * 1000000
Taxes_CY = Current_Year['Taxes less subsidies on products'].sum() * 1000000
Stats_CY = Current_Year['Statistical discrepancy'].sum() * 1000000

Current_Year_Sum = np.sum([Agr_CY, Mining_CY, Manufact_CY, Elect_CY, Construct_CY, WholeTrade_CY, RetailTrade_CY, AccomFS_CY,
                 Transport_CY, Info_CY, Financial_CY, Rental_CY, Professional_CY, Admin_CY, Public_CY,
                 Educate_CY, Health_CY, Arts_CY, Other_CY, Owner_CY, Taxes_CY, Stats_CY])


#Change over prior year

Agr = Agr_CY - Agr_PY 
Mining = Mining_CY - Mining_PY 
Manufact = Manufact_CY - Manufact_PY 
Elect = Elect_CY - Elect_PY 
Construct = Construct_CY - Construct_PY 
WholeTrade = WholeTrade_CY - WholeTrade_PY 
RetailTrade = RetailTrade_CY - RetailTrade_PY 
AccomFS = AccomFS_CY - AccomFS_PY 
Transport = Transport_CY - Transport_PY 
Info = Info_CY - Info_PY 
Financial = Financial_CY - Financial_PY 
Rental = Rental_CY - Rental_PY 
Professional = Professional_CY - Professional_PY 
Admin = Admin_CY - Admin_PY 
Public = Public_CY - Public_PY
Educate = Educate_CY - Educate_PY 
Health = Health_CY - Health_PY 
Arts = Arts_CY - Arts_PY
Other = Other_CY - Other_PY 
Owner = Owner_CY - Owner_PY 
Taxes = Taxes_CY - Taxes_PY
Stats = Stats_CY - Stats_PY


labels = ["Financial & insurance services", "Ownership of dwellings", "Mining", "Construction", "Health care & social assistance",
"Professional, scientific & technical services", "Taxes less subsidies on products", "Manufacturing", "Public administration & safety",
"Education and training", "Transport, postal & warehousing", "Retail trade", "Wholesale trade", "Administrative & support services",
"Rental, hiring & real estate services", "Information media & telecommunications", "Electricity, gas, water & waste services",
"Agriculture, forestry and fishing", "Accommodation & food services", "Other services", "Arts & recreation services", "Statistical discrepancy"]           


values = [Financial_CY, Owner_CY, Mining_CY, Construct_CY, Health_CY, Professional_CY,
Taxes_CY, Manufact_CY, Public_CY, Educate_CY, Transport_CY ,RetailTrade_CY
,WholeTrade_CY, Admin_CY, Rental_CY, Info_CY, Elect_CY, Agr_CY, AccomFS_CY
,Other_CY, Arts_CY, Stats_CY]


x = [Prior_Year_Sum, Agr, Mining, Manufact, Elect, Construct, WholeTrade, RetailTrade, AccomFS, Transport, Info, Financial,
		         Rental, Professional, Admin, Public, Educate, Health, Arts, Other, Owner, Taxes, Stats, Current_Year_Sum]

y = ["Prior Year", "Agriculture, forestry and fishing", "Mining", "Manufacturing",
		         "Electricity, gas, water & waste services", "Construction", "Wholesale trade", "Retail trade",
		         "Accommodation & food services", "Transport, postal & warehousing", "Information media & telecommunications",
		         "Financial & insurance services", "Rental, hiring & real estate services",
		         "Professional, scientific & technical services", "Administrative & support services",
		         "Public administration & safety", "Education and training", "Health care & social assistance",
		         "Arts & recreation services", "Other services", "Ownership of dwellings",
		         "Taxes less subsidies on products", "Statistical discrepancy", "Current Year"]

connector = {"mode":"between", "line":{"width":4, "color":"rgb(0, 0, 0)", "dash":"solid"}}

measure = ["absolute", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "relative",
 "relative", "relative", "relative", "relative", "relative","relative","relative","relative","relative","relative","relative",
 "relative", "relative", "absolute"]

layoutWF= go.Layout(
 margin=go.layout.Margin(l=260, r=10, t=40, b=30), yaxis=dict(showgrid=False), font=dict(size=10, color='black'),
 plot_bgcolor='rgba(0,0,0,0)', autosize=True, xaxis=go.layout.XAxis(autorange=False, range=[1780000000000, 1860000000000], showgrid=False)) 

layoutBar= go.Layout(
 margin=go.layout.Margin(l=0, r=10, t=40, b=250), showlegend=False, yaxis=dict(showgrid=False), xaxis=dict(showgrid=False),
 autosize=True, plot_bgcolor='rgba(0,0,0,0)', font=dict(size=10, color='black')) 


# Launch the application ----------------------------------------------
app = dash.Dash()
server = app.server



app.layout = html.Div([

html.Div([html.H2("Australian GDP Industry Volume Analysis")], style={"textAlign": "center"}),
dcc.Markdown('''*by [Ryan Ashton] (www.linkedin.com/in/ryan-mark-ashton) | Analytics Enthusiast*'''),

dcc.Markdown('''In this short analysis, we review the Australian economy in terms of volume changes by industry that the Australian Bureau of Statistics (ABS) provides.
The graphs below are created with Python programming (Plotly) and are directly linked to the ABS website.

In the background, the code downloads the excel file provided by ABS, cleans it, calculates it and then plots it in a way the ABS would not normally cut their data. To see the code, please feel free to visit [here] (https://github.com/Ryan-Ashton/GDP-Industry-Analysis)


The ABS normally show a rolling quarter on quarter or current quarter vs. the equivalent quarter last year change. The graphs below will be rolling up the previous 4 quarters and compare it with the prior 4 quarters to show a rolling year on year change to show a longer-term perspective.


The metric used to view the change is with chain volume measures which replaced constant price estimates in 1998.
This is to help normalise the price movements to help gain an accurate picture for the Australian economy.

The ABS also provide different estimates of the data, which includes Original, Seasonally Adjusted and Trend estimates.
The ABS recommend trend estimates as the best source of information for making decisions about what to do in the future as it’s directly comparable with different points in time. For that reason, this analysis uses the ‘Trend’ estimates.

Below, we see how big each industry is in terms of volume contribution to the economy.
 '''),

html.Div([html.H3("Australian GDP Industry by Size (Chain Volume Measure)")], style={"textAlign": "center"}),
html.Div([html.H4("December 2018 to December 2019 (12 months)")], style={"textAlign": "center"}),
dcc.Graph(
	figure= go.Figure(
		data=[
			go.Bar(
					y = values,
					x = labels
					)
				],

				layout = layoutBar
				
				)
			),


dcc.Markdown('''The next graph is a waterfall chart that shows the last 12 month movements by industry.

This way you can quickly see what has been growing (green) vs. going backwards (red) which provides a good starting point for a deep dive analysis. '''),



html.Div([html.H3("Australian GDP Year on Year Chain Volume Measure Movements by Industry")], style={"textAlign": "center"}),
html.Div([html.H4("(Last 12 months from Decemeber 2019 to Previous 12 months)")], style={"textAlign": "center"}),
	dcc.Graph(
	figure= go.Figure(
		data=[
			go.Waterfall(
					orientation = 'h',
					measure=measure,
					x=x,
					y=y,
					connector=connector
					)
				],

				layout = layoutWF
				
				)
			), dcc.Markdown('''Hopefully, with these two graphs you gain a quicker insight into what’s happening in the Australian economy over the longer term (compared to what’s normally reported).
			 I will endeavour to keep this up to date as new figures from the ABS is released. ''')
		]
	)



if __name__ == '__main__':
	app.run_server(debug=True)