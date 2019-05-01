#
# PySNMP MIB module NORTEL-NMI-FAULT-NOTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-NMI-FAULT-NOTI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
nortelNMInotificationGroups, = mibBuilder.importSymbols("NORTEL-NMI-GROUPS-MIB", "nortelNMInotificationGroups")
nortelNMInotificationsMIB, nortelNMInotifyNeUnknownStatus, nortelNMIcurrentTxNotificationSequenceNum, nortelNMInotifyNeType, nortelNMInotifyNeOperState, nortelNMInotifyNeAdminState, nortelNMInotifyNeName = mibBuilder.importSymbols("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotificationsMIB", "nortelNMInotifyNeUnknownStatus", "nortelNMIcurrentTxNotificationSequenceNum", "nortelNMInotifyNeType", "nortelNMInotifyNeOperState", "nortelNMInotifyNeAdminState", "nortelNMInotifyNeName")
NortelNMItimeStampDef, NortelNMIalarmProblemCategory, NortelNMIalarmProbableCause = mibBuilder.importSymbols("NORTEL-NMI-TC-MIB", "NortelNMItimeStampDef", "NortelNMIalarmProblemCategory", "NortelNMIalarmProbableCause")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ObjectIdentity, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, MibIdentifier, Counter32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "MibIdentifier", "Counter32", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortelNMIfaultNotiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4))
nortelNMIfaultNotiMIB.setRevisions(('1999-07-19 00:00', '1999-06-24 00:00', '1999-05-31 00:00', '1999-04-12 00:00', '1999-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nortelNMIfaultNotiMIB.setRevisionsDescriptions((' Add ASCII string limitations for componentID, etc.', ' The fourth version of this MIB module. Module-identity OID assignment changed. Revisions introduced by Shobana Sundaram.', ' The third version of this MIB module. Contact info updated and Revision history added. ', ' The second version of this MIB module. Contact info updated and Revision history added. Ne type varbind included at the state change notification.', ' The first version of this MIB module.',))
if mibBuilder.loadTexts: nortelNMIfaultNotiMIB.setLastUpdated('9907190000Z')
if mibBuilder.loadTexts: nortelNMIfaultNotiMIB.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nortelNMIfaultNotiMIB.setContactInfo(' Jingdong Liu Postal: Nortel Networks P. O. Box 3511, Station C Ottawa, Ontario CANADA K1Y 4H7 Email: jingdong@nortelnetworks.com')
if mibBuilder.loadTexts: nortelNMIfaultNotiMIB.setDescription('This module contains the fault management related notifications for the Nortel NMI.')
nortelNMIfaultNotiPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0))
if mibBuilder.loadTexts: nortelNMIfaultNotiPrefix.setStatus('current')
if mibBuilder.loadTexts: nortelNMIfaultNotiPrefix.setDescription('This OID represents the prefix branch for all Nortel NMI fault Notifications. The last but one sub identifier in the OID of any Notification must have the value zero to facilitate v2<-->v1 conversion.')
nortelNMIfaultNotiVarbinds = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1))
if mibBuilder.loadTexts: nortelNMIfaultNotiVarbinds.setStatus('current')
if mibBuilder.loadTexts: nortelNMIfaultNotiVarbinds.setDescription('This OID represents the branch which contains varbinds to fault management related notifications.')
nortelNMInotifyAlarmComponentId = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmComponentId.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmComponentId.setDescription("This variable represents the Distinguished Name (DN) (refer X.720) of the component object against which the particular alarm is raised. The entire component hierarchy should be presented in the category-value information model to unambiguosly identify the specific component object instance. Here category refers to the type of the component and value refers to the instance identifier, both are represented as strings. The format of the string is NEtype=NEname;component class=component instance Id;.... The root component is always the NE and the NE is identified via its type as the category and the value as the NE name. The managed element class for the NE is implicitly assumed. The NE type is based on NortelNMIneType textual convention. With NE as the root, the entire containment with the list of Relative Distinguished Names (RDNs) is presented upto the point where the alarming component is clearly identified. Semicolon is the delimiter between a 'category=value' pair. The string can only contain alphanumeric characters and underscores. No commas, spaces, slashes, hyphens, or dollar signs is allowed.")
nortelNMInotifyAlarmCategory = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 2), NortelNMIalarmProblemCategory()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmCategory.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmCategory.setDescription('This variable presents the problem category of the alarm as per the definition of the textual convention NortelNMIalarmProblemCategory from NORTEL-NMI-TC-MIB.')
nortelNMInotifyAlarmNotificationID = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1073741824))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmNotificationID.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmNotificationID.setDescription('This variable is the notification identifier of the alarm that must be unique across all notifications of the particular NE in context through the time that correlation is significant.')
nortelNMInotifyAlarmDescription = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmDescription.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmDescription.setDescription('This variable provides the description text for the particular alarm.')
nortelNMInotifyAlarmTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 5), NortelNMItimeStampDef()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmTimeStamp.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmTimeStamp.setDescription('This variable presents the relative timestamp of occurrence of the alarm. NortelNMItimeStampDef textual convention is defined at the NORTEL-NMI-TC-MIB.')
nortelNMInotifyAlarmProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 6), NortelNMIalarmProbableCause()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmProbableCause.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmProbableCause.setDescription('This variable provides the probable cause of the particular alarm.')
nortelNMInotifyAlarmSpecificProblem = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmSpecificProblem.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmSpecificProblem.setDescription('This variable provides the specific problem data (ITU-T X.733) to further qualify the probable cause of the particular alarm.')
nortelNMInotifyAlarmCorrelationIdList = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyAlarmCorrelationIdList.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyAlarmCorrelationIdList.setDescription("This variable provides the list of Notification Ids of previously reported alarms that this alarm correlates to. This correlation refers to implicitly clearing the previously raised alarms and overriding them with this alarm report. The format of this string is 'notificationID1;notificationID2......', with a list of integer notification ID values corresponding to the correlated alarms with ';' as the delimiter between any two Notification Identifiers.")
nortelNMInotifyNeStateChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 9), NortelNMItimeStampDef()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyNeStateChangeTime.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyNeStateChangeTime.setDescription('This variable represents the time at which a certain NE state has been changed. ')
nortelNMIneOSIstateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 101)).setObjects(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"), ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeType"), ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeName"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyNeStateChangeTime"), ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeAdminState"), ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeOperState"), ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeUnknownStatus"))
if mibBuilder.loadTexts: nortelNMIneOSIstateChangeNotification.setStatus('current')
if mibBuilder.loadTexts: nortelNMIneOSIstateChangeNotification.setDescription('This notification indicates that one of the NE OSI states has been changed. The modified value of the specific state would be included as the varbind in the actual Notification PDU. We currently support changes to admin state, operational state and unknown status.')
nortelNMIalarmClearNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 201)).setObjects(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
if mibBuilder.loadTexts: nortelNMIalarmClearNotification.setStatus('current')
if mibBuilder.loadTexts: nortelNMIalarmClearNotification.setDescription('This notification indicates that one or more previously reported alarms have been cleared and the previously reported alarms are identified via the correlation id list field. The varbinds include alarm context via the ComponentId field and other additional useful information.')
nortelNMIwarningAlarmNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 202)).setObjects(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
if mibBuilder.loadTexts: nortelNMIwarningAlarmNotification.setStatus('current')
if mibBuilder.loadTexts: nortelNMIwarningAlarmNotification.setDescription("This notification indicates that an alarm of 'Warning' severity has been raised on a NE. The varbinds include alarm context via the ComponentId field and other additional useful information on the alarm condition.")
nortelNMIminorAlarmNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 203)).setObjects(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
if mibBuilder.loadTexts: nortelNMIminorAlarmNotification.setStatus('current')
if mibBuilder.loadTexts: nortelNMIminorAlarmNotification.setDescription("This notification indicates that an alarm of 'Minor' severity has been raised on a NE. The varbinds include alarm context via the ComponentId field and other additional useful information on the alarm condition.")
nortelNMImajorAlarmNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 204)).setObjects(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
if mibBuilder.loadTexts: nortelNMImajorAlarmNotification.setStatus('current')
if mibBuilder.loadTexts: nortelNMImajorAlarmNotification.setDescription("This notification indicates that an alarm of 'Major' severity has been raised on a NE. The varbinds include alarm context via the ComponentId field and other additional useful information on the alarm condition.")
nortelNMIcriticalAlarmNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 205)).setObjects(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
if mibBuilder.loadTexts: nortelNMIcriticalAlarmNotification.setStatus('current')
if mibBuilder.loadTexts: nortelNMIcriticalAlarmNotification.setDescription("This notification indicates that an alarm of 'Critical' severity has been raised on a NE. The varbinds include alarm context via the ComponentId field and other additional useful information on the alarm condition.")
nortelNMIneStateChangeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 3)).setObjects(("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIneOSIstateChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nortelNMIneStateChangeNotificationGroup = nortelNMIneStateChangeNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: nortelNMIneStateChangeNotificationGroup.setDescription(' Nortel NMI NE state change notification group.')
nortelNMIneAlarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 4)).setObjects(("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIalarmClearNotification"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIwarningAlarmNotification"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIminorAlarmNotification"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMImajorAlarmNotification"), ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIcriticalAlarmNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nortelNMIneAlarmNotificationsGroup = nortelNMIneAlarmNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: nortelNMIneAlarmNotificationsGroup.setDescription(' Nortel NMI NE alarm notification group.')
mibBuilder.exportSymbols("NORTEL-NMI-FAULT-NOTI-MIB", nortelNMIneOSIstateChangeNotification=nortelNMIneOSIstateChangeNotification, nortelNMInotifyAlarmNotificationID=nortelNMInotifyAlarmNotificationID, nortelNMInotifyAlarmProbableCause=nortelNMInotifyAlarmProbableCause, nortelNMIfaultNotiVarbinds=nortelNMIfaultNotiVarbinds, nortelNMInotifyAlarmSpecificProblem=nortelNMInotifyAlarmSpecificProblem, nortelNMImajorAlarmNotification=nortelNMImajorAlarmNotification, nortelNMIcriticalAlarmNotification=nortelNMIcriticalAlarmNotification, nortelNMInotifyNeStateChangeTime=nortelNMInotifyNeStateChangeTime, nortelNMInotifyAlarmComponentId=nortelNMInotifyAlarmComponentId, nortelNMIfaultNotiMIB=nortelNMIfaultNotiMIB, nortelNMInotifyAlarmTimeStamp=nortelNMInotifyAlarmTimeStamp, nortelNMIneStateChangeNotificationGroup=nortelNMIneStateChangeNotificationGroup, nortelNMIwarningAlarmNotification=nortelNMIwarningAlarmNotification, nortelNMIfaultNotiPrefix=nortelNMIfaultNotiPrefix, nortelNMIminorAlarmNotification=nortelNMIminorAlarmNotification, PYSNMP_MODULE_ID=nortelNMIfaultNotiMIB, nortelNMInotifyAlarmCorrelationIdList=nortelNMInotifyAlarmCorrelationIdList, nortelNMIalarmClearNotification=nortelNMIalarmClearNotification, nortelNMIneAlarmNotificationsGroup=nortelNMIneAlarmNotificationsGroup, nortelNMInotifyAlarmCategory=nortelNMInotifyAlarmCategory, nortelNMInotifyAlarmDescription=nortelNMInotifyAlarmDescription)
