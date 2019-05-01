#
# PySNMP MIB module BAY-STACK-VRRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-VRRP-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ipAdEntAddr, = mibBuilder.importSymbols("IP-MIB", "ipAdEntAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, TimeTicks, Integer32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, NotificationType, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "TimeTicks", "Integer32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "NotificationType", "ModuleIdentity", "Counter32")
MacAddress, RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
vrrpOperPrimaryIpAddr, vrrpOperVrId = mibBuilder.importSymbols("VRRP-MIB", "vrrpOperPrimaryIpAddr", "vrrpOperVrId")
bayStackVrrpExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 11))
bayStackVrrpExtMib.setRevisions(('2005-07-01 00:00', '2012-10-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackVrrpExtMib.setRevisionsDescriptions(('v1: Initial version.', 'v2: Added new value reboot(16) to object bsveVrrpTrapStateTransitionCause.',))
if mibBuilder.loadTexts: bayStackVrrpExtMib.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: bayStackVrrpExtMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: bayStackVrrpExtMib.setContactInfo('Nortel Networks')
if mibBuilder.loadTexts: bayStackVrrpExtMib.setDescription("Nortel Networks VRRP Extension MIB Copyright 2005 Nortel Networks, Inc. All rights reserved. This Nortel Networks SNMP Management Information Base Specification embodies Nortel Networks' confidential and proprietary intellectual property. Nortel Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
bsveNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 11, 0))
bsveObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 11, 1))
bsveScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 1))
bsveVrrpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpEnabled.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpEnabled.setDescription('Indicates whether VRRP is globally enabled for the system.')
bsveVrrpPingVirtualAddrEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpPingVirtualAddrEnabled.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpPingVirtualAddrEnabled.setDescription("Indicates whether this device should respond to pings directed to a virtual router's IP address.")
bsveVrrpOperExtTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2), )
if mibBuilder.loadTexts: bsveVrrpOperExtTable.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtTable.setDescription('Extensions to the vrrpOperTable from RFC 2787.')
bsveVrrpOperExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"))
if mibBuilder.loadTexts: bsveVrrpOperExtEntry.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtEntry.setDescription('A set of objects that augments the vrrpOperTable.')
bsveVrrpOperExtCriticalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpOperExtCriticalIpAddr.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtCriticalIpAddr.setDescription('IP address of the interface that will cause a shutdown event.')
bsveVrrpOperExtCriticalIpAddrEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpOperExtCriticalIpAddrEnabled.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtCriticalIpAddrEnabled.setDescription('Indicates whether the user-defined critical IP address is enabled. If the user-defined critical IP address is not enabled, a default critical IP address of 0.0.0.0 will be used. No effect if an user-defined IP address does not exist.')
bsveVrrpOperExtHoldDownTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 21600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpOperExtHoldDownTimer.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtHoldDownTimer.setDescription('Used to configure the amount of time (in seconds) to wait before preempting the current vrrp master.')
bsveVrrpOperExtHoldDownState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dormant", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsveVrrpOperExtHoldDownState.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtHoldDownState.setDescription("Used to indicate the hold-down state of this vrrp interface. If the hold-down timer is operational this variable will be set to 'active'. 'dormant' otherwise.")
bsveVrrpOperExtHoldDownTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 21600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsveVrrpOperExtHoldDownTimeRemaining.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtHoldDownTimeRemaining.setDescription('Used to indicate the amount of time (in seconds) left before the bsveVrrpOperExtHoldDownTimer will expire.')
bsveVrrpOperExtAction = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("preemptHoldDownTimer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpOperExtAction.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtAction.setDescription('Used to trigger an action on this vrrp interface.')
bsveVrrpOperExtBackUpMasterEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpOperExtBackUpMasterEnabled.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtBackUpMasterEnabled.setDescription('')
bsveVrrpOperExtBackUpMasterState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsveVrrpOperExtBackUpMasterState.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtBackUpMasterState.setDescription('')
bsveVrrpOperExtFasterAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 1000)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpOperExtFasterAdvInterval.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtFasterAdvInterval.setDescription('This is the faster advertisement interval, in milliseconds, between sending advertisement messages. When the faster advertisement interval enable is checked, the faster advertisement interval is being used instead of the regular advertisement interval')
bsveVrrpOperExtFasterAdvIntervalEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsveVrrpOperExtFasterAdvIntervalEnabled.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpOperExtFasterAdvIntervalEnabled.setDescription("Used to indicate if the Faster Advertisement Interval should be used. 'Disable' means use regular Advertisement interval.")
bsveNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 4))
bsveVrrpTrapStateTransitionType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("none", 1), ("masterToBackup", 2), ("backupToMaster", 3), ("initializeToMaster", 4), ("masterToInitialize", 5), ("initializeToBackup", 6), ("backupToInitialize", 7), ("backupToBackUpMaster", 8), ("backUpMasterToBackup", 9)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsveVrrpTrapStateTransitionType.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpTrapStateTransitionType.setDescription('Potential types of state transitions. Used by bsveVrrpTrapStateTransition trap.')
bsveVrrpTrapStateTransitionCause = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 11, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("none", 1), ("higherPriorityAdvertizeReceived", 2), ("shutdownReceived", 3), ("vrrpAddrAndPhysicalAddrMatch", 4), ("masterDownInterval", 5), ("preempted", 6), ("criticalIPFail", 7), ("usrConfig", 8), ("syncFromPrimary", 9), ("iPInterfaceDown", 10), ("lowerPrioAdvReceived", 11), ("higherSrcIPEqualPrioAdvReceived", 12), ("lowerSrcIPEqualPrioAdvReceived", 13), ("startVR", 14), ("other", 15), ("reboot", 16)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsveVrrpTrapStateTransitionCause.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpTrapStateTransitionCause.setDescription('Potential types of causes that will generate a bsveVrrpTrapStateTransition trap.')
bsveVrrpTrapStateTransition = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 11, 0, 1)).setObjects(("BAY-STACK-VRRP-EXT-MIB", "bsveVrrpTrapStateTransitionType"), ("BAY-STACK-VRRP-EXT-MIB", "bsveVrrpTrapStateTransitionCause"), ("VRRP-MIB", "vrrpOperPrimaryIpAddr"), ("IP-MIB", "ipAdEntAddr"))
if mibBuilder.loadTexts: bsveVrrpTrapStateTransition.setStatus('current')
if mibBuilder.loadTexts: bsveVrrpTrapStateTransition.setDescription('A vrrpTrapStateTransition trap signifies a state transition has occurred on a particular vrrp interface. Implementation of this trap is optional.')
mibBuilder.exportSymbols("BAY-STACK-VRRP-EXT-MIB", bsveObjects=bsveObjects, bayStackVrrpExtMib=bayStackVrrpExtMib, bsveVrrpOperExtFasterAdvInterval=bsveVrrpOperExtFasterAdvInterval, bsveScalars=bsveScalars, bsveVrrpOperExtHoldDownState=bsveVrrpOperExtHoldDownState, bsveNotificationObjects=bsveNotificationObjects, bsveVrrpOperExtCriticalIpAddrEnabled=bsveVrrpOperExtCriticalIpAddrEnabled, bsveVrrpOperExtHoldDownTimer=bsveVrrpOperExtHoldDownTimer, bsveVrrpOperExtHoldDownTimeRemaining=bsveVrrpOperExtHoldDownTimeRemaining, bsveVrrpOperExtCriticalIpAddr=bsveVrrpOperExtCriticalIpAddr, bsveVrrpTrapStateTransition=bsveVrrpTrapStateTransition, bsveVrrpOperExtAction=bsveVrrpOperExtAction, bsveVrrpOperExtTable=bsveVrrpOperExtTable, bsveVrrpOperExtBackUpMasterEnabled=bsveVrrpOperExtBackUpMasterEnabled, bsveNotifications=bsveNotifications, bsveVrrpPingVirtualAddrEnabled=bsveVrrpPingVirtualAddrEnabled, PYSNMP_MODULE_ID=bayStackVrrpExtMib, bsveVrrpTrapStateTransitionType=bsveVrrpTrapStateTransitionType, bsveVrrpOperExtEntry=bsveVrrpOperExtEntry, bsveVrrpOperExtFasterAdvIntervalEnabled=bsveVrrpOperExtFasterAdvIntervalEnabled, bsveVrrpOperExtBackUpMasterState=bsveVrrpOperExtBackUpMasterState, bsveVrrpEnabled=bsveVrrpEnabled, bsveVrrpTrapStateTransitionCause=bsveVrrpTrapStateTransitionCause)
