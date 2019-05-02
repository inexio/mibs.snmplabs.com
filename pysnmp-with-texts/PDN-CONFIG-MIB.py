#
# PySNMP MIB module PDN-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_devConfig, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-devConfig")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, iso, NotificationType, ObjectIdentity, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, TimeTicks, Counter32, IpAddress, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "TimeTicks", "Counter32", "IpAddress", "Unsigned32", "Gauge32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
devConfigArea = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 1))
devConfigAreaCopy = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))).clone(namedValues=NamedValues(("noOp", 1), ("active-to-customer1", 2), ("active-to-customer2", 3), ("customer1-to-active", 4), ("customer1-to-customer2", 5), ("customer2-to-active", 6), ("customer2-to-customer1", 7), ("factory1-to-active", 8), ("factory1-to-customer1", 9), ("factory1-to-customer2", 10), ("factory2-to-active", 11), ("factory2-to-customer1", 12), ("factory2-to-customer2", 13), ("factory3-to-active", 14), ("factory3-to-customer1", 15), ("factory3-to-customer2", 16), ("factory4-to-active", 17), ("factory4-to-customer1", 18), ("factory4-to-customer2", 19), ("factory5-to-active", 20), ("factory5-to-customer1", 21), ("factory5-to-customer2", 22), ("factory6-to-active", 23), ("factory6-to-customer1", 24), ("factory6-to-customer2", 25), ("factory7-to-active", 26), ("factory7-to-customer1", 27), ("factory7-to-customer2", 28), ("factory8-to-active", 29), ("factory8-to-customer1", 30), ("factory8-to-customer2", 31), ("factory9-to-active", 32), ("factory9-to-customer1", 33), ("factory9-to-customer2", 34)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigAreaCopy.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigAreaCopy.setDescription('This object is used to copy the entire contents of one configuration area into another configuration area. The supported number of factory configuration areas depends on the device model. The value read from this object is always noOp(1).')
devConfigTestTimer = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2))
devConfigTestTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTestTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigTestTimeout.setDescription('This object specifies whether tests are to be terminated after a defined duration. If the value is enable(2), the duration is defined by devConfigTestDuration.')
devConfigTestDuration = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTestDuration.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigTestDuration.setDescription('This object specifies the duration that a test will be allowed to run before it is automatically terminated. Tests will only be terminated if devConfigTestTimeout is set to enable.')
devConfigClockSrc = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3))
devConfigClockSrcTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1), )
if mibBuilder.loadTexts: devConfigClockSrcTable.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigClockSrcTable.setDescription('The clock source table.')
devConfigClockSrcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1), ).setIndexNames((0, "PDN-CONFIG-MIB", "devCfgClkWhichSrc"))
if mibBuilder.loadTexts: devConfigClockSrcEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigClockSrcEntry.setDescription('An entry in the clock source table.')
devCfgClkWhichSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgClkWhichSrc.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgClkWhichSrc.setDescription('The clock source to which this entry is applicable.')
devCfgClkSource = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("interface", 3), ("dbm", 4), ("external2", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgClkSource.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgClkSource.setDescription('This object is used to select the source for the master clock for the device. The source selected provides synchronization for all the timing within the device, and the clocks for all of the external interfaces. If this object is interface(3), the specific interface used as the master clock source is specified using devCfgClkIfIndex. If this object is external(2), or external2(5), the clock rate can be specified using devCfgClkRate.')
devCfgClkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgClkIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgClkIfIndex.setDescription('This object is used to select the interface to be used as the source for the master clock for the device, if devCfgClkSource is set to interface(3). The interface selected provides synchronization for all the timing within the device, and the clocks for all of the external interfaces. NOTE: if a synchronous data port is selected and the EDL is enabled for that synchronous data port, then the external device must provide a clock 8 Kbps less than the expected data port rate. For example, if the data port rate is set at 64 Kbps, the external clock source needs to supply a 56 Kbps clock signal. If devCfgClkSource is not interface(3), the value of this object is meaningless.')
devCfgClkRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("rate400Hz", 1), ("rate8KHz", 2), ("rate64KHz", 3), ("rate1544KHz", 4), ("rate2048KHz", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgClkRate.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgClkRate.setDescription('This object is used to specify the clock signal rate associated with the external source selected by the devCfgClkSource object.')
devConfigTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4))
devConfigTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigTrapEnable.setDescription("Which trap types will be sent by the entity. This object is a bit map represented as a sum, therefore, multiple trap types can be enabled simultaneously. This objects sets flag (enable/disable) value on entity level. If trap enable/disable flags are set per interface level by some other object this object will read 'enabled' if any one of the interfaces is enabled. If any of the traps below are set to enabled by this object it will enable that trap on all interfaces on the entity. The various bit positions are: 1 warmStart traps 2 authenticationFailure traps 4 enterpriseSpecific traps 8 LinkUp trap 16 LinkDown Trap 32 path Trap 64 Latency Trap.")
cCNTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cCNTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: cCNTrapEnable.setDescription(' This object is used to enable or disable configuration change trap. It is a bit sequence sum with only accepted values 1 or 2. Setting the bit sequence to 2 would mean enabling the trap and 1 would mean disabling it.')
devConfigAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 5))
devConfigAlarmRelayCutoff = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 5, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigAlarmRelayCutoff.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigAlarmRelayCutoff.setDescription('Writing off(2) to this object will turn off the System Alarm Relay. Reading this object will always return noOp(1).')
devConfigCardType = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6))
devConfigCardTypeTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7), )
if mibBuilder.loadTexts: devConfigCardTypeTable.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigCardTypeTable.setDescription('The Paradyne Card Type Table.')
devConfigCardTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1), ).setIndexNames((0, "PDN-CONFIG-MIB", "devCfgCardSlot"))
if mibBuilder.loadTexts: devConfigCardTypeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigCardTypeEntry.setDescription('An entry in the Paradyne Card Type Table.')
devCfgCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgCardSlot.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgCardSlot.setDescription('The slot number which this card occupies in the chassis.')
devCfgCardConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))).clone(namedValues=NamedValues(("emptySlot", 1), ("unsupportedAPM", 2), ("t1NAM", 3), ("syncDataAPM", 4), ("voiceFxsAPM", 5), ("voiceEmAPM", 6), ("voiceFxoAPM", 7), ("dsxAPM", 8), ("t1NoDsxNAM", 9), ("misconfiguredAPM", 10), ("ocu2APM", 11), ("ocu6APM", 12), ("dce6APM", 13), ("sruAPM", 14), ("ocu4APM", 15), ("pktVoiceAPM", 16), ("acceptingAPM", 17), ("failedAPM", 18), ("dpNAM", 19), ("stNAM", 20), ("ddsNAM", 21), ("dualDsxNniNAM", 22), ("t3NniNAM", 23), ("t3NAM", 24), ("dslNAM", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgCardConfig.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgCardConfig.setDescription('The type of card which has been configured for this slot.')
devCfgCardActual = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))).clone(namedValues=NamedValues(("emptySlot", 1), ("unsupportedAPM", 2), ("t1NAM", 3), ("syncDataAPM", 4), ("voiceFxsAPM", 5), ("voiceEmAPM", 6), ("voiceFxoAPM", 7), ("voiceDsxAPM", 8), ("t1NoDsxNAM", 9), ("misconfigured", 10), ("ocu2APM", 11), ("ocu6APM", 12), ("dce6APM", 13), ("sruAPM", 14), ("ocu4APM", 15), ("pktVoiceAPM", 16), ("acceptingAPM", 17), ("failedAPM", 18), ("dpNAM", 19), ("stNAM", 20), ("ddsNAM", 21), ("dualDsxNniNAM", 22), ("t3NniNAM", 23), ("t3NAM", 24), ("dslNAM", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCfgCardActual.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgCardActual.setDescription('The type of card which is present in this slot.')
devCfgCardAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 6, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("accept", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devCfgCardAction.setStatus('mandatory')
if mibBuilder.loadTexts: devCfgCardAction.setDescription('Writing accept(2) to this object changes the configured card type to match the type of card currently present in the slot. Reading this object always returns noOp(1).')
devConfigNetSync = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 7))
devConfigNetSyncRole = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("tributary", 2), ("controller", 3))).clone('tributary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigNetSyncRole.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigNetSyncRole.setDescription('Network Time Synchronization role item for a device in the network. none - Device will ignore network time synchronization messages. tributary - Update the network reference time each time the device receives an update massage. controller - The device will generate the synchronization message and Time of Day clock will be the same as the Network Reference Time.')
devConfigTime = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 8))
devConfigTimeOfDay = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 8, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigTimeOfDay.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigTimeOfDay.setDescription("This is standard definition of Device Time of Day (DateAndTime) SYNTAX. The only difference is that our group is defining timezone filed (8) optional. Display format-&gt; 2d-1d-1d,1d:1d:1d.1d,1a1d:1d Fields description field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Timezone information (fileds 8-10) is optional. Note that if only local time is known, then timezone information (fields 8-10) is not present.")
devConfigChangeKeys = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9))
devConfigChangeKeysTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1), )
if mibBuilder.loadTexts: devConfigChangeKeysTable.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigChangeKeysTable.setDescription('The Paradyne Configuration Change Key Table. This table is in place to allow a Network Manager to know when the configuration on the device changes. Configuration can be found in several databases that may each have a unique access method. For this reason, the keys are in the form of a table.')
devConfigChangeKeysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1), ).setIndexNames((0, "PDN-CONFIG-MIB", "devConfigChangeKeysDbType"))
if mibBuilder.loadTexts: devConfigChangeKeysEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigChangeKeysEntry.setDescription('An entry in the Paradyne Configuration Change Key Table.')
devConfigChangeKeysDbType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generalConfig", 1), ("rmonAlarm", 2), ("rmonUserHistory", 3), ("routerConfig", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devConfigChangeKeysDbType.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigChangeKeysDbType.setDescription('The type of database that is being keyed. If a specific type is not supported by the device, noSuchName should be returned.')
devConfigChangeKeysDbKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 9, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devConfigChangeKeysDbKey.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigChangeKeysDbKey.setDescription('A unique value that will change each time the database is altered. Effort should be made to increase the number of times the database can change without seeing the same key.')
devConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10))
devConfigComDiscTime = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigComDiscTime.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigComDiscTime.setDescription('This object is used to specify how long to wait before disconnecting. Inactivity is defined as no keyboard activity within a given period of time. The time is kept in seconds. The default is 300 seconds.')
devConfigPortNumDisplayFormat = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sle", 1), ("unitport", 2), ("name", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigPortNumDisplayFormat.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigPortNumDisplayFormat.setDescription('This object is used to set display format for the port numbers. The default is unit/port number. sle(1) - this method is to use Single Logical Entity interface numbers. For example, if sle is confiugred the sle numbers range from 1 to 384 for a stack of 8 units with 48 ports each. unitport(2) - this method uses unitnumber/portnumber For previous example the numbers would be from 1/1 to 8/48. name(3) - This method allowes user to assign character strings (names) to each interface and to view the interfaces by names.')
devConfigDateDisplayFormat = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ddmmyy", 1), ("mmddyy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devConfigDateDisplayFormat.setStatus('mandatory')
if mibBuilder.loadTexts: devConfigDateDisplayFormat.setDescription("This object is used to specify which format will date be displayed in.The default is 'mmddyy'")
devAcceptRemoteResetFrame = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAcceptRemoteResetFrame.setStatus('mandatory')
if mibBuilder.loadTexts: devAcceptRemoteResetFrame.setDescription('This object is used to enable/disable acceptance of remote reset frame which would result in hardware reset. The default setting is disabled.')
cCN = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 7, 4) + (0,7)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cCN.setDescription("This trap signifies a Configuration change or software upgrade. This trap is of 'warning' class")
mibBuilder.exportSymbols("PDN-CONFIG-MIB", devConfigTrapEnable=devConfigTrapEnable, devConfigCardTypeTable=devConfigCardTypeTable, devConfigNetSync=devConfigNetSync, devConfigAreaCopy=devConfigAreaCopy, devCfgClkRate=devCfgClkRate, devConfigTimeOfDay=devConfigTimeOfDay, devConfigTrap=devConfigTrap, devConfiguration=devConfiguration, devConfigTestTimeout=devConfigTestTimeout, devCfgCardConfig=devCfgCardConfig, devConfigChangeKeysTable=devConfigChangeKeysTable, devConfigTestDuration=devConfigTestDuration, devConfigClockSrcEntry=devConfigClockSrcEntry, devConfigCardType=devConfigCardType, devCfgCardActual=devCfgCardActual, devConfigTestTimer=devConfigTestTimer, devConfigComDiscTime=devConfigComDiscTime, devConfigAlarm=devConfigAlarm, devCfgCardSlot=devCfgCardSlot, devConfigDateDisplayFormat=devConfigDateDisplayFormat, devCfgCardAction=devCfgCardAction, devConfigCardTypeEntry=devConfigCardTypeEntry, devCfgClkSource=devCfgClkSource, devConfigTime=devConfigTime, devConfigNetSyncRole=devConfigNetSyncRole, cCNTrapEnable=cCNTrapEnable, devConfigChangeKeys=devConfigChangeKeys, devAcceptRemoteResetFrame=devAcceptRemoteResetFrame, devConfigClockSrc=devConfigClockSrc, devCfgClkWhichSrc=devCfgClkWhichSrc, devConfigChangeKeysEntry=devConfigChangeKeysEntry, cCN=cCN, devConfigPortNumDisplayFormat=devConfigPortNumDisplayFormat, devConfigClockSrcTable=devConfigClockSrcTable, devConfigArea=devConfigArea, devConfigAlarmRelayCutoff=devConfigAlarmRelayCutoff, devConfigChangeKeysDbKey=devConfigChangeKeysDbKey, devCfgClkIfIndex=devCfgClkIfIndex, devConfigChangeKeysDbType=devConfigChangeKeysDbType)