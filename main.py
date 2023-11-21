
import streamlit as st
import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go
import plotly.express as px

st.title("Market Review in 2022  , 51 countries")

st.write("")
# SideBar
# demographics
st.header("1. Demographics Data")


st.sidebar.subheader("Place button for selecting number of countries")
top_num = st.sidebar.radio(
    "What's your favorite movie genre",
    ["10", "15", "20", "All"],
    captions = ["TOP 10", "Top 15", "Top 20", "ALL countries"])
if top_num == "All":
    top_num = "41"
    
    
st.sidebar.subheader("select data from the select box bellow") 
options = {"All ages":"df_general.csv", 
           "Under 18yr":"df_general_18.csv",
           "Between 19 and 44yrs":"df_general_19_44.csv",
           "Over 45yrs": "df_general_45.csv"}


selected_file = st.sidebar.selectbox(
    "Please select data file", 
    list(options.keys())
)

Lens_options_dict = {"SV Lens": "Spectacle SV Lenses(%)", 
                "BFT": "Spectacle BTF Lenses(%)", 
                "PAL":	"Spectacle PAL Lenses(%)",
                "CL": "Contact Lenses(%)",
                "Ready-Mades": "Ready-Mades(%)",
                "Myopia Control": "Myopia Control(%)"
}

Lens_select_option= st.sidebar.selectbox(
    "Please select items for eye correction",
    list(Lens_options_dict.keys()),
   
)


    

Lens_index_dict = {'Mineral':'GLASS', '1.5': '1.5', 'TRIVEX': 'TRIVEX','Mid-Index': '1.56','POLY':'POLY', 'HI16':'1.6','HI167': '1.67','> HI1.67': '> 1.67'}

Lens_index_select_option= st.sidebar.multiselect(
    "Please select items for eye correction",
    list(Lens_index_dict.keys()),
    ['Mineral','1.5']
)


# top_num = st.sidebar.number_input(
#     "Please select number of countries your want to see",
#     min_value=0,
#     max_value=41,
# )



# demographic data
st.write("Your selected data: '{}' ".format(selected_file))

options = {"All ages":"df_general.csv", 
           "Under 18yr":"df_general_18.csv",
           "Between 19 and 44yrs":"df_general_19_44.csv",
           "Over 45yrs": "df_general_45.csv"}

def age_range (selected_file):
    title_name = ""
    if options[selected_file] == "df_general.csv":
        title_name = "in all age groups"
    elif options[selected_file] == "df_general_18.csv":
        title_name = "under 18 yrs"    
    elif options[selected_file] == "df_general_19_44.csv":
        title_name = "between 19 and 44yrs"   
    else:
        title_name = "in over 45 yrs"    
    return title_name        

# 1 Population 
st.subheader("1.1. Tot Population(x10Million) " + age_range(selected_file) )
file_path = "./raw_data/" + options[selected_file]
df_total_p= pd.read_csv(file_path, index_col= 0)
df_total_p_tmp = df_total_p[["Country","Population(x000)"]]

df_total_p_tmp = df_total_p_tmp.sort_values("Population(x000)", ascending=False)
data_total = ([go.Bar(x= df_total_p_tmp.Country[:int(top_num)], y = df_total_p_tmp["Population(x000)"][:int(top_num)]/10000,  name = "" , marker_color='#87cefa', 
               hovertemplate =  '<i>Country</i>: %{x}'+'<br><b>Total</b>: %{y:.1f}千万人<br>') ])

layout = go.Layout(title = "")
fig = go.Figure(data=data_total, layout=layout)
#fig.update_traces(text=df["Population(x000)"])
fig.update_traces(marker_color='greenyellow')
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})

# レイアウトの設定
fig.update_layout(
    title="",
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Total population 総人口(千万人)',titlefont_size=16),
    yaxis_tickfont_size=10
)
st.plotly_chart(fig)


fig = px.pie(df_total_p_tmp[:int(top_num)], values="Population(x000)", names='Country', title="Ratio of each country to the total population" + age_range(selected_file))
st.plotly_chart(fig)





# 2 
st.subheader("1.2. Tot Population with a visual correction(x10 Million) " + age_range(selected_file))
file_path = "./raw_data/" + options[selected_file]
df= pd.read_csv(file_path, index_col= 0)

