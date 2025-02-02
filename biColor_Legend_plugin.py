from abaqusGui import getAFXApp, Activator, AFXMode
from abaqusConstants import ALL
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='BiColor Legend', 
    object=Activator(os.path.join(thisDir, 'biColor_LegendDB.py')),
    kernelInitString='import bicolor_legend',
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    applicableModules=['Visualization'],
    version='N/A',
    author='N/A',
    description='Simple plug-in to generate a legend with two colors in postprocessing.\nIntended to easily visualize tension/compression regions.',
    helpUrl='N/A'
)
