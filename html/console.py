#!/usr/bin/python
import pickle 
import sys 
import json
import netifaces as ni

def getPage(config,tf,page,totalPages,currentTab,thisPage):
	string="window.totalPages=%s;\n"%(totalPages)
	string+="window.page='%s';\n"%(page)
	string+="window.serverPage='%s';\n"%(thisPage)
	string+="window.currentTab=%s;\n"%(currentTab)

	thisFile=config['logFolder']+"/pickle/%s.pickle"%(currentTab)
	file = open(thisFile,'rb')
	out=[]

	while 3<4:
		try:
			data=pickle.load(file)
			out.append(data)
		except:
			# print(sys.exc_info()[0])
			break
	file.close() 

	string+="window.consoleLines=%s;\n"%(json.dumps(out).encode('utf8'))

	thisVersion=sys.version.split("\n")[0]
	thisVersion=thisVersion.replace("\"","'")
	string+="window.pythonVersion=\"%s\";\n"%(thisVersion)
	string+="window.pythonExecutable=\"%s\";"%(sys.executable)
	ips=[]
	for k in ni.interfaces():
	 ni.ifaddresses(k)
	 try:  
	    ip = ni.ifaddresses(k)[2][0]['addr']
	    ips.append(["%s"%(k),"%s"%(ip)])
	 except:
	    "no address"
	string+="window.ipAddresses=%s;"%(ips)

	currentExperiment=config['currentExperiment']
	packageFolder=config['packageFolder']
	domain=config['domain']
	this=''
	this+='<html>\n'
	this+='\t<head>\n'
	this+='\t\t<title>STEEP: Dashboard</title>\n'
	this+='\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf['common']['jquery.js'])
	this+='\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf[currentExperiment]['config.js'])
	this+='\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf['common']['common.js'])
	this+='\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf['common']['websocketConnect.js'])
	this+='\t\t<link rel="stylesheet" type="text/css" href="%s/%s/html/auto-version/%s" />\n'%(domain,packageFolder,tf['common']['common.css'])
	this+='\t\t<link rel="stylesheet" type="text/css" href="%s/%s/html/auto-version/%s" />\n'%(domain,packageFolder,tf['common']['switch.css'])
	this+='\t\t<link rel="stylesheet" type="text/css" href="%s/%s/html/auto-version/%s" />\n'%(domain,packageFolder,tf['common']['monitor.css'])
	this+='\t</head>\n'
	this+='\t<body>\n'
	this+='\t\t<div id="mainDiv"></div>\n'
	this+='\t\t\t<script type="text/javascript">%s</script>\n'%(string)
	this+='\t\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf['common']['index.js'])
	this+='\t\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf['common']['monitor.js'])
	this+='\t\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf['common']['console.js'])
	this+='\t\t\t<script type="text/javascript" src="%s/%s/html/auto-version/%s"></script>\n'%(domain,packageFolder,tf['common']['video.js'])
	this+='\t<body>\n'
	this+='</html>'

	return this