df_total_cor_tmp = df_total_p[["Country","Tot Population with a visual correction(x000)"]]
#col_list = ["Population(x000)"]#, "Spectacle BTF Lenses.(x000)", "Spectacle PAL Lenses.1(x000)", "Contact Lenses.1(x000)", "Myopia Control.1(x000)"]
df_total_cor_tmp = df_total_cor_tmp.sort_values("Tot Population with a visual correction(x000)", ascending=False)
data = ([go.Bar(x= df_total_cor_tmp.Country[:int(top_num)], y = df_total_cor_tmp["Tot Population with a visual correction(x000)"][:int(top_num)]/10000,  name = "", marker_color='#87cefa', 
               hovertemplate =  '<i>Country</i>: %{x}'+'<br><b>Total</b>: %{y:.1f}千万人<br>') ])


layout = go.Layout(title = "")

fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Tot Population with a visual correction(x000)"])
fig.update_traces(marker_color='lime')
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})

# レイアウトの設定
fig.update_layout(
    title='Total number of vision correction users 視力補正装用者数(千万人) ' + age_range(selected_file),
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Total number of wearers 使装用者数(千万人)',titlefont_size=16),
    yaxis_tickfont_size=10
)
st.plotly_chart(fig)


fig = px.pie(df_total_cor_tmp[:int(top_num)], values="Tot Population with a visual correction(x000)", names='Country', title='World wide (51 countries ) Tot Population with a visual correction(x Million) ' + age_range(selected_file))
st.plotly_chart(fig)


#3 Lens type
st.write("")
st.write("")
st.subheader('2. Percentage of Users of ' + Lens_select_option + ' in Corrected Population ' +  age_range(selected_file) + '(%) Duplicates' )
st.write('レンズタイプ：: ' + Lens_select_option )
st.write('使用者グループ: ' +  age_range(selected_file))

def lens_design(Lens_select_option):

    if Lens_select_option== "SV Lens":
        lens_d = "Spectacle SV Lenses(%)"
    elif Lens_select_option== "BFT":
        lens_d = "Spectacle BTF Lenses(%)"
    elif Lens_select_option== "PAL":
        lens_d = "Spectacle PAL Lenses(%)"
    elif Lens_select_option== "CL":
        lens_d = "Contact Lenses(%)"
    elif Lens_select_option== "Ready-Mades":
        lens_d = "Ready-Mades(%)"
    else: 
        lens_d =  "Myopia Control(%)"
    return lens_d    



color_list =  [ "green", "rosybrown", "royalblue", "hotpink", "orange","aqua", "indianred","greenyellow", "forestgreen", "limegreen", "lightgreen",  "darkgreen", "palegreen", "rosybrown", "royalblue", "hotpink", "indianred", "lemonchiffon"]


file_path = "./raw_data/" + options[selected_file]
df= pd.read_csv(file_path, index_col= 0)
#lens_list = ["Country","Spectacle SV Lenses(%)", "Spectacle BTF Lenses(%)", "Spectacle PAL Lenses(%)", "Contact Lenses(%)","Ready-Mades(%)", "Myopia Control(%)"]

lens_list = ["Country"]
select= lens_design(Lens_select_option)
lens_list.append(select)
df_lens= df[lens_list]
df_lens = df_lens.sort_values(select, ascending=False)


data = ([go.Bar(x= df_lens.Country[:int(top_num)], y = df_lens[select][:int(top_num)] ,name="", marker=dict(color ="lightgreen" ))  ])

layout = go.Layout(title = "", barmode='stack')
fig = go.Figure(data=data, layout=layout)
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='Percentage of Users of ' + Lens_select_option + ' in Corrected Population' +  age_range(selected_file) + '(%) Duplicates.（％)'+ age_range(selected_file) ,
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Percentage of Users （%）',titlefont_size=16),
    yaxis_tickfont_size=10
)
st.plotly_chart(fig)




st.subheader("3.Lens Materials by country")
st.write("3. 国別、レンズ素材について")

df = pd.read_csv('./raw_data/df_lensMarket_volume_By_material.csv', index_col =0)
df_copy= df.copy()
Lens_index_select_list = ["Country"]
for i in Lens_index_select_option:
    Lens_index_select_list.append(Lens_index_dict[i])
    
df_mate= df_copy[Lens_index_select_list ]
cols= df_mate.shape[1]
if cols <= 1:
    pass
elif cols == 2:
    df_mate['subtotal'] = df_mate.iloc[:,1]
    df_mate = df_mate.sort_values('subtotal', ascending=False)
