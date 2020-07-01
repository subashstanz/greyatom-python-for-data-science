# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
new=np.concatenate((data,new_record),axis=0)
age=new[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
zero=data[data[:,2]==0]
race_0=zero[:,2]
one=data[data[:,2]==1]
race_1=one[:,2]
two=data[data[:,2]==2]
race_2=two[:,2]
three=data[data[:,2]==3]
race_3=three[:,2]
four=data[data[:,2]==4]
race_4=four[:,2]
len_1=race_1.itemsize
len_2=race_2.itemsize
len_0=race_0.itemsize
len_3=race_3.itemsize
len_4=race_4.itemsize
#Code starts here
value=np.array([len_0,len_1,len_2,len_3,len_4])
minority_race=np.min(value)
senior_citizens=new[new[:,0]>60]
working_hours=senior_citizens[:,6]
working_hours_sum=np.sum(working_hours)
senior_citizens_len=senior_citizens.itemsize
avg_working_hours=np.mean(working_hours)
high=new[new[:,1]>10]
low=new[new[:,1]<=10]
avg_pay_low=np.mean(low[:,7])
avg_pay_high=np.mean(high[:,7])




