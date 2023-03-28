import numpy as np
import matplotlib.pyplot as plt 
from tqdm import tqdm
import sys as sys
import pandas as pd
sys.path.insert(1, './../..')

from Dispersion_NN import Dispersion_NN

#************Start of of user block******************
output_csv_file='./Fig2_cd_NN.csv'

read_csv=False	#change to True if one want to read the data from csv file,\
				# instead of calculating from SLiM_NN
read_output_csv_file='./Fig2_cd_NN.csv'

fontsize=12

nu=1.
zeff=1.
eta=2.
shat=0.012
beta=0.002
ky=0.000
mu=0.
xstar=10

mu_list=np.arange(0,6,0.1)

path='./../../Trained_model/'
NN_omega_file	   =path+'SLiM_NN_omega.h5'
NN_gamma_file	   =path+'SLiM_NN_stabel_unstable.h5'
norm_omega_csv_file=path+'NN_omega_norm_factor.csv'
norm_gamma_csv_file=path+'NN_stabel_unstable_norm_factor.csv'

#************End of user block******************

para_list=[[nu, zeff, eta, shat,  beta,  ky,   mu, xstar]\
			for mu in mu_list]

Dispersion_NN_obj=Dispersion_NN(NN_omega_file,NN_gamma_file,norm_omega_csv_file,norm_gamma_csv_file)

f_list=[]
gamma_list=[]
gamma_10_list=[]

if read_csv==True:
	data=pd.read_csv(read_output_csv_file)  	#data is a dataframe. 
	
	mu_list=data['mu']
	f_list=data['f']
	gamma_list=data['gamma']
	gamma_10_list=data['gamma_10']

else:
	nu_output_list=[]
	zeff_output_list=[]
	eta_output_list=[]
	shat_output_list=[]
	beta_output_list=[]
	ky_output_list=[]
	mu_output_list=[]
	xstar_output_list=[]
	
	for para in tqdm(para_list):
		[nu, zeff, eta, shat,  beta,  ky,   mu, xstar]=para
		nu_output_list.append(nu)
		zeff_output_list.append(zeff)
		eta_output_list.append(eta)
		shat_output_list.append(shat)
		beta_output_list.append(beta)
		ky_output_list.append(ky)
		mu_output_list.append(mu)
		xstar_output_list.append(xstar)
	
		w=Dispersion_NN_obj.Dispersion_omega(nu,zeff,eta,shat,beta,ky,mu,xstar)
		f_list.append(w.real)
		gamma_list.append(w.imag)
		if w.imag>0.00001:
			gamma_10_list.append(1)
		else:
			gamma_10_list.append(0)
	
	
	d = {'nu':nu_output_list, \
		'zeff':zeff_output_list,\
		'eta':eta_output_list,\
		'shat':shat_output_list,\
		'beta':beta_output_list, \
		'ky':ky_output_list,  \
		'mu':mu_output_list, \
		'xstar':xstar_output_list,\
		'f':f_list,'gamma':gamma_list,'gamma_10':gamma_10_list}
	df=pd.DataFrame(d)	#construct the panda dataframe
	df.to_csv(output_csv_file,index=False)

f_list=np.array(f_list)
gamma_list=np.array(gamma_list)
gamma_10_list=np.array(gamma_10_list)