else:    
    df_mate['subtotal'] = df_mate.iloc[:,2:cols].sum(axis=1)
    df_mate = df_mate.sort_values('subtotal', ascending=False)
    
Lens_index_select_list.remove("Country")

data = ([go.Bar(x= df_mate.Country[:int(top_num)], y = df_mate[response][:int(top_num)]/1000 ,name=response, marker=dict(color = color_list[co]))  for co, response in enumerate(Lens_index_select_list)])


layout = go.Layout(title = "国別レンズ素材シェア（百万枚）",barmode='stack')
fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Myopia Control.1(x000)"])
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='Lens Material share by country (Million piece)国別レンズ素材シェア（百万枚)',
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Number of lens (Million pieces)レンズ素材（百万枚）',titlefont_size=16),
    yaxis_tickfont_size=10
)
st.plotly_chart(fig)


st.subheader("")
series_mate= df_mate.sum()
if series_mate.shape[0] >2:
    tmp= df_mate.sum()
    df_mate2 = pd.DataFrame(tmp[1:-1])
    df_mate2.reset_index(inplace=True)
    df_mate2.rename(columns={'index':'Material', 0:"Volume"}, inplace=True)
    df_meta3 = df_mate2
    # df_meta3 = df_meta3.iloc[:, 1:].astype('int32')
    st.write("Table: Volumes of materials")
    st.dataframe(df_meta3)
    fig = px.pie(df_mate2, values='Volume', names='Material', title="Percentage of shares by selected materials(%) " )
    st.plotly_chart(fig)



# 5 Maker 
st.subheader("4. Lens Makers' shares by country")
st.write("4. レンズメーカーについて")
source_h_vol= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_e_vol= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_c_vol= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_h_vol_share= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_e_vol_share= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_c_vol_share= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
cname = ['ES group', 'HOYA', 'CZ', 'Others']
source_total_vol= pd.read_csv('./raw_data/df_lensMarket_volume_By_design.csv', usecols=['Country','SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1', 'TOT LENS.1'])
source_total_vol['SV_oth'] = source_total_vol['SV.1'] - source_h_vol['SV(000)'] - source_e_vol['SV(000)'] - source_c_vol['SV(000)']
source_total_vol['PAL_oth'] = source_total_vol['PAL.1'] - source_h_vol['PAL(000)'] - source_e_vol['PAL(000)'] - source_c_vol['PAL(000)']
source_total_vol['MC_oth'] = source_total_vol['Myopia Control.1'] - source_h_vol['Myopia Control(000)'] - source_e_vol['Myopia Control(000)'] - source_c_vol['Myopia Control(000)']


col_list = ['SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1']
data = ([go.Bar(x= source_h_vol.Country, y = source_h_vol['SV(000)']/1000 ,name="HOYA"),
         go.Bar(x= source_e_vol.Country, y = source_e_vol['SV(000)']/1000 ,name="ES group"),
        go.Bar(x= source_c_vol.Country, y = source_c_vol['SV(000)']/1000 ,name="CZ group"),
        go.Bar(x= source_total_vol.Country, y = source_total_vol['SV_oth']/1000 ,name="Others"),        
        ])


layout = go.Layout(title = "SV lens market share (M pieces) 単焦点レンズ・メーカー別シェア（百万枚）",barmode='stack')
fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Myopia Control.1(x000)"])
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='"SV lens market share (M pieces)単焦点レンズ・メーカー別シェア（百万枚)',
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='"Lens volume (M pieces) 単焦点レンズ（百万枚）',titlefont_size=16),
    yaxis_tickfont_size=10
)
st.plotly_chart(fig)


source_h_vol= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_e_vol= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_c_vol= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_h_vol_share= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_e_vol_share= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_c_vol_share= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
cname = ['ES group', 'HOYA', 'CZ', 'Others']
source_total_vol= pd.read_csv('./raw_data/df_lensMarket_volume_By_design.csv', usecols=['Country','SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1', 'TOT LENS.1'])
source_total_vol['SV_oth'] = source_total_vol['SV.1'] - source_h_vol['SV(000)'] - source_e_vol['SV(000)'] - source_c_vol['SV(000)']
source_total_vol['PAL_oth'] = source_total_vol['PAL.1'] - source_h_vol['PAL(000)'] - source_e_vol['PAL(000)'] - source_c_vol['PAL(000)']
source_total_vol['MC_oth'] = source_total_vol['Myopia Control.1'] - source_h_vol['Myopia Control(000)'] - source_e_vol['Myopia Control(000)'] - source_c_vol['Myopia Control(000)']


