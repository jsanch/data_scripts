import pandas as pd
import numpy as np 
import csv 
filename = "years11-15.csv"

for i in range(1):
  # year_str = str(201x4+i)
  f = open(filename)
  # Gets the number of lines in the file. 
  num_lines = sum(1 for line in f)
  # Desired number of lines for the sample
  random_sample_size = 10000 

  lines2skip = (np.random.choice(np.arange(1,num_lines+1),
                                 (num_lines - random_sample_size), replace=False))



  df = pd.read_csv(filename, skiprows=lines2skip) # skipp lines. 
  # df = pd.read_csv(filename) # BOOOM

  # df = pd.read_csv("years11-15.csv")
  pd.set_option('display.max_columns', None)
  

  dropList = ['lca_case_number','lca_case_submit', 'decision_date', 'visa_class', 'lca_case_employment_start_date', 'lca_case_employment_end_date', 'lca_case_employer_address',  'lca_case_employer_postal_code', 'lca_case_soc_code',  'lca_case_wage_rate_to', 'full_time_pos', 'total_workers', 'pw_source_1', 'other_wage_source_1', 'yr_source_pub_1', 'lca_case_workloc2_city', 'lca_case_workloc2_state', 'pw_2', 'pw_unit_2', 'pw_source_2', 'other_wage_source_2', 'yr_source_pub_2', 'lca_case_naics_code', 'serialid']

  df.drop(dropList,inplace=True,axis=1)


#filtering 
  # df = df[df.lca_case_wage_rate_unit == 'Year']


  # print df.lca_case_wage_rate_unit.nunique()

  # def calculateWage(x):
  #   if x == 'Hour':
  #     return 2087
  #   elif x == 'Month':
  #     return 2087/12
  #   elif x == 'Week':
  #     return 2087/52
  #   elif x == 'Bi-Weekly':
  #     return 2087/26
  #   else:
  #     return 1


  # df['wage'] = df['lca_case_wage_rate_from'] * df.lca_case_wage_rate_unit.map(calculateWage)

  # def correct(x):
  #   if x > 10000000:
  #     return 60000
  #   else:
  #     x
  #     
  
  
  # # correct. 
  # df['wage'] =  df['lca_case_wage_rate_from']

  # df.drop(['lca_case_wage_rate_from','lca_case_wage_rate_unit'],inplace=True,axis=1)

  # # df['prevailing_wage'] = df['pw_1'] * df.pw_unit_1.map(lambda x:  2087 if x == 'Hour' else 1)

  # df.drop(['pw_1','pw_unit_1'],inplace=True,axis=1)

  # df.drop(['lca_case_employer_city','lca_case_employer_state'],inplace=True,axis=1)

  # #renaming
  # df.rename(columns={'$lca_case_workloc1_state': 'state',
  #                    '$lca_case_soc_name': 'occupational_group'}, inplace=True)

  # df['state'] = df['lca_case_workloc1_state']
  # df['occupational_group'] = df['lca_case_soc_name']
  # df['job_title'] = df['lca_case_job_title']
  # df['employer_name'] = df['lca_case_employer_name']


  # df.drop(['lca_case_workloc1_city','lca_case_workloc1_state','lca_case_soc_name','lca_case_job_title','lca_case_employer_name'],inplace=True,axis=1)


  # print df

  df.to_csv( ("all.csv"), quoting=csv.QUOTE_ALL, index=False)
  
