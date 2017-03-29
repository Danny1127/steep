#!/usr/bin/python
import pickle 
import sys 
def getPage(config,page,totalPages,currentTab):
	thisFile=config['logFolder']+"/log%s.pickle"%(currentTab)
	file = open(thisFile,'rb')
	

	consoleString=""
	out=[]
	while 3<4:
		try:
			data=pickle.load(file)
			out.append(data)
		except:
			print(sys.exc_info()[0])
			break

	for k in out:
		consoleString+="%s   %s   %s<br>"%(k[0],k[1],k[2])

	file.close() 


	currentExperiment=config['currentExperiment']
	packageFolder=config['packageFolder']
	domain=config['domain']
	this="""
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">
<title>Console</title>
    <script type="text/javascript" src="<JAVASCRIPTCONFIGFILE>"></script>
    <script type="text/javascript" src="<PACKAGEFOLDERHERE>javascript/jquery-1.11.3.min.js"></script>
    <link rel="stylesheet" type="text/css" href="<PACKAGEFOLDERHERE>css/console.css" />
    <script>
    	window.currentLogTab="<CURRENTLOGTABHERE>";
    	window.currentLogURL="<PAGENUMBERHERE>";
    	window.totalPages="<TOTALPAGESHERE>";
    </script>
</head>

<body>
      <div id="mainDiv"></div>

      CONSOLETEXTHERE

<script type="text/javascript" src="<PACKAGEFOLDERHERE>javascript/console.js"></script>
<script type='text/javascript'>
document.getElementById("pythonConsole").addEventListener("click",toggle);
window.toggle=0;
function toggle(){
    window.toggle=1-window.toggle;
    console.log(window.toggle);
}
</script>
</body>
</html>
	"""    

	this=this.replace("CONSOLETEXTHERE",consoleString)
	this=this.replace("<CURRENTLOGTABHERE>",str(currentTab))
	this=this.replace("<TOTALPAGESHERE>",str(totalPages))
	this=this.replace("<PAGENUMBERHERE>",str(page))
	this=this.replace("<JAVASCRIPTCONFIGFILE>",config["configJsURL"])
	this=this.replace("<CURRENTEXPHERE>",domain+currentExperiment)
	this=this.replace("<PACKAGEFOLDERHERE>",domain+packageFolder)
	this=this.replace("<DOMAINHERE>",domain)
	return this



