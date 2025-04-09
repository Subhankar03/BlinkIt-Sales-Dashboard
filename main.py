import pandas as pd, streamlit as st
from streamlit_lottie import st_lottie

# Use README.md to generate the content
with open('README.md', encoding='utf-8') as f:
	md = f.read()
with open('BlinkIt Grocery Sales.xlsx', 'rb') as f:
	wb = f.read()

st.set_page_config(page_title='Blinkit Sales Dashboard', page_icon='📊', layout='wide')
st.title('Blinkit Sales Dashboard')

# Add 2 tabs: Overview, Dashboard
overview, dashboard = st.tabs([':material/description: Overview', ':material/space_dashboard: Dashboard'])
dashboard.video('Screen Captures/Dashboard.mp4', autoplay=True, loop=True, muted=True)

with overview:
	col1, col2 = st.columns((.7, .3))
	# Add a lottie animation
	with col2:
		st_lottie('https://lottie.host/1203acd2-cdce-4e1a-a7a0-44f76fe79481/EgTQj6s698.json')
		
	with col1:
		# Project overview, Objective
		st.markdown(md[md.find('---')+3 : md.find('## Methodology')])
		
	# Expander to show the dataset
	with st.expander('See the dataset', icon=':material/table:'):
		st.dataframe(pd.read_excel('BlinkIt Grocery Sales.xlsx'), hide_index=True)
		st.caption('''_This dataset includes historical sales data across multiple outlets
		    and categories, used to create the dashboard._''')

	# Methodology, Key Takeaways, Conclusion
	st.markdown(md[md.find('## Methodology'):])
		
	# Button to download the workbook
	st.divider()
	st.download_button(
		'Download workbook', wb, file_name='BlinkIt Grocery Sales.xlsx',
		icon=':material/download:')