col_list = ['SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1']
data = ([go.Bar(x= source_h_vol.Country, y = source_h_vol['PAL(000)']/1000 ,name="HOYA"),
         go.Bar(x= source_e_vol.Country, y = source_e_vol['PAL(000)']/1000 ,name="ES group"),
        go.Bar(x= source_c_vol.Country, y = source_c_vol['PAL(000)']/1000 ,name="CZ group"),
        go.Bar(x= source_total_vol.Country, y = source_total_vol['PAL_oth']/1000 ,name="Others"),        
        ])


layout = go.Layout(title = "PAL lens market share (M pieces) 累進レンズ・メーカー別シェア（百万枚）",barmode='stack')
fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Myopia Control.1(x000)"])
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='PAL lens market share (M pieces) 累進レンズ・メーカー別シェア（百万枚）',
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Lens volume (M pieces) 累進レンズ（百万枚）',titlefont_size=16),
    yaxis_tickfont_size=10
)
st.plotly_chart(fig)

source_h_vol= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_e_vol= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_c_vol= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_h_vol_share= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_e_vol_share= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_c_vol_share= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
cname = ['ES group', 'HOYA', 'CZ', 'Others']
source_total_vol= pd.read_csv('./raw_data/df_lensMarket_volume_By_design.csv', usecols=['Country','SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1', 'TOT LENS.1'])
source_total_vol['SV_oth'] = source_total_vol['SV.1'] - source_h_vol['SV(000)'] - source_e_vol['SV(000)'] - source_c_vol['SV(000)']
source_total_vol['PAL_oth'] = source_total_vol['PAL.1'] - source_h_vol['PAL(000)'] - source_e_vol['PAL(000)'] - source_c_vol['PAL(000)']
source_total_vol['MC_oth'] = source_total_vol['Myopia Control.1'] - source_h_vol['Myopia Control(000)'] - source_e_vol['Myopia Control(000)'] - source_c_vol['Myopia Control(000)']


col_list = ['SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1']
data = ([go.Bar(x= source_h_vol.Country, y = source_h_vol['Myopia Control(000)']/1000 ,name="HOYA"),
         go.Bar(x= source_e_vol.Country, y = source_e_vol['Myopia Control(000)']/1000 ,name="ES group"),
        go.Bar(x= source_c_vol.Country, y = source_c_vol['Myopia Control(000)']/1000 ,name="CZ group"),
        go.Bar(x= source_total_vol.Country, y = source_total_vol['MC_oth']/1000 ,name="Others"),        
        ])


layout = go.Layout(title = "MC lens market share (M pieces)近視抑制レンズ・メーカー別シェア（百万枚）",barmode='stack')
fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Myopia Control.1(x000)"])
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='MC lens market share (M pieces)近視抑制レンズ・メーカー別シェア（百万枚）',
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Lens Volume(M pieces)  近視抑制レンズ（百万枚）',titlefont_size=16),
    yaxis_tickfont_size=10
)

st.plotly_chart(fig)

source_h_vol= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_e_vol= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_c_vol= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_h_vol_share= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_e_vol_share= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_c_vol_share= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
cname = ['ES group', 'HOYA', 'CZ', 'Others']
source_total_vol= pd.read_csv('./raw_data/df_lensMarket_volume_By_design.csv', usecols=['Country','SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1', 'TOT LENS.1'])
source_total_vol['SV_oth'] = source_total_vol['SV.1'] - source_h_vol['SV(000)'] - source_e_vol['SV(000)'] - source_c_vol['SV(000)']
source_total_vol['PAL_oth'] = source_total_vol['PAL.1'] - source_h_vol['PAL(000)'] - source_e_vol['PAL(000)'] - source_c_vol['PAL(000)']
source_total_vol['MC_oth'] = source_total_vol['Myopia Control.1'] - source_h_vol['Myopia Control(000)'] - source_e_vol['Myopia Control(000)'] - source_c_vol['Myopia Control(000)']


