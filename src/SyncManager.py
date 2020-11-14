import pathlib
import os
import settings
from threading import Thread
import shutil
from datetime import datetime

class SyncManager():
	def __init__(self, sourceDir=None, targetDir=None):
		self.sourceRootDir = pathlib.Path((sourceDir or settings.SOURCE))
		self.targetRootDir = pathlib.Path((targetDir or settings.TARGET))

	def logState(self):
		print("Source: ", self.sourceRootDir )
		print("Target: ", self.targetRootDir )

	def copyFile(self, sync_file):
		target_file = sync_file.createFileWithNewRoot(
			str(self.sourceRootDir), str(self.targetRootDir)
		)

		# if same version of file already exists at destination
		if target_file.rawPath.exists():
			return None

		self.archiveOldVersions(target_file)
		src = str(sync_file.rawPath)
		dst = str(target_file.rawPath)

		try:
			target_file.rawPath.parent.mkdir(parents=True, exist_ok=True)
			print("Copying {0} to {1}".format(src, dst))
			#shutil.copyfile(src, dst)
			t = Thread(target=shutil.copyfile, args=[
				src,
				dst
			]).start()

			newCopy = None
			if settings.NEW_FILES_DIRECTORY is not None:
				newCopy = self.createSecondCopyInNewDirectory(src, target_file)

			return {"thread": t, "destination": target_file.rawPath, "optional": newCopy}
		except shutil.SameFileError:
			print("Source and destination represents the same file.")
		except IsADirectoryError:
			print("Destination is a directory.")
		except PermissionError:
			print("Permission denied.")
		except:
			print("Error copying file {0}".format(src))
		return None

	def archiveOldVersions(self, syncFile):
		matchesToArchive = syncFile.rawPath.parent.glob(syncFile.identifier+"*.pdf")
		for matchToArchive in matchesToArchive:
			if matchToArchive == syncFile.rawPath.name:
				continue
			newParts = list(matchToArchive.parts)
			newParts.insert(-1, settings.ARCHIVE_DIRECTORY_NAME)

			newPath = pathlib.Path(*newParts)
			newPath.parent.mkdir(parents=False, exist_ok=True)
			matchToArchive.rename(newPath)

	def createSecondCopyInNewDirectory(self, src, dest):
		newParts = list(dest.rawPath.parts)
		newParts.insert(-3, settings.NEW_FILES_DIRECTORY)
		newDest = pathlib.Path(*newParts)
		newDest.parent.mkdir(parents=False, exist_ok=True)

		t = Thread(target=shutil.copyfile, args=[
			src,
			str(newDest)
		]).start()
		return t