from SyncManager import SyncManager 
from SyncFile import SyncFile
import re
from datetime import datetime
from .settings import DO_LOGGING
"""
ENSURE THIS IMPORT BELOW IS CORRECT
"""

from .settings import testDirectoryList as directoryList
# from .settings import directoryList as directoryList

regexString = re.compile(r'(?:{})'.format('|'.join(map(re.escape, directoryList))))

def getPrefixFromCompanyFolder(company_folder):
	prefix = re.search(r"^[A-Z][1-9]-\d*",company_folder)
	return prefix[0] if prefix else None 

def shouldSyncDirectory(file):
	return bool(regexString.search(file))

def folder_sync(source_dir, target_dir, file_regex_suffix, createSecondCopy=False):
	syncManager = SyncManager(source_dir, target_dir, createSecondCopy)
	syncManager.logState()

	copy_threads = []
	syncFilesToCopy = []
	for year_folder in [x for x in syncManager.sourceRootDir.iterdir() if x.is_dir()]:
		for project_folder in [x for x in year_folder.iterdir() if x.is_dir()]:
			if not shouldSyncDirectory(project_folder.name):
				continue
			print("Syncing {0}".format(project_folder.name))

			filePrefix = getPrefixFromCompanyFolder(project_folder.name)
			allFiles = [x for x in (project_folder.glob(filePrefix + file_regex_suffix))]

			groupedFiles = {}
			for ungroupedFile in allFiles:
				file = SyncFile(ungroupedFile)
				filesInConflict = groupedFiles.get(file.identifier, [])
				filesInConflict.append(file)
				groupedFiles[file.identifier] = filesInConflict

			for k in groupedFiles:
				conflictingFiles = groupedFiles[k]
				maxFile = conflictingFiles[0]
				for f in conflictingFiles[1:]:
					maxFile = f if f > maxFile else maxFile
				syncFilesToCopy.append(maxFile)
				values = syncManager.copyFile(maxFile)
				if values is not None:
					t = values.get("thread")
					destination = values.get("destination")
					newCopy = values.get("newCopy", None)
					if (newCopy is not None):
						copy_threads.append(newCopy)

					syncFilesToCopy.append(destination)
					if t is not None:
						copy_threads.append(t)


	if DO_LOGGING:
		with open("log_{0}.txt".format(datetime.now().strftime("%Y-%m-%d %H %M %S")), 'w') as log:
			for f in syncFilesToCopy:
				log.write("{0}\n".format(str(f)))

	return copy_threads