col_list = ['SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1']
data = ([go.Bar(x= source_h_vol.Country, y = source_h_vol['TOTAL(000)']/1000 ,name="HOYA"),
         go.Bar(x= source_e_vol.Country, y = source_e_vol['TOTAL(000)']/1000 ,name="ES group"),
        go.Bar(x= source_c_vol.Country, y = source_c_vol['TOTAL(000)']/1000 ,name="CZ group"),
        go.Bar(x= source_total_vol.Country, y = source_total_vol['TOT LENS.1']/1000 - source_h_vol['TOTAL(000)']/1000 - source_e_vol['TOTAL(000)']/1000 -  source_c_vol['TOTAL(000)']/1000,name="Others"),        
        ])


layout = go.Layout(title = "TOTAL Lens market share by maker (M pieces) レンズ・メーカー別シェア（百万枚）",barmode='stack')
fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Myopia Control.1(x000)"])
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='TOTAL Lens market share by maker (M pieces) レンズ・メーカー別シェア（百万枚）',
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Lens volume (M pieces) TOTAL レンズ（百万枚）',titlefont_size=16),
    yaxis_tickfont_size=10
)

st.plotly_chart(fig)

from plotly.subplots import make_subplots

source_h_vol= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_e_vol= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_c_vol= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(000)', 'BTF(000)', 'PAL(000)', 'Myopia Control(000)','TOTAL(000)','Code'])
source_h_vol_share= pd.read_csv('./raw_data/df_lensCompe_HOYA_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_e_vol_share= pd.read_csv('./raw_data/df_lensCompe_Ess_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
source_c_vol_share= pd.read_csv('./raw_data/df_lensCompe_cz_vol.csv', usecols=['Country','SV(%)', 'BTF(%)', 'PAL(%)', 'Myopia Control(%)','TOTAL(%)','Code'])
cname = ['ES group', 'HOYA', 'CZ', 'Others']
source_total_vol= pd.read_csv('./raw_data/df_lensMarket_volume_By_design.csv', usecols=['Country','SV.1', 'BTF.1', 'PAL.1', 'Myopia Control.1', 'TOT LENS.1'])
source_total_vol['SV_oth'] = source_total_vol['SV.1'] - source_h_vol['SV(000)'] - source_e_vol['SV(000)'] - source_c_vol['SV(000)']
source_total_vol['PAL_oth'] = source_total_vol['PAL.1'] - source_h_vol['PAL(000)'] - source_e_vol['PAL(000)'] - source_c_vol['PAL(000)']
source_total_vol['MC_oth'] = source_total_vol['Myopia Control.1'] - source_h_vol['Myopia Control(000)'] - source_e_vol['Myopia Control(000)'] - source_c_vol['Myopia Control(000)']

SV_h= source_h_vol['SV(000)'].sum()
SV_e= source_e_vol['SV(000)'].sum()
SV_c= source_c_vol['SV(000)'].sum()
source_total_vol['SV(000)'] = source_total_vol['SV_oth']
SV_oth= source_total_vol['SV(000)'].sum()
SV_values= [SV_e,SV_h,SV_c, SV_oth]

PAL_h= source_h_vol['PAL(000)'].sum()
PAL_e= source_e_vol['PAL(000)'].sum()
PAL_c= source_c_vol['PAL(000)'].sum()
source_total_vol['PAL(000)'] = source_total_vol['PAL_oth']
PAL_oth= source_total_vol['PAL(000)'].sum()
PAL_values= [PAL_e,PAL_h,PAL_c, PAL_oth]

MC_h= source_h_vol['Myopia Control(000)'].sum()
MC_e= source_e_vol['Myopia Control(000)'].sum()
MC_c= source_c_vol['Myopia Control(000)'].sum()
source_total_vol['Myopia Control(000)'] = source_total_vol['MC_oth']
MC_oth= source_total_vol['Myopia Control(000)'].sum()
MC_values= [MC_e,MC_h,MC_c, MC_oth]


total_h= source_h_vol['TOTAL(000)'].sum()
total_e= source_e_vol['TOTAL(000)'].sum()
total_c= source_c_vol['TOTAL(000)'].sum()
source_total_vol['TOTAL(000)'] = source_total_vol['SV_oth']+ source_total_vol['PAL_oth']+ source_total_vol['MC_oth']
total_oth= source_total_vol['TOTAL(000)'].sum()
total_values= [total_e,total_h,total_c, total_oth]
labels=['Essilor group', 'HOYA', 'CZ', 'Others']

# Create subplots: use 'domain' type for Pie subplot
specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]]
fig = make_subplots(rows=2, cols=2, specs =specs)
fig.add_trace(go.Pie(labels=labels, values= total_values, name="Totallensmarket"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values= SV_values, name="SVlensmarket"),
              1, 2)
