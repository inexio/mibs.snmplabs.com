#
# PySNMP MIB module HOST-RESOURCES-TYPES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HOST-RESOURCES-TYPES
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hrStorage, hrMIBAdminInfo, hrDevice = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorage", "hrMIBAdminInfo", "hrDevice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, Counter32, Gauge32, IpAddress, ObjectIdentity, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, iso, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "iso", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hostResourcesTypesModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 25, 7, 4))
hostResourcesTypesModule.setRevisions(('2000-03-06 00:00',))
if mibBuilder.loadTexts: hostResourcesTypesModule.setLastUpdated('200003060000Z')
if mibBuilder.loadTexts: hostResourcesTypesModule.setOrganization('IETF Host Resources MIB Working Group')
hrStorageTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 25, 2, 1))
hrStorageOther = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 1))
if mibBuilder.loadTexts: hrStorageOther.setStatus('current')
hrStorageRam = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 2))
if mibBuilder.loadTexts: hrStorageRam.setStatus('current')
hrStorageVirtualMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 3))
if mibBuilder.loadTexts: hrStorageVirtualMemory.setStatus('current')
hrStorageFixedDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 4))
if mibBuilder.loadTexts: hrStorageFixedDisk.setStatus('current')
hrStorageRemovableDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 5))
if mibBuilder.loadTexts: hrStorageRemovableDisk.setStatus('current')
hrStorageFloppyDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 6))
if mibBuilder.loadTexts: hrStorageFloppyDisk.setStatus('current')
hrStorageCompactDisc = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 7))
if mibBuilder.loadTexts: hrStorageCompactDisc.setStatus('current')
hrStorageRamDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 8))
if mibBuilder.loadTexts: hrStorageRamDisk.setStatus('current')
hrStorageFlashMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 9))
if mibBuilder.loadTexts: hrStorageFlashMemory.setStatus('current')
hrStorageNetworkDisk = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 2, 1, 10))
if mibBuilder.loadTexts: hrStorageNetworkDisk.setStatus('current')
hrDeviceTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 25, 3, 1))
hrDeviceOther = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 1))
if mibBuilder.loadTexts: hrDeviceOther.setStatus('current')
hrDeviceUnknown = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 2))
if mibBuilder.loadTexts: hrDeviceUnknown.setStatus('current')
hrDeviceProcessor = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 3))
if mibBuilder.loadTexts: hrDeviceProcessor.setStatus('current')
hrDeviceNetwork = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 4))
if mibBuilder.loadTexts: hrDeviceNetwork.setStatus('current')
hrDevicePrinter = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 5))
if mibBuilder.loadTexts: hrDevicePrinter.setStatus('current')
hrDeviceDiskStorage = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 6))
if mibBuilder.loadTexts: hrDeviceDiskStorage.setStatus('current')
hrDeviceVideo = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 10))
if mibBuilder.loadTexts: hrDeviceVideo.setStatus('current')
hrDeviceAudio = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 11))
if mibBuilder.loadTexts: hrDeviceAudio.setStatus('current')
hrDeviceCoprocessor = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 12))
if mibBuilder.loadTexts: hrDeviceCoprocessor.setStatus('current')
hrDeviceKeyboard = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 13))
if mibBuilder.loadTexts: hrDeviceKeyboard.setStatus('current')
hrDeviceModem = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 14))
if mibBuilder.loadTexts: hrDeviceModem.setStatus('current')
hrDeviceParallelPort = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 15))
if mibBuilder.loadTexts: hrDeviceParallelPort.setStatus('current')
hrDevicePointing = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 16))
if mibBuilder.loadTexts: hrDevicePointing.setStatus('current')
hrDeviceSerialPort = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 17))
if mibBuilder.loadTexts: hrDeviceSerialPort.setStatus('current')
hrDeviceTape = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 18))
if mibBuilder.loadTexts: hrDeviceTape.setStatus('current')
hrDeviceClock = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 19))
if mibBuilder.loadTexts: hrDeviceClock.setStatus('current')
hrDeviceVolatileMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 20))
if mibBuilder.loadTexts: hrDeviceVolatileMemory.setStatus('current')
hrDeviceNonVolatileMemory = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 1, 21))
if mibBuilder.loadTexts: hrDeviceNonVolatileMemory.setStatus('current')
hrFSTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 25, 3, 9))
hrFSOther = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 1))
if mibBuilder.loadTexts: hrFSOther.setStatus('current')
hrFSUnknown = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 2))
if mibBuilder.loadTexts: hrFSUnknown.setStatus('current')
hrFSBerkeleyFFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 3))
if mibBuilder.loadTexts: hrFSBerkeleyFFS.setStatus('current')
hrFSSys5FS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 4))
if mibBuilder.loadTexts: hrFSSys5FS.setStatus('current')
hrFSFat = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 5))
if mibBuilder.loadTexts: hrFSFat.setStatus('current')
hrFSHPFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 6))
if mibBuilder.loadTexts: hrFSHPFS.setStatus('current')
hrFSHFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 7))
if mibBuilder.loadTexts: hrFSHFS.setStatus('current')
hrFSMFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 8))
if mibBuilder.loadTexts: hrFSMFS.setStatus('current')
hrFSNTFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 9))
if mibBuilder.loadTexts: hrFSNTFS.setStatus('current')
hrFSVNode = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 10))
if mibBuilder.loadTexts: hrFSVNode.setStatus('current')
hrFSJournaled = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 11))
if mibBuilder.loadTexts: hrFSJournaled.setStatus('current')
hrFSiso9660 = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 12))
if mibBuilder.loadTexts: hrFSiso9660.setStatus('current')
hrFSRockRidge = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 13))
if mibBuilder.loadTexts: hrFSRockRidge.setStatus('current')
hrFSNFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 14))
if mibBuilder.loadTexts: hrFSNFS.setStatus('current')
hrFSNetware = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 15))
if mibBuilder.loadTexts: hrFSNetware.setStatus('current')
hrFSAFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 16))
if mibBuilder.loadTexts: hrFSAFS.setStatus('current')
hrFSDFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 17))
if mibBuilder.loadTexts: hrFSDFS.setStatus('current')
hrFSAppleshare = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 18))
if mibBuilder.loadTexts: hrFSAppleshare.setStatus('current')
hrFSRFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 19))
if mibBuilder.loadTexts: hrFSRFS.setStatus('current')
hrFSDGCFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 20))
if mibBuilder.loadTexts: hrFSDGCFS.setStatus('current')
hrFSBFS = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 21))
if mibBuilder.loadTexts: hrFSBFS.setStatus('current')
hrFSFAT32 = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 22))
if mibBuilder.loadTexts: hrFSFAT32.setStatus('current')
hrFSLinuxExt2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 25, 3, 9, 23))
if mibBuilder.loadTexts: hrFSLinuxExt2.setStatus('current')
mibBuilder.exportSymbols("HOST-RESOURCES-TYPES", hrFSSys5FS=hrFSSys5FS, hrDeviceVideo=hrDeviceVideo, hrFSAppleshare=hrFSAppleshare, hrStorageCompactDisc=hrStorageCompactDisc, hrDeviceDiskStorage=hrDeviceDiskStorage, hrFSOther=hrFSOther, PYSNMP_MODULE_ID=hostResourcesTypesModule, hrFSiso9660=hrFSiso9660, hrDeviceProcessor=hrDeviceProcessor, hostResourcesTypesModule=hostResourcesTypesModule, hrFSRockRidge=hrFSRockRidge, hrFSVNode=hrFSVNode, hrDeviceSerialPort=hrDeviceSerialPort, hrDeviceNetwork=hrDeviceNetwork, hrFSMFS=hrFSMFS, hrStorageFixedDisk=hrStorageFixedDisk, hrDeviceParallelPort=hrDeviceParallelPort, hrDeviceTape=hrDeviceTape, hrStorageFlashMemory=hrStorageFlashMemory, hrFSLinuxExt2=hrFSLinuxExt2, hrDeviceNonVolatileMemory=hrDeviceNonVolatileMemory, hrFSRFS=hrFSRFS, hrFSUnknown=hrFSUnknown, hrFSJournaled=hrFSJournaled, hrFSFAT32=hrFSFAT32, hrDeviceTypes=hrDeviceTypes, hrFSFat=hrFSFat, hrStorageRemovableDisk=hrStorageRemovableDisk, hrStorageRamDisk=hrStorageRamDisk, hrFSTypes=hrFSTypes, hrDevicePointing=hrDevicePointing, hrFSBerkeleyFFS=hrFSBerkeleyFFS, hrStorageRam=hrStorageRam, hrDeviceUnknown=hrDeviceUnknown, hrFSBFS=hrFSBFS, hrStorageVirtualMemory=hrStorageVirtualMemory, hrFSDGCFS=hrFSDGCFS, hrFSAFS=hrFSAFS, hrDeviceModem=hrDeviceModem, hrDeviceCoprocessor=hrDeviceCoprocessor, hrFSDFS=hrFSDFS, hrDeviceVolatileMemory=hrDeviceVolatileMemory, hrFSNetware=hrFSNetware, hrDeviceOther=hrDeviceOther, hrStorageTypes=hrStorageTypes, hrFSHFS=hrFSHFS, hrStorageOther=hrStorageOther, hrDeviceKeyboard=hrDeviceKeyboard, hrFSHPFS=hrFSHPFS, hrDevicePrinter=hrDevicePrinter, hrFSNTFS=hrFSNTFS, hrDeviceClock=hrDeviceClock, hrStorageFloppyDisk=hrStorageFloppyDisk, hrDeviceAudio=hrDeviceAudio, hrFSNFS=hrFSNFS, hrStorageNetworkDisk=hrStorageNetworkDisk)
