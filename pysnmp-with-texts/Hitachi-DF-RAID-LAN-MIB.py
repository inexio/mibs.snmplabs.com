#
# PySNMP MIB module Hitachi-DF-RAID-LAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Hitachi-DF-RAID-LAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, MibIdentifier, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Gauge32, iso, Bits, ObjectIdentity, Integer32, Counter32, TimeTicks, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibIdentifier", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Gauge32", "iso", "Bits", "ObjectIdentity", "Integer32", "Counter32", "TimeTicks", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hitachi = MibIdentifier((1, 3, 6, 1, 4, 1, 116))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3))
storage = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3, 11))
dfraid = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3, 11, 1))
dfraidLan = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2))
systemExMib = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5))
storageExMib = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11))
dfraidExMib = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1))
dfraidLanExMib = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2))
dfSystemParameter = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1))
dfWarningCondition = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2))
dfCommandExecutionCondition = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3))
dfCacheLoadCondition = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 4))
dfLUNS = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5))
dfPort = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6))
dfCommandExecutionInternalCondition = MibIdentifier((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7))
dfSystemProductName = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfSystemProductName.setStatus('mandatory')
if mibBuilder.loadTexts: dfSystemProductName.setDescription('The description of the product name. It is mandatory that this only contain printable ASCII characters.')
dfSystemMicroRevision = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfSystemMicroRevision.setStatus('mandatory')
if mibBuilder.loadTexts: dfSystemMicroRevision.setDescription('The software revision. It is mandatory that this only contain printable ASCII characters.')
dfSystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfSystemSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfSystemSerialNumber.setDescription('The serial number.')
dfRegressionStatus = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfRegressionStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dfRegressionStatus.setDescription('A value of regression status. Bit Comment 0 drive status. 1 spare drive status. 2 data drive status. 3 ENC status. 4-5 not used,always 0. 6 warning status. 7 Other controller status. 8 UPS status. 9 loop status. 10 path status. 11 NAS Server status. 12 NAS Path status. 13 NAS UPS status. 14-15 not used,always 0. 16 battery status. 17 power supply status. 18 AC status. 19 BK status. 20 fan status. 21-23 not used,always 0. 24 cache memory status. 25-31 not used,always 0. When the status is normal,each bit value is 0. When the status is abnormal,each bit value is 1. ')
dfPreventiveMaintenanceInformation = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPreventiveMaintenanceInformation.setStatus('mandatory')
if mibBuilder.loadTexts: dfPreventiveMaintenanceInformation.setDescription('The Preventive Maintenance Information .')
dfWarningReserve1 = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWarningReserve1.setStatus('mandatory')
if mibBuilder.loadTexts: dfWarningReserve1.setDescription('This is not used.')
dfWarningReserve2 = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWarningReserve2.setStatus('mandatory')
if mibBuilder.loadTexts: dfWarningReserve2.setDescription('This is not used.')
dfCommandTable = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1), )
if mibBuilder.loadTexts: dfCommandTable.setStatus('mandatory')
if mibBuilder.loadTexts: dfCommandTable.setDescription('The command execution conditon table.')
dfCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfLun"))
if mibBuilder.loadTexts: dfCommandEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfCommandEntry.setDescription('The command execution conditon table entry.')
dfLun = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfLun.setStatus('mandatory')
if mibBuilder.loadTexts: dfLun.setDescription('The logical unit number.')
dfReadCommandNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfReadCommandNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfReadCommandNumber.setDescription('The numbers of received read commands.')
dfReadHitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfReadHitNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfReadHitNumber.setDescription('The numbers of read hit commands.')
dfReadHitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfReadHitRate.setStatus('mandatory')
if mibBuilder.loadTexts: dfReadHitRate.setDescription('The read hit rate.')
dfWriteCommandNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWriteCommandNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfWriteCommandNumber.setDescription('The numbers of received write commands.')
dfWriteHitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWriteHitNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfWriteHitNumber.setDescription('The numbers of write hit commands.')
dfWriteHitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWriteHitRate.setStatus('mandatory')
if mibBuilder.loadTexts: dfWriteHitRate.setDescription('The write hit rate.')
dfWriteDataRate = MibScalar((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWriteDataRate.setStatus('mandatory')
if mibBuilder.loadTexts: dfWriteDataRate.setDescription('The write date rate in the cache memory.')
dfLUNSSwitch = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1), )
if mibBuilder.loadTexts: dfLUNSSwitch.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSSwitch.setDescription('LUN security switch.')
dfLUNSSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfSwitchSerialNumber"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfSwitchPortID"))
if mibBuilder.loadTexts: dfLUNSSwitchEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSSwitchEntry.setDescription('Entry of LUN security switch.')
dfSwitchSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfSwitchSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfSwitchSerialNumber.setDescription('Serial Number of the DF.')
dfSwitchPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfSwitchPortID.setStatus('mandatory')
if mibBuilder.loadTexts: dfSwitchPortID.setDescription('Port ID of the DF.')
dfSwitchOnOff = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfSwitchOnOff.setStatus('mandatory')
if mibBuilder.loadTexts: dfSwitchOnOff.setDescription('Functional switch. Value Mean 0 off (LUN Security unused) 1 on (Use LUN Security) ')
dfSwitchControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfSwitchControlStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dfSwitchControlStatus.setDescription('Control flag. Value Mean 1 Return value. ')
dfLUNSWWN = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2), )
if mibBuilder.loadTexts: dfLUNSWWN.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSWWN.setDescription('WWN information.')
dfLUNSWWNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNSerialNumber"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNPortID"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNControlIndex"))
if mibBuilder.loadTexts: dfLUNSWWNEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSWWNEntry.setDescription('Entry of WWN information.')
dfWWNSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNSerialNumber.setDescription('Serial number of the DF.')
dfWWNPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNPortID.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNPortID.setDescription('Port ID of the DF.')
dfWWNControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNControlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNControlIndex.setDescription('Index for WWN control.')
dfWWNWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNWWN.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNWWN.setDescription('WWN. (World Wide Name)')
dfWWNID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNID.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNID.setDescription('ID of the WWN.')
dfWWNNickname = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNNickname.setStatus('deprecated')
if mibBuilder.loadTexts: dfWWNNickname.setDescription('Nickname of the WWN.')
dfWWNUseNickname = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNUseNickname.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNUseNickname.setDescription('Using of nickname. Valus Mean 0 Nickname Unused. ')
dfWWNControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfWWNControlStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNControlStatus.setDescription('Control flag. Value Mean 1 Return value. ')
dfLUNSWWNGroup = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3), )
if mibBuilder.loadTexts: dfLUNSWWNGroup.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSWWNGroup.setDescription('WWN group information.')
dfLUNSWWNGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNGroupSerialNumber"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNGroupPortID"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfWWNGroupControlIndex"))
if mibBuilder.loadTexts: dfLUNSWWNGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSWWNGroupEntry.setDescription('Entry of WWN group information.')
dfWWNGroupSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: dfWWNGroupSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNGroupSerialNumber.setDescription('Serial number of the DF.')
dfWWNGroupPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: dfWWNGroupPortID.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNGroupPortID.setDescription('Port ID of the DF.')
dfWWNGroupControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: dfWWNGroupControlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNGroupControlIndex.setDescription('Index for WWN group control.')
dfWWNGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 4), Integer32())
if mibBuilder.loadTexts: dfWWNGroupID.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNGroupID.setDescription('ID of the WWN.')
dfWWNGroupNickname = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8)))
if mibBuilder.loadTexts: dfWWNGroupNickname.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNGroupNickname.setDescription('Nickname of the WWN group.')
dfWWNGroupedWWNs = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2)))
if mibBuilder.loadTexts: dfWWNGroupedWWNs.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNGroupedWWNs.setDescription('Grouped WWNs. It is shown whether the bit at the position corresponding to WWNID belongs to the group. Value Mean 0 Does not belong. 1 Belongs. ')
dfWWNGroupControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 3, 1, 7), Integer32())
if mibBuilder.loadTexts: dfWWNGroupControlStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dfWWNGroupControlStatus.setDescription('Control flag. Value Mean 1 Return value. 2 Add request. 3 Delete request. 4 Set request. ')
dfLUNSLUN = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4), )
if mibBuilder.loadTexts: dfLUNSLUN.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSLUN.setDescription('LUN information.')
dfLUNSLUNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNSerialNumber"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNPortID"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNLUN"))
if mibBuilder.loadTexts: dfLUNSLUNEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSLUNEntry.setDescription('Entry of LUN information.')
dfLUNSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfLUNSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSerialNumber.setDescription('Serial number of the DF.')
dfLUNPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfLUNPortID.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNPortID.setDescription('Port ID of the DF.')
dfLUNLUN = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfLUNLUN.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNLUN.setDescription('LUN of the Port.')
dfLUNWWNSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfLUNWWNSecurity.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNWWNSecurity.setDescription('WWN security setting. The bit at the position corresponding to WWNID shows the state of the access permittee. Value Mean 0 Does not accessible. 1 Accessible. ')
dfLUNWWNGroupSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfLUNWWNGroupSecurity.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNWWNGroupSecurity.setDescription('WWN group Security setting. The bit at the position corresponding to WWNID group shows the state of the access permittee. Value Mean 0 Does not accessible. ')
dfLUNControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfLUNControlStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNControlStatus.setDescription('Control flag. Value Mean 1 Return value. ')
dfLUNSLUNGroup = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5), )
if mibBuilder.loadTexts: dfLUNSLUNGroup.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSLUNGroup.setDescription('LUN group information.')
dfLUNSLUNGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNGroupSerialNumber"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNGroupPortID"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfLUNGroupControlIndex"))
if mibBuilder.loadTexts: dfLUNSLUNGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNSLUNGroupEntry.setDescription('Entry of LUN group information.')
dfLUNGroupSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: dfLUNGroupSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupSerialNumber.setDescription('Serial number of the DF.')
dfLUNGroupPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: dfLUNGroupPortID.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupPortID.setDescription('Port ID of the DF.')
dfLUNGroupControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: dfLUNGroupControlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupControlIndex.setDescription('Index for LUN group control.')
dfLUNGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 4), Integer32())
if mibBuilder.loadTexts: dfLUNGroupID.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupID.setDescription('ID of the WWN group.')
dfLUNGroupNickname = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8)))
if mibBuilder.loadTexts: dfLUNGroupNickname.setStatus('deprecated')
if mibBuilder.loadTexts: dfLUNGroupNickname.setDescription('Nickname of the LUN group.')
dfLUNGroupedLUNs = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15)))
if mibBuilder.loadTexts: dfLUNGroupedLUNs.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupedLUNs.setDescription('Grouped LUNs. It is shown whether the bit at the position corresponding to LUN belongs to the group. (0:does not belong 1:belongs) Value Mean 0 Does not belong. 1 Belongs. ')
dfLUNGroupWWNSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2)))
if mibBuilder.loadTexts: dfLUNGroupWWNSecurity.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupWWNSecurity.setDescription('WWN Security setting. The bit at the position corresponding to WWNID shows the state of the access permittee. Value Mean 0 Does not accessible. 1 Accessible. ')
dfLUNGroupWWNGroupSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1)))
if mibBuilder.loadTexts: dfLUNGroupWWNGroupSecurity.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupWWNGroupSecurity.setDescription('WWN group Security setting. The bit at the position corresponding to WWNID group shows the state of the access permittee. Value Mean 0 Does not accessible. 1 Accessible. ')
dfLUNGroupControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 5, 5, 1, 9), Integer32())
if mibBuilder.loadTexts: dfLUNGroupControlStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dfLUNGroupControlStatus.setDescription('Control flag. Value Mean 1 Return value. 2 Add request. 3 Delete request. 4 Set request. ')
dfPortinf = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1), )
if mibBuilder.loadTexts: dfPortinf.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortinf.setDescription('Port information.')
dfPortinfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfPortSerialNumber"), (0, "Hitachi-DF-RAID-LAN-MIB", "dfPortID"))
if mibBuilder.loadTexts: dfPortinfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortinfEntry.setDescription('Entry of port information.')
dfPortSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortSerialNumber.setDescription('Serial Number of the DF.')
dfPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortID.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortID.setDescription('Port ID.')
dfPortKind = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortKind.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortKind.setDescription('Kind of port. Value Mean SCSI SCSI port. Fibre Fibre port. ')
dfPortHostMode = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortHostMode.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortHostMode.setDescription('Host mode of the port. Upper 4 bits. - Each bit has the meaning. Bit Mean 0 Not used. (For reservation. Always 0.) 1 Not used. (For reservation. Always 0.) 2 Not used. (For reservation. Always 0.) 3 Ultra-SCSI mode. Lower 4 bits. - Numerical value shown by four bits. Value Mean 0 Normal setting. 1 IBM-7135 mode. 2 NCR mode. 3 Not usesd. (Reserved) 4 Sequent mode. 5 DEC OPEN VMS mode. 6 UNISYS-NX mode 7 UNISYS-IX mode. 8 HP mode. 9 VxVM-DMP mode. 10 Not used. (Reserved) 11 MPE mode. other Not used. (Reserved) Note: The following value has a special meaning. Value Mean 0xFF Out of the host mode setting object. ')
dfPortFibreAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortFibreAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortFibreAddress.setDescription('Fibre address. Value & Mean - describes by the format of Value(Address). 1:(EF) 17:(CD) 33:(B2) 49:(98) 65:(72) 81:(55) 97:(3A) 113:(25) 2:(E8) 18:(CC) 34:(B1) 50:(97) 66:(71) 82:(54) 98:(39) 114:(23) 3:(E4) 19:(CB) 35:(AE) 51:(90) 67:(6E) 83:(53) 99:(36) 115:(1F) 4:(E2) 20:(CA) 36:(AD) 52:(8F) 68:(6D) 84:(52) 100:(35) 116:(1E) 5:(E1) 21:(C9) 37:(AC) 53:(88) 69:(6C) 85:(51) 101:(34) 117:(1D) 6:(E0) 22:(C7) 38:(AB) 54:(84) 70:(6B) 86:(4E) 102:(33) 118:(1B) 7:(DC) 23:(C6) 39:(AA) 55:(82) 71:(6A) 87:(4D) 103:(32) 119:(18) 8:(DA) 24:(C5) 40:(A9) 56:(81) 72:(69) 88:(4C) 104:(31) 120:(17) 9:(D9) 25:(C3) 41:(A7) 57:(80) 73:(67) 89:(4B) 105:(2E) 121:(10) 10:(D6) 26:(BC) 42:(A6) 58:(7C) 74:(66) 90:(4A) 106:(2D) 122:(0F) 11:(D5) 27:(BA) 43:(A5) 59:(7A) 75:(65) 91:(49) 107:(2C) 123:(08) 12:(D4) 28:(B9) 44:(A3) 60:(79) 76:(63) 92:(47) 108:(2B) 124:(04) 13:(D3) 29:(B6) 45:(9F) 61:(76) 77:(5C) 93:(46) 109:(2A) 125:(02) 14:(D2) 30:(B5) 46:(9E) 62:(75) 78:(5A) 94:(45) 110:(29) 126:(01) 15:(D1) 31:(B4) 47:(9D) 63:(74) 79:(59) 95:(43) 111:(27) 16:(CE) 32:(B3) 48:(9B) 64:(73) 80:(56) 96:(3C) 112:(26) Note: The following value has a special meaning. Value Mean 0 Out of the Fibre address setting object. ')
dfPortFibreTopology = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortFibreTopology.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortFibreTopology.setDescription('Toplogy information. Value Mean 1 Fabric(on)&FCAL 2 Fabric(off)&FCAL 3 Fabric(on)&PointToPoint 4 Fabric(off)&PointToPoint 5 Not Fibre ')
dfPortControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortControlStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortControlStatus.setDescription('Control flag. Value Mean 1 Return value. ')
dfPortDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortDisplayName.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortDisplayName.setDescription('Display name of the port.')
dfPortWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 6, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfPortWWN.setStatus('mandatory')
if mibBuilder.loadTexts: dfPortWWN.setDescription('WWN of the port.')
dfCommandInternalTable = MibTable((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1), )
if mibBuilder.loadTexts: dfCommandInternalTable.setStatus('mandatory')
if mibBuilder.loadTexts: dfCommandInternalTable.setDescription('The internal command execution conditon table.')
dfCommandInternalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1), ).setIndexNames((0, "Hitachi-DF-RAID-LAN-MIB", "dfInternalLun"))
if mibBuilder.loadTexts: dfCommandInternalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dfCommandInternalEntry.setDescription('The internal command execution conditon table entry.')
dfInternalLun = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfInternalLun.setStatus('mandatory')
if mibBuilder.loadTexts: dfInternalLun.setDescription('The internal logical unit number.')
dfInternalReadCommandNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfInternalReadCommandNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfInternalReadCommandNumber.setDescription('The numbers of received read commands to the internal LUN.')
dfInternalReadHitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfInternalReadHitNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfInternalReadHitNumber.setDescription('The numbers of read hit commands to the internal LUN.')
dfInternalReadHitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfInternalReadHitRate.setStatus('mandatory')
if mibBuilder.loadTexts: dfInternalReadHitRate.setDescription('The read hit rate to the internal LUN.')
dfInternalWriteCommandNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfInternalWriteCommandNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfInternalWriteCommandNumber.setDescription('The numbers of received write commands to the internal LUN.')
dfInternalWriteHitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfInternalWriteHitNumber.setStatus('mandatory')
if mibBuilder.loadTexts: dfInternalWriteHitNumber.setDescription('The numbers of write hit commands to the internal LUN.')
dfInternalWriteHitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 116, 5, 11, 1, 2, 7, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dfInternalWriteHitRate.setStatus('mandatory')
if mibBuilder.loadTexts: dfInternalWriteHitRate.setDescription('The write hit rate to the internal LUN.')
systemDown = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,1))
if mibBuilder.loadTexts: systemDown.setDescription('System down occurred.')
driveFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,2))
if mibBuilder.loadTexts: driveFailure.setDescription('Drive blocking occurred.')
fanFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,3))
if mibBuilder.loadTexts: fanFailure.setDescription('Fan failure occurred.')
powerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,4))
if mibBuilder.loadTexts: powerSupplyFailure.setDescription('Power supply failure occurred.')
batteryFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,5))
if mibBuilder.loadTexts: batteryFailure.setDescription('Battery failure occurred.')
cacheFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,6))
if mibBuilder.loadTexts: cacheFailure.setDescription('Cache memory failure occurred.')
upsFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,7))
if mibBuilder.loadTexts: upsFailure.setDescription('UPS failure occurred.')
inboxFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,8))
if mibBuilder.loadTexts: inboxFailure.setDescription('AC line or inbox failure occurred.')
backupCircuitFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,9))
if mibBuilder.loadTexts: backupCircuitFailure.setDescription('Cache backup circuit failure occurred.')
otherControllerFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,10))
if mibBuilder.loadTexts: otherControllerFailure.setDescription('Other controller failure occurred.')
warning = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,11))
if mibBuilder.loadTexts: warning.setDescription('Warning occurred.')
spareDriveFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,12))
if mibBuilder.loadTexts: spareDriveFailure.setDescription('Spare drive failure occurred.')
microprogramReplacementExecuted = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,13))
if mibBuilder.loadTexts: microprogramReplacementExecuted.setDescription('Microprogram Replacement Executed.')
encFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,14))
if mibBuilder.loadTexts: encFailure.setDescription('Enclosure controller failure occurred.')
loopFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,15))
if mibBuilder.loadTexts: loopFailure.setDescription('Loop failure occurred.')
pathFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,16))
if mibBuilder.loadTexts: pathFailure.setDescription('Path failure occurred.')
drivePreMainte = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,21))
if mibBuilder.loadTexts: drivePreMainte.setDescription('The count has exceeded the drive preventive maintenance threshold.')
nasServerFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,200))
if mibBuilder.loadTexts: nasServerFailure.setDescription('NAS Server failure occurred.')
nasPathFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,201))
if mibBuilder.loadTexts: nasPathFailure.setDescription('NAS Path failure occurred.')
nasUpsFailure = NotificationType((1, 3, 6, 1, 4, 1, 116, 3, 11, 1, 2) + (0,202))
if mibBuilder.loadTexts: nasUpsFailure.setDescription('NAS UPS failure occurred.')
mibBuilder.exportSymbols("Hitachi-DF-RAID-LAN-MIB", dfPortDisplayName=dfPortDisplayName, dfInternalLun=dfInternalLun, drivePreMainte=drivePreMainte, dfPort=dfPort, dfLUNLUN=dfLUNLUN, dfInternalReadCommandNumber=dfInternalReadCommandNumber, dfLUNWWNSecurity=dfLUNWWNSecurity, inboxFailure=inboxFailure, storageExMib=storageExMib, systemExMib=systemExMib, dfInternalWriteHitNumber=dfInternalWriteHitNumber, dfLUNGroupedLUNs=dfLUNGroupedLUNs, hitachi=hitachi, microprogramReplacementExecuted=microprogramReplacementExecuted, dfLUNGroupControlIndex=dfLUNGroupControlIndex, dfPortWWN=dfPortWWN, spareDriveFailure=spareDriveFailure, dfraidExMib=dfraidExMib, dfLUNGroupWWNSecurity=dfLUNGroupWWNSecurity, dfWWNGroupPortID=dfWWNGroupPortID, dfRegressionStatus=dfRegressionStatus, dfLUNSLUNGroup=dfLUNSLUNGroup, loopFailure=loopFailure, dfWWNSerialNumber=dfWWNSerialNumber, dfCacheLoadCondition=dfCacheLoadCondition, backupCircuitFailure=backupCircuitFailure, dfWWNUseNickname=dfWWNUseNickname, dfSwitchPortID=dfSwitchPortID, dfPortFibreAddress=dfPortFibreAddress, nasUpsFailure=nasUpsFailure, dfPortKind=dfPortKind, dfWWNControlStatus=dfWWNControlStatus, dfLUNGroupNickname=dfLUNGroupNickname, driveFailure=driveFailure, dfPortinf=dfPortinf, dfWWNWWN=dfWWNWWN, dfWarningReserve2=dfWarningReserve2, dfWWNPortID=dfWWNPortID, warning=warning, dfLUNGroupPortID=dfLUNGroupPortID, dfSwitchOnOff=dfSwitchOnOff, dfSystemMicroRevision=dfSystemMicroRevision, dfWriteDataRate=dfWriteDataRate, dfSwitchSerialNumber=dfSwitchSerialNumber, dfLUNSerialNumber=dfLUNSerialNumber, dfWWNGroupNickname=dfWWNGroupNickname, dfSwitchControlStatus=dfSwitchControlStatus, dfPortHostMode=dfPortHostMode, dfInternalReadHitNumber=dfInternalReadHitNumber, dfPortinfEntry=dfPortinfEntry, dfPortID=dfPortID, dfWWNGroupControlIndex=dfWWNGroupControlIndex, dfSystemProductName=dfSystemProductName, dfWWNNickname=dfWWNNickname, dfCommandExecutionInternalCondition=dfCommandExecutionInternalCondition, dfWWNGroupID=dfWWNGroupID, dfWriteCommandNumber=dfWriteCommandNumber, dfraid=dfraid, otherControllerFailure=otherControllerFailure, dfWarningReserve1=dfWarningReserve1, dfWWNID=dfWWNID, dfLUNSSwitch=dfLUNSSwitch, dfLUNSWWNGroup=dfLUNSWWNGroup, dfLUNSLUNGroupEntry=dfLUNSLUNGroupEntry, dfLUNSLUNEntry=dfLUNSLUNEntry, upsFailure=upsFailure, dfReadHitRate=dfReadHitRate, pathFailure=pathFailure, dfInternalWriteCommandNumber=dfInternalWriteCommandNumber, dfPreventiveMaintenanceInformation=dfPreventiveMaintenanceInformation, nasServerFailure=nasServerFailure, storage=storage, dfLun=dfLun, dfLUNGroupWWNGroupSecurity=dfLUNGroupWWNGroupSecurity, cacheFailure=cacheFailure, system=system, dfPortControlStatus=dfPortControlStatus, dfWarningCondition=dfWarningCondition, dfLUNSWWNEntry=dfLUNSWWNEntry, dfLUNControlStatus=dfLUNControlStatus, dfInternalWriteHitRate=dfInternalWriteHitRate, dfCommandEntry=dfCommandEntry, dfLUNGroupID=dfLUNGroupID, dfSystemParameter=dfSystemParameter, dfSystemSerialNumber=dfSystemSerialNumber, dfWriteHitRate=dfWriteHitRate, dfPortSerialNumber=dfPortSerialNumber, dfLUNPortID=dfLUNPortID, dfraidLanExMib=dfraidLanExMib, dfLUNSWWNGroupEntry=dfLUNSWWNGroupEntry, systemDown=systemDown, batteryFailure=batteryFailure, dfraidLan=dfraidLan, dfLUNSLUN=dfLUNSLUN, dfLUNSSwitchEntry=dfLUNSSwitchEntry, dfCommandTable=dfCommandTable, dfLUNSWWN=dfLUNSWWN, dfWWNGroupControlStatus=dfWWNGroupControlStatus, dfLUNS=dfLUNS, dfInternalReadHitRate=dfInternalReadHitRate, dfPortFibreTopology=dfPortFibreTopology, powerSupplyFailure=powerSupplyFailure, dfReadHitNumber=dfReadHitNumber, dfCommandInternalEntry=dfCommandInternalEntry, dfReadCommandNumber=dfReadCommandNumber, dfWWNGroupSerialNumber=dfWWNGroupSerialNumber, dfLUNGroupSerialNumber=dfLUNGroupSerialNumber, encFailure=encFailure, dfWriteHitNumber=dfWriteHitNumber, nasPathFailure=nasPathFailure, fanFailure=fanFailure, dfCommandInternalTable=dfCommandInternalTable, dfWWNGroupedWWNs=dfWWNGroupedWWNs, dfCommandExecutionCondition=dfCommandExecutionCondition, dfWWNControlIndex=dfWWNControlIndex, dfLUNWWNGroupSecurity=dfLUNWWNGroupSecurity, dfLUNGroupControlStatus=dfLUNGroupControlStatus)
