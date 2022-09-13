import pandas as pd
import numpy as np
from sqlalchemy import false

##########  load in the data   (SPARC and Neighborhood Atlas 2015) 
Hospital_Inpatient_Discharges = pd.read_csv(r'Example Data\SPARCS_data\Hospital_Inpatient_Discharges_SPARCS_De_Identified_2015.csv',low_memory=False)
NeighborhoodAtlas = pd.read_csv(r'Example Data\NeighborhoodAtlas2015\AL_2015_ADI_9 Digit_Zip_Code_v3_1_upd_new_col.csv', low_memory=False)

### Load column names from each file
Hospital_Inpatient_Discharges.columns
NeighborhoodAtlas.columns

## Convert Dtype to make common columns for merging purposes (ZIPID.1)
Hospital_Inpatient_Discharges.dtypes
NeighborhoodAtlas.dtypes
NeighborhoodAtlas['ZIPID.1'] = NeighborhoodAtlas['ZIPID.1'].astype(str)
NeighborhoodAtlas.dtypes


## To make a shorter view of report with necessary columns
Hos_inp_dis_small = Hospital_Inpatient_Discharges[{'Zip Code - 3 digits','Type of Admission','APR Severity of Illness Description','Health Service Area','Hospital County'}]
print (Hos_inp_dis_small.head(5).to_markdown())
Atlas_small = NeighborhoodAtlas[{'ZIPID.1','ADI_STATERNK'}] 
print (Atlas_small.head(5).to_markdown())


### Below, I am going to take Hospital Inpatient Discharges table, and enrich it with  
### NeighborhoodAtlas table, using  zip code as common variable to bring up report of 
# City/State/County with inpatient admission and Severity of illness among disadvantaged 
# neighborhood where has been linked to a number of healthcare outcomes.
###
combined_df = Hos_inp_dis_small.merge(Atlas_small, how='left', left_on='Zip Code - 3 digits', right_on= 'ZIPID.1')

## OR

combined_df = Hos_inp_dis_small.merge(Atlas_small, how='left', left_on='Zip Code - 3 digits', right_on='ZIPID.1')

## update columns after merging 
combined_df.columns

### Output merged report and save into new file (combined_df)
combined_df
print (combined_df.sample(10).to_markdown())
combined_df.to_csv('Example Data\combined_df.csv')

############################################################# END  #########################################################
#############################################################################################################
##choose another dataset: Inpatient Prospective Payment System (IPPS))from Kraggle 

import pandas as pd
import numpy as np

##########  load in the data   (SPARC & Inpatient Prospective Payment System (IPPS))
Hospital_Inpatient_Discharges = pd.read_csv(r'Example Data\SPARCS_data\Hospital_Inpatient_Discharges_SPARCS_De_Identified_2015.csv',low_memory=False)
Inpatient_Prospective_Payment_System= pd.read_csv(r'Example Data\Inpatient Prospective Payment System (IPPS)\Inpatient_Prospective_Payment_System.csv', low_memory=False)

### Load column names from each file
Hospital_Inpatient_Discharges.columns
Inpatient_Prospective_Payment_System.columns


### Below, I am going to utilize 'State'as common variable between Hospital 
# Inpatient Discharges table and Inpatient Prospective Payment System (IPPS) 
# to bring up report of inpatient admission and cost associated with inpatient discharge.


## To make a shorter view of report with necessary columns
dff_Hos_inp_dis_small = Hospital_Inpatient_Discharges[{'Total Charges','Total Costs','Health Service Area','Hospital County'}]
dff_Inp_pay_sys_small = Inpatient_Prospective_Payment_System[{'Provider City','Provider State',' Total Discharges ',' Average Covered Charges ',' Average Total Payments ','Average Medicare Payments'}]

### Load column names from each file
dff_Hos_inp_dis_small.columns
dff_Inp_pay_sys_small.columns

## ## Check Dtype to ensure common columns datatype for merging purposes
dff_Hos_inp_dis_small.dtypes
dff_Inp_pay_sys_small.dtypes


# Print report with 5 rows information
print (dff_Hos_inp_dis_small.head(5).to_markdown())
print (dff_Inp_pay_sys_small.head(5).to_markdown())

## Merging Hospital Inpatient Discharges table and Inpatient Prospective Payment System (IPPS) 
##  using 'state' as a common variable to bring up report of inpatient admission and cost 
### associated with inpatient discharge.

combined_dff = dff_Hos_inp_dis_small.merge(dff_Inp_pay_sys_small, how='left', left_on='Health Service Area', right_on= 'Provider State')


### Output merged report and save into new file (combined_dff)
print (combined_dff.head(5).to_markdown())
print (combined_dff.sample(5).to_markdown())
combined_dff.to_csv('Example Data\combined_dff.csv')

################################################ END   #####################################################################
###################################################################### END ##########################################
#####################################################################
