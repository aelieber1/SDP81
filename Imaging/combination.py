####################################################################
                      ##################### General information ###########################

########## This script contains the steps that have already been performed to create the measurement sets SDP.81_Band4_continuum.ms and SDP.81_Band4.ms, which can be found in the Imaging directory. This script does not need to run by the students, it is purely informative.
 

                     ####################################################################
                      ##################### Startup ###########################



########## importing packages and aliases

import re
import os
import analysisUtils as au
import analysisUtils as aU
es = aU.stuffForScienceDataReduction() 

###################################################################


# NOTE spectral averaging was already done (every 16 channels for
# continuum and 20 for the line data) in the individual calibration
# scripts.

# Concatenate datasets:
band4_calibrated_data = ['uid___A002_X91068d_Xa1e.ms.split.cal.science',
                         'uid___A002_X91068d_Xc50.ms.split.cal.science',
                         'uid___A002_X91068d_Xead.ms.split.cal.science',
                         'uid___A002_X915f1c_X5d0.ms.split.cal.science',
                         'uid___A002_X924c91_X12c.ms.split.cal.science',
                         'uid___A002_X924c91_X34f.ms.split.cal.science',
                         'uid___A002_X924c91_X572.ms.split.cal.science',
                         'uid___A002_X924c91_X847.ms.split.cal.science',
                         'uid___A002_X924c91_Xa47.ms.split.cal.science',
                         'uid___A002_X93514d_X1634.ms.split.cal.science',
                         'uid___A002_X93514d_X1857.ms.split.cal.science',
                         'uid___A002_X93514d_Xfc6.ms.split.cal.science']

os.system('rm -rf SDP.81_Band4.ms')
concat(vis = band4_calibrated_data, concatvis = 'SDP.81_Band4.ms')

# Define spectral windows for the continuum.  
spw_cont = '0~2,4~6,8~10,12~14,16~18,20~22,24~26,28~30,32~34,36~38,40~42,44~46'
os.system('rm -rf SDP.81_Band4_continuum.ms')
split(vis='SDP.81_Band4.ms',outputvis='SDP.81_Band4_continuum.ms',
      spw=spw_cont,datacolumn='data')

### prepare a dataset with only the bandpass calibrator, from only one execution:
split(vis='SDP81_B4_uncalibrated.ms.split',outputvis='bandpass.ms',field='0',datacolumn='corrected',spw='0,1,2')
