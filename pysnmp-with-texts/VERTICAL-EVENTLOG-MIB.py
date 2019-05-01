#
# PySNMP MIB module VERTICAL-EVENTLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERTICAL-EVENTLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter32, enterprises, MibIdentifier, Counter64, Bits, NotificationType, Unsigned32, TimeTicks, IpAddress, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter32", "enterprises", "MibIdentifier", "Counter64", "Bits", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vertical = MibIdentifier((1, 3, 6, 1, 4, 1, 2338))
eventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 13))
eventLogTrapInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 13, 1))
lastTrapLogType = MibScalar((1, 3, 6, 1, 4, 1, 2338, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("system", 1), ("security", 2), ("application", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTrapLogType.setStatus('mandatory')
if mibBuilder.loadTexts: lastTrapLogType.setDescription('This object describes the Log Type of the last Event Log trap reported. The following are valid values: system (1) -> Win NT System Log security (2) -> Win NT Security Log application (3) -> The Application Log unknown (4) -> Unknown Log')
lastTrapEventType = MibScalar((1, 3, 6, 1, 4, 1, 2338, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("information", 3), ("audit-success", 4), ("audit-fail", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTrapEventType.setStatus('mandatory')
if mibBuilder.loadTexts: lastTrapEventType.setDescription('This object describes the Event Type of the last Event Log trap reported. The following are valid values: error (1) -> Error events indicate significant problems that the user should know about. Error events usually indicate a loss of functionality or data. For example, if a service cannot be loaded as the system boots, it can log an error event. warning (2) -> Warning events indicate problems that are not immediately significant, but that may indicate conditions that could cause future problems. For example,an application can logs warning event if disk space is low. information (3) -> Information events indicate infrequent but significant successful operations. audit-success (4) -> Success audit events are security events that occur when an audited access attempt is successful. For example, a successful logon attempt is a success audit event. audit-fail (5) -> Failure audit events are security events that occur when an audited access attempt fails. For example, a failed attempt to open a file is a failure audit event. unknown (6) -> Indicates an event type other than those described above.')
lastTrapInfoString = MibScalar((1, 3, 6, 1, 4, 1, 2338, 13, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTrapInfoString.setStatus('mandatory')
if mibBuilder.loadTexts: lastTrapInfoString.setDescription('This object describes,in more detail,the last Event Log Trap event that occured. ')
eventLog_FailedToStartSTD = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,53)).setLabel("eventLog-FailedToStartSTD").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_FailedToStartSTD.setDescription(' This notification is sent when an attempt to start the Self Start Daemon fails.')
eventLog_FailedToStopSTD = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,54)).setLabel("eventLog-FailedToStopSTD").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_FailedToStopSTD.setDescription(' This notification is sent when an attempt to stop the Self Start Daemon fails.')
eventLog_CannotCreateUserTracePipe = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,55)).setLabel("eventLog-CannotCreateUserTracePipe").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_CannotCreateUserTracePipe.setDescription(' This notification is sent when an attempt to create the User Trace request pipe fails.')
eventLog_CannotConnectUserTracePipe = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,56)).setLabel("eventLog-CannotConnectUserTracePipe").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_CannotConnectUserTracePipe.setDescription(' This notification is sent when an attempt to connect to the User Trace request pipe fails.')
eventLog_VoiceMailDiskIsFull = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,57)).setLabel("eventLog-VoiceMailDiskIsFull").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_VoiceMailDiskIsFull.setDescription(' This notification is sent when the Voice Mail disk capacity is reached.')
eventLog_SystemDiskIsFull = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,58)).setLabel("eventLog-SystemDiskIsFull").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_SystemDiskIsFull.setDescription(' This notification is sent when the specific disk capacity is reached.')
eventLog_SecurityError = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,59)).setLabel("eventLog-SecurityError").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_SecurityError.setDescription(' This notification is sent when a failure audit event occurs, i.e. an audited access attempt fails. For example, a failed attempt to open a file is a failure audit event.')
eventLog_SecuritySuccess = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,60)).setLabel("eventLog-SecuritySuccess").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_SecuritySuccess.setDescription(' This notification is sent when a success audit event occurs, i.e. when an audited access attempt is successful. For example, a successful logon attempt is a success audit event.')
eventLog_GenericEventLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,61)).setLabel("eventLog-GenericEventLogTrap").setObjects(("VERTICAL-EVENTLOG-MIB", "lastTrapLogType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapEventType"), ("VERTICAL-EVENTLOG-MIB", "lastTrapInfoString"))
if mibBuilder.loadTexts: eventLog_GenericEventLogTrap.setDescription(' This notification is sent whenever an error or warning event is written to the Event Log. More information about this event (i.e. which log - system, app or security, as well as which event type - error, warning or audit,etc) can be found from the trap data.')
mibBuilder.exportSymbols("VERTICAL-EVENTLOG-MIB", eventLog_SecurityError=eventLog_SecurityError, eventLog_FailedToStopSTD=eventLog_FailedToStopSTD, eventLog_GenericEventLogTrap=eventLog_GenericEventLogTrap, lastTrapEventType=lastTrapEventType, eventLog_SystemDiskIsFull=eventLog_SystemDiskIsFull, lastTrapInfoString=lastTrapInfoString, eventLog_FailedToStartSTD=eventLog_FailedToStartSTD, eventLog=eventLog, eventLog_SecuritySuccess=eventLog_SecuritySuccess, eventLogTrapInfoGroup=eventLogTrapInfoGroup, vertical=vertical, eventLog_CannotConnectUserTracePipe=eventLog_CannotConnectUserTracePipe, eventLog_CannotCreateUserTracePipe=eventLog_CannotCreateUserTracePipe, lastTrapLogType=lastTrapLogType, eventLog_VoiceMailDiskIsFull=eventLog_VoiceMailDiskIsFull)
