#
# PySNMP MIB module NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NoiNotificationType, NoiAlarmLogCount, NoiSystemDistinguishedName, NoiLogFullAction, NoiPerceivedSeverity, NoiAlarmId, NoiEventType, NoiNotificationId, NoiSpecificProblem, NoiProbableCause, NoiAcknowledgementState, NoiAcknowledgementUserId, NoiAdditionalText, NoiAcknowledgementTime, NoiAlarmLogControl, NoiAlarmTableCount, NoiAlarmText, NoiEventTime = mibBuilder.importSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION", "NoiNotificationType", "NoiAlarmLogCount", "NoiSystemDistinguishedName", "NoiLogFullAction", "NoiPerceivedSeverity", "NoiAlarmId", "NoiEventType", "NoiNotificationId", "NoiSpecificProblem", "NoiProbableCause", "NoiAcknowledgementState", "NoiAcknowledgementUserId", "NoiAdditionalText", "NoiAcknowledgementTime", "NoiAlarmLogControl", "NoiAlarmTableCount", "NoiAlarmText", "NoiEventTime")
noiFMCompliance, noiFaultManagementVariable, noiAlarmTables, noiAlarmNotification, noiOpenInterfaceModule, noiAlarmLog = mibBuilder.importSymbols("NOKIA-NE3S-REGISTRATION-MIB", "noiFMCompliance", "noiFaultManagementVariable", "noiAlarmTables", "noiAlarmNotification", "noiOpenInterfaceModule", "noiAlarmLog")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, iso, Gauge32, IpAddress, Counter32, Integer32, TimeTicks, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Gauge32", "IpAddress", "Counter32", "Integer32", "TimeTicks", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
noiSnmpAlarmIrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 2))
noiSnmpAlarmIrp.setRevisions(('2002-11-01 00:00',))
if mibBuilder.loadTexts: noiSnmpAlarmIrp.setLastUpdated('200211010000Z')
if mibBuilder.loadTexts: noiSnmpAlarmIrp.setOrganization('Nokia Networks')
noiAlarmIrpVersion = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmIrpVersion.setStatus('current')
noiAlarmLastSendNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 1, 2, 2), NoiNotificationId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLastSendNotificationId.setStatus('current')
noiAlarmTableCount = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 1), NoiAlarmTableCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmTableCount.setStatus('current')
noiAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2), )
if mibBuilder.loadTexts: noiAlarmTable.setStatus('current')
noiAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1), ).setIndexNames((0, "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"))
if mibBuilder.loadTexts: noiAlarmEntry.setStatus('current')
noiAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 1), NoiAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmId.setStatus('current')
noiAlarmSystemDN = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 2), NoiSystemDistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmSystemDN.setStatus('current')
noiAlarmEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 3), NoiEventTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmEventTime.setStatus('current')
noiAlarmSpecificProblem = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 4), NoiSpecificProblem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmSpecificProblem.setStatus('current')
noiAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 5), NoiAlarmText()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmText.setStatus('current')
noiAlarmPerceivedSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 6), NoiPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmPerceivedSeverity.setStatus('current')
noiAlarmAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 7), NoiAdditionalText()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmAdditionalText.setStatus('current')
noiAlarmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 8), NoiProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmProbableCause.setStatus('current')
noiAlarmEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 9), NoiEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmEventType.setStatus('current')
noiAlarmNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 10), NoiNotificationId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmNotificationId.setStatus('current')
noiAlarmAckState = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 11), NoiAcknowledgementState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiAlarmAckState.setStatus('current')
noiAlarmAckTime = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 12), NoiAcknowledgementTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiAlarmAckTime.setStatus('current')
noiAlarmAckUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 4, 2, 1, 13), NoiAcknowledgementUserId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiAlarmAckUserId.setStatus('current')
noiAlarmNew = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 1)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
if mibBuilder.loadTexts: noiAlarmNew.setStatus('current')
noiAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 2)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
if mibBuilder.loadTexts: noiAlarmCleared.setStatus('current')
noiAlarmListRebuild = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 3)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
if mibBuilder.loadTexts: noiAlarmListRebuild.setStatus('current')
noiAlarmListRebuildInitiated = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 4)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
if mibBuilder.loadTexts: noiAlarmListRebuildInitiated.setStatus('current')
noiAlarmChanged = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 5)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"))
if mibBuilder.loadTexts: noiAlarmChanged.setStatus('current')
noiAlarmAckStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 1, 3, 0, 6)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckState"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckUserId"))
if mibBuilder.loadTexts: noiAlarmAckStateChanged.setStatus('current')
noiAlarmLogFullAction = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 1), NoiLogFullAction().clone('wrap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiAlarmLogFullAction.setStatus('current')
noiAlarmLogControl = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 2), NoiAlarmLogControl().clone('logging')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiAlarmLogControl.setStatus('current')
noiAlarmLogCount = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 3), NoiAlarmLogCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogCount.setStatus('current')
noiAlarmLogMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 4), NoiAlarmLogCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogMaxCount.setStatus('current')
noiAlarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5), )
if mibBuilder.loadTexts: noiAlarmLogTable.setStatus('current')
noiAlarmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1), ).setIndexNames((0, "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryNotificationId"))
if mibBuilder.loadTexts: noiAlarmLogEntry.setStatus('current')
noiAlarmLogEntryNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 1), NoiNotificationId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryNotificationId.setStatus('current')
noiAlarmLogEntryAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 2), NoiAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryAlarmId.setStatus('current')
noiAlarmLogEntrySystemDN = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 3), NoiSystemDistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntrySystemDN.setStatus('current')
noiAlarmLogEntryEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 4), NoiEventTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryEventTime.setStatus('current')
noiAlarmLogEntrySpecificProblem = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 5), NoiSpecificProblem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntrySpecificProblem.setStatus('current')
noiAlarmLogEntryAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 6), NoiAlarmText()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryAlarmText.setStatus('current')
noiAlarmLogEntryPerceivedSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 7), NoiPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryPerceivedSeverity.setStatus('current')
noiAlarmLogEntryAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 8), NoiAdditionalText()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryAdditionalText.setStatus('current')
noiAlarmLogEntryProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 9), NoiProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryProbableCause.setStatus('current')
noiAlarmLogEntryEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 10), NoiEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryEventType.setStatus('current')
noiAlarmLogEntryAckState = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 11), NoiAcknowledgementState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryAckState.setStatus('current')
noiAlarmLogEntryAckTime = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 12), NoiAcknowledgementTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryAckTime.setStatus('current')
noiAlarmLogEntryAckUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 13), NoiAcknowledgementUserId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryAckUserId.setStatus('current')
noiAlarmLogEntryNotificationType = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 1, 5, 5, 1, 14), NoiNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiAlarmLogEntryNotificationType.setStatus('current')
noiAlarmIRPompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 1)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdministrationMandatoryGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationMandatoryGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationOptionalGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmTableOptionalGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmTableRebuildOptionalGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAcknwledgementOptionalGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmIRPompliance = noiAlarmIRPompliance.setStatus('current')
noiAlarmAdministrationMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 2)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmIrpVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmAdministrationMandatoryGroup = noiAlarmAdministrationMandatoryGroup.setStatus('current')
noiAlarmNotificationMandatoryGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 4)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNew"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmNotificationMandatoryGroup = noiAlarmNotificationMandatoryGroup.setStatus('current')
noiAlarmNotificationOptionalGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 5)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmNotificationOptionalGroup = noiAlarmNotificationOptionalGroup.setStatus('current')
noiAlarmTableOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 6)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmTableCount"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLastSendNotificationId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmSpecificProblem"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmPerceivedSeverity"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmProbableCause"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmEventType"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmNotificationId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckState"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckUserId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmTableOptionalGroup = noiAlarmTableOptionalGroup.setStatus('current')
noiAlarmTableRebuildOptionalGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 7)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmListRebuild"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmListRebuildInitiated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmTableRebuildOptionalGroup = noiAlarmTableRebuildOptionalGroup.setStatus('current')
noiAlarmAcknwledgementOptionalGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 8)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmAckStateChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmAcknwledgementOptionalGroup = noiAlarmAcknwledgementOptionalGroup.setStatus('current')
noiAlarmLogOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 7, 1, 6, 9)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogFullAction"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogControl"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogCount"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogMaxCount"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAlarmId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntrySystemDN"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntrySpecificProblem"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAlarmText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryPerceivedSeverity"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryProbableCause"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryEventType"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryNotificationId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAckState"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAckTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryAckUserId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", "noiAlarmLogEntryNotificationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiAlarmLogOptionalGroup = noiAlarmLogOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-ALARM-IRP", noiAlarmLogEntrySystemDN=noiAlarmLogEntrySystemDN, PYSNMP_MODULE_ID=noiSnmpAlarmIrp, noiAlarmLogEntryProbableCause=noiAlarmLogEntryProbableCause, noiAlarmEventType=noiAlarmEventType, noiAlarmCleared=noiAlarmCleared, noiAlarmLogEntryAckTime=noiAlarmLogEntryAckTime, noiAlarmLastSendNotificationId=noiAlarmLastSendNotificationId, noiAlarmSpecificProblem=noiAlarmSpecificProblem, noiAlarmLogEntryNotificationType=noiAlarmLogEntryNotificationType, noiAlarmTableRebuildOptionalGroup=noiAlarmTableRebuildOptionalGroup, noiAlarmLogTable=noiAlarmLogTable, noiAlarmEntry=noiAlarmEntry, noiAlarmTable=noiAlarmTable, noiAlarmLogMaxCount=noiAlarmLogMaxCount, noiAlarmLogEntryEventTime=noiAlarmLogEntryEventTime, noiAlarmLogEntryAckState=noiAlarmLogEntryAckState, noiAlarmAdministrationMandatoryGroup=noiAlarmAdministrationMandatoryGroup, noiAlarmLogOptionalGroup=noiAlarmLogOptionalGroup, noiAlarmListRebuildInitiated=noiAlarmListRebuildInitiated, noiAlarmListRebuild=noiAlarmListRebuild, noiAlarmAckStateChanged=noiAlarmAckStateChanged, noiAlarmLogEntryAckUserId=noiAlarmLogEntryAckUserId, noiAlarmLogEntryEventType=noiAlarmLogEntryEventType, noiAlarmNew=noiAlarmNew, noiAlarmLogEntryNotificationId=noiAlarmLogEntryNotificationId, noiAlarmText=noiAlarmText, noiAlarmLogEntrySpecificProblem=noiAlarmLogEntrySpecificProblem, noiAlarmSystemDN=noiAlarmSystemDN, noiAlarmAcknwledgementOptionalGroup=noiAlarmAcknwledgementOptionalGroup, noiAlarmLogFullAction=noiAlarmLogFullAction, noiAlarmId=noiAlarmId, noiSnmpAlarmIrp=noiSnmpAlarmIrp, noiAlarmIrpVersion=noiAlarmIrpVersion, noiAlarmAckState=noiAlarmAckState, noiAlarmPerceivedSeverity=noiAlarmPerceivedSeverity, noiAlarmAdditionalText=noiAlarmAdditionalText, noiAlarmLogControl=noiAlarmLogControl, noiAlarmLogEntry=noiAlarmLogEntry, noiAlarmLogCount=noiAlarmLogCount, noiAlarmLogEntryAlarmId=noiAlarmLogEntryAlarmId, noiAlarmTableOptionalGroup=noiAlarmTableOptionalGroup, noiAlarmTableCount=noiAlarmTableCount, noiAlarmAckUserId=noiAlarmAckUserId, noiAlarmEventTime=noiAlarmEventTime, noiAlarmLogEntryAdditionalText=noiAlarmLogEntryAdditionalText, noiAlarmNotificationOptionalGroup=noiAlarmNotificationOptionalGroup, noiAlarmAckTime=noiAlarmAckTime, noiAlarmNotificationMandatoryGroup=noiAlarmNotificationMandatoryGroup, noiAlarmLogEntryPerceivedSeverity=noiAlarmLogEntryPerceivedSeverity, noiAlarmNotificationId=noiAlarmNotificationId, noiAlarmProbableCause=noiAlarmProbableCause, noiAlarmChanged=noiAlarmChanged, noiAlarmIRPompliance=noiAlarmIRPompliance, noiAlarmLogEntryAlarmText=noiAlarmLogEntryAlarmText)
