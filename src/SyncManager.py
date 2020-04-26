import pathlib
import INCLUDE_REGEX, EXCLUDE_REGEX from settings

class SyncManager():
	def __init__(self, sourceDir, targetDir):
		self.readDir = pathlib.Path(sourceDir)
		self.writeDir = pathlib.Path(targetDir)
		self.includeRegex = None
		self.excludeRegex = None
	
	def initialize_from_settings(self):
		self.includeRegex = INCLUDE_REGEX
		self.excludeRegex = EXCLUDE_REGEX
