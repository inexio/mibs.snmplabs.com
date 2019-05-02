#
# PySNMP MIB module PDN-DSLAM-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DSLAM-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_dslam, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-dslam")
IdslClockMode, SwitchState = mibBuilder.importSymbols("PDN-TC", "IdslClockMode", "SwitchState")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysObjectID, = mibBuilder.importSymbols("SNMPv2-MIB", "sysObjectID")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Bits, ModuleIdentity, Counter32, iso, ObjectIdentity, TimeTicks, Counter64, NotificationType, Integer32, Unsigned32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Bits", "ModuleIdentity", "Counter32", "iso", "ObjectIdentity", "TimeTicks", "Counter64", "NotificationType", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32")
RowStatus, DisplayString, TextualConvention, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TAddress")
sysDevDslamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1))
sysDevDslamMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2))
sysDevStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1))
sysDevConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2))
loginHistTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1), )
if mibBuilder.loadTexts: loginHistTable.setStatus('mandatory')
if mibBuilder.loadTexts: loginHistTable.setDescription('This table shows the most recent 10 logins and all active users currently accessing the device. It is indexed by userId and loginTime.')
loginHistTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1), ).setIndexNames((0, "PDN-DSLAM-SYSTEM-MIB", "loginUserId"), (0, "PDN-DSLAM-SYSTEM-MIB", "loginTime"))
if mibBuilder.loadTexts: loginHistTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: loginHistTableEntry.setDescription('This object corresponds to an entry in the login history table.')
loginUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginUserId.setStatus('mandatory')
if mibBuilder.loadTexts: loginUserId.setDescription('This object containes the user login id.')
loginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginTime.setStatus('mandatory')
if mibBuilder.loadTexts: loginTime.setDescription('This object containes the login time in seconds when the login session is established.')
loginAccessApp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("console", 1), ("telnet", 2), ("ftp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginAccessApp.setStatus('mandatory')
if mibBuilder.loadTexts: loginAccessApp.setDescription('This object describes the access application used by the end user to access the device. This can be done through console, using telnet or using ftp.')
loginAccessHost = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginAccessHost.setStatus('mandatory')
if mibBuilder.loadTexts: loginAccessHost.setDescription('This object containes the ip address of the network management station when the access application is telnet or ftp. In case of console, this object contains 0.0.0.0.')
loginUserPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("administrator", 1), ("operator", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginUserPriv.setStatus('mandatory')
if mibBuilder.loadTexts: loginUserPriv.setDescription('This object containes the access privileges of the user.')
loginStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginStatus.setStatus('mandatory')
if mibBuilder.loadTexts: loginStatus.setDescription('This object indicates whether the user is still accessing the device.')
loginFailureCountTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2), )
if mibBuilder.loadTexts: loginFailureCountTable.setStatus('mandatory')
if mibBuilder.loadTexts: loginFailureCountTable.setDescription('This table containes the statistics for login failures. It is indexed by access type i.e console, telnet or ftp.')
loginFailureCountTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1), ).setIndexNames((0, "PDN-DSLAM-SYSTEM-MIB", "loginFailureAccessApp"))
if mibBuilder.loadTexts: loginFailureCountTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: loginFailureCountTableEntry.setDescription('This object corresponds to an entry in the login failure count table.')
loginFailureAccessApp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("console", 1), ("telnet", 2), ("ftp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginFailureAccessApp.setStatus('mandatory')
if mibBuilder.loadTexts: loginFailureAccessApp.setDescription('This object describes the access application used by the end user to access the device. This can be done through console, using telnet or using ftp.')
loginFailureCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loginFailureCount.setStatus('mandatory')
if mibBuilder.loadTexts: loginFailureCount.setDescription('This object containes the number of unsuccesful logins for console, ftp or telnet.')
enablePowerSourceFailureAlarm = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enablePowerSourceFailureAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: enablePowerSourceFailureAlarm.setDescription('This objects corresponds to enabling/disabling the power source failure alarm - for both A and B power sources This object is for the MCC only. The default value of this object should be 1.')
devIfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2), )
if mibBuilder.loadTexts: devIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: devIfTable.setDescription('This table is used to configure information for a particular interface')
devIfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: devIfTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devIfTableEntry.setDescription('This object corresponds to an entry in the DevifTable ')
devPacketDiscardPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noOp", 1), ("mrrp", 2), ("lrrp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devPacketDiscardPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: devPacketDiscardPolicy.setDescription('This object corresponds to the policy for packet discards during periods of congestion : mrrp - most recently received packets are discarded. lrrp - least recently received packets are discarded. The default value of this object should be 2')
devLinkIntegrity = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devLinkIntegrity.setStatus('mandatory')
if mibBuilder.loadTexts: devLinkIntegrity.setDescription('This object corresponds to the enabling or disabling of the ethernet link integrity : enable - enable link integrity disable - disable link integrity none - for interfaces that do not support link integrity The default value of this object should be 1')
communityTrapAddressInfoTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3), )
if mibBuilder.loadTexts: communityTrapAddressInfoTable.setStatus('mandatory')
if mibBuilder.loadTexts: communityTrapAddressInfoTable.setDescription('This table is used to set the trap destination address for a particular community.')
communityTrapAddressInfoTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1), ).setIndexNames((0, "PDN-DSLAM-SYSTEM-MIB", "trapCommunityName"), (0, "PDN-DSLAM-SYSTEM-MIB", "trapDestAndPort"))
if mibBuilder.loadTexts: communityTrapAddressInfoTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: communityTrapAddressInfoTableEntry.setDescription('This object corresponds to an entry in the community trap address info table.')
trapCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapCommunityName.setStatus('mandatory')
if mibBuilder.loadTexts: trapCommunityName.setDescription('This object corresponds to the name of the SNMP Community.')
trapDestAndPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDestAndPort.setStatus('mandatory')
if mibBuilder.loadTexts: trapDestAndPort.setDescription('The IP Address and Port of the destination to which a trap must be sent.')
trapsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapsEnable.setStatus('mandatory')
if mibBuilder.loadTexts: trapsEnable.setDescription('This object corresponds to turning traps on/off for a particular destination. enable (1) - traps will be sent to the specified destination. disable (2)- traps will not be sent to the specified destination. The default value of this object should be 2.')
trapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: trapRowStatus.setDescription('This object is used to add or delete a a row from the table.')
entCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4), )
if mibBuilder.loadTexts: entCommunityTable.setStatus('mandatory')
if mibBuilder.loadTexts: entCommunityTable.setDescription('This table is used to set the various configuration parameters for a particular community.')
entCommunityTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1), ).setIndexNames((0, "PDN-DSLAM-SYSTEM-MIB", "entCommunityName"))
if mibBuilder.loadTexts: entCommunityTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: entCommunityTableEntry.setDescription('This object corresponds to an entry in the community table.')
entCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entCommunityName.setStatus('mandatory')
if mibBuilder.loadTexts: entCommunityName.setDescription('This object corresponds to the name of the SNMP Community')
entCommunityType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entCommunityType.setStatus('mandatory')
if mibBuilder.loadTexts: entCommunityType.setDescription("The type of the community readOnly - this community is only allowed to do get's readWrite - this community is allowed to do get's and set's The default value of this object should be 1")
entCommunityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entCommunityRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: entCommunityRowStatus.setDescription('This object is used to add or delete a a row from the table.')
sysDevUserAccountTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5), )
if mibBuilder.loadTexts: sysDevUserAccountTable.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevUserAccountTable.setDescription('This table contains the user accounts.')
sysDevUserAccountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1), ).setIndexNames((0, "PDN-DSLAM-SYSTEM-MIB", "sysDevUserAccountUserId"))
if mibBuilder.loadTexts: sysDevUserAccountEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevUserAccountEntry.setDescription('An entry containing user account information.')
sysDevUserAccountUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDevUserAccountUserId.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevUserAccountUserId.setDescription('This object corresponds to the login ID of the user account.')
sysDevUserAccountPrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operator", 1), ("administrator", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevUserAccountPrivilege.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevUserAccountPrivilege.setDescription('This object corresponds to the access privilege of the user account. 1 = Operator, 2 = Administrator.')
sysDevUserAccountUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDevUserAccountUserPassword.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevUserAccountUserPassword.setDescription('This object corresponds to the password of the user account.')
sysDevUserAccountAccessPartition = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevUserAccountAccessPartition.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevUserAccountAccessPartition.setDescription("This object corresponds to the access partition of the user account. The default value of this object is 'all'")
sysDevUserAccountRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevUserAccountRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevUserAccountRowStatus.setDescription('This object corresponds to create or delete a row in sysDevUserAccountTable.')
sysDevIDSLConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6), )
if mibBuilder.loadTexts: sysDevIDSLConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevIDSLConfigTable.setDescription('A table that contains configuration information about IDSL Card.')
sysDevIDSLConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: sysDevIDSLConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevIDSLConfigEntry.setDescription('A list of information for IDSL device Configuration.')
sysDevIDSLConfigPrimaryNetClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1, 1), IdslClockMode().clone('triState')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevIDSLConfigPrimaryNetClockMode.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevIDSLConfigPrimaryNetClockMode.setDescription('This object indicates the network clock mode set for the primary network clock. IDSL portcards with a port configured as an NT will be set to portCardDriveClockOnboard(4), both driving the backplane and using the clock for the other Local Timing transceivers on the card. Port cards with only LT ports configured will receive a clock from the backplane using portCardSinkClock(2). portCardDriveClock(3) will drive the backplane alone. The default value of this object is triState(1).')
sysDevIDSLConfigSecondaryNetClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1, 2), IdslClockMode().clone('triState')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevIDSLConfigSecondaryNetClockMode.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevIDSLConfigSecondaryNetClockMode.setDescription('This object indicates the network clock mode set for the secondary network clock. IDSL portcards with a port configured as an NT will be set to portCardDriveClockOnboard(4), both driving the backplane and using the clock for the other Local Timing transceivers on the card. Port cards with only LT ports configured will receive a clock from the backplane using portCardSinkClock(2). portCardDriveClock(3) will drive the backplane alone. The default value of this object is triState(1).')
sysDevDslamSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7))
sysDevSyslogFtpServerXferStatsEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7, 1), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevSyslogFtpServerXferStatsEnable.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevSyslogFtpServerXferStatsEnable.setDescription('This object allows the network manager to enable and disable syslog messages for FTP server file transfer statistics')
sysDevSyslogTftpServerXferStatsEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7, 2), SwitchState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDevSyslogTftpServerXferStatsEnable.setStatus('mandatory')
if mibBuilder.loadTexts: sysDevSyslogTftpServerXferStatsEnable.setDescription('This object allows the network manager to enable and disable syslog messages for TFTP server file transfer statistics')
cCN = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,7)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cCN.setDescription("This trap signifies a Configuration change or software upgrade in the xDSL card. This trap is of 'warning' class")
authenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,8)).setObjects(("PDN-DSLAM-SYSTEM-MIB", "loginFailureAccessApp"), ("PDN-DSLAM-SYSTEM-MIB", "loginFailureCount"))
if mibBuilder.loadTexts: authenticationFailure.setDescription('This trap signifies an authentication failure. Authentication failures can be telnet based or terminal based. This trap is in addition to the SNMP based authentication failure trap, which is a generic trap.')
fanModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,9))
if mibBuilder.loadTexts: fanModuleFailure.setDescription("This trap indicates the indicates the failure of the fan module on the device. This trap is sent only by the MCC card. this trap is of 'minor' class")
fanModuleOperational = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,109))
if mibBuilder.loadTexts: fanModuleOperational.setDescription("This trap indicates the indicates the fan module on the device is operational. This trap is sent only by the MCC card. This trap is of 'minor' class")
powerSourceAFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,10))
if mibBuilder.loadTexts: powerSourceAFailure.setDescription("This trap indicates that power source A has failed. This is sent only by the MCC card. This trap is of 'minor' class.")
powerSourceAOperational = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,110))
if mibBuilder.loadTexts: powerSourceAOperational.setDescription("This trap indicates that the power source A is operational. This is sent only by the MCC card. This trap is of 'minor' class. This trap compliments powerSourceAFailure trap.")
slotPollFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,11)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: slotPollFailure.setDescription("This trap indicates a slot poll failure. This is sent only by the MCC card. this trap is of 'major' class.")
newCardDetected = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,111)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: newCardDetected.setDescription("This trap indicates that a new card was detected in a slot. This is sent only by the MCC card. this trap is of 'warning' class.")
ethernetJabber = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetJabber.setDescription("This trap indicates that a jabber condition has been detected on the ethernet interface. This trap is of 'major' class.")
ethernetJabberClear = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,112)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetJabberClear.setDescription("This trap indicates that the jabber condition that was detected no longer exists. This trap is of 'major' class.")
ethernetJumbos = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,13)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetJumbos.setDescription("This trap indicates ethernet jumbos. this trap is of 'minor' class")
ethernetRunts = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,14)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetRunts.setDescription("This trap indicates ethernet runts. this trap is of 'minor'")
powerSourceBFailure = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,17))
if mibBuilder.loadTexts: powerSourceBFailure.setDescription("This trap indicates that power source B has failed. This is sent only by the MCC card. This trap is of 'minor' class.")
powerSourceBOperational = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,117))
if mibBuilder.loadTexts: powerSourceBOperational.setDescription("This trap indicates that the power source B is operational. This is sent only by the MCC card. This trap is of 'minor' class. This trap compliments powerSourceBFailure trap.")
nonIpConservativeCardDetected = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,18)).setObjects(("ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: nonIpConservativeCardDetected.setDescription("This trap indicates that a non ip conservative DSL card exist in the chassis at the slot 'slotNumber'.This is sent only by the MCC card. This trap is of warning class.")
nonSupportedMCC = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,20)).setObjects(("SNMPv2-MIB", "sysObjectID"))
if mibBuilder.loadTexts: nonSupportedMCC.setDescription('AN has detected MCC firmware release too low to support this device')
nonSupportedChassis = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2) + (0,21)).setObjects(("SNMPv2-MIB", "sysObjectID"))
if mibBuilder.loadTexts: nonSupportedChassis.setDescription('AN in slot xx has been installed in a chassis that cannot support one or more of its features. ')
mibBuilder.exportSymbols("PDN-DSLAM-SYSTEM-MIB", ethernetJabber=ethernetJabber, sysDevDslamMIBTraps=sysDevDslamMIBTraps, fanModuleOperational=fanModuleOperational, enablePowerSourceFailureAlarm=enablePowerSourceFailureAlarm, authenticationFailure=authenticationFailure, loginStatus=loginStatus, fanModuleFailure=fanModuleFailure, sysDevSyslogFtpServerXferStatsEnable=sysDevSyslogFtpServerXferStatsEnable, loginHistTableEntry=loginHistTableEntry, sysDevIDSLConfigSecondaryNetClockMode=sysDevIDSLConfigSecondaryNetClockMode, loginFailureCount=loginFailureCount, slotPollFailure=slotPollFailure, loginUserId=loginUserId, sysDevIDSLConfigEntry=sysDevIDSLConfigEntry, loginUserPriv=loginUserPriv, trapCommunityName=trapCommunityName, devIfTableEntry=devIfTableEntry, sysDevUserAccountTable=sysDevUserAccountTable, trapsEnable=trapsEnable, loginFailureAccessApp=loginFailureAccessApp, loginAccessApp=loginAccessApp, sysDevConfig=sysDevConfig, sysDevUserAccountAccessPartition=sysDevUserAccountAccessPartition, nonSupportedMCC=nonSupportedMCC, sysDevUserAccountUserPassword=sysDevUserAccountUserPassword, sysDevIDSLConfigTable=sysDevIDSLConfigTable, sysDevUserAccountUserId=sysDevUserAccountUserId, ethernetRunts=ethernetRunts, loginFailureCountTable=loginFailureCountTable, sysDevDslamMIBObjects=sysDevDslamMIBObjects, devPacketDiscardPolicy=devPacketDiscardPolicy, sysDevUserAccountPrivilege=sysDevUserAccountPrivilege, sysDevIDSLConfigPrimaryNetClockMode=sysDevIDSLConfigPrimaryNetClockMode, loginFailureCountTableEntry=loginFailureCountTableEntry, newCardDetected=newCardDetected, sysDevUserAccountEntry=sysDevUserAccountEntry, entCommunityType=entCommunityType, entCommunityTableEntry=entCommunityTableEntry, trapDestAndPort=trapDestAndPort, trapRowStatus=trapRowStatus, sysDevSyslogTftpServerXferStatsEnable=sysDevSyslogTftpServerXferStatsEnable, ethernetJabberClear=ethernetJabberClear, powerSourceAFailure=powerSourceAFailure, sysDevUserAccountRowStatus=sysDevUserAccountRowStatus, ethernetJumbos=ethernetJumbos, loginHistTable=loginHistTable, nonIpConservativeCardDetected=nonIpConservativeCardDetected, entCommunityName=entCommunityName, cCN=cCN, powerSourceBOperational=powerSourceBOperational, nonSupportedChassis=nonSupportedChassis, loginAccessHost=loginAccessHost, devIfTable=devIfTable, sysDevStats=sysDevStats, communityTrapAddressInfoTable=communityTrapAddressInfoTable, entCommunityTable=entCommunityTable, entCommunityRowStatus=entCommunityRowStatus, powerSourceBFailure=powerSourceBFailure, sysDevDslamSyslog=sysDevDslamSyslog, communityTrapAddressInfoTableEntry=communityTrapAddressInfoTableEntry, loginTime=loginTime, devLinkIntegrity=devLinkIntegrity, powerSourceAOperational=powerSourceAOperational)