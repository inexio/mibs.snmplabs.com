#
# PySNMP MIB module INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
bladeSlotId, = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId")
chassis, = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassis")
groups, regModule = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "groups", "regModule")
FaultLedStates, Index, IdromBinary16, Power, PresenceLedStates, PowerLedStates = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-TC", "FaultLedStates", "Index", "IdromBinary16", "Power", "PresenceLedStates", "PowerLedStates")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, Counter64, Unsigned32, IpAddress, Bits, Gauge32, Counter32, ModuleIdentity, NotificationType, TimeTicks, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Counter64", "Unsigned32", "IpAddress", "Bits", "Gauge32", "Counter32", "ModuleIdentity", "NotificationType", "TimeTicks", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
multiFlexServerStorageMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 18))
multiFlexServerStorageMibModule.setRevisions(('2007-09-12 11:10', '2007-08-16 13:30', '2007-07-20 16:30', '2007-07-09 12:00', '2007-06-07 20:30', '2007-06-07 13:30', '2007-04-18 19:05', '2007-04-18 19:05', '2007-04-09 15:45', '2007-04-09 10:30', '2007-03-15 18:30', '2007-03-10 16:00', '2007-02-22 17:00', '2007-01-08 09:50', '2006-12-28 17:30', '2006-12-05 10:30', '2006-12-04 16:30', '2006-11-07 07:01', '2006-10-02 06:29',))
if mibBuilder.loadTexts: multiFlexServerStorageMibModule.setLastUpdated('200709121110Z')
if mibBuilder.loadTexts: multiFlexServerStorageMibModule.setOrganization('Intel Corporation')
storage = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208))
if mibBuilder.loadTexts: storage.setStatus('current')
interposer = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1))
if mibBuilder.loadTexts: interposer.setStatus('current')
storageWWN = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 3), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageWWN.setStatus('current')
storageInterConnectionType = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("unsupported", 0), ("sas", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageInterConnectionType.setStatus('current')
interposerVendor = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerVendor.setStatus('current')
interposerMfgDate = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerMfgDate.setStatus('current')
interposerDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerDeviceName.setStatus('current')
interposerPart = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 4), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerPart.setStatus('current')
interposerSerialNo = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 5), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerSerialNo.setStatus('current')
interposerMaximumPower = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 6), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerMaximumPower.setStatus('current')
interposerNominalPower = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 7), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerNominalPower.setStatus('current')
interposerAssetTag = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 1, 8), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interposerAssetTag.setStatus('current')
storagePoolTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5), )
if mibBuilder.loadTexts: storagePoolTable.setStatus('current')
storagePoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolIndex"))
if mibBuilder.loadTexts: storagePoolEntry.setStatus('current')
poolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 1), Index()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolIndex.setStatus('current')
poolAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolAlias.setStatus('current')
poolOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolOperationalStatus.setStatus('current')
poolCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolCondition.setStatus('current')
poolOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolOperation.setStatus('current')
poolPhysicalCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolPhysicalCapacity.setStatus('current')
poolConfigurableCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolConfigurableCapacity.setStatus('current')
poolFreeCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolFreeCapacity.setStatus('current')
poolMaxContiguousCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolMaxContiguousCapacity.setStatus('current')
poolMediaPatrolEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolMediaPatrolEnabled.setStatus('current')
poolPDMEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolPDMEnabled.setStatus('current')
poolNumOfPhysicalDrives = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumOfPhysicalDrives.setStatus('current')
poolNumOfVirtualDrives = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumOfVirtualDrives.setStatus('current')
poolNumOfDedicatedSpares = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolNumOfDedicatedSpares.setStatus('current')
poolPhysicalDriveIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolPhysicalDriveIDs.setStatus('current')
poolVirtualDriveIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolVirtualDriveIDs.setStatus('current')
poolDedicatedSpareIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolDedicatedSpareIDs.setStatus('current')
poolWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 5, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: poolWWN.setStatus('current')
virtualDriveTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6), )
if mibBuilder.loadTexts: virtualDriveTable.setStatus('current')
virtualDriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveId"))
if mibBuilder.loadTexts: virtualDriveEntry.setStatus('current')
virtDriveId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 1), Index()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveId.setStatus('current')
virtDriveAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveAlias.setStatus('current')
virtDriveSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveSerialNo.setStatus('current')
virtDriveWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 4), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveWWN.setStatus('current')
virtDriveOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveOperationalStatus.setStatus('current')
virtDriveCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveCondition.setStatus('current')
virtDriveOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveOperation.setStatus('current')
virtDriveSynchronized = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveSynchronized.setStatus('current')
virtDriveRAIDLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 3, 5, 6, 10, 16, 80, 81, 85, 95, 96))).clone(namedValues=NamedValues(("unknown", -1), ("raid0", 0), ("raid1", 1), ("raid3", 3), ("raid5", 5), ("raid6", 6), ("jbod", 10), ("raid10", 16), ("raid50", 80), ("raid51", 81), ("raid55", 85), ("raid1e", 95), ("raid60", 96)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveRAIDLevel.setStatus('current')
virtDriveCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveCapacity.setStatus('current')
virtDrivePhysicalCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDrivePhysicalCapacity.setStatus('current')
virtDriveStoragePoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStoragePoolId.setStatus('current')
virtDriveNumOfAxels = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveNumOfAxels.setStatus('current')
virtDriveNumOfUsedPD = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveNumOfUsedPD.setStatus('current')
virtDriveSectorSize = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveSectorSize.setStatus('current')
virtDrivePreferredScmId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 6, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("unavailable", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDrivePreferredScmId.setStatus('current')
virtualDriveStatsTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7), )
if mibBuilder.loadTexts: virtualDriveStatsTable.setStatus('current')
virtualDriveStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1), )
virtualDriveEntry.registerAugmentions(("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtualDriveStatsEntry"))
virtualDriveStatsEntry.setIndexNames(*virtualDriveEntry.getIndexNames())
if mibBuilder.loadTexts: virtualDriveStatsEntry.setStatus('current')
virtDriveStatsDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsDataTransferred.setStatus('current')
virtDriveStatsReadDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsReadDataTransferred.setStatus('current')
virtDriveStatsWriteDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsWriteDataTransferred.setStatus('current')
virtDriveStatsNumOfErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfErrors.setStatus('current')
virtDriveStatsNumOfNonRWErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfNonRWErrors.setStatus('current')
virtDriveStatsNumOfReadErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfReadErrors.setStatus('current')
virtDriveStatsNumOfWriteErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfWriteErrors.setStatus('current')
virtDriveStatsNumOfIORequests = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfIORequests.setStatus('current')
virtDriveStatsNumOfNonRWRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfNonRWRequests.setStatus('current')
virtDriveStatsNumOfReadRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfReadRequests.setStatus('current')
virtDriveStatsNumOfWriteRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsNumOfWriteRequests.setStatus('current')
virtDriveStatsStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsStartTime.setStatus('current')
virtDriveStatsCollectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 7, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtDriveStatsCollectionTime.setStatus('current')
spareDriveTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8), )
if mibBuilder.loadTexts: spareDriveTable.setStatus('current')
spareDriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareIndex"))
if mibBuilder.loadTexts: spareDriveEntry.setStatus('current')
spareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 1), Index()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareIndex.setStatus('current')
spareOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareOperationalStatus.setStatus('current')
sparePhysicalDriveId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparePhysicalDriveId.setStatus('current')
sparePhysicalCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sparePhysicalCapacity.setStatus('current')
spareConfigurableCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareConfigurableCapacity.setStatus('current')
spareRevertible = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareRevertible.setStatus('current')
spareType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("dedicated", 2), ("global", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareType.setStatus('current')
spareNumOfAssociatedStoragePools = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareNumOfAssociatedStoragePools.setStatus('current')
spareAssociatedStoragePoolIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareAssociatedStoragePoolIDs.setStatus('current')
spareDriveWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 8, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spareDriveWWN.setStatus('current')
vdb2lTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 9), )
if mibBuilder.loadTexts: vdb2lTable.setStatus('current')
vdb2lEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 9, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveId"), (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"))
if mibBuilder.loadTexts: vdb2lEntry.setStatus('current')
vdb2Lun = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vdb2Lun.setStatus('current')
bl2vdTable = MibTable((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 10), )
if mibBuilder.loadTexts: bl2vdTable.setStatus('current')
bl2vdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 10, 1), ).setIndexNames((0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"), (0, "INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "vdb2Lun"))
if mibBuilder.loadTexts: bl2vdEntry.setStatus('current')
bl2vdVirtualDriveId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 208, 10, 1, 1), Index()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bl2vdVirtualDriveId.setStatus('current')
storageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 18)).setObjects(("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerVendor"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerMfgDate"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerDeviceName"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerPart"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerSerialNo"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerMaximumPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerNominalPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "interposerAssetTag"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "storageWWN"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "storageInterConnectionType"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolIndex"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolAlias"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolOperationalStatus"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolCondition"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolOperation"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolPhysicalCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolConfigurableCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolFreeCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolMaxContiguousCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolMediaPatrolEnabled"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolPDMEnabled"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolNumOfPhysicalDrives"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolNumOfVirtualDrives"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolNumOfDedicatedSpares"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolPhysicalDriveIDs"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolVirtualDriveIDs"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolDedicatedSpareIDs"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "poolWWN"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveAlias"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveSerialNo"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveWWN"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveOperationalStatus"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveCondition"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveOperation"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveSynchronized"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveRAIDLevel"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDrivePhysicalCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStoragePoolId"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveNumOfAxels"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveNumOfUsedPD"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveSectorSize"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDrivePreferredScmId"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveId"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsDataTransferred"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsReadDataTransferred"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsWriteDataTransferred"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfErrors"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfNonRWErrors"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfReadErrors"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfWriteErrors"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfIORequests"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfNonRWRequests"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfReadRequests"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsNumOfWriteRequests"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsStartTime"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "virtDriveStatsCollectionTime"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareIndex"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareOperationalStatus"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "sparePhysicalDriveId"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "sparePhysicalCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareConfigurableCapacity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareRevertible"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareType"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareNumOfAssociatedStoragePools"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareAssociatedStoragePoolIDs"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "spareDriveWWN"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "vdb2Lun"), ("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", "bl2vdVirtualDriveId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    storageGroup = storageGroup.setStatus('current')
mibBuilder.exportSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-STORAGE-MIB", poolMaxContiguousCapacity=poolMaxContiguousCapacity, poolNumOfPhysicalDrives=poolNumOfPhysicalDrives, virtDriveStatsWriteDataTransferred=virtDriveStatsWriteDataTransferred, poolMediaPatrolEnabled=poolMediaPatrolEnabled, interposerVendor=interposerVendor, virtDrivePreferredScmId=virtDrivePreferredScmId, sparePhysicalCapacity=sparePhysicalCapacity, virtDriveStatsNumOfNonRWRequests=virtDriveStatsNumOfNonRWRequests, interposer=interposer, storagePoolTable=storagePoolTable, virtDriveStatsNumOfIORequests=virtDriveStatsNumOfIORequests, spareIndex=spareIndex, poolVirtualDriveIDs=poolVirtualDriveIDs, virtDriveStatsCollectionTime=virtDriveStatsCollectionTime, virtDriveOperationalStatus=virtDriveOperationalStatus, spareDriveWWN=spareDriveWWN, bl2vdEntry=bl2vdEntry, storageInterConnectionType=storageInterConnectionType, virtDriveSerialNo=virtDriveSerialNo, spareRevertible=spareRevertible, virtDriveAlias=virtDriveAlias, virtDriveWWN=virtDriveWWN, interposerPart=interposerPart, virtDriveNumOfUsedPD=virtDriveNumOfUsedPD, virtDriveCondition=virtDriveCondition, poolWWN=poolWWN, poolCondition=poolCondition, interposerSerialNo=interposerSerialNo, poolDedicatedSpareIDs=poolDedicatedSpareIDs, virtDriveStatsNumOfErrors=virtDriveStatsNumOfErrors, virtDriveNumOfAxels=virtDriveNumOfAxels, virtDriveStatsNumOfReadErrors=virtDriveStatsNumOfReadErrors, spareDriveTable=spareDriveTable, interposerDeviceName=interposerDeviceName, virtualDriveStatsTable=virtualDriveStatsTable, interposerMaximumPower=interposerMaximumPower, poolPhysicalCapacity=poolPhysicalCapacity, storage=storage, poolNumOfDedicatedSpares=poolNumOfDedicatedSpares, vdb2lEntry=vdb2lEntry, virtDriveStatsNumOfReadRequests=virtDriveStatsNumOfReadRequests, virtDriveStatsDataTransferred=virtDriveStatsDataTransferred, interposerAssetTag=interposerAssetTag, poolOperationalStatus=poolOperationalStatus, multiFlexServerStorageMibModule=multiFlexServerStorageMibModule, spareAssociatedStoragePoolIDs=spareAssociatedStoragePoolIDs, spareType=spareType, storageGroup=storageGroup, spareNumOfAssociatedStoragePools=spareNumOfAssociatedStoragePools, PYSNMP_MODULE_ID=multiFlexServerStorageMibModule, virtDriveSectorSize=virtDriveSectorSize, virtDriveStoragePoolId=virtDriveStoragePoolId, poolAlias=poolAlias, spareOperationalStatus=spareOperationalStatus, virtDriveCapacity=virtDriveCapacity, interposerMfgDate=interposerMfgDate, bl2vdVirtualDriveId=bl2vdVirtualDriveId, poolPhysicalDriveIDs=poolPhysicalDriveIDs, storageWWN=storageWWN, virtDriveStatsStartTime=virtDriveStatsStartTime, virtDriveStatsNumOfWriteRequests=virtDriveStatsNumOfWriteRequests, interposerNominalPower=interposerNominalPower, poolOperation=poolOperation, virtDriveId=virtDriveId, storagePoolEntry=storagePoolEntry, spareConfigurableCapacity=spareConfigurableCapacity, poolFreeCapacity=poolFreeCapacity, virtDriveStatsNumOfNonRWErrors=virtDriveStatsNumOfNonRWErrors, virtDriveOperation=virtDriveOperation, virtDriveStatsNumOfWriteErrors=virtDriveStatsNumOfWriteErrors, virtualDriveEntry=virtualDriveEntry, virtDriveSynchronized=virtDriveSynchronized, poolPDMEnabled=poolPDMEnabled, sparePhysicalDriveId=sparePhysicalDriveId, virtDriveStatsReadDataTransferred=virtDriveStatsReadDataTransferred, virtualDriveTable=virtualDriveTable, poolIndex=poolIndex, virtDrivePhysicalCapacity=virtDrivePhysicalCapacity, bl2vdTable=bl2vdTable, poolConfigurableCapacity=poolConfigurableCapacity, vdb2lTable=vdb2lTable, poolNumOfVirtualDrives=poolNumOfVirtualDrives, vdb2Lun=vdb2Lun, virtDriveRAIDLevel=virtDriveRAIDLevel, virtualDriveStatsEntry=virtualDriveStatsEntry, spareDriveEntry=spareDriveEntry)