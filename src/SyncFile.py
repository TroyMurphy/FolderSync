import re
import pathlib

class SyncFile():
	def __init__(self, file_path):
		self.rawPath = pathlib.Path(file_path)
		self._identifier = None
		self._version = None

	@property
	def name(self):
		return self.rawPath.name

	@property
	def identifier(self):
		if self._identifier is not None:
			return self._identifier
		
		leftSide = self.rawPath.stem.upper().rsplit("REV")[0]
		self._identifier = re.split(r'[\s-]*$', leftSide)[0]
		return self._identifier
	
	@property
	def version(self):
		if self._version is not None:
			return self._version

		parts = self.rawPath.stem.upper().rsplit("REV")
		if len(parts):
			return None
		
		self._version = str(re.search(r"\w", parts[1])[0])
		return self._version

	def createFileWithNewRoot(self, source, target):
		return SyncFile(
			str(self.rawPath).replace(
				str(source), str(target)
			)
		)

	def __gt__(self, otherFile):
		this_version = self.version
		that_version = otherFile.version

		if that_version is None:
			return True

		if this_version.isnumeric():
			if that_version.isnumeric():
				return int(this_version) > int(that_version)
			return True

		if that_version.isnumeric():
			return True
		return this_version > that_version

	def __str__(self):
		return str(self.rawPath.absolute())
