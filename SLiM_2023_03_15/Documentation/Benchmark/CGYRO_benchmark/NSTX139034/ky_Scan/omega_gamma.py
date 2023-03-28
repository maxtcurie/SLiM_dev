import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('output.csv')
df_SLiM=pd.read_csv('SLiM.csv')
df_SLiM=df_SLiM[df_SLiM.gamma_cs_a>0]

fontsize0=12

f_ky=56.6767124406508/0.139321461
doppler_ky=(77.07228226-70.79222032)/0.139321461


fig, ax=plt.subplots(nrows=2,ncols=1,sharex=True) 
df['n']=df['ky']/0.034282055

convert_dict={}
convert_dict['n']='int'

df=df.astype(convert_dict)

df=df[df.n%2==0]
df_itg=df[df.modetype=='itg']
df_mtm=df[df.modetype=='mtm']
df_tem=df[df.modetype=='etg']
df_kbm=df[df.modetype=='mystery']


df_stable=df[df['modetype'].str.contains('_stable', case=False, na=False)]



ax[0].scatter(df_SLiM['ky'],df_SLiM['gamma_cs_a'],label='SLiM')
ax[0].scatter(df_mtm['ky'],df_mtm['growth_rate'],label='CGYRO')
#ax[0].scatter(df_tem['ky'],df_tem['growth_rate'],label='TEM',color='blue')
#ax[0].scatter(df_kbm['ky'],df_kbm['growth_rate'],color='blue')

#ax[0].scatter(df_stable['ky'],[0]*len(df_stable),label='stable',color='black')

ax[1].scatter(df_SLiM['ky'],df_SLiM['omega_lab_kHz'])
ax[1].scatter(df_mtm['ky'],\
				abs(df_mtm['realfreq_over_omegastar']*\
					df_mtm['ky']*f_ky\
					-df_mtm['ky']*doppler_ky))

ax[0].set_ylabel(r'$\gamma (c_s/a)$',fontsize=fontsize0)
ax[1].set_ylabel(r'$frequency (kHz)$',fontsize=fontsize0)
ax[1].set_xlabel(r'$k_y\rho_s$',fontsize=fontsize0)
ax[0].legend()
ax[0].grid(alpha=0.3)
ax[1].grid(alpha=0.3)
plt.tight_layout()
plt.show()