fig.add_trace(go.Pie(labels=labels, values= PAL_values, name="PAL lensmarket"),
              2, 1)
fig.add_trace(go.Pie(labels=labels, values= MC_values, name="MC lensmarket"),
              2, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="Global Lens Market share in 2022",
    # Add annotations in the center of the donut pies.
    annotations=[
                  dict(text='TOTAL', x=0.20, y=0.82, font_size=16, showarrow=False),
                  dict(text='SV  ', x=0.80, y=0.82, font_size=16, showarrow=False),
                  dict(text='PAL  ', x=0.20, y=0.18, font_size=16, showarrow=False),
                  dict(text='MC  ', x=0.80, y=0.18, font_size=16, showarrow=False),
                ])

st.plotly_chart(fig)

st.subheader("5.Blue Light Cut by country")
st.write("5. 国別、ブルーライトカットについて")

source_coat_p= pd.read_csv('./raw_data/df_lensMarket_volume_protection.csv',usecols=["Country", "HMC_UV_Coating", "HMC_OTHER_Coating", "HMC_Blue_cut_by_Coating", "Blue_cut_by_Material_only", "Blue_cut_by_Coating_plus_Material", "Total_blue_cut"])

source_blue_p= pd.read_csv('./raw_data/df_lensMarket_volume_protection.csv',usecols=["Country", "HMC_UV_Coating", "HMC_OTHER_Coating", "HMC_Blue_cut_by_Coating", "Blue_cut_by_Material_only", "Blue_cut_by_Coating_plus_Material", "Total_blue_cut"])
blue_list = ["HMC_UV_Coating", "HMC_OTHER_Coating", "HMC_Blue_cut_by_Coating", "Blue_cut_by_Material_only", "Blue_cut_by_Coating_plus_Material"]


data = ([go.Bar(x= source_coat_p.Country, y = source_coat_p[coat]/1000 ,name=coat) for coat in blue_list] )
      



layout = go.Layout(title = "TOTAL Blue light cut share by country（％）",barmode='stack')
fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Myopia Control.1(x000)"])
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='TOTAL Blue light cut share by country（％）',
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='TOTAL Blue light cut share by country（％）',titlefont_size=16),
    yaxis_tickfont_size=10
)
st.plotly_chart(fig)

st.subheader("6.Vision Defect by country")
st.write("6. 国別、近視、老眼等の比率について")


source_defect_p= pd.read_csv('./raw_data/df_general_visionDefect.csv', usecols=["Country","Myopia_per", "Hyperopia_per","Astigmatism_per","Presbyopia_per","Myopia(x000)","Hyperopia(x000)","Astigmatism(x000)", "Presbyopia(x000)"])
col_list = ["Myopia_per", "Hyperopia_per","Astigmatism_per","Presbyopia_per"]
col_list_2= ["Myopia(x000)","Hyperopia(x000)","Astigmatism(x000)", "Presbyopia(x000)"]

data = ([go.Bar(x= source_defect_p.Country, y = source_defect_p[coat] ,name=coat) for coat in col_list] )
      



layout = go.Layout(title = "Percentage of Vision Defect by country（％）",barmode='stack')
fig = go.Figure(data=data, layout=layout)
#fig.update_traces(text=df["Myopia Control.1(x000)"])
#fig.update_traces(hovertext=["%d千万枚:%s" % (l, w) for l, w in zip(df["Spectacle SV Lenses(x000)"]/10000, df["Country"])])
#fig.update_traces(marker_color='#4F81BD') # marker_line_color='white',marker_line_width=1.5, opacity=0.6
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.update_layout(hovermode='x unified')
# レイアウトの設定
fig.update_layout(
    title='Percentage of Vision Defect by country（％）',
    xaxis=dict(title='Country',titlefont_size=16),
    xaxis_tickfont_size=10,
    yaxis=dict(title='Vision Defect by country（％）',titlefont_size=16),
    yaxis_tickfont_size=10
)


st.plotly_chart(fig)

st.subheader("7. Average wholesale price of lens by class (High-Mid-Low) USD/p")
st.write("7. レンズの卸売価格（メーカーから小売店）")

