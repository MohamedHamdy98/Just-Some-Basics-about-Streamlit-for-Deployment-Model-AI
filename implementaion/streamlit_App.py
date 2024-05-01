from streamlit_process import webApp

web = webApp()
df_selected_year_sorted = web.create_sidebar(web.df)
web.show_visualization(df_selected_year_sorted)
