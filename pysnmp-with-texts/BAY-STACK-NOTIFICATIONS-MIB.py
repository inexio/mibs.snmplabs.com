#
# PySNMP MIB module BAY-STACK-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-NOTIFICATIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
bayStackConfigExpectedStackSize, bayStackUnitConfigIndex = mibBuilder.importSymbols("BAY-STACK-MIB", "bayStackConfigExpectedStackSize", "bayStackUnitConfigIndex")
dot1xAuthPaeState, dot1xAuthBackendAuthState = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthPaeState", "dot1xAuthBackendAuthState")
ifIndex, InterfaceIndex, ifAdminStatus = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "ifAdminStatus")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
s5AgSysUsbTargetUnit, s5AgentScriptStatus = mibBuilder.importSymbols("S5-AGENT-MIB", "s5AgSysUsbTargetUnit", "s5AgentScriptStatus")
s5ChasComType, = mibBuilder.importSymbols("S5-CHASSIS-MIB", "s5ChasComType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Bits, Counter32, iso, TimeTicks, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "iso", "TimeTicks", "Integer32", "IpAddress")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackNotificationsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 2))
bayStackNotificationsMib.setRevisions(('2014-07-07 00:00', '2014-01-27 00:00', '2013-10-11 00:00', '2013-08-22 00:00', '2013-03-19 00:00', '2012-09-04 00:00', '2012-08-22 00:00', '2012-08-16 00:00', '2012-06-21 00:00', '2012-06-20 00:00', '2011-11-30 00:00', '2010-12-21 00:00', '2009-09-28 00:00', '2008-07-09 00:00', '2008-03-31 00:00', '2007-03-05 00:00', '2006-04-06 00:00', '2006-04-04 00:00', '2005-08-22 00:00', '2005-06-30 00:00', '2005-03-26 00:00', '2004-08-06 00:00', '2004-08-02 00:00', '2004-07-20 00:00', '2003-03-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackNotificationsMib.setRevisionsDescriptions(('Version 28: Added bsnAaaUserPasswordExpired', 'Version 27: Added bsnAAAUserName, bsnAaaUserAccountNotUsed, bsnAaaAlreadyConnected, bsnAaaIncorrectLogOnThresholdExceeded, bsnAaaMaxNoOfSessionsExceeded, bsnAuditUnsentMessages, bsnAuditRecordEventsFailure, bsnAuditStartUpTrap, bsnAuditShutDownTrap', 'Version 26: Added DisplayString to IMPORTS.', 'Version 25: Added bsnRunScripts', 'Version 24: Added bsnUSBInfo and bsnSFPInfo objects.', 'Version 23: Added bsnStackProtection.', 'Version 22: Added bsnROPasswordExpired, bsnRWPasswordExpired.', "Version 21: Modified bsnLacTrunkUnavailable's description.", 'Version 20: Added bsnUSBInsertion, bsnUSBRemoval, bsnSFPInsertion, bsnSFPRemoval.', 'Version 19: Added bayStackUnitConfigIndex parameter to bsnSystemUp365Days notification type.', 'Version 18: Added IP address related parameters to bsnEnteredForcedStackMode notification type.', 'Version 17: Added bsnSystemUp365Days.', 'Version 16: Added bsnRateLimitExceeded.', 'Version 15: Added bsnTemperatureExceeded.', 'Version 14: Added bsnEnteredForcedStackModeMAC, bsnEnteredForcedStackMode.', 'Version 13: Added bsnTrialLicenseExpirationTime, bsnTrialLicenseExpirationNumber, bsnTrialLicenseExpiration.', 'Version 12: Fix typo.', 'Version 11: Added bsnEapUbpFailure trap.', 'Version 10: Added bsnStackConfigurationError trap.', 'Version 9: Added additional MLT/LACP-related traps.', 'Version 8: Added bsnMLTHealthFailure.', 'Version 7: Added serialConsole(4) enumeration.', 'Version 6: Added bsnLoginFailure and associated objects.', 'v005: Added version info', 'v000: The Initial Revision',))
if mibBuilder.loadTexts: bayStackNotificationsMib.setLastUpdated('201407070000Z')
if mibBuilder.loadTexts: bayStackNotificationsMib.setOrganization('Avaya')
if mibBuilder.loadTexts: bayStackNotificationsMib.setContactInfo('Avaya')
if mibBuilder.loadTexts: bayStackNotificationsMib.setDescription('Miscellaneous NOTIFICATION definitions for BayStack products.')
bsnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 2, 1))
bsnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 2, 2))
bsnNotifications0 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0))
bsnEapAccessViolationMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEapAccessViolationMacAddress.setStatus('current')
if mibBuilder.loadTexts: bsnEapAccessViolationMacAddress.setDescription('The MAC address which caused an EAP access violation.')
bsnLoginFailureType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("telnet", 1), ("ssh", 2), ("web", 3), ("serialConsole", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnLoginFailureType.setStatus('current')
if mibBuilder.loadTexts: bsnLoginFailureType.setDescription('The type of login being attempted when the failure occurred.')
bsnLoginFailureAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnLoginFailureAddressType.setStatus('current')
if mibBuilder.loadTexts: bsnLoginFailureAddressType.setDescription('The address type contained in the associated value of bnsLoginFailureAddress.')
bsnLoginFailureAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnLoginFailureAddress.setStatus('current')
if mibBuilder.loadTexts: bsnLoginFailureAddress.setDescription('The IP address from which the login was attempted when the failure occurred.')
bsnLoginFailureUsername = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 5), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnLoginFailureUsername.setStatus('current')
if mibBuilder.loadTexts: bsnLoginFailureUsername.setDescription('The username for which the login failure occurred.')
bsnActualStackSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnActualStackSize.setStatus('current')
if mibBuilder.loadTexts: bsnActualStackSize.setDescription('The actual stack size when a bsnStackConfigurationError notification is generated.')
bsnEapUbpFailureIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 7), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEapUbpFailureIfIndex.setStatus('current')
if mibBuilder.loadTexts: bsnEapUbpFailureIfIndex.setDescription('The ifIndex of the port for which UBP policies could not be installed.')
bsnEapUbpFailureMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 8), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEapUbpFailureMacAddress.setStatus('current')
if mibBuilder.loadTexts: bsnEapUbpFailureMacAddress.setDescription('The MAC address for which UBP policies could not be installed.')
bsnEapUbpFailureRoleString = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEapUbpFailureRoleString.setStatus('current')
if mibBuilder.loadTexts: bsnEapUbpFailureRoleString.setDescription('The role string of the UBP policies which could not be installed.')
bsnTrialLicenseExpirationTime = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnTrialLicenseExpirationTime.setStatus('current')
if mibBuilder.loadTexts: bsnTrialLicenseExpirationTime.setDescription('The number of days until a feature trial license will expire. A value of 0 means the license has expired.')
bsnTrialLicenseExpirationNumber = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnTrialLicenseExpirationNumber.setStatus('current')
if mibBuilder.loadTexts: bsnTrialLicenseExpirationNumber.setDescription('The number of the license that will expire or that has expired.')
bsnEnteredForcedStackModeMAC = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 12), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEnteredForcedStackModeMAC.setStatus('current')
if mibBuilder.loadTexts: bsnEnteredForcedStackModeMAC.setDescription('The MAC address of a switch which has entered forced stack mode.')
bsnEapRAVErrorMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 13), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEapRAVErrorMacAddress.setStatus('current')
if mibBuilder.loadTexts: bsnEapRAVErrorMacAddress.setDescription('The MAC address that was authorized on a port which could not be moved to the Radius-Assigned VLAN.')
bsnEapRAVErrorPort = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 14), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEapRAVErrorPort.setStatus('current')
if mibBuilder.loadTexts: bsnEapRAVErrorPort.setDescription('The ifIndex of the port that could not be moved to the Radius-Assigned VLAN.')
bsnEnteredForcedStackModeAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 15), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEnteredForcedStackModeAddressType.setStatus('current')
if mibBuilder.loadTexts: bsnEnteredForcedStackModeAddressType.setDescription('The address type contained in the associated value of bsnEnteredForcedStackModeAddress.')
bsnEnteredForcedStackModeAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 16), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnEnteredForcedStackModeAddress.setStatus('current')
if mibBuilder.loadTexts: bsnEnteredForcedStackModeAddress.setDescription('The IP address in use on the switch that entered forced stack mode.')
bsnStackProtectionEvent = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cannotJoinStack", 1), ("unitIgnored", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnStackProtectionEvent.setStatus('current')
if mibBuilder.loadTexts: bsnStackProtectionEvent.setDescription('This object specifies the Stack Protection events which may occur. cannotJoinStack(1) occurs on a BU (base unit) enabled switch which tries to join an existing operational stack. unitIgnored(2) occurs on an operational stack, when a BU enabled switch tries to join the stack.')
bsnUSBInfo = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnUSBInfo.setStatus('current')
if mibBuilder.loadTexts: bsnUSBInfo.setDescription('The USB module information.')
bsnSFPInfo = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnSFPInfo.setStatus('current')
if mibBuilder.loadTexts: bsnSFPInfo.setDescription('The SFP module information.')
bsnAaaUserName = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 2, 1, 20), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(10, 16))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsnAaaUserName.setStatus('current')
if mibBuilder.loadTexts: bsnAaaUserName.setDescription('The user name of an AAA user account.')
bsnConfigurationSavedToNvram = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 1))
if mibBuilder.loadTexts: bsnConfigurationSavedToNvram.setStatus('current')
if mibBuilder.loadTexts: bsnConfigurationSavedToNvram.setDescription('This notification is generated whenever the device saves its configuration to non-volatile storage. The system should limit the frequency with which this notification is generated, as frequent configuration changes could potentially generate too many of these notifications. How the frequency is limitted is an implementation details, but it is suggested that no more than one notification be generated per minute.')
bsnEapAccessViolation = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 2)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapAccessViolationMacAddress"))
if mibBuilder.loadTexts: bsnEapAccessViolation.setStatus('current')
if mibBuilder.loadTexts: bsnEapAccessViolation.setDescription('This notification is generated whenever an EAP access violation occurs.')
bsnPortSpeedDuplexMismatch = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnPortSpeedDuplexMismatch.setStatus('current')
if mibBuilder.loadTexts: bsnPortSpeedDuplexMismatch.setDescription('This notification is generated when a speed or duplex mismatch is detected. Once notification has been sent, further notifications may be sent, but it is suggested these be at least 5 minutes apart.')
bsnStackManagerReconfiguration = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 4))
if mibBuilder.loadTexts: bsnStackManagerReconfiguration.setStatus('current')
if mibBuilder.loadTexts: bsnStackManagerReconfiguration.setDescription('This notification is generated by a stackable system when the stack manager detects a problem with a link between stack members.')
bsnLacTrunkUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 5))
if mibBuilder.loadTexts: bsnLacTrunkUnavailable.setStatus('current')
if mibBuilder.loadTexts: bsnLacTrunkUnavailable.setDescription('This notification is generated when the last trunk is occupied out of a limited number of trunks that can be created. The condition usually occurs because a system has some hardware or software limit on the number of trunks that can be created.')
bsnLoginFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 6)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureType"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureAddressType"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureAddress"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnLoginFailureUsername"))
if mibBuilder.loadTexts: bsnLoginFailure.setStatus('current')
if mibBuilder.loadTexts: bsnLoginFailure.setDescription('This notification is generated when an attempt to login to the system fails as a result of an incorrect password.')
bsnMLTHealthFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 7)).setObjects(("IF-MIB", "ifAdminStatus"))
if mibBuilder.loadTexts: bsnMLTHealthFailure.setStatus('current')
if mibBuilder.loadTexts: bsnMLTHealthFailure.setDescription("This notification is generated when a receiving switch does not receive an expected number of autotopology frames on an MLT in a given time interval from the sending switch(es) on the other end of the MLT. Once notification has been sent, further notifications may be sent, but it is suggested these be at least 5 minutes apart. The ifAdminStatus object reflects the state of the port. The port may be partitioned by the switch or still be active depending on the detection algorithm's control parameters.")
bsnTrunkPortDisabledToPreventBroadcastStorm = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 8)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnTrunkPortDisabledToPreventBroadcastStorm.setStatus('current')
if mibBuilder.loadTexts: bsnTrunkPortDisabledToPreventBroadcastStorm.setDescription('This notification is generated when an MLT port is disabled as a result of an MLT trunk being disabled.')
bsnLacPortDisabledToPreventBroadcastStorm = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 9)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnLacPortDisabledToPreventBroadcastStorm.setStatus('current')
if mibBuilder.loadTexts: bsnLacPortDisabledToPreventBroadcastStorm.setDescription('This notification is generated when a LAG port that was port of a trunk is disabled as a result of the LAC setting on the port being turned off.')
bsnTrunkPortEnabledToPreventBroadcastStorm = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 10)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnTrunkPortEnabledToPreventBroadcastStorm.setStatus('current')
if mibBuilder.loadTexts: bsnTrunkPortEnabledToPreventBroadcastStorm.setDescription('This notification is generated when an MLT port is enabled as a result of an MLT trunk being disabled.')
bsnLacPortDisabledDueToLossOfVLACPDU = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 11)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnLacPortDisabledDueToLossOfVLACPDU.setStatus('current')
if mibBuilder.loadTexts: bsnLacPortDisabledDueToLossOfVLACPDU.setDescription('Generated when a port is disabled due to the loss of a VLACP PDU.')
bsnLacPortEnabledDueToReceiptOfVLACPDU = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnLacPortEnabledDueToReceiptOfVLACPDU.setStatus('current')
if mibBuilder.loadTexts: bsnLacPortEnabledDueToReceiptOfVLACPDU.setDescription('Generated when a port is enabled due to receipt of a VLACP PDU.')
bsnStackConfigurationError = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 13)).setObjects(("BAY-STACK-MIB", "bayStackConfigExpectedStackSize"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnActualStackSize"))
if mibBuilder.loadTexts: bsnStackConfigurationError.setStatus('current')
if mibBuilder.loadTexts: bsnStackConfigurationError.setDescription('This notification is generated when the expected size of a stack is not equal to the actual size of the stack.')
bsnEapUbpFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 14)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapUbpFailureIfIndex"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapUbpFailureMacAddress"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapUbpFailureRoleString"))
if mibBuilder.loadTexts: bsnEapUbpFailure.setStatus('current')
if mibBuilder.loadTexts: bsnEapUbpFailure.setDescription('This notification is generated when installation of a UBP policy fails following EAP authentication.')
bsnTrialLicenseExpiration = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 15)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnTrialLicenseExpirationTime"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnTrialLicenseExpirationNumber"))
if mibBuilder.loadTexts: bsnTrialLicenseExpiration.setStatus('current')
if mibBuilder.loadTexts: bsnTrialLicenseExpiration.setDescription('This notification is generated to indicate that a trial license is going to expire soon, or has already expired.')
bsnEnteredForcedStackMode = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 16)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnEnteredForcedStackModeMAC"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEnteredForcedStackModeAddressType"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEnteredForcedStackModeAddress"))
if mibBuilder.loadTexts: bsnEnteredForcedStackMode.setStatus('current')
if mibBuilder.loadTexts: bsnEnteredForcedStackMode.setDescription('This notification is generated to indicate that a switch has entered forced stack mode.')
bsnTemperatureExceeded = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 17)).setObjects(("S5-CHASSIS-MIB", "s5ChasComType"))
if mibBuilder.loadTexts: bsnTemperatureExceeded.setStatus('current')
if mibBuilder.loadTexts: bsnTemperatureExceeded.setDescription('This notification is generated when the temperature of a chassis component has exceeded some threshold. The instance of s5ChasComType included in the notification identifies the component.')
bsnEapRAVError = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 18)).setObjects(("IEEE8021-PAE-MIB", "dot1xAuthPaeState"), ("IEEE8021-PAE-MIB", "dot1xAuthBackendAuthState"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapRAVErrorMacAddress"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnEapRAVErrorPort"))
if mibBuilder.loadTexts: bsnEapRAVError.setStatus('current')
if mibBuilder.loadTexts: bsnEapRAVError.setDescription('This notification indicates that an Eap client MAC address was authorized on a port, but the port could not be moved to the Radius-Assigned VLAN.')
bsnEapRateLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 19)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnEapRateLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: bsnEapRateLimitExceeded.setDescription('This notification indicates that incoming traffic on a port exceeded the rate limit settings on that port.')
bsnSystemUp365Days = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 20)).setObjects(("BAY-STACK-MIB", "bayStackUnitConfigIndex"))
if mibBuilder.loadTexts: bsnSystemUp365Days.setStatus('current')
if mibBuilder.loadTexts: bsnSystemUp365Days.setDescription('This notification indicates that the system has been up for 365 days. In stack configuration, bayStackUnitConfigIndex specifies the unit number. For a standalone unit bayStackUnitConfigIndex is always 1.')
bsnUSBInsertion = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 21)).setObjects(("S5-AGENT-MIB", "s5AgSysUsbTargetUnit"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnUSBInfo"))
if mibBuilder.loadTexts: bsnUSBInsertion.setStatus('current')
if mibBuilder.loadTexts: bsnUSBInsertion.setDescription('This notification is triggered when an USB device is inserted. In stack configuration, s5AgSysUsbTargetUnit specifies the unit number. For standalone, s5AgSysUsbTargetUnit is always 0.')
bsnUSBRemoval = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 22)).setObjects(("S5-AGENT-MIB", "s5AgSysUsbTargetUnit"))
if mibBuilder.loadTexts: bsnUSBRemoval.setStatus('current')
if mibBuilder.loadTexts: bsnUSBRemoval.setDescription('This notification is triggered when an USB device is removed. In stack configuration, s5AgSysUsbTargetUnit specifies the unit number. For standalone, s5AgSysUsbTargetUnit is always 0.')
bsnSFPInsertion = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 23)).setObjects(("IF-MIB", "ifIndex"), ("BAY-STACK-NOTIFICATIONS-MIB", "bsnSFPInfo"))
if mibBuilder.loadTexts: bsnSFPInsertion.setStatus('current')
if mibBuilder.loadTexts: bsnSFPInsertion.setDescription('This notification is triggered when an SFP module is inserted.')
bsnSFPRemoval = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 24)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bsnSFPRemoval.setStatus('current')
if mibBuilder.loadTexts: bsnSFPRemoval.setDescription('This notification is triggered when an SFP module is removed.')
bsnROPasswordExpired = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 25))
if mibBuilder.loadTexts: bsnROPasswordExpired.setStatus('current')
if mibBuilder.loadTexts: bsnROPasswordExpired.setDescription('This notification is sent when RO password expired.')
bsnRWPasswordExpired = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 26))
if mibBuilder.loadTexts: bsnRWPasswordExpired.setStatus('current')
if mibBuilder.loadTexts: bsnRWPasswordExpired.setDescription('This notification is sent when RW password expired.')
bsnStackProtection = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 27)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnStackProtectionEvent"))
if mibBuilder.loadTexts: bsnStackProtection.setStatus('current')
if mibBuilder.loadTexts: bsnStackProtection.setDescription('This notification is sent when a stack protection event occurs. The event type is specified by the bsnStackProtectionEvent object.')
bsnRunScripts = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 28)).setObjects(("S5-AGENT-MIB", "s5AgentScriptStatus"))
if mibBuilder.loadTexts: bsnRunScripts.setStatus('current')
if mibBuilder.loadTexts: bsnRunScripts.setDescription('This notification is sent when a script has been run. It indicates whether the execution was successful or not.')
bsnAaaUserAccountNotUsed = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 29)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName"))
if mibBuilder.loadTexts: bsnAaaUserAccountNotUsed.setStatus('current')
if mibBuilder.loadTexts: bsnAaaUserAccountNotUsed.setDescription('A bsnAaaUserAccountNotUsed trap signifies that a user account has never been used during a time interval.')
bsnAaaAlreadyConnected = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 30)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName"))
if mibBuilder.loadTexts: bsnAaaAlreadyConnected.setStatus('current')
if mibBuilder.loadTexts: bsnAaaAlreadyConnected.setDescription('A bsnAaaAlreadyConnected trap signifies that a user is already connected while he attempts to connect again.')
bsnAaaIncorrectLogOnThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 31)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName"))
if mibBuilder.loadTexts: bsnAaaIncorrectLogOnThresholdExceeded.setStatus('current')
if mibBuilder.loadTexts: bsnAaaIncorrectLogOnThresholdExceeded.setDescription('A bsnAaaIncorrectLogOnThresholdExceeded trap signifies that the threshold for incorrect user-entered information is exceeded.')
bsnAaaMaxNoOfSessionsExceeded = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 32)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName"))
if mibBuilder.loadTexts: bsnAaaMaxNoOfSessionsExceeded.setStatus('current')
if mibBuilder.loadTexts: bsnAaaMaxNoOfSessionsExceeded.setDescription('A bsnAaaMaxNoOfSessionsExceeded trap signifies that the maxim number of current sessions for an AAA user account is exceeded.')
bsnAuditUnsentMessages = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 33))
if mibBuilder.loadTexts: bsnAuditUnsentMessages.setStatus('current')
if mibBuilder.loadTexts: bsnAuditUnsentMessages.setDescription('A bsnAuditUnsentMessages trap signifies that the number of audit unsent messages has reached 50% from the total capacity.')
bsnAuditRecordEventsFailure = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 34))
if mibBuilder.loadTexts: bsnAuditRecordEventsFailure.setStatus('current')
if mibBuilder.loadTexts: bsnAuditRecordEventsFailure.setDescription('A bsnAuditRecordEventsFailure trap signifies that security log fails to record the events that are required to be recorded.')
bsnAuditStartUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 35))
if mibBuilder.loadTexts: bsnAuditStartUpTrap.setStatus('current')
if mibBuilder.loadTexts: bsnAuditStartUpTrap.setDescription('A bsnAuditStartUpTrap trap signifies that the audit function starts up.')
bsnAuditShutDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 36))
if mibBuilder.loadTexts: bsnAuditShutDownTrap.setStatus('current')
if mibBuilder.loadTexts: bsnAuditShutDownTrap.setDescription('A bsnAuditStartUpTrap trap signifies that the audit function shuts down.')
bsnAaaUserPasswordExpired = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 2, 2, 0, 37)).setObjects(("BAY-STACK-NOTIFICATIONS-MIB", "bsnAaaUserName"))
if mibBuilder.loadTexts: bsnAaaUserPasswordExpired.setStatus('current')
if mibBuilder.loadTexts: bsnAaaUserPasswordExpired.setDescription('A bsnAaaUserPasswordExpired trap signifies that the password stored for an AAA user account has expired.')
mibBuilder.exportSymbols("BAY-STACK-NOTIFICATIONS-MIB", bsnNotifications=bsnNotifications, bsnNotifications0=bsnNotifications0, bsnEnteredForcedStackModeAddressType=bsnEnteredForcedStackModeAddressType, bsnAuditUnsentMessages=bsnAuditUnsentMessages, bsnUSBInsertion=bsnUSBInsertion, bsnSFPInfo=bsnSFPInfo, bsnSFPRemoval=bsnSFPRemoval, bsnStackProtection=bsnStackProtection, bsnRWPasswordExpired=bsnRWPasswordExpired, bayStackNotificationsMib=bayStackNotificationsMib, bsnEapRateLimitExceeded=bsnEapRateLimitExceeded, bsnTemperatureExceeded=bsnTemperatureExceeded, bsnActualStackSize=bsnActualStackSize, bsnAuditShutDownTrap=bsnAuditShutDownTrap, bsnTrunkPortEnabledToPreventBroadcastStorm=bsnTrunkPortEnabledToPreventBroadcastStorm, PYSNMP_MODULE_ID=bayStackNotificationsMib, bsnLoginFailureType=bsnLoginFailureType, bsnAaaIncorrectLogOnThresholdExceeded=bsnAaaIncorrectLogOnThresholdExceeded, bsnConfigurationSavedToNvram=bsnConfigurationSavedToNvram, bsnEapRAVError=bsnEapRAVError, bsnAaaMaxNoOfSessionsExceeded=bsnAaaMaxNoOfSessionsExceeded, bsnObjects=bsnObjects, bsnAaaAlreadyConnected=bsnAaaAlreadyConnected, bsnAuditStartUpTrap=bsnAuditStartUpTrap, bsnEapUbpFailureRoleString=bsnEapUbpFailureRoleString, bsnLoginFailureUsername=bsnLoginFailureUsername, bsnMLTHealthFailure=bsnMLTHealthFailure, bsnStackManagerReconfiguration=bsnStackManagerReconfiguration, bsnStackConfigurationError=bsnStackConfigurationError, bsnEapUbpFailure=bsnEapUbpFailure, bsnEnteredForcedStackModeMAC=bsnEnteredForcedStackModeMAC, bsnEapRAVErrorPort=bsnEapRAVErrorPort, bsnRunScripts=bsnRunScripts, bsnSFPInsertion=bsnSFPInsertion, bsnTrialLicenseExpirationNumber=bsnTrialLicenseExpirationNumber, bsnEnteredForcedStackModeAddress=bsnEnteredForcedStackModeAddress, bsnAaaUserAccountNotUsed=bsnAaaUserAccountNotUsed, bsnTrialLicenseExpiration=bsnTrialLicenseExpiration, bsnEnteredForcedStackMode=bsnEnteredForcedStackMode, bsnEapAccessViolationMacAddress=bsnEapAccessViolationMacAddress, bsnAaaUserName=bsnAaaUserName, bsnStackProtectionEvent=bsnStackProtectionEvent, bsnUSBRemoval=bsnUSBRemoval, bsnLacPortDisabledToPreventBroadcastStorm=bsnLacPortDisabledToPreventBroadcastStorm, bsnAuditRecordEventsFailure=bsnAuditRecordEventsFailure, bsnLacTrunkUnavailable=bsnLacTrunkUnavailable, bsnLoginFailure=bsnLoginFailure, bsnTrunkPortDisabledToPreventBroadcastStorm=bsnTrunkPortDisabledToPreventBroadcastStorm, bsnEapUbpFailureMacAddress=bsnEapUbpFailureMacAddress, bsnLacPortEnabledDueToReceiptOfVLACPDU=bsnLacPortEnabledDueToReceiptOfVLACPDU, bsnLoginFailureAddress=bsnLoginFailureAddress, bsnSystemUp365Days=bsnSystemUp365Days, bsnLoginFailureAddressType=bsnLoginFailureAddressType, bsnEapRAVErrorMacAddress=bsnEapRAVErrorMacAddress, bsnPortSpeedDuplexMismatch=bsnPortSpeedDuplexMismatch, bsnAaaUserPasswordExpired=bsnAaaUserPasswordExpired, bsnUSBInfo=bsnUSBInfo, bsnTrialLicenseExpirationTime=bsnTrialLicenseExpirationTime, bsnEapAccessViolation=bsnEapAccessViolation, bsnLacPortDisabledDueToLossOfVLACPDU=bsnLacPortDisabledDueToLossOfVLACPDU, bsnROPasswordExpired=bsnROPasswordExpired, bsnEapUbpFailureIfIndex=bsnEapUbpFailureIfIndex)
