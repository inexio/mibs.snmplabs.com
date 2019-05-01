#
# PySNMP MIB module AILUXCONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AILUXCONNECT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
AIIConnType, = mibBuilder.importSymbols("AISYSTEM-MIB", "AIIConnType")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, ObjectIdentity, enterprises, Counter32, Bits, Unsigned32, Integer32, Gauge32, NotificationType, TimeTicks, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "ObjectIdentity", "enterprises", "Counter32", "Bits", "Unsigned32", "Integer32", "Gauge32", "NotificationType", "TimeTicks", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiLuxConnect = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 33))
aiLuxConnect.setRevisions(('2001-04-30 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aiLuxConnect.setRevisionsDescriptions(('The initial revision of this module.',))
if mibBuilder.loadTexts: aiLuxConnect.setLastUpdated('200104301700Z')
if mibBuilder.loadTexts: aiLuxConnect.setOrganization('Applied Innovation Inc.')
if mibBuilder.loadTexts: aiLuxConnect.setContactInfo(' Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email: snmp@aiinet.com')
if mibBuilder.loadTexts: aiLuxConnect.setDescription('MIB module for the AI LuxConnect.')
aiLCTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 33, 0))
aiLCTrapGtranSwitch = NotificationType((1, 3, 6, 1, 4, 1, 539, 33, 0, 1)).setObjects(("AILUXCONNECT-MIB", "aiLCGtranActiveIndex"), ("AILUXCONNECT-MIB", "aiLCGtranActiveSpan"))
if mibBuilder.loadTexts: aiLCTrapGtranSwitch.setStatus('current')
if mibBuilder.loadTexts: aiLCTrapGtranSwitch.setDescription('Trap sent when the GTRAN switches the fiber span utilized by the active laser.')
aiLCTrapGbicInserted = NotificationType((1, 3, 6, 1, 4, 1, 539, 33, 0, 2)).setObjects(("AILUXCONNECT-MIB", "aiLCGbicIndex"), ("AILUXCONNECT-MIB", "aiLCGbicConnectorType"))
if mibBuilder.loadTexts: aiLCTrapGbicInserted.setStatus('current')
if mibBuilder.loadTexts: aiLCTrapGbicInserted.setDescription('Trap sent when a Gigabit Ethernet Interface Converter is inserted.')
aiLCTrapGbicRemoved = NotificationType((1, 3, 6, 1, 4, 1, 539, 33, 0, 3)).setObjects(("AILUXCONNECT-MIB", "aiLCGbicIndex"), ("AILUXCONNECT-MIB", "aiLCGbicConnectorType"))
if mibBuilder.loadTexts: aiLCTrapGbicRemoved.setStatus('current')
if mibBuilder.loadTexts: aiLCTrapGbicRemoved.setDescription('Trap sent when a Gigabit Ethernet Interface Converter is removed.')
aiLCGtranActiveTable = MibTable((1, 3, 6, 1, 4, 1, 539, 33, 1), )
if mibBuilder.loadTexts: aiLCGtranActiveTable.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveTable.setDescription('Information on the active laser of the GTRAN module.')
aiLCGtranActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 33, 1, 1), ).setIndexNames((0, "AILUXCONNECT-MIB", "aiLCGtranActiveIndex"))
if mibBuilder.loadTexts: aiLCGtranActiveEntry.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveEntry.setDescription('Information on a given GTRAN active laser')
aiLCGtranActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranActiveIndex.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveIndex.setDescription('Index of this object in the current table. Since this table entry is an extension of the ifTable, this should object should have the same value as the corresponding ifIndex.')
aiLCGtranActiveBackupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranActiveBackupIndex.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveBackupIndex.setDescription('Index of the corresponding backup laser.')
aiLCGtranActiveSpan = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("work", 1), ("protect", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLCGtranActiveSpan.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveSpan.setDescription('Indicates which fiber span is currently being utilized by the actvie laser')
aiLCGtranActiveRxUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranActiveRxUtilization.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveRxUtilization.setDescription('Approximate percentage utilization of the fiber. This only accounts for incoming (received) packets.')
aiLCGtranActiveTxUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranActiveTxUtilization.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveTxUtilization.setDescription('Approximate percentage utilization of the fiber. This only accounts for outgoing (transmitted) packets.')
aiLCGtranActiveClockSlave = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLCGtranActiveClockSlave.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveClockSlave.setDescription('True if this laser is the clock slave.')
aiLCGtranActiveCoolerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLCGtranActiveCoolerStatus.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveCoolerStatus.setDescription('The state of the laser cooler. While the cooler can be disabled, this will render the laser ineffective. This object is primarily here for status purposes.')
aiLCGtranActiveTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("okay", 1), ("trouble", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranActiveTemperature.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveTemperature.setDescription('The GTRAN part is aware when it passes out of its operational temperature range. This object turns to trouble(2) as soon as we get such a report from the GTRAN.')
aiLCGtranActiveRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("okay", 1), ("under", 2), ("over", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranActiveRxPower.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveRxPower.setDescription('Input power level.')
aiLCGtranActiveTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("okay", 1), ("under", 2), ("over", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranActiveTxPower.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranActiveTxPower.setDescription('Output power level. The GTRAN will report under(2) if its self monitoring indicates that the laser is not transmitting at full power. over(3) is not currently used, but included for symmetry.')
aiLCGtranBackupTable = MibTable((1, 3, 6, 1, 4, 1, 539, 33, 2), )
if mibBuilder.loadTexts: aiLCGtranBackupTable.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranBackupTable.setDescription('')
aiLCGtranBackupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 33, 2, 1), ).setIndexNames((0, "AILUXCONNECT-MIB", "aiLCGtranBackupIndex"))
if mibBuilder.loadTexts: aiLCGtranBackupEntry.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranBackupEntry.setDescription('')
aiLCGtranBackupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranBackupIndex.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranBackupIndex.setDescription('Index of this object in the current table. Since this table entry is an extension of the ifTable, this should object should have the same value as the corresponding ifIndex.')
aiLCGtranBackupActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGtranBackupActiveIndex.setStatus('current')
if mibBuilder.loadTexts: aiLCGtranBackupActiveIndex.setDescription('Index of the corresponding active laser.')
aiLcGbicTable = MibTable((1, 3, 6, 1, 4, 1, 539, 33, 3), )
if mibBuilder.loadTexts: aiLcGbicTable.setStatus('current')
if mibBuilder.loadTexts: aiLcGbicTable.setDescription('Information on the GBIC interfaces')
aiLCGbicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 33, 3, 1), ).setIndexNames((0, "AILUXCONNECT-MIB", "aiLCGbicIndex"))
if mibBuilder.loadTexts: aiLCGbicEntry.setStatus('current')
if mibBuilder.loadTexts: aiLCGbicEntry.setDescription('Information on a given GBIC')
aiLCGbicIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGbicIndex.setStatus('current')
if mibBuilder.loadTexts: aiLCGbicIndex.setDescription('Index of this object in the current table. Since this table entry is an extension of the ifTable, this should object should have the same value as the corresponding ifIndex.')
aiLCGbicConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 2), AIIConnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGbicConnectorType.setStatus('current')
if mibBuilder.loadTexts: aiLCGbicConnectorType.setDescription('Type of connector in this GBIC slot.')
aiLCGbicTxMode = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("down", 1), ("up", 2), ("gtran", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiLCGbicTxMode.setStatus('current')
if mibBuilder.loadTexts: aiLCGbicTxMode.setDescription('The true administrative state of this interface. down(1) and up(2) carry the same semantics as ifAdminStatus. gtran(3) is used when this interface should only be operational if the gtran device is capable of passing packets. Note that the test status of the device is not truly orthogonal to this variable and is set separately. However, setting that variable may effect the state of this one.')
aiLCGbicRxUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGbicRxUtilization.setStatus('current')
if mibBuilder.loadTexts: aiLCGbicRxUtilization.setDescription('Approximate percentage utilization of the fiber. This only accounts for incoming (received) packets.')
aiLCGbicTxUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 33, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aiLCGbicTxUtilization.setStatus('current')
if mibBuilder.loadTexts: aiLCGbicTxUtilization.setDescription('Approximate percentage utilization of the fiber. This only accounts for outgoing (transmitted) packets.')
mibBuilder.exportSymbols("AILUXCONNECT-MIB", aiLuxConnect=aiLuxConnect, aiLCTrapInfo=aiLCTrapInfo, aiLcGbicTable=aiLcGbicTable, aiLCGtranBackupEntry=aiLCGtranBackupEntry, aiLCGtranBackupActiveIndex=aiLCGtranBackupActiveIndex, aiLCGbicRxUtilization=aiLCGbicRxUtilization, aiLCGtranActiveTxUtilization=aiLCGtranActiveTxUtilization, aiLCGtranActiveRxUtilization=aiLCGtranActiveRxUtilization, aiLCGtranActiveRxPower=aiLCGtranActiveRxPower, aii=aii, aiLCGtranActiveBackupIndex=aiLCGtranActiveBackupIndex, aiLCGtranActiveCoolerStatus=aiLCGtranActiveCoolerStatus, aiLCGtranActiveTxPower=aiLCGtranActiveTxPower, aiLCGbicConnectorType=aiLCGbicConnectorType, aiLCGtranActiveTable=aiLCGtranActiveTable, aiLCTrapGtranSwitch=aiLCTrapGtranSwitch, aiLCGtranBackupTable=aiLCGtranBackupTable, aiLCGbicTxMode=aiLCGbicTxMode, aiLCGbicEntry=aiLCGbicEntry, aiLCTrapGbicInserted=aiLCTrapGbicInserted, aiLCGtranActiveClockSlave=aiLCGtranActiveClockSlave, aiLCGtranBackupIndex=aiLCGtranBackupIndex, aiLCGtranActiveSpan=aiLCGtranActiveSpan, aiLCGbicTxUtilization=aiLCGbicTxUtilization, aiLCGtranActiveIndex=aiLCGtranActiveIndex, aiLCTrapGbicRemoved=aiLCTrapGbicRemoved, aiLCGtranActiveTemperature=aiLCGtranActiveTemperature, PYSNMP_MODULE_ID=aiLuxConnect, aiLCGtranActiveEntry=aiLCGtranActiveEntry, aiLCGbicIndex=aiLCGbicIndex)
