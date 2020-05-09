import pathlib
import unittest

from SyncFile import SyncFile
from tests.factories.SyncFileFactory import SyncFileFactory


class SyncFileTest(unittest.TestCase):
    def setup(self):
        self.syncFileFactory = SyncFileFactory()

class TestCreate(SyncFileTest):
    def testCreateFromString(self):
        filePath = "."
        file = SyncFileFactory.CreateSyncFile(filePath)
        self.assertIsInstance(file, SyncFile)
        self.assertIsInstance(file.rawPath, pathlib.Path)

    def testCreateFromString(self):
        filePath = pathlib.Path(".")
        file = SyncFileFactory.CreateSyncFile(filePath)
        self.assertIsInstance(file, SyncFile)
        self.assertIsInstance(file.rawPath, pathlib.Path)

class TestIdentifier(SyncFileTest):
    def testIdentifier(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something")
        self.assertEqual(file.identifier, "Something")

    def testIdentifierWithRev(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something - rev 1")
        self.assertEqual(file.identifier, "Something")

    def testIdentiferWithCaseRev(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something - Rev 1")
        self.assertEqual(file.identifier, "Something")

    def testIdentifierWithSigned(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something - Rev 1 - Signed")
        self.assertEqual(file.identifier, "Something")

class TestVersion(SyncFileTest):
    def testVersion(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something")
        self.assertIsNone(file.version)

    def testVersion1(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something - rev 1")
        self.assertEqual(file.version, "1")

    def testVersionA(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something - Rev A")
        self.assertEqual(file.version, "A")

    def testVersionSigned(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\Something - Rev 1 - Signed")
        self.assertEqual(file.version, "1")


class TestSwitchRoot(SyncFileTest):
    def testSwitchFileRoot(self):
        file = SyncFileFactory.CreateSyncFile(r".\source\myfile")
        newFile = file.createFileWithNewRoot("source", "target")
        self.assertNotEqual(file.rawPath, newFile.rawPath)

class TestOverloads(SyncFileTest):
    def testGreaterThan(self):
        file1 = SyncFileFactory.CreateSyncFile(r".\source\myfile - Rev A")
        file2 = SyncFileFactory.CreateSyncFile(r".\source\myfile - Rev F")
        file3 = SyncFileFactory.CreateSyncFile(r".\source\myfile - Rev 0")
        file4 = SyncFileFactory.CreateSyncFile(r".\source\myfile - Rev 3")
        self.assertTrue(file1 < file2 < file3 < file4)
