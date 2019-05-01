#
# PySNMP MIB module MITEL-SX2000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-SX2000-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
mitelConfCompliances, mitelGrpCs2000, mitelConfAgents, mitelAppCallServer, mitelIdCs2000Light = mibBuilder.importSymbols("MITEL-MIB", "mitelConfCompliances", "mitelGrpCs2000", "mitelConfAgents", "mitelAppCallServer", "mitelIdCs2000Light")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, TimeTicks, Counter64, Counter32, NotificationType, ObjectIdentity, IpAddress, Integer32, Gauge32, NotificationType, MibIdentifier, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "TimeTicks", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32", "Gauge32", "NotificationType", "MibIdentifier", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
mitelAppCs2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1))
class MitelCs2000AlarmLevelType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 1, 2, 3, 4))
    namedValues = NamedValues(("almNil", 1), ("almClear", 1), ("almMinor", 2), ("almMajor", 3), ("almCritical", 4))

mitelCs2000System = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 1))
mitelCs2000Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2))
mitelCs2000SysName = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000SysName.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000SysName.setDescription('The name of the call server.')
mitelCs2000AlmLevel = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 1), MitelCs2000AlarmLevelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000AlmLevel.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000AlmLevel.setDescription('The current overall alarm level for the call server.')
mitelCs2000AlmDetectDate = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000AlmDetectDate.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000AlmDetectDate.setDescription('Defines when the alarm was detected.')
mitelCs2000AlmNbrCategories = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000AlmNbrCategories.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000AlmNbrCategories.setDescription('Defines the number of associated entries in the categories table.')
mitelCs2000CategoryTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4), )
if mibBuilder.loadTexts: mitelCs2000CategoryTable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CategoryTable.setDescription('Table defining the alarm state for individual call server categories. There will be multiple categories for each call server. The number of rows in the table is determined by the total of the mitelCs2000AlmTblNbrCategories value.')
mitelCs2000CategoryTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1), ).setIndexNames((0, "MITEL-SX2000-MIB", "mitelCs2000CatTblIndex"))
if mibBuilder.loadTexts: mitelCs2000CategoryTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CategoryTableEntry.setDescription('A row defining a single category.')
mitelCs2000CatTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblIndex.setDescription('Differentiates the different category reports for the call server. The first category will have an index value of 1, the second will have 2, etc. up to the last category report. The highest possible index value is 100.')
mitelCs2000CatTblAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblAvailable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblAvailable.setDescription('The number of available resources of this type of category on this call server.')
mitelCs2000CatTblUnavailable = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblUnavailable.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblUnavailable.setDescription('The number of unavailable resources of this type of category on this call server.')
mitelCs2000CatTblLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 4), MitelCs2000AlarmLevelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblLevel.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblLevel.setDescription('Defines the alarm level for this category on this call server.')
mitelCs2000CatTblMinorThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblMinorThresh.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblMinorThresh.setDescription('The percentage unavailable threshold indicating a minor alarm on this call server category.')
mitelCs2000CatTblMajorThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblMajorThresh.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblMajorThresh.setDescription('The percentage unavailable threshold indicating a major alarm on this call server category.')
mitelCs2000CatTblCriticalThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblCriticalThresh.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblCriticalThresh.setDescription('The percentage unavailable threshold indicating a critical alarm on this call server category.')
mitelCs2000CatTblName = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 2, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelCs2000CatTblName.setStatus('mandatory')
if mibBuilder.loadTexts: mitelCs2000CatTblName.setDescription('The name of this resource category.')
mitelCs2000Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 1, 3))
mitelCs2000NotifAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1027, 1, 2, 2) + (0,201)).setObjects(("MITEL-SX2000-MIB", "mitelCs2000SysName"), ("MITEL-SX2000-MIB", "mitelCs2000AlmLevel"), ("MITEL-SX2000-MIB", "mitelCs2000AlmDetectDate"), ("MITEL-SX2000-MIB", "mitelCs2000AlmNbrCategories"))
if mibBuilder.loadTexts: mitelCs2000NotifAlarm.setDescription('This notification is generated whenever an alarm condition is detected or cleared. The manager is expected to retrieve the corresponding alarm and category table information.')
mitelComplCs2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 1, 4))
mitelGrpCs2000System = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3, 1))
mitelGrpCs2000Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3, 2))
mitelAgentCs2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 5, 3, 2))
mibBuilder.exportSymbols("MITEL-SX2000-MIB", mitelCs2000NotifAlarm=mitelCs2000NotifAlarm, mitelCs2000CatTblMajorThresh=mitelCs2000CatTblMajorThresh, mitelCs2000AlmLevel=mitelCs2000AlmLevel, mitelCs2000System=mitelCs2000System, mitelGrpCs2000System=mitelGrpCs2000System, mitelCs2000CatTblMinorThresh=mitelCs2000CatTblMinorThresh, mitelAppCs2000=mitelAppCs2000, mitelCs2000AlmNbrCategories=mitelCs2000AlmNbrCategories, mitelCs2000CategoryTableEntry=mitelCs2000CategoryTableEntry, mitelCs2000CatTblIndex=mitelCs2000CatTblIndex, mitelCs2000CatTblLevel=mitelCs2000CatTblLevel, mitelCs2000CatTblName=mitelCs2000CatTblName, mitelCs2000CategoryTable=mitelCs2000CategoryTable, MitelCs2000AlarmLevelType=MitelCs2000AlarmLevelType, mitelCs2000CatTblAvailable=mitelCs2000CatTblAvailable, mitelCs2000Alarms=mitelCs2000Alarms, mitelCs2000SysName=mitelCs2000SysName, mitelCs2000CatTblCriticalThresh=mitelCs2000CatTblCriticalThresh, mitelComplCs2000=mitelComplCs2000, mitelCs2000CatTblUnavailable=mitelCs2000CatTblUnavailable, mitelGrpCs2000Alarms=mitelGrpCs2000Alarms, mitelAgentCs2000=mitelAgentCs2000, mitelCs2000Notifications=mitelCs2000Notifications, mitelCs2000AlmDetectDate=mitelCs2000AlmDetectDate)
