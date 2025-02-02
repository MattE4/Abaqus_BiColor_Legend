from abaqus import *
from abaqusConstants import *
from caeModules import visualization

def setBiLegend(kw_max=None, 
				kw_max_value=None,
				kw_neutral=None,
				kw_neutral_value=None,
				kw_min=None,
				kw_min_value=None,
				kw_invert=None,
				kw_reset=None):

	# print(f'{kw_max=}, {kw_max_value=}, {kw_neutral=}, {kw_neutral_value=}, {kw_min=}, {kw_min_value=}, {kw_invert=}, {kw_reset=}')

	vps = session.viewports.values()[0]
	disp = session.viewports[vps.name].odbDisplay

	#########################################################################################

	# reset
	disp.contourOptions.setValues(numIntervals=12, intervalType=UNIFORM, intervalValues=(), spectrum='Rainbow')    

	if not kw_reset:
		
		if kw_max.find('Auto') > 0:
			maxValue = session.defaultOdbDisplay.contourOptions.autoMaxValue
		else:
			maxValue = float(kw_max_value)

		if kw_min.find('Auto') > 0:
			minValue = session.defaultOdbDisplay.contourOptions.autoMinValue
		else:
			minValue = float(kw_min_value)

		if kw_neutral.find('Auto') > 0:
			neutralValue = 0
			if minValue >= 0 or maxValue <= 0:
				neutralValue = round((maxValue-minValue)/2., 3)
				print('\nNeutral value adjusted to be midway between Max and Min value.')
		else:
			neutralValue = float(kw_neutral_value)
		

		if maxValue <= minValue:
			getWarningReply(message='Max value must be greater than Min value!', buttons=(CANCEL,))
			return
		elif neutralValue >= maxValue or neutralValue <= minValue:
			getWarningReply(message='Neutral value must be between Max and Min value!', buttons=(CANCEL,))
			return

		
		if kw_invert:
			disp.contourOptions.setValues(spectrum='Reversed rainbow', numIntervals=2, intervalType=USER_DEFINED, intervalValues=(minValue, neutralValue, maxValue, ))
		else:
			disp.contourOptions.setValues(spectrum='Rainbow', numIntervals=2, intervalType=USER_DEFINED, intervalValues=(minValue, neutralValue, maxValue, ))
			
	

if __name__ == '__main__':
	setBiLegend()