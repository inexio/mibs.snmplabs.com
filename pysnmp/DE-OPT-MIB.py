#
# PySNMP MIB module DE-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DE-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, enterprises, Bits, iso, TimeTicks, ModuleIdentity, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, MibIdentifier, Counter32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "Bits", "iso", "TimeTicks", "ModuleIdentity", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "MibIdentifier", "Counter32", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatOtherStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
class DisplayString(OctetString):
    pass

cdx6500StatEncryption = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12))
statEncryptionGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1))
deDataEncryptionHardwareStatus = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deDataEncryptionHardwareStatus.setStatus('mandatory')
deMaxChannelAvailable = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deMaxChannelAvailable.setStatus('mandatory')
deMaxChannelConfigured = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deMaxChannelConfigured.setStatus('mandatory')
deChannelsInUse = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deChannelsInUse.setStatus('mandatory')
deMaxSimultaneousChannelsUsed = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deMaxSimultaneousChannelsUsed.setStatus('mandatory')
deCurrentEncryptionQueueLength = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deCurrentEncryptionQueueLength.setStatus('mandatory')
deMaxEncryptionQueueDepth = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deMaxEncryptionQueueDepth.setStatus('mandatory')
deTimeLastStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deTimeLastStatisticsReset.setStatus('mandatory')
deAlgorithmSupportedByHardwareStatus = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-simm", 1), ("des-40", 2), ("des-64", 3), ("des-128", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deAlgorithmSupportedByHardwareStatus.setStatus('mandatory')
statEncryptionChannelTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2), )
if mibBuilder.loadTexts: statEncryptionChannelTable.setStatus('mandatory')
statEncryptionChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1), ).setIndexNames((0, "DE-OPT-MIB", "deStatChannelNumber"))
if mibBuilder.loadTexts: statEncryptionChannelEntry.setStatus('mandatory')
deStatChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deStatChannelNumber.setStatus('mandatory')
deLastStatisticsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deLastStatisticsReset.setStatus('mandatory')
deChannelState = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonData", 1), ("data", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deChannelState.setStatus('mandatory')
deSourceChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deSourceChannel.setStatus('mandatory')
deDestinationChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deDestinationChannel.setStatus('mandatory')
deCorruptedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 12, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deCorruptedPackets.setStatus('mandatory')
cdx6500ControlsEncryption = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18))
ctrlEncryptionGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 1))
deCtrlEncryptionGeneral = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetStatistics", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: deCtrlEncryptionGeneral.setStatus('mandatory')
ctrlEncryptionChannelTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2), )
if mibBuilder.loadTexts: ctrlEncryptionChannelTable.setStatus('mandatory')
ctrlEncryptionChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2, 1), ).setIndexNames((0, "DE-OPT-MIB", "deCtrlChannelNumber"))
if mibBuilder.loadTexts: ctrlEncryptionChannelEntry.setStatus('mandatory')
deCtrlChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: deCtrlChannelNumber.setStatus('mandatory')
deCtrlEncryptionChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 18, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetStatistics", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: deCtrlEncryptionChannel.setStatus('mandatory')
mibBuilder.exportSymbols("DE-OPT-MIB", statEncryptionChannelEntry=statEncryptionChannelEntry, cdx6500StatOtherStatsGroup=cdx6500StatOtherStatsGroup, deChannelsInUse=deChannelsInUse, deCorruptedPackets=deCorruptedPackets, statEncryptionGeneral=statEncryptionGeneral, deStatChannelNumber=deStatChannelNumber, ctrlEncryptionChannelTable=ctrlEncryptionChannelTable, statEncryptionChannelTable=statEncryptionChannelTable, deDataEncryptionHardwareStatus=deDataEncryptionHardwareStatus, deCtrlChannelNumber=deCtrlChannelNumber, cdx6500Configuration=cdx6500Configuration, deDestinationChannel=deDestinationChannel, cdx6500StatEncryption=cdx6500StatEncryption, codex=codex, ctrlEncryptionGeneral=ctrlEncryptionGeneral, cdx6500Statistics=cdx6500Statistics, ctrlEncryptionChannelEntry=ctrlEncryptionChannelEntry, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, cdx6500Controls=cdx6500Controls, cdx6500=cdx6500, deMaxChannelAvailable=deMaxChannelAvailable, deMaxChannelConfigured=deMaxChannelConfigured, deSourceChannel=deSourceChannel, DisplayString=DisplayString, deMaxSimultaneousChannelsUsed=deMaxSimultaneousChannelsUsed, deCurrentEncryptionQueueLength=deCurrentEncryptionQueueLength, deLastStatisticsReset=deLastStatisticsReset, deMaxEncryptionQueueDepth=deMaxEncryptionQueueDepth, cdx6500ControlsEncryption=cdx6500ControlsEncryption, deCtrlEncryptionChannel=deCtrlEncryptionChannel, deAlgorithmSupportedByHardwareStatus=deAlgorithmSupportedByHardwareStatus, deCtrlEncryptionGeneral=deCtrlEncryptionGeneral, cdxProductSpecific=cdxProductSpecific, deTimeLastStatisticsReset=deTimeLastStatisticsReset, deChannelState=deChannelState)