if 2==2:
	mu = [0., 0.2, 0.4000000000000001, 0.6000000000000001, 0.8, \
        	1.0000000000000002, 1.2000000000000002, 1.4000000000000001, 1.6, \
        	1.8, 2., 2.2, 2.4, 2.6, 2.8, 3., 3.2, 3.4, 3.6, 3.8, 4., \
        	4.2, 4.4, 4.6000000000000005, 4.8, 5., 5.2, 5.4, \
        	5.6000000000000005, 5.8, 6.]

	omega_GL=[3.2533927970956658 + 0.1358485645238026j, \
	        3.252375836953931 + 0.1353270349336096j, \
	        3.249325865942241 + 0.13376431316026058j, \
	        3.244245611813753 + 0.13116598583199576j, \
	        3.2371396184238184 + 0.12754131663920407j, \
	        3.2280142394448488 + 0.12290317724100468j, \
	        3.2168776243266612 + 0.11726795473596333j, \
	        3.203739691612367 + 0.11065544066250796j, \
	        3.188612083922529 + 0.10308870900615145j, \
	        3.1715080988027653 + 0.09459399402405119j, \
	        3.152442590555741 + 0.08520058301111909j, \
	        3.131431840755448 + 0.07494074450792336j, \
	        3.1084934001416547 + 0.06384971889540975j, \
	        3.083645913158974 + 0.05196580560495304j, \
	        3.056908950026006 + 0.0393305886709109j, \
	        3.0283028919113293 + 0.025989348940074656j, \
	        2.99784894517671 + 0.011991714517273077j, \
	        2.965569403920876 - 0.0026074030895052737j, \
	        2.9314883397713256 - 0.017746558625004443j, \
	        2.895632976568785 - 0.03335622643770265j, \
	        2.858036103675831 - 0.04935707015506529j, \
	        2.818739981651133 - 0.06565831580940956j, \
	        2.777802257817854 - 0.08215681068713111j, \
	        2.7353043461036655 - 0.09873780004739353j, \
	        2.6913623698256406 - 0.11527903649278244j, \
	        2.6461398923390913 - 0.13166036687045118j, \
	        2.59986013121379 - 0.14778092405620769j, \
	        2.552813511521986 - 0.1635846591729228j, \
	        2.505355607155056 - 0.17909151815266805j, \
	        2.45789295249667 - 0.19442682318536933j, \
	        2.4108610434625235 - 0.20983837072073913j]
	
	
	
	omega_LL=[3.3293919175714777 + 0.09621674541054291j, \
	  3.3282101680760814 + 0.09621977414934132j, \
	  3.32466749162681 + 0.09622862230676332j, \
	  3.3187715942542897 + 0.09624257770106019j, \
	  3.310535285809938 + 0.09626046000143777j, \
	  3.2999764298742065 + 0.09628063063762661j, \
	  3.2871178740449745 + 0.09630100656858068j, \
	  3.2719873610203303 + 0.09631907782089176j, \
	  3.2546174209990077 + 0.09633192865779006j, \
	  3.23504524603341 + 0.09633626223868538j, \
	  3.2133125470695725 + 0.09632842857971995j, \
	  3.189465394512058 + 0.09630445561962443j, \
	  3.1635540432360933 + 0.09626008316260033j, \
	  3.1356327430538813 + 0.09619079945040131j, \
	  3.105759535726556 + 0.09609188010003678j, \
	  3.073996039666665 + 0.09595842911853486j, \
	  3.0404072235483954 + 0.09578542169570047j, \
	  3.0050611700828385 + 0.09556774845927969j, \
	  2.9680288312627194 + 0.09530026086720578j, \
	  2.9293837764052824 + 0.09497781739842924j, \
	  2.8892019343500976 + 0.09459533019704898j, \
	  2.847561331170988 + 0.09414781182477255j, \
	  2.8045418247699603 + 0.09363042176793608j, \
	  2.7602248377054472 + 0.0930385123457332j, \
	  2.714693089596834 + 0.09236767367554878j, \
	  2.668030330409244 + 0.09161377735014099j, \
	  2.620321075895488 + 0.09077301849166847j, \
	  2.5716503464222504 + 0.0898419558611907j, \
	  2.5221034103565225 + 0.0888175497164256j, \
	  2.4717655331277197 + 0.08769719712429805j, \
	  2.420721733014601 + 0.08647876446024459j]
	
	
	print(len(mu))
	print(len(omega_GL))
	print(len(omega_LL))
	
	f_GL    =np.real(omega_GL)
	gamma_GL=np.imag(omega_GL)
	
	f_LL    =np.real(omega_LL)
	gamma_LL=np.imag(omega_LL)



plt.clf()
plt.plot(mu,gamma_GL/(1.+eta),label='SLiM')
#plt.plot(mu_list,gamma_list/max(gamma_list),label='SLiM_NN')
plt.plot(mu_list,gamma_10_list*np.max(gamma_GL/(1.+eta)),label='SLiM_NN')
plt.xlabel(r'$\mu$',fontsize=fontsize)
plt.ylabel(r'$\gamma/\omega_{*peak}$',fontsize=fontsize)
plt.axhline(0,color='black',alpha=0.5)
plt.grid(alpha=0.2)
plt.legend()
plt.show()

plt.clf()
plt.plot(mu,f_GL/(1.+eta),label='SLiM')
plt.plot(mu_list,f_list/(1.+eta),label='SLiM_NN')
plt.xlabel(r'$\mu$',fontsize=fontsize)
plt.ylabel(r'$\omega/\omega_{*peak}$',fontsize=fontsize)
plt.ylim(0,2)
plt.grid(alpha=0.2)
plt.legend()
plt.show()

