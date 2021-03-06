#
# PySNMP MIB module HP-ICF-FAULT-FINDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-FAULT-FINDER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:33:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
PhysicalIndex, PhysicalClass = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "PhysicalClass")
hpicfObjectModules, hpicfCommonTrapsPrefix, hpicfCommon = mibBuilder.importSymbols("HP-ICF-OID", "hpicfObjectModules", "hpicfCommonTrapsPrefix", "hpicfCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, Bits, NotificationType, TimeTicks, ModuleIdentity, ObjectIdentity, Gauge32, IpAddress, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Bits", "NotificationType", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Gauge32", "IpAddress", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
hpicfFaultFinderMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12))
hpicfFaultFinderMib.setRevisions(('2015-08-04 14:12', '2013-08-21 00:00', '2010-01-25 20:24', '2009-05-22 00:00', '2009-02-25 13:31', '2007-01-09 14:56', '2005-05-02 19:34', '2005-03-22 11:30', '2003-07-28 07:07', '2000-11-03 07:07', '1998-11-20 23:50', '1997-10-21 02:49',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfFaultFinderMib.setRevisionsDescriptions(('Added hpicfFfLinkFlapControlPortConfig to hpicfFaultFinder.', 'Added hpicfFfBcastStormControlPortConfig to hpicfFaultFinder.', 'Added hpicfFfFaultLightStatus to return the fault light status.', 'Added intel82566dmportprotect to hpicfFaultType.', "Added link-flap fault-id in the existing fault-id's. The maximum tolerance value is 10,6 and 3 for low, medium and high sensitivity.", 'Added hpicfFfLogPhysEntity to hpicfFaultFinderTrap.', 'Added 3 new Transceiver related fault messages.', 'Added Transceiver related fault messages, jumbos/flow control fault. Also added Connection-Rate-Filtering fault type to extend support for virus throttling.', 'Add duplexMismatch type. Update division name.', 'Add lossOfStackMember and hotSwapReboot fault types. Update division name.', "Added several fault types, and the ability to reduce a port's speed as one of the actions to take on a fault.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpicfFaultFinderMib.setLastUpdated('201508041412Z')
if mibBuilder.loadTexts: hpicfFaultFinderMib.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfFaultFinderMib.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfFaultFinderMib.setDescription('This MIB module contains object definitions for managing the Fault Finder feature in web-capable HP devices.')
hpicfFaultFinder = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7))
class HpicfFaultType(TextualConvention, Integer32):
    description = 'An enumerated value which indicates a type of fault which is monitored by the agent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("badDriver", 1), ("badXcvr", 2), ("badCable", 3), ("tooLongCable", 4), ("overBandwidth", 5), ("bcastStorm", 6), ("partition", 7), ("misconfiguredSQE", 8), ("polarityReversal", 9), ("networkLoop", 10), ("lossOfLink", 11), ("portSecurityViolation", 12), ("backupLinkTransition", 13), ("meshingFault", 14), ("fanFault", 15), ("rpsFault", 16), ("stuck10MbFault", 17), ("lossOfStackMember", 18), ("hotSwapReboot", 19), ("duplexMismatchHDX", 20), ("duplexMismatchFDX", 21), ("flowcntlJumbosFault", 22), ("portSelftestFailure", 23), ("xcvrUnidentified", 24), ("xcvrUnsupported", 25), ("crfNotify", 26), ("crfThrottled", 27), ("crfBlocked", 28), ("xcvrNotYetSupported", 29), ("xcvrBRevOnly", 30), ("xcvrNotSupportedOnPort", 31), ("phyReadFailure", 32), ("linkFlap", 33), ("intel82566dmportprotect", 34), ("xcvrExceedQty", 35), ("xcvrClone", 36), ("xcvrCloneReminder", 37), ("bcastStormPerPort", 38), ("linkFlapPerPort", 39), ("rxNonStdPreamble", 40))

class HpicfFaultTolerance(TextualConvention, Integer32):
    description = 'Objects of this type are used to scale internal fault thresholds between hard-coded minimum and maximum threshold values as follows: actual = min + ((max - min) * tol)/maxTol where: actual - actual threshold used by Fault Finder min - minimum threshold for this fault max - maximum threshold for this fault tol - configured tolerance for this fault maxTol - maximum tolerance value (255)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class HpicfFaultAction(TextualConvention, Integer32):
    description = 'Objects of this type are used to indicate actions taken on detection of a fault.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("warn", 2), ("warnAndDisable", 3), ("warnAndSpeedReduce", 4), ("warnAndSpeedReduceAndDisable", 5))

class HpicfUrlString(TextualConvention, OctetString):
    description = 'This TC describes an object which holds a reference to a (remote) resource by using the Uniform Resource Locator (URL) notation as defined in RFC 1738. The allowed character set and the encoding rules for this textual convention are defined in RFC 1738 section 2.2.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

hpicfFfControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1), )
if mibBuilder.loadTexts: hpicfFfControlTable.setStatus('current')
if mibBuilder.loadTexts: hpicfFfControlTable.setDescription('This table contains one entry per fault type that this agent is capable of monitoring.')
hpicfFfControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfControlIndex"))
if mibBuilder.loadTexts: hpicfFfControlEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfFfControlEntry.setDescription('Configuration information for a particular fault type.')
hpicfFfControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 1), HpicfFaultType())
if mibBuilder.loadTexts: hpicfFfControlIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfFfControlIndex.setDescription('The type of fault for which this entry contains configuration information.')
hpicfFfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 2), HpicfFaultAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfAction.setStatus('current')
if mibBuilder.loadTexts: hpicfFfAction.setDescription("This object is used to configure the action, if any, to be taken if a fault of this type is detected by the agent. Setting an instance of this object to 'none' will clear any previous state of the associated fault on all ports. This object is used to enable or disable the port disable feature for this fault type. Setting this object to 'warnAndDisable' will enable the port disable feature for this fault type. This feature is intended to allow an agent to disable ports that are being disruptive to the rest of the network. Note that not all agents will support setting this object to 'warnAndDisable'. The agent may choose not to disable a particular port for a particular fault based on its knowledge of if/how that fault disrupts the network.")
hpicfFfWarnTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 3), HpicfFaultTolerance()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfWarnTolerance.setStatus('current')
if mibBuilder.loadTexts: hpicfFfWarnTolerance.setDescription('The tolerance level used to calculate the fault warning threshold for this fault type. The agent will periodically check relevant statistics for each port for each type of fault. If the warning threshold has been exceeded, and fault warning action is enabled for that fault type, an hpicfFaultFinderTrap notification will be sent. In addition, an entry will be made in the hpicfFfLogTable for the fault. Once a fault warning has fired, a hysteresis mechanism assures that another warning will not be fired until the relevant counter drops below a hysteresis threshold value.')
hpicfFfDisablePortTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 4), HpicfFaultTolerance()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfDisablePortTolerance.setStatus('current')
if mibBuilder.loadTexts: hpicfFfDisablePortTolerance.setDescription('The tolerance level used to calculate the port disable threshold for this fault type. The value of an instance of this object MUST be greater than the value of the corresponding instance of the hpicfFfWarnTolerance. The agent will periodically check relevant statistics for each port for each type of fault. If the port disable threshold has been exceeded, and port disable is enabled for that fault type, an hpicfFaultFinderTrap notification will be sent. In addition, an entry will be made in the hpicfFfLogTable for the fault. Ports will not be disabled until at least one polling interval after a warning has fired. In addition, the agent may further delay disabling a port in certain situations. For example, it may choose to delay disabling a cascade port to give the cascaded device a chance to correct the problem.')
hpicfFfSpeedReduceTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 1, 1, 5), HpicfFaultTolerance()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfSpeedReduceTolerance.setStatus('current')
if mibBuilder.loadTexts: hpicfFfSpeedReduceTolerance.setDescription('The tolerance level used to calculate the speed reduction threshold for this fault type. The value of an instance of this object MUST be greater than the value of the corresponding instance of the hpicfFfWarnTolerance, and less than or equal to the corresponding instance of hpicfFfDisablePortTolerance. The agent will only reduce speed on a port if auto-negotiation has been performed, and the partners link abilities allow operation at a slower media speed. The agent will periodically check relevant statistics for each port for each type of fault. If the speed reduction threshold has been exceeded, and speed reduction option is enabled for that fault type, an hpicfFaultFinderTrap notification will be sent. In addition, an entry will be made in the hpicfFfLogTable for the fault. The agent may elect not to reduce speed or delay speed reduction of certain ports. For example, it may choose to delay taking action on a cascade port to give the cascaded device a chance to correct the problem.')
hpicfFfLogTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2), )
if mibBuilder.loadTexts: hpicfFfLogTable.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogTable.setDescription('A log of fault warnings and ports disabled by the Fault Finder.')
hpicfFfLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogIndex"))
if mibBuilder.loadTexts: hpicfFfLogEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogEntry.setDescription('An entry in the Fault Finder log, containing information about a single fault.')
hpicfFfLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpicfFfLogIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogIndex.setDescription('An arbitrary value which uniquely identifies this log entry. The index for a particular log entry must not change, even though entries with lower valued indices have been deleted.')
hpicfFfLogCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogCreateTime.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogCreateTime.setDescription('The value of sysUpTime when this log entry was added to the hpicfFfLogTable.')
hpicfFfLogPhysEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 3), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogPhysEntity.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogPhysEntity.setDescription('The entPhysicalIndex of the device port or other physical component on which the fault was detected. On agents which do not implement the Entity MIB, this will contain the ifIndex of the offending port.')
hpicfFfLogFaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 4), HpicfFaultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogFaultType.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogFaultType.setDescription('The type of fault which was detected on the physical entity indicated by hpicfFfLogPhysEntity.')
hpicfFfLogAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 5), HpicfFaultAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogAction.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogAction.setDescription('The action, if any, that was taken by the agent when this fault was detected.')
hpicfFfLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("informational", 1), ("medium", 2), ("critical", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogSeverity.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogSeverity.setDescription("The severity level of the fault. Port disables will always be logged as 'critical'. An agent may need to remove faults from the fault log in order to reclaim resources. If so, it must remove lower severity faults before removing higher severity faults. Faults at the same severity level should be removed from oldest to newest.")
hpicfFfLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("new", 1), ("active", 2), ("old", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLogStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogStatus.setDescription("Log entries will initially be created with the value 'new'. A manager cannot set this object to 'new'. Setting this object to 'active' indicates that the fault has been displayed to a user. Setting this object to 'old' indicates that the agent should remove this fault from the log.")
hpicfFfLogPhysClass = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 8), PhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogPhysClass.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogPhysClass.setDescription('The PhysicalClass as defined by Entity MIB to which this hpicfFfLogPhysIndex belongs. ')
hpicfFfLogInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4Address", 1), ("displayString", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogInfoType.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogInfoType.setDescription("This field can be used to indicate the class of information that 'hpicfFfLogInfo' holds")
hpicfFfLogInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfLogInfo.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLogInfo.setDescription('This can be used to hold any relevant information about the current fault')
hpicfFfFaultInfoURL = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 3), HpicfUrlString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfFfFaultInfoURL.setStatus('current')
if mibBuilder.loadTexts: hpicfFfFaultInfoURL.setDescription('A URL which a management station can use to access additional information about the fault which triggered the notification in which this object was sent.')
hpicfFfFaultLightStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("faultLightOff", 1), ("faultLightOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFfFaultLightStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfFfFaultLightStatus.setDescription('This indicates the current state of the switch fault light. Examples of faults that could cause the LED to be turned on include fan, power supply, and port link failures.')
hpicfFfBcastStormControlPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5))
hpicfFfBcastStormControlPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1), )
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortConfigTable.setDescription('This table provides information about Broadcast Storm control configuration of all ports.')
hpicfFfBcastStormControlPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlPortIndex"))
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortConfigEntry.setDescription('This object provides information about Broadcast Storm Control configuration of each port.')
hpicfFfBcastStormControlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortIndex.setDescription('The ifIndex value which uniquely identifies a row in the Interfaces Table.')
hpicfFfBcastStormControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("bcastRisingLevelpercent", 2), ("bcastRisingLevelpps", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlMode.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlMode.setDescription('The Broadcast Storm Control mode of a port. A value of disable (1) indicates that no rising threshold value is set for broadcast storm traffic on this port. A value of bcastRisingLevelpercent (2) indicates that the rising threshold rate for broadcast storm traffic is configured in percentage of port bandwidth. A value of bcastRisinglevelpps(3) indicates that the rising threshold rate for broadcast storm traffic is configured in packets per second.')
hpicfFfBcastStormControlRisingpercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlRisingpercent.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlRisingpercent.setDescription('This is the rising threshold Level in percent of bandwidth of the port. hpicfFfBcastStormControlAction occurs when broadcast traffic reaches this level.')
hpicfFfBcastStormControlRisingpps = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlRisingpps.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlRisingpps.setDescription('This object indicates the rising threshold for Broadcast Storm Control. This value is in packets-per-second of received broadcast traffic. hpicfFfBcastStormControlAction object takes action when broadcast traffic reaches this level.')
hpicfFfBcastStormControlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("warn", 2), ("warnAndDisable", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlAction.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlAction.setDescription('This object defines the action taken by the switch when a broadcast storm occurs on a port. A value of none (1) indicates that no action is performed. A value of warn (2) indicates that an event is logged when broadcast traffic crosses the threshold value set on that port. A value of warnAndDisable (3) indicates that the port is disabled and an event is logged as soon as the broadcast traffic reaches the threshold value set on that port.')
hpicfFfBcastStormControlPortDisableTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 5, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortDisableTimer.setStatus('current')
if mibBuilder.loadTexts: hpicfFfBcastStormControlPortDisableTimer.setDescription('This object specifies the time period for which the port remains in disabled state. A port is disabled when broadcast traffic reaches the threshold value set on that port. This time period is specified in seconds. The default value is zero which means that the port remains disabled and is not enabled again.')
hpicfFfLinkFlapControlPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6))
hpicfFfLinkFlapControlPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1), )
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortConfigTable.setDescription('This table provides information about Link Flapping control configuration of all ports.')
hpicfFfLinkFlapControlPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1), ).setIndexNames((0, "HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlPortIndex"))
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortConfigEntry.setDescription('This object provides information about Link Flapping Control configuration of each port.')
hpicfFfLinkFlapControlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortIndex.setDescription('The ifIndex value which uniquely identifies a row in the Interfaces Table.')
hpicfFfLinkFlapControlSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 6, 10))).clone(namedValues=NamedValues(("none", 0), ("high", 3), ("medium", 6), ("low", 10))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLinkFlapControlSensitivity.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLinkFlapControlSensitivity.setDescription('The Link Flapping Control sensitivity of a port. A value of low (1) indicates that the sensitivity of the link flap threshold is set to 10 link flaps per 10 second interval. A value of medium (2) indicates that the sensitivity of the link flap threshold is set to 6 link flaps per 10 second interval. A value of high (3) indicates that the sensitivity of the link flap threshold is set to 3 link flaps per 10 second interval.')
hpicfFfLinkFlapControlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("warn", 2), ("warnAndDisable", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLinkFlapControlAction.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLinkFlapControlAction.setDescription('This object defines the action taken by the switch when link flaps occurs on a port. A value of none (1) indicates that no action is performed. A value of warn (2) indicates that an event is logged when the number of link flaps crosses the threshold rate set on that port. A value of warnAndDisable (3) indicates that the port is disabled and an event is logged as soon as the number of link flaps reaches the threshold rate set on that port.')
hpicfFfLinkFlapControlPortDisableTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7, 6, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortDisableTimer.setStatus('current')
if mibBuilder.loadTexts: hpicfFfLinkFlapControlPortDisableTimer.setDescription('This object specifies the time period for which the port remains in disabled state. A port is disabled when the number of link flaps reaches the threshold rate set on that port. This time period is specified in seconds. The default value is zero which means that the port remains disabled and is not enabled again.')
hpicfFaultFinderTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 5)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogFaultType"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogSeverity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultInfoURL"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysEntity"))
if mibBuilder.loadTexts: hpicfFaultFinderTrap.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultFinderTrap.setDescription('This notification is sent whenever the Fault Finder creates an entry in the hpicfFfLogTable.')
hpicfFaultFinderConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1))
hpicfFaultFinderCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1))
hpicfFaultFinderGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2))
hpicfFaultFinderCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 1)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfigGroup"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultLogGroup"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinderCompliance = hpicfFaultFinderCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultFinderCompliance.setDescription('The compliance statement for devices implementing the HP Fault Finder capability.')
hpicfFaultFinder2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 2)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfig2Group"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultLogGroup"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinder2Compliance = hpicfFaultFinder2Compliance.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultFinder2Compliance.setDescription('The compliance statement for devices implementing the HP Fault Finder capability.')
hpicfFaultStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 3)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultStatusCompliance = hpicfFaultStatusCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultStatusCompliance.setDescription('The compliance statement for devices implementing the switch fault status.')
hpicfFaultFinder3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 4)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfig3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinder3Compliance = hpicfFaultFinder3Compliance.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultFinder3Compliance.setDescription('The compliance statement for devices implementing the HP Fault Finder capability.')
hpicfFaultFinder4Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 1, 5)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultConfig4Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultFinder4Compliance = hpicfFaultFinder4Compliance.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultFinder4Compliance.setDescription('The compliance statement for devices implementing the HP Fault Finder capability.')
hpicfFaultConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 1)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfWarnTolerance"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfDisablePortTolerance"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfigGroup = hpicfFaultConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultConfigGroup.setDescription('A collection of objects for configuring the Fault Finder feature.')
hpicfFaultLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 2)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogCreateTime"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysEntity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogFaultType"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogSeverity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogStatus"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultInfoURL"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogPhysClass"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogInfoType"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLogInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultLogGroup = hpicfFaultLogGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultLogGroup.setDescription('A collection of objects for accessing the log of discovered faults.')
hpicfFaultNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 3)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFaultFinderTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultNotifyGroup = hpicfFaultNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultNotifyGroup.setDescription('A collection of notifications used to indicate the discovery of a network fault.')
hpicfFaultConfig2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 4)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfWarnTolerance"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfDisablePortTolerance"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfSpeedReduceTolerance"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfig2Group = hpicfFaultConfig2Group.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultConfig2Group.setDescription("A collection of objects for configuring the Fault Finder feature, including the ability to reduce a port's media speed in the event of a fault.")
hpicfFaultStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 5)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfFaultLightStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultStatusGroup = hpicfFaultStatusGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultStatusGroup.setDescription('A collection of objects used to indicate fault status.')
hpicfFaultConfig3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 6)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlMode"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlRisingpercent"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlRisingpps"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfBcastStormControlPortDisableTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfig3Group = hpicfFaultConfig3Group.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultConfig3Group.setDescription('A collection of objects for configuring the Fault Finder broadcast storm feature on a per per port basis, including the ability to disable a port in the event of a fault.')
hpicfFaultConfig4Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12, 1, 2, 7)).setObjects(("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlSensitivity"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlAction"), ("HP-ICF-FAULT-FINDER-MIB", "hpicfFfLinkFlapControlPortDisableTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFaultConfig4Group = hpicfFaultConfig4Group.setStatus('current')
if mibBuilder.loadTexts: hpicfFaultConfig4Group.setDescription('A collection of objects for configuring the Fault Finder Link Flap feature on a per per port basis, including the ability to disable a port in the event of a fault.')
mibBuilder.exportSymbols("HP-ICF-FAULT-FINDER-MIB", hpicfFfLogFaultType=hpicfFfLogFaultType, hpicfFaultConfig4Group=hpicfFaultConfig4Group, HpicfFaultType=HpicfFaultType, hpicfFfLogInfoType=hpicfFfLogInfoType, hpicfFfLogIndex=hpicfFfLogIndex, hpicfFfBcastStormControlPortConfigTable=hpicfFfBcastStormControlPortConfigTable, hpicfFaultFinderConformance=hpicfFaultFinderConformance, hpicfFfBcastStormControlRisingpps=hpicfFfBcastStormControlRisingpps, hpicfFfBcastStormControlPortConfigEntry=hpicfFfBcastStormControlPortConfigEntry, hpicfFaultConfigGroup=hpicfFaultConfigGroup, hpicfFaultFinder3Compliance=hpicfFaultFinder3Compliance, hpicfFaultFinderMib=hpicfFaultFinderMib, hpicfFaultConfig2Group=hpicfFaultConfig2Group, hpicfFfLinkFlapControlPortIndex=hpicfFfLinkFlapControlPortIndex, HpicfFaultTolerance=HpicfFaultTolerance, hpicfFfLogPhysClass=hpicfFfLogPhysClass, hpicfFaultFinderGroups=hpicfFaultFinderGroups, hpicfFaultFinderCompliances=hpicfFaultFinderCompliances, hpicfFaultNotifyGroup=hpicfFaultNotifyGroup, hpicfFaultConfig3Group=hpicfFaultConfig3Group, hpicfFaultFinder2Compliance=hpicfFaultFinder2Compliance, hpicfFfLinkFlapControlSensitivity=hpicfFfLinkFlapControlSensitivity, hpicfFfLinkFlapControlAction=hpicfFfLinkFlapControlAction, hpicfFfLogAction=hpicfFfLogAction, hpicfFfLogCreateTime=hpicfFfLogCreateTime, hpicfFaultFinder=hpicfFaultFinder, hpicfFfFaultLightStatus=hpicfFfFaultLightStatus, hpicfFfBcastStormControlPortDisableTimer=hpicfFfBcastStormControlPortDisableTimer, hpicfFfLinkFlapControlPortConfigEntry=hpicfFfLinkFlapControlPortConfigEntry, hpicfFaultFinder4Compliance=hpicfFaultFinder4Compliance, hpicfFfControlTable=hpicfFfControlTable, hpicfFfWarnTolerance=hpicfFfWarnTolerance, hpicfFfLogSeverity=hpicfFfLogSeverity, hpicfFfAction=hpicfFfAction, hpicfFfDisablePortTolerance=hpicfFfDisablePortTolerance, hpicfFfLogTable=hpicfFfLogTable, hpicfFfBcastStormControlMode=hpicfFfBcastStormControlMode, HpicfFaultAction=HpicfFaultAction, hpicfFfControlIndex=hpicfFfControlIndex, hpicfFfLogStatus=hpicfFfLogStatus, hpicfFaultStatusGroup=hpicfFaultStatusGroup, hpicfFfLogEntry=hpicfFfLogEntry, hpicfFfBcastStormControlRisingpercent=hpicfFfBcastStormControlRisingpercent, PYSNMP_MODULE_ID=hpicfFaultFinderMib, hpicfFfLogPhysEntity=hpicfFfLogPhysEntity, HpicfUrlString=HpicfUrlString, hpicfFfLogInfo=hpicfFfLogInfo, hpicfFfLinkFlapControlPortConfig=hpicfFfLinkFlapControlPortConfig, hpicfFfSpeedReduceTolerance=hpicfFfSpeedReduceTolerance, hpicfFaultStatusCompliance=hpicfFaultStatusCompliance, hpicfFfFaultInfoURL=hpicfFfFaultInfoURL, hpicfFaultFinderTrap=hpicfFaultFinderTrap, hpicfFfBcastStormControlPortIndex=hpicfFfBcastStormControlPortIndex, hpicfFfBcastStormControlPortConfig=hpicfFfBcastStormControlPortConfig, hpicfFfLinkFlapControlPortConfigTable=hpicfFfLinkFlapControlPortConfigTable, hpicfFfControlEntry=hpicfFfControlEntry, hpicfFfLinkFlapControlPortDisableTimer=hpicfFfLinkFlapControlPortDisableTimer, hpicfFfBcastStormControlAction=hpicfFfBcastStormControlAction, hpicfFaultLogGroup=hpicfFaultLogGroup, hpicfFaultFinderCompliance=hpicfFaultFinderCompliance)
