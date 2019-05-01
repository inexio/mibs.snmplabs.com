#
# PySNMP MIB module VERTICAL-STATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERTICAL-STATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity, Gauge32, Counter64, Bits, Integer32, MibIdentifier, enterprises, Unsigned32, iso, IpAddress, NotificationType, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Counter64", "Bits", "Integer32", "MibIdentifier", "enterprises", "Unsigned32", "iso", "IpAddress", "NotificationType", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vertical = MibIdentifier((1, 3, 6, 1, 4, 1, 2338))
vStationModule = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7))
vStationCommonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 1))
vStationFirstDigitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationFirstDigitTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: vStationFirstDigitTimeout.setDescription('Specifies the maximum number of seconds to wait for the first digit.')
vStationDigitTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDigitTimeout.setDescription('Specifies the maximum number of seconds to wait between digits.')
vStationOffHookTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationOffHookTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: vStationOffHookTimeout.setDescription('Specifies the maximum number of seconds to wait for the user to hang up phone after call disconnects or user executes an invalid operation. Howler tone is applied at timeout.')
vStationNumStationCards = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationNumStationCards.setStatus('mandatory')
if mibBuilder.loadTexts: vStationNumStationCards.setDescription('Specifies the number of station cards installed in the system.')
vStationExternalDialDigit = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationExternalDialDigit.setStatus('mandatory')
if mibBuilder.loadTexts: vStationExternalDialDigit.setDescription('Identifies the starting digit for making an external call.')
vStationCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 2))
vStationCardTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1), )
if mibBuilder.loadTexts: vStationCardTable.setStatus('current')
if mibBuilder.loadTexts: vStationCardTable.setDescription('Table of status, control and configuraion about cards containing station devices within the system. There are as many entries as there are cards containing station devices')
vStationCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationCardSlotNumber"))
if mibBuilder.loadTexts: vStationCardEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vStationCardEntry.setDescription('An entry in the Vertical Station Card table.')
vStationCardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationCardSlotNumber.setDescription('Physical slot in the system in which the card is installed.')
vStationCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4))).clone(namedValues=NamedValues(("card-type-NOT-CONFIGURED", 0), ("card-type-24-CHANNEL-STATION", 2), ("card-type-BRIDGE1", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardType.setStatus('mandatory')
if mibBuilder.loadTexts: vStationCardType.setDescription("The Vertical's card Type. The following types are defined: card-type-NOT-CONFIGURED = 0, card-type-24-CHANNEL-STATION = 2, card-type-BRIDGE1 = 4")
vStationCardIOPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardIOPortAddress.setStatus('mandatory')
if mibBuilder.loadTexts: vStationCardIOPortAddress.setDescription('The ISA bus base address for this Card.')
vStationCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 255))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("removed", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardState.setStatus('mandatory')
if mibBuilder.loadTexts: vStationCardState.setDescription('The current status of the card. The valid values are 0 -> Disabled, 1 -> Enabled, 0xff -> Removed.')
vStationCardErrorLED = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardErrorLED.setStatus('mandatory')
if mibBuilder.loadTexts: vStationCardErrorLED.setDescription('All Vertical cards have an ERROR LED and a READY LED. The combined values of these LEDs are as follows - ERRORLed READYLed VALUE OPERATIONAL DEFINITION OFF OFF (0 0) Invalid state ON OFF (1 0) Just after power up. This state remains until card is ready to service io. ON ON (1 1) Statue during software initialization OFF ON (0 1) The normal operational state of the card.')
vStationCardReadyLED = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardReadyLED.setStatus('mandatory')
if mibBuilder.loadTexts: vStationCardReadyLED.setDescription('All Vertical cards have a READY LED and an ERROR LED. The combined values of these LEDs are as follows - ERRORLed READYLed OPERATIONAL DEFINITION OFF OFF invalid state ON OFF Just after power up. This state remains until card is ready to service io. ON ON Statue during software initialization OFF ON The normal operational state of the card.')
vStationDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2), )
if mibBuilder.loadTexts: vStationDeviceTable.setStatus('current')
if mibBuilder.loadTexts: vStationDeviceTable.setDescription('Table of status, control and configuraion about station devices within the system. There are as many entries as there are station devices.')
vStationDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationDeviceSlotNumber"))
if mibBuilder.loadTexts: vStationDeviceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceEntry.setDescription('An entry in the Vertical Station device Configuration table.')
vStationDeviceSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceSlotNumber.setDescription('Physical slot number inside the system in which the card containing this device is installed')
vStationDeviceDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceDeviceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceDeviceNumber.setDescription('The logical device number for this station device in its card.')
vStationDeviceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceIfIndex.setDescription('The interface Index for this device. The value for this object correlates to the IfIndex found in MIB-II.')
vStationDeviceBaseIOAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceBaseIOAddress.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceBaseIOAddress.setDescription('The ISA bus base address for this Card.')
vStationDeviceEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDeviceEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceEnabled.setDescription('Setting this variable to Disabled will disable this particular station device. ')
vStationDeviceInterrupt = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceInterrupt.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceInterrupt.setDescription('Interrupt Request level for this card. ')
vStationDeviceNumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceNumChannels.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceNumChannels.setDescription('The ISA bus address for this Card.')
vStationDeviceMVIPStartingChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceMVIPStartingChannel.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceMVIPStartingChannel.setDescription('Vertical card revision level.')
vStationDeviceMVIPStream = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceMVIPStream.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceMVIPStream.setDescription('Vertical card identification number.')
vStationDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 8))).clone(namedValues=NamedValues(("dev-undef", 0), ("dev-station", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceType.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceType.setDescription('Specifies the Type of this device Valid values are : dev-undef, // 0 : undefined dev-station, // 8 : Station channels')
vStationDeviceChangePending = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDeviceChangePending.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDeviceChangePending.setDescription('Interrupt Request level for this card/trunk. ')
vStationChannelTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3), )
if mibBuilder.loadTexts: vStationChannelTable.setStatus('current')
if mibBuilder.loadTexts: vStationChannelTable.setDescription('Table of status, control and configuraion about station device channels within the system. There is an entry for each channel of each station device.')
vStationChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), (0, "VERTICAL-STATION-MIB", "vStationChannelIndex"))
if mibBuilder.loadTexts: vStationChannelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelEntry.setDescription('An entry in the Vertical Station device Configuration table.')
vStationChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelIndex.setDescription('This is the logical channel number of the channel within its station device. For 12 channel station devices, it is between 1 and 12 and for 24 channel stations, it is between 1 and 24.')
vStationChannelSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelSlotNumber.setDescription('The value for this object is the logical number of the slot in which the card containing this channel is located (vStationDeviceSlotNumber).')
vStationChannelDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelDeviceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelDeviceNumber.setDescription('The value for this object is the logical device number of the device containing this channel within its slot, ie vStationDeviceDeviceNumber ')
vStationChannelChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("loopStart", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelChannelType.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelChannelType.setDescription('The Channel Type. Valid values are 1 -> Loop Start')
vStationChannelMWIType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stutter", 1), ("lamp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelMWIType.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelMWIType.setDescription('Defines the type of Message Waiting Indication. The valid values are : 1 -> stutter, 2 -> lamp.')
vStationChannelOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("station", 1), ("voiceMail", 2), ("pBX", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelOperationMode.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelOperationMode.setDescription('Defines the operation mode of the channel. Valid values are : 1 -> station, 2 -> voiceMail, 3 -> PBX.')
vStationChannelState = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("notConfigured", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelState.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelState.setDescription('Indicates the operational status of this channel. Valid values are: 0 -> disabled, 1 -> enabled, 2 -> not configured ')
vStationChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("basic", 1), ("callerID", 2), ("callerID-callWaiting", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelType.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelType.setDescription('The phone type for this particular channel. Valid values are: 1 -> basic, 2 -> callerID, 3 -> callerID-callWaiting (caller ID with call waiting). ')
vStationChannelCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("call-state-VOID", 0), ("call-state-IDLE", 1), ("call-state-DIALING", 2), ("call-state-COLLECT-FIRST-DIGIT", 3), ("call-state-COLLECT-DIGITS", 4), ("call-state-CALL-OFFERED", 5), ("call-state-PROCEEDING", 6), ("call-state-RINGING", 7), ("call-state-ALERTING", 8), ("call-state-CONNECTED", 9), ("call-state-DISCONNECTING", 10), ("call-state-FAILED", 11), ("call-state-UNAVAILABLE", 12), ("call-state-OFFHOOK", 13), ("call-state-INITIALIZE", 14), ("call-state-INITIALIZING", 15), ("call-state-DIAL-REQUEST", 16), ("call-state-HELD", 17), ("call-state-FEATURE-INVOKED", 18), ("call-state-OFFHOOK-IDLE", 19), ("call-state-OFFHOOK-ACTIVE", 20), ("call-state-OUT-OF-SERVICE", 21), ("call-state-OUTPULSING", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelCallState.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelCallState.setDescription('Indicates the phone call state of this channel. Valid values are: call-state-VOID (0), -> invalid state call-state-IDLE (1), -> the line is in idle state call-state-DIALING (2), -> the line is originating a call call-state-COLLECT-FIRST-DIGIT (3), -> waiting to collect the first digit call-state-COLLECT-DIGITS (4), -> collecting additional digits call-state-CALL-OFFERED (5), -> the station call request has been offered to the PBX control call-state-PROCEEDING (6), -> the call is in progress call-state-RINGING (7), -> the call has seized a destination line call-state-ALERTING (8), -> the destination has been seized call-state-CONNECTED (9), -> the destination has answered the call call-state-DISCONNECTING (10), -> the call is in the process of terminating call-state-FAILED (11), -> the call attempt failed, wait for hangup call-state-UNAVAILABLE (12), -> destination is not available to receive call call-state-OFFHOOK (13), -> the call has been completed but the phone is offhook call-state-INITIALIZE (14), -> initialize the call object (binds with Conn Mgr) call-state-INITIALIZING (15), -> waiting for the response from Conn Mgr (Inservice Ack) call-state-DIAL-REQUEST (16), -> call object sent up OffhookInd and waiting for ACK call-state-HELD (17), -> the call has been put on hold call-state-FEATURE-INVOKED (18), -> indications that a feature has been invoked and waiting response call-state-OFFHOOK-IDLE (19), -> indicates that the phone is set to offhook and is IDLE call-state-OFFHOOK-ACTIVE (20), -> indicates that the phone is set to offhook and is ACTIVE call-state-OUT-OF-SERVICE (21), -> indicates that the phone is out of service call-state-OUTPULSING (22), -> digits are being sent to the external key or voice mail system')
vStationChannelCalledPartyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelCalledPartyNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelCalledPartyNumber.setDescription('Indicates the called party number, either an internal extension or external number.')
vStationChannelCallingPartyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelCallingPartyNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelCallingPartyNumber.setDescription('Indicates the calling party number, either an internal extension or external number.')
vStationChannelChangePending = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelChangePending.setStatus('mandatory')
if mibBuilder.loadTexts: vStationChannelChangePending.setDescription('Indicates that a change to the channel values have been made to the registry. The intepretation of the values are : 1 => change made to the registry, but not incorporated in the device yet 0 => the device changes the value to 0 from 1, after it incorporates the value from registry.')
vStationDigitTableGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 3))
vStationFirstDigitTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1), )
if mibBuilder.loadTexts: vStationFirstDigitTable.setStatus('current')
if mibBuilder.loadTexts: vStationFirstDigitTable.setDescription('Table of settings for each digits (0-9) which may be dialled as the first digit. There are 10 entries, one for each digit, in this table.')
vStationFirstDigitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationDigitIndex"))
if mibBuilder.loadTexts: vStationFirstDigitEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vStationFirstDigitEntry.setDescription('An entry in the Vertical Station First Digit Table.')
vStationDigitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDigitIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDigitIndex.setDescription('This is the index to an entry in the first digit table')
vStationDigitString = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDigitString.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDigitString.setDescription("The first digit string . Valid values : '0' to '9'")
vStationDigitCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("fc-VOID", 0), ("fc-HOLD-CALL", 1), ("fc-PARK-CALL", 2), ("fc-STATION-CALL", 3), ("fc-LONG-DISTANCE-CALL", 4), ("fc-INTERNATIONAL-CALL", 5), ("fc-LOCAL-CALL", 6), ("fc-OPERATOR-CALL", 7), ("fc-RECEPTIONIST-CALL", 8), ("fc-CAMP-ON-CALL", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitCallType.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDigitCallType.setDescription('Type of call generated by this digit. Valid values are : fc-VOID (0), // undefined feature code fc-HOLD-CALL (1), fc-PARK-CALL (2), fc-STATION-CALL (3), fc-LONG-DISTANCE-CALL (4), fc-INTERNATIONAL-CALL (5), fc-LOCAL-CALL (6), fc-OPERATOR-CALL (7), fc-RECEPTIONIST-CALL (8), fc-CAMP-ON-CALL (9)')
vStationDigitMoreDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitMoreDigits.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDigitMoreDigits.setDescription('The number of additional digits to collect after the matched digits.')
vStationDigitTimeout2 = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dontTerminate", 0), ("terminate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitTimeout2.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDigitTimeout2.setDescription('Indicates whether the dialling should terminate on a timeout. valid values are : dontTerminate -> 0 terminate -> 1')
vStationDigitStripDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitStripDigits.setStatus('mandatory')
if mibBuilder.loadTexts: vStationDigitStripDigits.setDescription('Indicates the number of leading digits to strip from the digitss collected before they are reported up to the connection manager.')
vStationExtVoiceMailGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 4))
vStationATTSystem25Group = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1))
vStationMWILampON = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationMWILampON.setStatus('mandatory')
if mibBuilder.loadTexts: vStationMWILampON.setDescription("Command expected from the external voice mail system to turn on a station's lamp.")
vStationMWILampOFF = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationMWILampOFF.setStatus('mandatory')
if mibBuilder.loadTexts: vStationMWILampOFF.setDescription("Command expected from the external voice mail system to turn off a station's lamp.")
vStationVMCallHandleTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3), )
if mibBuilder.loadTexts: vStationVMCallHandleTable.setStatus('current')
if mibBuilder.loadTexts: vStationVMCallHandleTable.setDescription('Table of settings and commands for accessing the voice mail port for different types of access, i.e. external caller coming directly to voice mail port, external caller being forwarded to a voice mail port, etc.')
vStationVMCallHandleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationVMCallHandleIndex"))
if mibBuilder.loadTexts: vStationVMCallHandleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vStationVMCallHandleEntry.setDescription('An entry in the Vertical Station Voice Mail call handle table.')
vStationVMCallHandleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationVMCallHandleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vStationVMCallHandleIndex.setDescription('This is the index to an entry in the Voice Mail call handle table.')
vStationVMCallHandleType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("directExternal", 1), ("forwardExternal", 2), ("directInternal", 3), ("forwardInternal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationVMCallHandleType.setStatus('mandatory')
if mibBuilder.loadTexts: vStationVMCallHandleType.setDescription('Indicates the type of access to voice mail port made. valid values are : directExternal (1) -> An external caller coming directly into the voice mail port. forwardExternal (2) -> An external caller caling an extension, but was then forwarded to the voice mail port. directInternal (3) -> An internal caller coming directly into the voice mail port. forwardInternal (4) -> An internal caller caling an extension, but was then forwarded to the voice mail port.')
vStationVMCallHandleOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationVMCallHandleOpcode.setStatus('mandatory')
if mibBuilder.loadTexts: vStationVMCallHandleOpcode.setDescription('The opcode string for this operation.')
vStationVMCallHandleSRCNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationVMCallHandleSRCNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationVMCallHandleSRCNumber.setDescription("The source number format string. It contains a C type '%s' where the source number would be filled in")
vStationVMCallHandleDSTNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationVMCallHandleDSTNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vStationVMCallHandleDSTNumber.setDescription("The destination number format string. It contains a C type '%s' where the destination number would be filled in")
vStationCannotPlayTone = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,12)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
if mibBuilder.loadTexts: vStationCannotPlayTone.setDescription(' This notification is sent when the specific channel cannot play tone. ')
vStationCannotCancelTone = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,13)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
if mibBuilder.loadTexts: vStationCannotCancelTone.setDescription(' This notification is sent when the specific channel cannot cancel tone. ')
vStationCannotAttachDigitCollector = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,14)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
if mibBuilder.loadTexts: vStationCannotAttachDigitCollector.setDescription(' This notification is sent when the specific channel cannot attach digits collected ')
vStationCannotReleaseDigitCollector = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,15)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
if mibBuilder.loadTexts: vStationCannotReleaseDigitCollector.setDescription(' This notification is sent when the specific channel cannot release digits collected ')
vStationRECONFIG_COMPLETE = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,16)).setLabel("vStationRECONFIG-COMPLETE").setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"))
if mibBuilder.loadTexts: vStationRECONFIG_COMPLETE.setDescription(' This notification is sent when the specific station device successfully reads and incorporates the values from the registry.')
vStationRECONFIG_ERROR = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,17)).setLabel("vStationRECONFIG-ERROR").setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"))
if mibBuilder.loadTexts: vStationRECONFIG_ERROR.setDescription(' This notification is sent when the specific station device fails to incorporate the values read from the registry. ')
mibBuilder.exportSymbols("VERTICAL-STATION-MIB", vStationCardReadyLED=vStationCardReadyLED, vStationATTSystem25Group=vStationATTSystem25Group, vStationOffHookTimeout=vStationOffHookTimeout, vStationCannotReleaseDigitCollector=vStationCannotReleaseDigitCollector, vStationCardState=vStationCardState, vStationDeviceDeviceNumber=vStationDeviceDeviceNumber, vStationChannelOperationMode=vStationChannelOperationMode, vStationCannotAttachDigitCollector=vStationCannotAttachDigitCollector, vertical=vertical, vStationNumStationCards=vStationNumStationCards, vStationChannelCalledPartyNumber=vStationChannelCalledPartyNumber, vStationDeviceSlotNumber=vStationDeviceSlotNumber, vStationChannelChangePending=vStationChannelChangePending, vStationChannelIndex=vStationChannelIndex, vStationDigitTimeout2=vStationDigitTimeout2, vStationChannelEntry=vStationChannelEntry, vStationCommonGroup=vStationCommonGroup, vStationChannelSlotNumber=vStationChannelSlotNumber, vStationChannelTable=vStationChannelTable, vStationVMCallHandleOpcode=vStationVMCallHandleOpcode, vStationChannelMWIType=vStationChannelMWIType, vStationDeviceIfIndex=vStationDeviceIfIndex, vStationRECONFIG_ERROR=vStationRECONFIG_ERROR, vStationCannotPlayTone=vStationCannotPlayTone, vStationRECONFIG_COMPLETE=vStationRECONFIG_COMPLETE, vStationDeviceInterrupt=vStationDeviceInterrupt, vStationExternalDialDigit=vStationExternalDialDigit, vStationVMCallHandleDSTNumber=vStationVMCallHandleDSTNumber, vStationDeviceMVIPStartingChannel=vStationDeviceMVIPStartingChannel, vStationChannelCallingPartyNumber=vStationChannelCallingPartyNumber, vStationVMCallHandleEntry=vStationVMCallHandleEntry, vStationDigitTableGroup=vStationDigitTableGroup, vStationChannelChannelType=vStationChannelChannelType, vStationDigitString=vStationDigitString, vStationDigitCallType=vStationDigitCallType, vStationVMCallHandleType=vStationVMCallHandleType, vStationDeviceEnabled=vStationDeviceEnabled, vStationChannelDeviceNumber=vStationChannelDeviceNumber, vStationVMCallHandleTable=vStationVMCallHandleTable, vStationDigitMoreDigits=vStationDigitMoreDigits, vStationDigitStripDigits=vStationDigitStripDigits, vStationCardTable=vStationCardTable, vStationCardEntry=vStationCardEntry, vStationCardErrorLED=vStationCardErrorLED, vStationChannelState=vStationChannelState, vStationChannelCallState=vStationChannelCallState, vStationFirstDigitTable=vStationFirstDigitTable, vStationDigitIndex=vStationDigitIndex, vStationVMCallHandleIndex=vStationVMCallHandleIndex, vStationDeviceMVIPStream=vStationDeviceMVIPStream, vStationMWILampOFF=vStationMWILampOFF, vStationCannotCancelTone=vStationCannotCancelTone, vStationExtVoiceMailGroup=vStationExtVoiceMailGroup, vStationFirstDigitTimeout=vStationFirstDigitTimeout, vStationMWILampON=vStationMWILampON, vStationDigitTimeout=vStationDigitTimeout, vStationChannelType=vStationChannelType, vStationModule=vStationModule, vStationDeviceEntry=vStationDeviceEntry, vStationDeviceType=vStationDeviceType, vStationDeviceChangePending=vStationDeviceChangePending, vStationCardSlotNumber=vStationCardSlotNumber, vStationDeviceBaseIOAddress=vStationDeviceBaseIOAddress, vStationCardGroup=vStationCardGroup, vStationFirstDigitEntry=vStationFirstDigitEntry, vStationDeviceNumChannels=vStationDeviceNumChannels, vStationVMCallHandleSRCNumber=vStationVMCallHandleSRCNumber, vStationCardType=vStationCardType, vStationDeviceTable=vStationDeviceTable, vStationCardIOPortAddress=vStationCardIOPortAddress)
