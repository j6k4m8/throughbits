import os, datetime

os.system('git add .')
os.system('git commit -am "' +
	format(datetime.datetime.now(), "%H:%M.%S") + '"')
os.system('git push origin master')
os.system('git pull')
os.system('git rebase master') # :)
