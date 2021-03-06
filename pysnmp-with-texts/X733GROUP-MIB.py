#
# PySNMP MIB module X733GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/X733GROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:42:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Integer32, iso, NotificationType, ModuleIdentity, enterprises, IpAddress, Gauge32, Counter64, TimeTicks, Unsigned32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Integer32", "iso", "NotificationType", "ModuleIdentity", "enterprises", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "Unsigned32", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
siemensUnits = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7))
oenProductMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1))
nms = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3))
ncProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1))
ewsdAlarms = ModuleIdentity((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1))
if mibBuilder.loadTexts: ewsdAlarms.setLastUpdated('200110150000Z')
if mibBuilder.loadTexts: ewsdAlarms.setOrganization('Siemens AG Osterreich')
if mibBuilder.loadTexts: ewsdAlarms.setContactInfo(' Technical Support Postal: Siemens AG Oesterreich Rampengasse 3-5 1190 Wien, Austria Tel: + 43 5 1707 43623 Fax: E-mail: martin.zach@siemens.at')
if mibBuilder.loadTexts: ewsdAlarms.setDescription('This MIB module implements X733 Alarms which are extracted from MML alarms (EWSD classic), from SNMP alarms (EWSD InterNode and other SNMP managed devices) and from Q3 alarms (EWSD PowerNode). According to this distinction, different traps for spontaneous alarms are defined. This MIB module is compatible to previous versions which did not support SNMP and Q3 alarms, and countAlarms with the number of major, critical and minor alarms of the relevant Network Element.')
commonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1))
controlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2))
summaryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3))
miscGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 4))
x733Group = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5))
q3Group = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6))
osGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7))
neName = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: neName.setStatus('current')
if mibBuilder.loadTexts: neName.setDescription('name of the EWSD')
managedObjectClass = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 2), DisplayString())
if mibBuilder.loadTexts: managedObjectClass.setStatus('current')
if mibBuilder.loadTexts: managedObjectClass.setDescription('naming attribute of the class of alarm Object (only EWSD classic); possible values: DLU, SAL, MAL, LTG, SN, MB ...')
notificationId = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 3), DisplayString())
if mibBuilder.loadTexts: notificationId.setStatus('current')
if mibBuilder.loadTexts: notificationId.setDescription('corresponds to X.721/X.733:NotificationIdentifier - an ascii string uniquely identifying an alarm within all EWSDs.')
globalAlarmIds = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8192)))
if mibBuilder.loadTexts: globalAlarmIds.setStatus('current')
if mibBuilder.loadTexts: globalAlarmIds.setDescription('an ascii string containing 0..64 commaseparated strings uniquely identifying an alarm within all EWSDs.')
setPeriod = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setPeriod.setStatus('current')
if mibBuilder.loadTexts: setPeriod.setDescription('defines the time period for the periodical alarm summaries unit of measurement: 8 minutes, initially set to 1 (i.e. 8 minutes).')
sendSummary = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sendSummary.setStatus('current')
if mibBuilder.loadTexts: sendSummary.setDescription('The value must be a neName. Setting a value causes an immediate alarm status summary with respect to the chosen EWSD( forced alarm status summary). Possible EWSD names can be learned from the periodical status summary alarms.')
resendAlarm = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: resendAlarm.setStatus('current')
if mibBuilder.loadTexts: resendAlarm.setDescription('The value must be a notificationID. Setting a value causes an immediate alarm notification. Possible notificationIDs can be learned from the status summary alarms.')
sendAllAlarms = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sendAllAlarms.setStatus('current')
if mibBuilder.loadTexts: sendAllAlarms.setDescription('Whenever this object is set to any (!) integer value all open Alarms will be sent.')
alarmSpontan = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSpontan.setStatus('current')
if mibBuilder.loadTexts: alarmSpontan.setDescription('Setting to no(2) disables sending of spontaneousAlarms, default: yes(1).')
countAlarmPeriod = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: countAlarmPeriod.setStatus('current')
if mibBuilder.loadTexts: countAlarmPeriod.setDescription('defines the time period for the periodic count alarms unit of measurement: 8 minutes; initially set to 0 (which means no periodic count alarms.')
countAlarmSpontan = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: countAlarmSpontan.setStatus('current')
if mibBuilder.loadTexts: countAlarmSpontan.setDescription('Setting to yes(1) enables sending of spontaneous count alarms default: no(2).')
numberOfAlarms = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 1), Integer32())
if mibBuilder.loadTexts: numberOfAlarms.setStatus('current')
if mibBuilder.loadTexts: numberOfAlarms.setDescription('Total number of open alarms of the relevant EWSD.')
connectionReliable = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))))
if mibBuilder.loadTexts: connectionReliable.setStatus('current')
if mibBuilder.loadTexts: connectionReliable.setDescription('The connection to the relevant EWSD is reliable if the last information exchange with ADS is not longer than 8 minutes ago (valid for MML alarms).')
critical = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 3), Integer32())
if mibBuilder.loadTexts: critical.setStatus('current')
if mibBuilder.loadTexts: critical.setDescription('Total number of critical alarms of the relevant EWSD.')
major = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 4), Integer32())
if mibBuilder.loadTexts: major.setStatus('current')
if mibBuilder.loadTexts: major.setDescription('Total number of major alarms of the relevant EWSD.')
minor = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 5), Integer32())
if mibBuilder.loadTexts: minor.setStatus('current')
if mibBuilder.loadTexts: minor.setDescription('Total number of minor alarms of the relevant EWSD.')
timePeriod = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(1))
if mibBuilder.loadTexts: timePeriod.setStatus('current')
if mibBuilder.loadTexts: timePeriod.setDescription('actual value of time period for alarm summaries - unit of measurement: 8 minutes - initially set to 1 (i.e. 8 minutes)')
q3AlarmNumber = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)))
if mibBuilder.loadTexts: q3AlarmNumber.setStatus('current')
if mibBuilder.loadTexts: q3AlarmNumber.setDescription("number of q3Alarm traps in which a Q3 alarm is divided (with CONTINUE_FLAG). Started from value 0, if it's not the last trap for this alarm value is incremented with 9000. A complete Q3 alarm consists of one q3Alarm trap, plus 'q3AlarmNumber' q3contAlarm traps.")
eventType = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 8, 9, 10, 11, 13, 15))).clone(namedValues=NamedValues(("indeterminate", 0), ("communicationsAlarm", 2), ("enviromentalAlarm", 3), ("equipmentAlarm", 4), ("integrityViolation", 5), ("operationalViolation", 8), ("physicalViolation", 9), ("processingErrorAlarm", 10), ("qualityOfServiceAlarm", 11), ("securityServiceOrMechanismViolation", 13), ("timeDomainViolation", 15))))
if mibBuilder.loadTexts: eventType.setStatus('current')
if mibBuilder.loadTexts: eventType.setDescription('last component of the respective OID defined in X.721.')
severity = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("indeterminate", 0), ("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("cleared", 5))))
if mibBuilder.loadTexts: severity.setStatus('current')
if mibBuilder.loadTexts: severity.setDescription(' corresponds to X.721/X.733:PerceivedSeverity.')
probableCause = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 3), DisplayString())
if mibBuilder.loadTexts: probableCause.setStatus('current')
if mibBuilder.loadTexts: probableCause.setDescription(' corresponds to X.721/X.733:ProbableCause.')
originalAlarm = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8192)))
if mibBuilder.loadTexts: originalAlarm.setStatus('current')
if mibBuilder.loadTexts: originalAlarm.setDescription('corresponds to X.721/X.733:AdditionalText: The original EWSD alarm (max. 8 kByte) for EWSD classic, formatted output for SNMP traps and Q3 alarms')
processingStatus = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("not-processed", 0), ("in-process", 1), ("under-repair", 2), ("deferred", 3), ("cleared", 4))))
if mibBuilder.loadTexts: processingStatus.setStatus('current')
if mibBuilder.loadTexts: processingStatus.setDescription('An element of X.721:SpecificProblem ')
alarmClass = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 6), DisplayString())
if mibBuilder.loadTexts: alarmClass.setStatus('current')
if mibBuilder.loadTexts: alarmClass.setDescription('An element of X.721:AdditionalInformation; can be seen as a CMIS-ManagedObjectClass-field if an object model with a finer granularity would be defined; example: SLM (subscriber line module) identifies a line card')
managedObjectInstance = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 7), DisplayString())
if mibBuilder.loadTexts: managedObjectInstance.setStatus('current')
if mibBuilder.loadTexts: managedObjectInstance.setDescription('An element of X.721:AdditionalInformation; can be seen as a part of the CMIS-ManagedObjectInstance-field if an object model with a finer granularity would be defined ')
rack = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)))
if mibBuilder.loadTexts: rack.setStatus('current')
if mibBuilder.loadTexts: rack.setDescription('An element of X.721:AdditionalInformation ')
shelf = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)))
if mibBuilder.loadTexts: shelf.setStatus('current')
if mibBuilder.loadTexts: shelf.setDescription('An element of X.721:AdditionalInformation ')
fromCard = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)))
if mibBuilder.loadTexts: fromCard.setStatus('current')
if mibBuilder.loadTexts: fromCard.setDescription('An element of X.721:AdditionalInformation ')
toCard = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)))
if mibBuilder.loadTexts: toCard.setStatus('current')
if mibBuilder.loadTexts: toCard.setDescription('An element of X.721:AdditionalInformation; - same value as fromCard: a single card is affected by the alarm - otherweise cards from fromCard to toCard are affected ')
fromPort = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)))
if mibBuilder.loadTexts: fromPort.setStatus('current')
if mibBuilder.loadTexts: fromPort.setDescription('An element of X.721:AdditionalInformation ')
toPort = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)))
if mibBuilder.loadTexts: toPort.setStatus('current')
if mibBuilder.loadTexts: toPort.setDescription('An element of X.721:AdditionalInformation; - same value as fromPort: a single port is affected by the alarm - otherweise ports from fromPort to toPort are affected ')
eventTime = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 14), DisplayString())
if mibBuilder.loadTexts: eventTime.setStatus('current')
if mibBuilder.loadTexts: eventTime.setDescription('An element of X.710: Parameter contains the time of generation of the event, if event time is sent from network element, otherwise it is the time of reception of the alarm by NetM The EventTime is a GeneralizedTime (defined in X.208), format is YYYYMMDDhhmmss.f+hhmm where Y year M month in year D day in month h hour in day (0-23) m minute in hour s second in minute f tenth part of second +hhmm local time offset(+-) to UTC time. Time represents the local time (t1), and the time differential (t2) enables UTC time to be determined as follows: UTC time = t1 - t2')
ipAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 15), DisplayString())
if mibBuilder.loadTexts: ipAddress.setStatus('current')
if mibBuilder.loadTexts: ipAddress.setDescription('An element of X.721:AdditionalInformation; indicates the source of the original SNMP trap.')
trapName = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 16), DisplayString())
if mibBuilder.loadTexts: trapName.setStatus('current')
if mibBuilder.loadTexts: trapName.setDescription('An element of X.721:AdditionalInformation; the name/OID of the original SNMP trap.')
specificProblems = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 17), DisplayString())
if mibBuilder.loadTexts: specificProblems.setStatus('current')
if mibBuilder.loadTexts: specificProblems.setDescription("corresponds to X.733:SpecificProblems; further refinements to the ProbableCause; example: the value of 'slmiAlarmStateReason' for an 'slmiAlarmStateTrap'.")
additionalText = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048)))
if mibBuilder.loadTexts: additionalText.setStatus('current')
if mibBuilder.loadTexts: additionalText.setDescription('This parameter allows the inclusion of a set of additional information in the event report.')
additionalInformation = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8192)))
if mibBuilder.loadTexts: additionalInformation.setStatus('current')
if mibBuilder.loadTexts: additionalInformation.setDescription('This parameter allows the inclusion of a set of additional information in the event report.')
backupStatus = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))))
if mibBuilder.loadTexts: backupStatus.setStatus('current')
if mibBuilder.loadTexts: backupStatus.setDescription('This parameter specifies whether or not the object emitting the alarm has been backed-up.')
backupObject = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 2), DisplayString())
if mibBuilder.loadTexts: backupObject.setStatus('current')
if mibBuilder.loadTexts: backupObject.setDescription('This parameter specifies the managed object instance that is providing backup services for the managed object about which the notification pertains.')
trendIndication = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("moresevere", 1), ("nochange", 2), ("lesssevere", 3))))
if mibBuilder.loadTexts: trendIndication.setStatus('current')
if mibBuilder.loadTexts: trendIndication.setDescription('This parameter, when present, specifies the current severity trend of the managed object.')
thresholdInformation = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 4), DisplayString())
if mibBuilder.loadTexts: thresholdInformation.setStatus('current')
if mibBuilder.loadTexts: thresholdInformation.setDescription('This parameter shall be present when the alarm is a result of crossing a threshold.')
correlatedEvents = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8192)))
if mibBuilder.loadTexts: correlatedEvents.setStatus('current')
if mibBuilder.loadTexts: correlatedEvents.setDescription('an ascii string containing comma-separated notifications, considered to be correlated.')
stateChanges = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 6), DisplayString())
if mibBuilder.loadTexts: stateChanges.setStatus('current')
if mibBuilder.loadTexts: stateChanges.setDescription('This parameter is used to indicate a state transition associated with the alarm.')
monitoredAttributes = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8192)))
if mibBuilder.loadTexts: monitoredAttributes.setStatus('current')
if mibBuilder.loadTexts: monitoredAttributes.setDescription('an ascii string containing comma-separated List of Monitored Attributes( attribute:value ).')
securityAlarmDetector = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 8), DisplayString())
if mibBuilder.loadTexts: securityAlarmDetector.setStatus('current')
if mibBuilder.loadTexts: securityAlarmDetector.setDescription('This attribute identifies the entity that detected the security alarm.')
serviceUser = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 9), DisplayString())
if mibBuilder.loadTexts: serviceUser.setStatus('current')
if mibBuilder.loadTexts: serviceUser.setDescription('This attribute contains information about the service user associated with the service request that caused the security alarm.')
serviceProvider = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 10), DisplayString())
if mibBuilder.loadTexts: serviceProvider.setStatus('current')
if mibBuilder.loadTexts: serviceProvider.setDescription('This attribute contains information about the service provider associated with the service request that caused the security alarm.')
listOfFaultyBoards = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8192)))
if mibBuilder.loadTexts: listOfFaultyBoards.setStatus('current')
if mibBuilder.loadTexts: listOfFaultyBoards.setDescription('PowerNode equipment alarms contain a list of faulty boards. This information exactly defines the boards, which must be considered for repair/replacement. An ascii string containing comma-separated items. Each item contains: Module_name:LocationName:RackID:ShelfID:PitchID')
mmnKey = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7, 1), DisplayString())
if mibBuilder.loadTexts: mmnKey.setStatus('current')
if mibBuilder.loadTexts: mmnKey.setDescription('This identifies the Help Topic for the OS Alarm in the OS Alarm Help file. The format of the MMN key for the Basic Components: BASE_<Component Code>_<Alarm number>')
thresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: thresholdValue.setStatus('current')
if mibBuilder.loadTexts: thresholdValue.setDescription('This attribute is relevant only for OS Threshold Alarms. - specifies the threshold value for any counter/monitored object, which is allowed and can be tolerated')
currentValue = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: currentValue.setStatus('current')
if mibBuilder.loadTexts: currentValue.setDescription('This attribute is relevant only for OS Threshold Alarms. - specifies the current value for the measurements, which has violated th threhold value of monitored measurements ')
summaryAlarms = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 201)).setObjects(("X733GROUP-MIB", "neName"), ("X733GROUP-MIB", "numberOfAlarms"), ("X733GROUP-MIB", "connectionReliable"), ("X733GROUP-MIB", "globalAlarmIds"))
if mibBuilder.loadTexts: summaryAlarms.setStatus('current')
if mibBuilder.loadTexts: summaryAlarms.setDescription('This trap will be sent periodically or after an explicit request via SNMP set. It is useful for these reasons: - to notice that the connection to NetM is reliable - to notice that the connection from NetM to an EWSD is reliable - to learn the names of EWSDs under control of NetM - to notice that traps got lost.')
spontaneousAlarms = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 202)).setObjects(("X733GROUP-MIB", "neName"), ("X733GROUP-MIB", "managedObjectClass"), ("X733GROUP-MIB", "notificationId"), ("X733GROUP-MIB", "severity"), ("X733GROUP-MIB", "eventType"), ("X733GROUP-MIB", "eventTime"), ("X733GROUP-MIB", "probableCause"), ("X733GROUP-MIB", "processingStatus"), ("X733GROUP-MIB", "alarmClass"), ("X733GROUP-MIB", "managedObjectInstance"), ("X733GROUP-MIB", "rack"), ("X733GROUP-MIB", "shelf"), ("X733GROUP-MIB", "fromCard"), ("X733GROUP-MIB", "toCard"), ("X733GROUP-MIB", "fromPort"), ("X733GROUP-MIB", "toPort"), ("X733GROUP-MIB", "originalAlarm"))
if mibBuilder.loadTexts: spontaneousAlarms.setStatus('current')
if mibBuilder.loadTexts: spontaneousAlarms.setDescription("Spontaneous Alarm from EWSD classic (MML). This trap will notify management systems after notifications from the EWSD classic. This trap type will be sent also in case of a 'resend' request. Each spontaneous alarm contains the variable binding 'originalAlarm' representing the original EWSD alarm. This information can be very large ( about 8 Kbyte).")
snmpAlarm = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 203)).setObjects(("X733GROUP-MIB", "neName"), ("X733GROUP-MIB", "notificationId"), ("X733GROUP-MIB", "severity"), ("X733GROUP-MIB", "eventType"), ("X733GROUP-MIB", "eventTime"), ("X733GROUP-MIB", "probableCause"), ("X733GROUP-MIB", "specificProblems"), ("X733GROUP-MIB", "managedObjectClass"), ("X733GROUP-MIB", "managedObjectInstance"), ("X733GROUP-MIB", "ipAddress"), ("X733GROUP-MIB", "trapName"), ("X733GROUP-MIB", "originalAlarm"))
if mibBuilder.loadTexts: snmpAlarm.setStatus('current')
if mibBuilder.loadTexts: snmpAlarm.setDescription("Spontaneous Alarm from EWSD InterNode or other SNMP managed devices. This trap will notify management systems after an SNMP alarm trap has been received by NetM. This trap type will be sent also in case of a 'resend' request. Each snmpAlarm trap contains the formatted output of the original SNMP trap in 'originalAlarm'.")
q3Alarm = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 204)).setObjects(("X733GROUP-MIB", "neName"), ("X733GROUP-MIB", "notificationId"), ("X733GROUP-MIB", "q3AlarmNumber"), ("X733GROUP-MIB", "severity"), ("X733GROUP-MIB", "eventType"), ("X733GROUP-MIB", "eventTime"), ("X733GROUP-MIB", "probableCause"), ("X733GROUP-MIB", "specificProblems"), ("X733GROUP-MIB", "managedObjectClass"), ("X733GROUP-MIB", "managedObjectInstance"), ("X733GROUP-MIB", "additionalText"), ("X733GROUP-MIB", "additionalInformation"), ("X733GROUP-MIB", "backupStatus"), ("X733GROUP-MIB", "backupObject"), ("X733GROUP-MIB", "trendIndication"), ("X733GROUP-MIB", "thresholdInformation"), ("X733GROUP-MIB", "correlatedEvents"), ("X733GROUP-MIB", "stateChanges"), ("X733GROUP-MIB", "monitoredAttributes"), ("X733GROUP-MIB", "securityAlarmDetector"), ("X733GROUP-MIB", "serviceUser"), ("X733GROUP-MIB", "serviceProvider"), ("X733GROUP-MIB", "listOfFaultyBoards"), ("X733GROUP-MIB", "originalAlarm"))
if mibBuilder.loadTexts: q3Alarm.setStatus('current')
if mibBuilder.loadTexts: q3Alarm.setDescription("Spontaneous Alarm from EWSD PowerNode. This trap will notify management systems after a Q3 alarm has been received from EWSD PowerNode. This trap type will be sent also in case of a 'resend' request. Each q3Alarm trap contains the formatted output of the original PowerNode trap in 'originalAlarm'. If the size of q3alarm exceeds 10KB, or one of the variables exceeds 8KB, 'q3alarm' is followed by 'q3contAlarm'. 'q3AlarmNumber' is 0 if the whole Q3 alarm is contained, or 9000 if it is continued with a 'q3contAlarm' sequence.")
q3contAlarm = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 205)).setObjects(("X733GROUP-MIB", "neName"), ("X733GROUP-MIB", "notificationId"), ("X733GROUP-MIB", "q3AlarmNumber"), ("X733GROUP-MIB", "correlatedEvents"), ("X733GROUP-MIB", "monitoredAttributes"), ("X733GROUP-MIB", "listOfFaultyBoards"), ("X733GROUP-MIB", "originalAlarm"))
if mibBuilder.loadTexts: q3contAlarm.setStatus('current')
if mibBuilder.loadTexts: q3contAlarm.setDescription("Continuation of a Q3 Alarm. If the size of the trap exceeds 10KB, or one of the variables exceeds 8KB, the next 'q3contAlarm' is generated. In 'q3AlarmNumber' there is the sequence number and a flag (9000) if it continues with a new 'q3contAlarm'.")
timeAckAlarms = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 206)).setObjects(("X733GROUP-MIB", "timePeriod"))
if mibBuilder.loadTexts: timeAckAlarms.setStatus('current')
if mibBuilder.loadTexts: timeAckAlarms.setDescription("A 'timeAckAlarms' trap is sent as acknowledgement for a 'setPeriod' set request.")
proxyStartUp = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 207))
if mibBuilder.loadTexts: proxyStartUp.setStatus('current')
if mibBuilder.loadTexts: proxyStartUp.setDescription("A 'proxyStartUp' trap is sent if the proxy comes up.")
countAlarm = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 208)).setObjects(("X733GROUP-MIB", "neName"), ("X733GROUP-MIB", "critical"), ("X733GROUP-MIB", "major"), ("X733GROUP-MIB", "minor"))
if mibBuilder.loadTexts: countAlarm.setStatus('current')
if mibBuilder.loadTexts: countAlarm.setDescription("Spontaneous or periodical trap, which contains the number of critical, major and minor alarms for a Network Element. Spontaneous: if the number of critical, major or minor alarms for a Network Element has changed. Periodical: depending on the setting of 'countAlarmPeriod'.")
osAlarm = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 209)).setObjects(("X733GROUP-MIB", "neName"), ("X733GROUP-MIB", "notificationId"), ("X733GROUP-MIB", "severity"), ("X733GROUP-MIB", "eventType"), ("X733GROUP-MIB", "eventTime"), ("X733GROUP-MIB", "probableCause"), ("X733GROUP-MIB", "managedObjectClass"), ("X733GROUP-MIB", "managedObjectInstance"), ("X733GROUP-MIB", "mmnKey"), ("X733GROUP-MIB", "additionalText"), ("X733GROUP-MIB", "thresholdValue"), ("X733GROUP-MIB", "currentValue"), ("X733GROUP-MIB", "securityAlarmDetector"), ("X733GROUP-MIB", "serviceUser"), ("X733GROUP-MIB", "serviceProvider"))
if mibBuilder.loadTexts: osAlarm.setStatus('current')
if mibBuilder.loadTexts: osAlarm.setDescription("Spontaneous OS Alarm from NetManager. This trap will notify management systems after a OS alarm has been generated from the NetManager. This trap type will be sent also in case of a 'resend' request. NeName is filled up with OS Name. Notification ID has form: OS_<AlarmID> ")
mibBuilder.exportSymbols("X733GROUP-MIB", managedObjectInstance=managedObjectInstance, commonGroup=commonGroup, listOfFaultyBoards=listOfFaultyBoards, proxyStartUp=proxyStartUp, additionalInformation=additionalInformation, managedObjectClass=managedObjectClass, osGroup=osGroup, timePeriod=timePeriod, toCard=toCard, correlatedEvents=correlatedEvents, originalAlarm=originalAlarm, sendSummary=sendSummary, shelf=shelf, fromPort=fromPort, q3AlarmNumber=q3AlarmNumber, backupStatus=backupStatus, q3contAlarm=q3contAlarm, processingStatus=processingStatus, toPort=toPort, mmnKey=mmnKey, eventTime=eventTime, spontaneousAlarms=spontaneousAlarms, osAlarm=osAlarm, neName=neName, summaryAlarms=summaryAlarms, countAlarm=countAlarm, trendIndication=trendIndication, probableCause=probableCause, countAlarmSpontan=countAlarmSpontan, rack=rack, q3Group=q3Group, sendAllAlarms=sendAllAlarms, siemensUnits=siemensUnits, critical=critical, currentValue=currentValue, ipAddress=ipAddress, connectionReliable=connectionReliable, minor=minor, thresholdInformation=thresholdInformation, alarmClass=alarmClass, miscGroup=miscGroup, additionalText=additionalText, PYSNMP_MODULE_ID=ewsdAlarms, oenProductMibs=oenProductMibs, serviceProvider=serviceProvider, summaryGroup=summaryGroup, x733Group=x733Group, sni=sni, trapName=trapName, major=major, specificProblems=specificProblems, thresholdValue=thresholdValue, q3Alarm=q3Alarm, fromCard=fromCard, stateChanges=stateChanges, countAlarmPeriod=countAlarmPeriod, notificationId=notificationId, numberOfAlarms=numberOfAlarms, ncProxy=ncProxy, alarmSpontan=alarmSpontan, controlGroup=controlGroup, ewsdAlarms=ewsdAlarms, globalAlarmIds=globalAlarmIds, backupObject=backupObject, resendAlarm=resendAlarm, serviceUser=serviceUser, eventType=eventType, severity=severity, snmpAlarm=snmpAlarm, nms=nms, timeAckAlarms=timeAckAlarms, securityAlarmDetector=securityAlarmDetector, setPeriod=setPeriod, monitoredAttributes=monitoredAttributes)