st.write("")
st.write("7.1. Average wholesale price of SV by class(High-Mid-Low) USD/p")
file_path_price = "./raw_data/" + "df_lensPrice_85.csv"
df_total_price= pd.read_csv(file_path_price) #, usecols= ["Country","Spectacle SV Lenses(%)"],index_col= 0)


fig = go.Figure(
    data=[go.Candlestick(x=df_total_price['Country'], open=df_total_price['SV_price_Mid'], high=df_total_price['SV_price_High'], low=df_total_price['SV_price_Low'], close=df_total_price['SV_price_Mid'], showlegend=False)]
)
# Layout
fig.update_layout(
    title={
        "text": "SVL wholesale price (High-Mid-Low)",
        "y":0.9,
        "x":0.5,
    },
    yaxis_title='Price(USD/piece)',
    xaxis_title="Country",
)

# fig.update_yaxes(separatethousands=True)
# fig.update(layout_xaxis_rangeslider_visible=False) #追加
st.plotly_chart(fig)

st.write("7.2. Average wholesale price of PAL by class(High-Mid-Low) USD/p")
file_path_price = "./raw_data/" + "df_lensPrice_85.csv"
df_total_price= pd.read_csv(file_path_price) #, usecols= ["Country","Spectacle SV Lenses(%)"],index_col= 0)


fig = go.Figure(
    data=[go.Candlestick(x=df_total_price['Country'], open=df_total_price['PAL_price_Mid'], high=df_total_price['PAL_price_High'], low=df_total_price['PAL_price_Low'], close=df_total_price['PAL_price_Mid'], showlegend=False)]
)
# Layout
fig.update_layout(
    title={
        "text": "PAL wholesale price (High-Mid-Low)",
        "y":0.9,
        "x":0.5,
    },
    yaxis_title='Price(USD/piece)',
    xaxis_title="Country",
)

# fig.update_yaxes(separatethousands=True)
# fig.update(layout_xaxis_rangeslider_visible=False) #追加
st.plotly_chart(fig)


# Analysis 
# GDP & Popuration MAP 
st.subheader("8. Gross Domestic Product per capita x 000 USD/p Source: IMF 2023")
df_p= pd.read_csv("./raw_data/df_general.csv", index_col= 0)
df_gdp= pd.read_csv("./raw_data/df_GDP.csv", index_col= 0)
df_gdp["GDP_per_cap"] =df_gdp['GDP(USD)']/df_p["Population(x000)"]
fig = px.choropleth(
    df_gdp,
    locations = "Code",
    color = "GDP_per_cap",
    #colorscale="Viridis",
    height = 800,
    width= 800
)
st.plotly_chart(fig)

st.subheader("9. GDP per capita vs. PAL penetration ratio in World wide market")
st.write("A circle size represents the PAL market size")
file_path = "./raw_data/" + "df_general_45.csv"
df_total_p= pd.read_csv(file_path, usecols= ["Country","Population(x000)","Spectacle PAL Lenses(%)","Spectacle PAL Lenses.1(x000)"],index_col= 0)


df_p= pd.read_csv("./raw_data/df_general.csv", usecols =["Country","Population(x000)"],index_col= 0)
df_gdp= pd.read_csv("./raw_data/df_GDP.csv", usecols = ["Country",'GDP(USD)'],index_col= 0 )
df_gdp["GDP_per_cap"] =df_gdp.loc[:,"GDP(USD)" ]/df_p.loc[:,"Population(x000)"]

df_defect_p= pd.read_csv('./raw_data/df_general_visionDefect.csv', usecols = ["Country","Presbyopia(x000)"],index_col= 0)
df_tmp = pd.merge(df_gdp, df_defect_p, left_index=True, right_index=True)
df_tmp = pd.merge(df_tmp, df_total_p, left_index=True, right_index=True)
df_tmp.reset_index(inplace=True)
fig = px.scatter(
    df_tmp,
    x="GDP_per_cap",
    y="Spectacle PAL Lenses(%)",
    size="Spectacle PAL Lenses.1(x000)",
    color="Spectacle PAL Lenses.1(x000)",
    hover_name="Country",
    height=600,
    width=600,
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
# st.plotly_chart(fig)

st.sidebar.button("Reset", type="primary")

if st.button('御礼'):
    st.subheader( ':green[前回の不手際で、この度は皆さまのお時間を頂き有難うございました。]')
    st.subheader( ':green[Thank you all for your time due to the previous mishap.]')
    
    st.balloons()
else:
    pass 
    
