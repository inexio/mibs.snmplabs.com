#
# PySNMP MIB module ACD-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACD-ALARM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:12:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, IpAddress, Counter32, Gauge32, ObjectIdentity, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime", "TruthValue")
acdAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 1))
acdAlarm.setRevisions(('2011-10-10 01:00', '2010-11-10 01:00', '2009-02-04 01:00', '2008-02-01 01:00', '2007-05-22 01:00', '2006-12-19 01:00', '2006-08-06 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acdAlarm.setRevisionsDescriptions(('Add acdAlarmCfgTableLastChangeTid and acdAlarmStatusTableLastChangeTid.', 'Fix compliance section.', 'Add new fields in acdAlarmCfgEntry, acdAlarmActiveState and acdAlarmClearState.', 'Add UNITS clause to object, where appropriate.', 'Add acdAlarmCfgNumber object to Alarm traps.', 'Add 802.3AH notification enable and msg field in status table.', 'Initial version of MIB module ACD-ALARM-MIB.',))
if mibBuilder.loadTexts: acdAlarm.setLastUpdated('201110100100Z')
if mibBuilder.loadTexts: acdAlarm.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: acdAlarm.setContactInfo('Accedian Technical Assistance Center Accedian Networks, Inc. 4878 Levy, suite 202 Saint-Laurent, Quebec Canada H4R 2P1 E-mail: support@accedian.com')
if mibBuilder.loadTexts: acdAlarm.setDescription('The alarm Table for this Accedian Networks device.')
acdAlarmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15))
acdAlarmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 1))
acdAlarmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 2))
acdAlarmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3))
acdAlarmTableTid = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 4))
acdAlarmGenThreshOn = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(500, 50000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmGenThreshOn.setStatus('current')
if mibBuilder.loadTexts: acdAlarmGenThreshOn.setDescription('This value represents the Alarm On Hysteris. This is the time since the detection of the On event inside the system versus the report. This is to avoid storm of notifications.')
acdAlarmGenThreshOff = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(500, 50000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmGenThreshOff.setStatus('current')
if mibBuilder.loadTexts: acdAlarmGenThreshOff.setDescription('This value represents the Alarm Off Hysteris. This is the time since the detection of the Off event inside the system versus the report. This is to avoid storm of notifications.')
acdAlarmGenLedEnable = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmGenLedEnable.setStatus('current')
if mibBuilder.loadTexts: acdAlarmGenLedEnable.setDescription('This is to Enable the alarms reporting through the LEDs.')
acdAlarmGenSyslogEnable = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmGenSyslogEnable.setStatus('current')
if mibBuilder.loadTexts: acdAlarmGenSyslogEnable.setDescription('This is to Enable the alarms reporting through the syslog system.')
acdAlarmGenSNMPEnable = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmGenSNMPEnable.setStatus('current')
if mibBuilder.loadTexts: acdAlarmGenSNMPEnable.setDescription('This is to Enable the alarms reporting through the SNMP agent.')
acdAlarmGen8023AHEnable = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmGen8023AHEnable.setStatus('current')
if mibBuilder.loadTexts: acdAlarmGen8023AHEnable.setDescription('This is to Enable the alarms reporting through the 802.3AH protocol.')
acdAlarmCfgTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10), )
if mibBuilder.loadTexts: acdAlarmCfgTable.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgTable.setDescription('Table of all alarms.')
acdAlarmCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1), ).setIndexNames((0, "ACD-ALARM-MIB", "acdAlarmCfgID"))
if mibBuilder.loadTexts: acdAlarmCfgEntry.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgEntry.setDescription('An alarm is an exceptional event that requires user notificaton.')
acdAlarmCfgID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmCfgID.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgID.setDescription('Unique value for each alarm. Its value ranges from 1 to MAXINT (4 bytes). ')
acdAlarmCfgNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmCfgNumber.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgNumber.setDescription('Unique number that identifies this alarm. Assigned by the unit. The alarm identifier is compose of 3 fields, the module number, the instance number and the error number. The alarm number looks like this: A.BBB.CC and is expressed in decimal, A is the module number, BBB is the instance number (1-999) and CC is the error number (1-99). A module number is assigned for each source of alarm in the system. For example the port module is set to 1, the SFP module is set to 2, the PAA is set to 3 and the environmental is set to 8.')
acdAlarmCfgDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmCfgDesc.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgDesc.setDescription('This string is to describe the alarm in a readable way, e.g.: +5Vdc Power supply fail.')
acdAlarmCfgEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmCfgEnable.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgEnable.setDescription('This is to indicate if the alarm is reported or not.')
acdAlarmCfgSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("info", 0), ("minor", 1), ("major", 2), ("critical", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmCfgSeverity.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgSeverity.setDescription('Accedian Networks classifies alarms into four severity types. These types and their associated decimal codes are, informational(0), minor(1), major(2) and critical(3).')
acdAlarmCfgServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdAlarmCfgServiceAffecting.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgServiceAffecting.setDescription('This is to indicate if the alarm is service affecting or not. This value depends on the utilization of the box. For instance in an application where the monitoring of the traffic is mandatory the link down event on the monitor port is service affecting.')
acdAlarmCfgExtNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmCfgExtNumber.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgExtNumber.setDescription('Unique number that identifies this alarm. Assigned by the unit. The alarm identifier is compose of 3 fields, the module number, the instance number and the error number. The alarm number looks like this: A.B.C and is expressed in decimal, A is the module number, B is the instance number and C is the error number. A module number is assigned for each source of alarm in the system (see Accedian documentation for more detail).')
acdAlarmCfgConditionType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmCfgConditionType.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgConditionType.setDescription('This is the type of alarm condition.')
acdAlarmCfgAMOType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmCfgAMOType.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgAMOType.setDescription('This is the Alarm Maintenance Object.')
acdAlarmStatusTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 1, 11), )
if mibBuilder.loadTexts: acdAlarmStatusTable.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusTable.setDescription('Table of all alarms')
acdAlarmStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1), ).setIndexNames((0, "ACD-ALARM-MIB", "acdAlarmStatusID"))
if mibBuilder.loadTexts: acdAlarmStatusEntry.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusEntry.setDescription('An alarm is an exceptional event that requires user notificaton.')
acdAlarmStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmStatusID.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusID.setDescription('Unique value for each alarm. Its value ranges from 1 to MAXINT (4 bytes). ')
acdAlarmStatusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmStatusNumber.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusNumber.setDescription('Unique number that identifies this alarm. Assigned by the unit. The alarm identifier is compose of 3 fields, the module number, the instance number and the error number. The alarm number looks like this: AAA.BBB.CC and is expressed in decimal, AAA is the module number, BBB is the instance number (1-999) and CC is the error number (1-99). A module number is assigned for each source of alarm in the system. For example the port module is set to 1, the SFP module is set to 2, the PAA is set to 3 and the environmental is set to 8.')
acdAlarmStatusOn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmStatusOn.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusOn.setDescription('This is to indicate if the alarm is On or Off.')
acdAlarmStatusLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmStatusLastChange.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusLastChange.setDescription('This is the time of the last change for this alarm. A value of zero means that nothing happened to this alarm since the last reboot.')
acdAlarmStatusMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmStatusMsg.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusMsg.setDescription('This string is to add information why the alarm is reported.')
acdAlarmV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 12))
acdAlarmActiveState = NotificationType((1, 3, 6, 1, 4, 1, 22420, 2, 1, 12, 1)).setObjects(("ACD-ALARM-MIB", "acdAlarmCfgID"), ("ACD-ALARM-MIB", "acdAlarmCfgNumber"), ("ACD-ALARM-MIB", "acdAlarmCfgSeverity"), ("ACD-ALARM-MIB", "acdAlarmCfgServiceAffecting"), ("ACD-ALARM-MIB", "acdAlarmCfgDesc"), ("ACD-ALARM-MIB", "acdAlarmStatusLastChange"), ("ACD-ALARM-MIB", "acdAlarmCfgExtNumber"), ("ACD-ALARM-MIB", "acdAlarmCfgConditionType"), ("ACD-ALARM-MIB", "acdAlarmCfgAMOType"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: acdAlarmActiveState.setStatus('current')
if mibBuilder.loadTexts: acdAlarmActiveState.setDescription('The SNMP trap that is generated when an alarm entry crosses its rising threshold and generates an event that is configured for sending SNMP traps.')
acdAlarmClearState = NotificationType((1, 3, 6, 1, 4, 1, 22420, 2, 1, 12, 2)).setObjects(("ACD-ALARM-MIB", "acdAlarmCfgID"), ("ACD-ALARM-MIB", "acdAlarmCfgNumber"), ("ACD-ALARM-MIB", "acdAlarmCfgSeverity"), ("ACD-ALARM-MIB", "acdAlarmCfgServiceAffecting"), ("ACD-ALARM-MIB", "acdAlarmCfgDesc"), ("ACD-ALARM-MIB", "acdAlarmStatusLastChange"), ("ACD-ALARM-MIB", "acdAlarmCfgExtNumber"), ("ACD-ALARM-MIB", "acdAlarmCfgConditionType"), ("ACD-ALARM-MIB", "acdAlarmCfgAMOType"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: acdAlarmClearState.setStatus('current')
if mibBuilder.loadTexts: acdAlarmClearState.setDescription('The SNMP trap that is generated when an alarm entry crosses its falling threshold and generates an event that is configured for sending SNMP traps.')
acdAlarmCfgTableLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmCfgTableLastChangeTid.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgTableLastChangeTid.setDescription('This is the transaction ID of the last change of the acdAlarmCfgTable table. If this value is different since the last read this is indicate a table change.')
acdAlarmStatusTableLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 4, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdAlarmStatusTableLastChangeTid.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusTableLastChangeTid.setDescription('This is the transaction ID of the last change of the acdAlarmStatusTable table. If this value is different since the last read this is indicate a table change.')
acdAlarmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 1))
acdAlarmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2))
acdAlarmGenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 1)).setObjects(("ACD-ALARM-MIB", "acdAlarmGenThreshOn"), ("ACD-ALARM-MIB", "acdAlarmGenThreshOff"), ("ACD-ALARM-MIB", "acdAlarmGenLedEnable"), ("ACD-ALARM-MIB", "acdAlarmGenSyslogEnable"), ("ACD-ALARM-MIB", "acdAlarmGenSNMPEnable"), ("ACD-ALARM-MIB", "acdAlarmGen8023AHEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmGenGroup = acdAlarmGenGroup.setStatus('current')
if mibBuilder.loadTexts: acdAlarmGenGroup.setDescription('.')
acdAlarmCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 2)).setObjects(("ACD-ALARM-MIB", "acdAlarmCfgID"), ("ACD-ALARM-MIB", "acdAlarmCfgNumber"), ("ACD-ALARM-MIB", "acdAlarmCfgDesc"), ("ACD-ALARM-MIB", "acdAlarmCfgEnable"), ("ACD-ALARM-MIB", "acdAlarmCfgSeverity"), ("ACD-ALARM-MIB", "acdAlarmCfgServiceAffecting"), ("ACD-ALARM-MIB", "acdAlarmCfgExtNumber"), ("ACD-ALARM-MIB", "acdAlarmCfgConditionType"), ("ACD-ALARM-MIB", "acdAlarmCfgAMOType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmCfgGroup = acdAlarmCfgGroup.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCfgGroup.setDescription('.')
acdAlarmStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 3)).setObjects(("ACD-ALARM-MIB", "acdAlarmStatusID"), ("ACD-ALARM-MIB", "acdAlarmStatusNumber"), ("ACD-ALARM-MIB", "acdAlarmStatusOn"), ("ACD-ALARM-MIB", "acdAlarmStatusLastChange"), ("ACD-ALARM-MIB", "acdAlarmStatusMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmStatusGroup = acdAlarmStatusGroup.setStatus('current')
if mibBuilder.loadTexts: acdAlarmStatusGroup.setDescription('.')
acdAlarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 4)).setObjects(("ACD-ALARM-MIB", "acdAlarmActiveState"), ("ACD-ALARM-MIB", "acdAlarmClearState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmNotificationsGroup = acdAlarmNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: acdAlarmNotificationsGroup.setDescription('Objects for the Notifications group.')
acdAlarmTidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 5)).setObjects(("ACD-ALARM-MIB", "acdAlarmCfgTableLastChangeTid"), ("ACD-ALARM-MIB", "acdAlarmStatusTableLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmTidGroup = acdAlarmTidGroup.setStatus('current')
if mibBuilder.loadTexts: acdAlarmTidGroup.setDescription('List of scalars to monitior changes in tables.')
acdAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 1, 1)).setObjects(("ACD-ALARM-MIB", "acdAlarmGenGroup"), ("ACD-ALARM-MIB", "acdAlarmCfgGroup"), ("ACD-ALARM-MIB", "acdAlarmStatusGroup"), ("ACD-ALARM-MIB", "acdAlarmNotificationsGroup"), ("ACD-ALARM-MIB", "acdAlarmTidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmCompliance = acdAlarmCompliance.setStatus('current')
if mibBuilder.loadTexts: acdAlarmCompliance.setDescription('The compliance statement for support of the ACD-ALARM-MIB module.')
mibBuilder.exportSymbols("ACD-ALARM-MIB", acdAlarm=acdAlarm, acdAlarmActiveState=acdAlarmActiveState, acdAlarmStatusTable=acdAlarmStatusTable, PYSNMP_MODULE_ID=acdAlarm, acdAlarmGenThreshOn=acdAlarmGenThreshOn, acdAlarmCfgTableLastChangeTid=acdAlarmCfgTableLastChangeTid, acdAlarmStatusGroup=acdAlarmStatusGroup, acdAlarmCfgConditionType=acdAlarmCfgConditionType, acdAlarmCfgExtNumber=acdAlarmCfgExtNumber, acdAlarmStatusID=acdAlarmStatusID, acdAlarmCfgTable=acdAlarmCfgTable, acdAlarmCfgGroup=acdAlarmCfgGroup, acdAlarmCompliances=acdAlarmCompliances, acdAlarmCfgSeverity=acdAlarmCfgSeverity, acdAlarmStatus=acdAlarmStatus, acdAlarmStatusLastChange=acdAlarmStatusLastChange, acdAlarmGen8023AHEnable=acdAlarmGen8023AHEnable, acdAlarmTidGroup=acdAlarmTidGroup, acdAlarmCfgEntry=acdAlarmCfgEntry, acdAlarmGenGroup=acdAlarmGenGroup, acdAlarmCfgEnable=acdAlarmCfgEnable, acdAlarmGenLedEnable=acdAlarmGenLedEnable, acdAlarmCfgServiceAffecting=acdAlarmCfgServiceAffecting, acdAlarmGenThreshOff=acdAlarmGenThreshOff, acdAlarmConformance=acdAlarmConformance, acdAlarmTableTid=acdAlarmTableTid, acdAlarmStatusEntry=acdAlarmStatusEntry, acdAlarmConfig=acdAlarmConfig, acdAlarmStatusNumber=acdAlarmStatusNumber, acdAlarmGroups=acdAlarmGroups, acdAlarmCfgNumber=acdAlarmCfgNumber, acdAlarmNotificationsGroup=acdAlarmNotificationsGroup, acdAlarmClearState=acdAlarmClearState, acdAlarmStatusTableLastChangeTid=acdAlarmStatusTableLastChangeTid, acdAlarmMIBObjects=acdAlarmMIBObjects, acdAlarmCfgAMOType=acdAlarmCfgAMOType, acdAlarmStatusOn=acdAlarmStatusOn, acdAlarmCompliance=acdAlarmCompliance, acdAlarmGenSyslogEnable=acdAlarmGenSyslogEnable, acdAlarmV2=acdAlarmV2, acdAlarmStatusMsg=acdAlarmStatusMsg, acdAlarmCfgID=acdAlarmCfgID, acdAlarmCfgDesc=acdAlarmCfgDesc, acdAlarmGenSNMPEnable=acdAlarmGenSNMPEnable)
