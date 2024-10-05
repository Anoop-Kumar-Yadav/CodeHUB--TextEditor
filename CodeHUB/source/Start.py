'''
Concept :-      Simple Text Editor
Developed by :- Anoop Kumar Yadav 
Year :-         12th Final Project For Boards 2021>2022
Guidance :-     Ankit Prabhakar Sir
School :-       Shree Mahaprabhu Public School

Requirements :>
    >> Python3.4 or higher
    >> Windows 7 or higher

    >> Purpose of Libraries here >

        1.) pygments - To get all the keywords, or  idenfiers and other important predefined class of different langugages to highlight it in text Editor
        2.) tkinter - To Create Gui( Graphic User Interface ) Based project ,So it can be a user friendly software.
        3.) json - To store settings applied by the user ,so that when user opens next time get last applied settings.
        4.) csv - To store some values  for future use.
        5.) os - To apply some operations on file and folders.


Hierarchy of Project Folder  :>

>>>>>>codeHUB
>>>>>>|>>>>source
>>>>>>|>>>>|>>>data
>>>>>>|>>>>|>>>|>>>>config
>>>>>>|>>>>|>>>|>>>>|---- about.txt
>>>>>>|>>>>|>>>|>>>>|---- conda_defaultSetting.json
>>>>>>|>>>>|>>>|>>>>|---- conda_lastSetting.json
>>>>>>|>>>>|>>>|>>>>|---- recentfiles.csv
>>>>>>|>>>>|>>>|>>>>|---- xtension.json
>>>>>>|>>>>|>>>|>>>>icons
>>>>>>|>>>>|>>>|>>>>images
>>>>>>|>>>>|>>>|>>>>|---- ide1.ico
>>>>>>|>>>>|>>>|>>>>|---- ide12.png
>>>>>>|>>>>|>>>|>>>>themes
>>>>>>|>>>>|>>>|>>>>|---- quiet_light.json
>>>>>>|>>>>|-- conda_lineNumber.py
>>>>>>|>>>>|-- conda_main.py
>>>>>>|>>>>|-- conda_menuBar.py
>>>>>>|>>>>|-- conda_statusBar.py
>>>>>>|>>>>|-- conda_textArea.py
>>>>>>|>>>>|-- conda_Loader.py
>>>>>>|>>>>|-- highlighter.py
>>>>>>|>>>>|-- popup.py
>>>>>>|>>>>|-- setting.py
>>>>>>|>>>>|-- Start.py

'''

from conda_main import MainEditor

if __name__ =="__main__":
    root = MainEditor()
    root.mainloop()
