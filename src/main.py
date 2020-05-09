from SyncManager import SyncManager 
from SyncFile import SyncFile
import re
import settings

regexString = re.compile(r'(?:{})'.format('|'.join(map(re.escape, settings.directoryList))))

def getPrefixFromCompanyFolder(company_folder):
	prefix = re.search(r"^[A-Z][1-9]-\d*",company_folder)
	return prefix[0] if prefix else None 

def shouldSyncDirectory(file):
	return bool(regexString.search(file))

def main():
	syncManager = SyncManager()
	syncManager.logState()

	for project_folder in syncManager.sourceRootDir.iterdir():
		for company_folder in project_folder.iterdir():
			if not shouldSyncDirectory(company_folder.name):
				continue
			print("Syncing {0}".format(company_folder.name))

			filePrefix = getPrefixFromCompanyFolder(company_folder.name)
			allFiles = [x for x in (company_folder.glob(filePrefix+"*.pdf"))]

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
				syncManager.copyFile(maxFile)

if __name__ == "__main__":
	main()
 