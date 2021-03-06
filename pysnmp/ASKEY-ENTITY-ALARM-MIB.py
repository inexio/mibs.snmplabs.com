#
# PySNMP MIB module ASKEY-ENTITY-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASKEY-ENTITY-ALARM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
AskeyVendorTypeEnum, ipDslam = mibBuilder.importSymbols("ASKEY-DSLAM-MIB", "AskeyVendorTypeEnum", "ipDslam")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32, IpAddress, TimeTicks, Counter32, MibIdentifier, iso, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32", "IpAddress", "TimeTicks", "Counter32", "MibIdentifier", "iso", "Counter64", "NotificationType")
DisplayString, TruthValue, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "AutonomousType")
askeyEntityAlarmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12))
askeyEntityAlarmMIB.setRevisions(('1904-11-22 15:41', '1904-10-13 14:00', '1904-08-10 16:10', '1904-08-10 10:10', '1904-07-30 14:10',))
if mibBuilder.loadTexts: askeyEntityAlarmMIB.setLastUpdated('0411221541Z')
if mibBuilder.loadTexts: askeyEntityAlarmMIB.setOrganization('Askey Computer Corp.')
class AskeyAlarmBit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 31)

class AskeyAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("info", 5), ("none", 99))

class AskeyAlarmName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class AskeyAlarmList(TextualConvention, Unsigned32):
    status = 'current'

class AskeyAlarmAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("set", 1), ("clear", 2))

askeyEntityAlarmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1))
askeyEntityAlarmMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2))
aeAlarmDefinition = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2))
aeAlarmMonitoring = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3))
aeAlarmHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4))
aeAlarmDefinitionTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1), )
if mibBuilder.loadTexts: aeAlarmDefinitionTable.setStatus('current')
aeAlarmDefinitionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefVendorTypeEnum"), (0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefType"))
if mibBuilder.loadTexts: aeAlarmDefinitionEntry.setStatus('current')
aeAlarmDefVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 1), AskeyVendorTypeEnum())
if mibBuilder.loadTexts: aeAlarmDefVendorTypeEnum.setStatus('current')
aeAlarmDefType = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 2), AskeyAlarmBit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmDefType.setStatus('current')
aeAlarmDefName = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 3), AskeyAlarmName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmDefName.setStatus('current')
aeAlarmDefDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmDefDescr.setStatus('current')
aeAlarmDefSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 5), AskeyAlarmSeverity().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeAlarmDefSeverity.setStatus('current')
aeAlarmDefFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 6), TruthValue().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeAlarmDefFiltered.setStatus('current')
aeAlarmDefSuppressedby = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 7), AskeyAlarmList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeAlarmDefSuppressedby.setStatus('current')
aeAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1), )
if mibBuilder.loadTexts: aeAlarmTable.setStatus('current')
aeAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmPhysicalIndex"))
if mibBuilder.loadTexts: aeAlarmEntry.setStatus('current')
aeAlarmPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmPhysicalIndex.setStatus('current')
aeAlarmPlannedVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 2), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmPlannedVendorTypeEnum.setStatus('current')
aeAlarmOnlineVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 3), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmOnlineVendorTypeEnum.setStatus('current')
aeAlarmList = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 4), AskeyAlarmList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmList.setStatus('current')
aeAlarmLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmLastChange.setStatus('current')
aeAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 6), AskeyAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeAlarmSeverity.setStatus('current')
aeHistoryAlarmTableSize = MibScalar((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmTableSize.setStatus('current')
aeHistoryAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2), )
if mibBuilder.loadTexts: aeHistoryAlarmTable.setStatus('current')
aeHistoryAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeHistoryAlarmIndex"))
if mibBuilder.loadTexts: aeHistoryAlarmEntry.setStatus('current')
aeHistoryAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2146483647)))
if mibBuilder.loadTexts: aeHistoryAlarmIndex.setStatus('current')
aeHistoryAlarmPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmPhysicalIndex.setStatus('current')
aeHistoryAlarmPlannedVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 3), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmPlannedVendorTypeEnum.setStatus('current')
aeHistoryAlarmOnlineVendorTypeEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 4), AskeyVendorTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmOnlineVendorTypeEnum.setStatus('current')
aeHistoryAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 5), AskeyAlarmBit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmType.setStatus('current')
aeHistoryAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmTime.setStatus('current')
aeHistoryAlarmAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 7), AskeyAlarmAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeHistoryAlarmAction.setStatus('current')
aeRelayInTable = MibTable((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5), )
if mibBuilder.loadTexts: aeRelayInTable.setStatus('current')
aeRelayInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1), ).setIndexNames((0, "ASKEY-ENTITY-ALARM-MIB", "aeRelayInPhysicalIndex"))
if mibBuilder.loadTexts: aeRelayInEntry.setStatus('current')
aeRelayInPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeRelayInPhysicalIndex.setStatus('current')
aeRelayInName = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeRelayInName.setStatus('current')
aeRelayInNormalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("close", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aeRelayInNormalStatus.setStatus('current')
aeRelayInCurrentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("open", 1), ("close", 2), ("disable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aeRelayInCurrentStatus.setStatus('current')
askeyEntityMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2, 0))
askeyEntityAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2, 0, 1)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPhysicalIndex"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPlannedVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmOnlineVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmList"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmLastChange"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmSeverity"))
if mibBuilder.loadTexts: askeyEntityAlarmTrap.setStatus('current')
askeyEntityAlarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3))
askeyEntityAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 1))
askeyEntityAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2))
askeyEntityAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 1, 1)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmDefinitionGroup"), ("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmMonitoringGroup"), ("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmCompliance = askeyEntityAlarmCompliance.setStatus('current')
askeyEntityAlarmDefinitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 2)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefType"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefName"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefDescr"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefSeverity"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefFiltered"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefSuppressedby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmDefinitionGroup = askeyEntityAlarmDefinitionGroup.setStatus('current')
askeyEntityAlarmMonitoringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 3)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPlannedVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmOnlineVendorTypeEnum"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmList"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmLastChange"), ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmMonitoringGroup = askeyEntityAlarmMonitoringGroup.setStatus('current')
askeyEntityAlarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 4)).setObjects(("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    askeyEntityAlarmNotificationsGroup = askeyEntityAlarmNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ASKEY-ENTITY-ALARM-MIB", aeAlarmDefinitionTable=aeAlarmDefinitionTable, askeyEntityAlarmCompliance=askeyEntityAlarmCompliance, aeAlarmDefDescr=aeAlarmDefDescr, askeyEntityAlarmMIBTraps=askeyEntityAlarmMIBTraps, aeRelayInTable=aeRelayInTable, aeHistoryAlarmAction=aeHistoryAlarmAction, askeyEntityAlarmConformance=askeyEntityAlarmConformance, aeHistoryAlarmPlannedVendorTypeEnum=aeHistoryAlarmPlannedVendorTypeEnum, aeAlarmDefinitionEntry=aeAlarmDefinitionEntry, aeAlarmLastChange=aeAlarmLastChange, aeAlarmDefSuppressedby=aeAlarmDefSuppressedby, aeRelayInName=aeRelayInName, aeRelayInNormalStatus=aeRelayInNormalStatus, aeAlarmSeverity=aeAlarmSeverity, askeyEntityAlarmGroups=askeyEntityAlarmGroups, aeHistoryAlarmEntry=aeHistoryAlarmEntry, aeHistoryAlarmOnlineVendorTypeEnum=aeHistoryAlarmOnlineVendorTypeEnum, aeAlarmPhysicalIndex=aeAlarmPhysicalIndex, aeRelayInCurrentStatus=aeRelayInCurrentStatus, askeyEntityAlarmMIB=askeyEntityAlarmMIB, aeAlarmDefinition=aeAlarmDefinition, aeRelayInPhysicalIndex=aeRelayInPhysicalIndex, aeHistoryAlarmTime=aeHistoryAlarmTime, AskeyAlarmList=AskeyAlarmList, aeHistoryAlarmIndex=aeHistoryAlarmIndex, AskeyAlarmBit=AskeyAlarmBit, aeAlarmDefSeverity=aeAlarmDefSeverity, aeHistoryAlarmTableSize=aeHistoryAlarmTableSize, askeyEntityAlarmCompliances=askeyEntityAlarmCompliances, aeAlarmList=aeAlarmList, aeHistoryAlarmType=aeHistoryAlarmType, AskeyAlarmName=AskeyAlarmName, AskeyAlarmSeverity=AskeyAlarmSeverity, askeyEntityAlarmDefinitionGroup=askeyEntityAlarmDefinitionGroup, AskeyAlarmAction=AskeyAlarmAction, aeRelayInEntry=aeRelayInEntry, askeyEntityAlarmTrap=askeyEntityAlarmTrap, askeyEntityAlarmMIBObjects=askeyEntityAlarmMIBObjects, aeAlarmMonitoring=aeAlarmMonitoring, askeyEntityAlarmMonitoringGroup=askeyEntityAlarmMonitoringGroup, askeyEntityAlarmNotificationsGroup=askeyEntityAlarmNotificationsGroup, aeAlarmDefVendorTypeEnum=aeAlarmDefVendorTypeEnum, aeAlarmDefName=aeAlarmDefName, askeyEntityMIBTrapPrefix=askeyEntityMIBTrapPrefix, aeAlarmHistory=aeAlarmHistory, aeAlarmDefType=aeAlarmDefType, aeHistoryAlarmPhysicalIndex=aeHistoryAlarmPhysicalIndex, aeHistoryAlarmTable=aeHistoryAlarmTable, PYSNMP_MODULE_ID=askeyEntityAlarmMIB, aeAlarmPlannedVendorTypeEnum=aeAlarmPlannedVendorTypeEnum, aeAlarmTable=aeAlarmTable, aeAlarmOnlineVendorTypeEnum=aeAlarmOnlineVendorTypeEnum, aeAlarmEntry=aeAlarmEntry, aeAlarmDefFiltered=aeAlarmDefFiltered)
