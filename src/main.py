from SyncManager import SyncManager 
from SyncFile import SyncFile
import re
from datetime import datetime
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

<<<<<<< HEAD
	for project_folder in [x for x in syncManager.sourceRootDir.iterdir() if x.is_dir()]:
		for company_folder in [x for x in project_folder.iterdir() if x.is_dir()]:
=======
	copy_threads = []
	syncFilesToCopy = []

	for project_folder in syncManager.sourceRootDir.iterdir():
		for company_folder in project_folder.iterdir():
>>>>>>> 432adf2d71721f158eb4c7d07da83d7fb7aaf84a
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

	for t in copy_threads:
		t.join()

	with open("log_{0}.txt".format(datetime.now().strftime("%Y-%m-%d %H %M %S")), 'w') as log:
		for f in syncFilesToCopy:
			log.write("{0}\n".format(str(f)))

	print("Done.")
	return True

if __name__ == "__main__":
	main()
 