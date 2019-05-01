#
# PySNMP MIB module RFC1231-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1231-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:35:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, Unsigned32, iso, MibIdentifier, NotificationType, transmission, IpAddress, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "Unsigned32", "iso", "MibIdentifier", "NotificationType", "transmission", "IpAddress", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dot5 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9))
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

dot5Table = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 1), )
if mibBuilder.loadTexts: dot5Table.setStatus('mandatory')
if mibBuilder.loadTexts: dot5Table.setDescription('This table contains Token Ring interface parameters and state variables, one entry per 802.5 interface.')
dot5Entry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 1, 1), ).setIndexNames((0, "RFC1231-MIB", "dot5IfIndex"))
if mibBuilder.loadTexts: dot5Entry.setStatus('mandatory')
if mibBuilder.loadTexts: dot5Entry.setDescription('A list of Token Ring status and parameter values for an 802.5 interface.')
dot5IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5IfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dot5IfIndex.setDescription('The value of this object identifies the 802.5 interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in [4,6], for the same interface.')
dot5Commands = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-op", 1), ("open", 2), ("reset", 3), ("close", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5Commands.setStatus('mandatory')
if mibBuilder.loadTexts: dot5Commands.setDescription('When this object is set to the value of open(2), the station should go into the open state. The progress and success of the open is given by the values of the objects dot5RingState and dot5RingOpenStatus. When this object is set to the value of reset(3), then the station should do a reset. On a reset, all MIB counters should retain their values, if possible. Other side affects are dependent on the hardware chip set. When this object is set to the value of close(4), the station should go into the stopped state by removing itself from the ring. Setting this object to a value of no-op(1) has no effect. When read, this object always has a value of no-op(1).')
dot5RingStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5RingStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dot5RingStatus.setDescription("The current interface status which can be used to diagnose fluctuating problems that can occur on token rings, after a station has successfully been added to the ring. Before an open is completed, this object has the value for the 'no status' condition. The dot5RingState and dot5RingOpenStatus objects provide for debugging problems when the station can not even enter the ring. The object's value is a sum of values, one for each currently applicable condition. The following values are defined for various conditions: 0 = No Problems detected 32 = Ring Recovery 64 = Single Station 256 = Remove Received 512 = reserved 1024 = Auto-Removal Error 2048 = Lobe Wire Fault 4096 = Transmit Beacon 8192 = Soft Error 16384 = Hard Error 32768 = Signal Loss 131072 = no status, open not completed.")
dot5RingState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("opened", 1), ("closed", 2), ("opening", 3), ("closing", 4), ("openFailure", 5), ("ringFailure", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5RingState.setStatus('mandatory')
if mibBuilder.loadTexts: dot5RingState.setDescription('The current interface state with respect to entering or leaving the ring.')
dot5RingOpenStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("noOpen", 1), ("badParam", 2), ("lobeFailed", 3), ("signalLoss", 4), ("insertionTimeout", 5), ("ringFailed", 6), ("beaconing", 7), ("duplicateMAC", 8), ("requestFailed", 9), ("removeReceived", 10), ("open", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5RingOpenStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dot5RingOpenStatus.setDescription("This object indicates the success, or the reason for failure, of the station's most recent attempt to enter the ring.")
dot5RingSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("oneMegabit", 2), ("fourMegabit", 3), ("sixteenMegabit", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5RingSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: dot5RingSpeed.setDescription("The ring's bandwidth.")
dot5UpStream = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5UpStream.setStatus('mandatory')
if mibBuilder.loadTexts: dot5UpStream.setDescription('The MAC-address of the up stream neighbor station in the ring.')
dot5ActMonParticipate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5ActMonParticipate.setStatus('mandatory')
if mibBuilder.loadTexts: dot5ActMonParticipate.setDescription('If this object has a value of true(1) then this interface will participate in the active monitor selection process. If the value is false(2) then it will not. Setting this object might not have an effect until the next time the interface is opened.')
dot5Functional = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 9), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5Functional.setStatus('mandatory')
if mibBuilder.loadTexts: dot5Functional.setDescription('The bit mask of all Token Ring functional addresses for which this interface will accept frames.')
dot5StatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 2), )
if mibBuilder.loadTexts: dot5StatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsTable.setDescription("A table containing Token Ring statistics, one entry per 802.5 interface. All the statistics are defined using the syntax Counter as 32-bit wrap around counters. Thus, if an interface's hardware maintains these statistics in 16-bit counters, then the agent must read the hardware's counters frequently enough to prevent loss of significance, in order to maintain 32-bit counters in software.")
dot5StatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 2, 1), ).setIndexNames((0, "RFC1231-MIB", "dot5StatsIfIndex"))
if mibBuilder.loadTexts: dot5StatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsEntry.setDescription('An entry contains the 802.5 statistics for a particular interface.')
dot5StatsIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsIfIndex.setDescription('The value of this object identifies the 802.5 interface for which this entry contains management information. The value of this object for a particular interface has the same value as the ifIndex object, defined in [4,6], for the same interface.')
dot5StatsLineErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsLineErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsLineErrors.setDescription('This counter is incremented when a frame or token is copied or repeated by a station, the E bit is zero in the frame or token and one of the following conditions exists: 1) there is a non-data bit (J or K bit) between the SD and the ED of the frame or token, or 2) there is an FCS error in the frame.')
dot5StatsBurstErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsBurstErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsBurstErrors.setDescription('This counter is incremented when a station detects the absence of transitions for five half-bit timers (burst-five error).')
dot5StatsACErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsACErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsACErrors.setDescription('This counter is incremented when a station receives an AMP or SMP frame in which A is equal to C is equal to 0, and then receives another SMP frame with A is equal to C is equal to 0 without first receiving an AMP frame. It denotes a station that cannot set the AC bits properly.')
dot5StatsAbortTransErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsAbortTransErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsAbortTransErrors.setDescription('This counter is incremented when a station transmits an abort delimiter while transmitting.')
dot5StatsInternalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsInternalErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsInternalErrors.setDescription('This counter is incremented when a station recognizes an internal error.')
dot5StatsLostFrameErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsLostFrameErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsLostFrameErrors.setDescription('This counter is incremented when a station is transmitting and its TRR timer expires. This condition denotes a condition where a transmitting station in strip mode does not receive the trailer of the frame before the TRR timer goes off.')
dot5StatsReceiveCongestions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsReceiveCongestions.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsReceiveCongestions.setDescription('This counter is incremented when a station recognizes a frame addressed to its specific address, but has no available buffer space indicating that the station is congested.')
dot5StatsFrameCopiedErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsFrameCopiedErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsFrameCopiedErrors.setDescription('This counter is incremented when a station recognizes a frame addressed to its specific address and detects that the FS field A bits are set to 1 indicating a possible line hit or duplicate address.')
dot5StatsTokenErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsTokenErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsTokenErrors.setDescription('This counter is incremented when a station acting as the active monitor recognizes an error condition that needs a token transmitted.')
dot5StatsSoftErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsSoftErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsSoftErrors.setDescription('The number of Soft Errors the interface has detected. It directly corresponds to the number of Report Error MAC frames that this interface has transmitted. Soft Errors are those which are recoverable by the MAC layer protocols.')
dot5StatsHardErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsHardErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsHardErrors.setDescription('The number of times this interface has detected an immediately recoverable fatal error. It denotes the number of times this interface is either transmitting or receiving beacon MAC frames.')
dot5StatsSignalLoss = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsSignalLoss.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsSignalLoss.setDescription('The number of times this interface has detected the loss of signal condition from the ring.')
dot5StatsTransmitBeacons = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsTransmitBeacons.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsTransmitBeacons.setDescription('The number of times this interface has transmitted a beacon frame.')
dot5StatsRecoverys = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsRecoverys.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsRecoverys.setDescription('The number of Claim Token MAC frames received or transmitted after the interface has received a Ring Purge MAC frame. This counter signifies the number of times the ring has been purged and is being recovered back into a normal operating state.')
dot5StatsLobeWires = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsLobeWires.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsLobeWires.setDescription('The number of times the interface has detected an open or short circuit in the lobe data path. The adapter will be closed and dot5RingState will signify this condition.')
dot5StatsRemoves = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsRemoves.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsRemoves.setDescription('The number of times the interface has received a Remove Ring Station MAC frame request. When this frame is received the interface will enter the close state and dot5RingState will signify this condition.')
dot5StatsSingles = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsSingles.setStatus('mandatory')
if mibBuilder.loadTexts: dot5StatsSingles.setDescription('The number of times the interface has sensed that it is the only station on the ring. This will happen if the interface is the first one up on a ring, or if there is a hardware problem.')
dot5StatsFreqErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsFreqErrors.setStatus('optional')
if mibBuilder.loadTexts: dot5StatsFreqErrors.setDescription('The number of times the interface has detected that the frequency of the incoming signal differs from the expected frequency by more than that specified by the IEEE 802.5 standard, see chapter 7 in [10].')
dot5TimerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 5), )
if mibBuilder.loadTexts: dot5TimerTable.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerTable.setDescription('This table contains Token Ring interface timer values, one entry per 802.5 interface.')
dot5TimerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 5, 1), ).setIndexNames((0, "RFC1231-MIB", "dot5TimerIfIndex"))
if mibBuilder.loadTexts: dot5TimerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerEntry.setDescription('A list of Token Ring timer values for an 802.5 interface.')
dot5TimerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerIfIndex.setDescription('The value of this object identifies the 802.5 interface for which this entry contains timer values. The value of this object for a particular interface has the same value as the ifIndex object, defined in [4,6], for the same interface.')
dot5TimerReturnRepeat = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerReturnRepeat.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerReturnRepeat.setDescription('The time-out value used to ensure the interface will return to Repeat State, in units of 100 micro-seconds. The value should be greater than the maximum ring latency. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerHolding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerHolding.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerHolding.setDescription('Maximum period of time a station is permitted to transmit frames after capturing a token, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerQueuePDU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerQueuePDU.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerQueuePDU.setDescription('The time-out value for enqueuing of an SMP PDU after reception of an AMP or SMP frame in which the A and C bits were equal to 0, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerValidTransmit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerValidTransmit.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerValidTransmit.setDescription('The time-out value used by the active monitor to detect the absence of valid transmissions, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerNoToken = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerNoToken.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerNoToken.setDescription('The time-out value used to recover from various-related error situations [9]. If N is the maximum number of stations on the ring, the value of this timer is normally: dot5TimerReturnRepeat + N*dot5TimerHolding. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerActiveMon = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerActiveMon.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerActiveMon.setDescription('The time-out value used by the active monitor to stimulate the enqueuing of an AMP PDU for transmission, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerStandbyMon = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerStandbyMon.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerStandbyMon.setDescription('The time-out value used by the stand-by monitors to ensure that there is an active monitor on the ring and to detect a continuous stream of tokens, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerErrorReport = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerErrorReport.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerErrorReport.setDescription('The time-out value which determines how often a station shall send a Report Error MAC frame to report its error counters, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerBeaconTransmit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerBeaconTransmit.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerBeaconTransmit.setDescription('The time-out value which determines how long a station shall remain in the state of transmitting Beacon frames before entering the Bypass state, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5TimerBeaconReceive = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerBeaconReceive.setStatus('mandatory')
if mibBuilder.loadTexts: dot5TimerBeaconReceive.setDescription('The time-out value which determines how long a station shall receive Beacon frames from its downstream neighbor before entering the Bypass state, in units of 100 micro-seconds. Implementors are encouraged to provide read-write access to this object if that is possible/useful in their system, but giving due consideration to the dangers of write-able timers.')
dot5Tests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 3))
testInsertFunc = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 3, 1))
dot5ChipSets = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4))
chipSetIBM16 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4, 1))
chipSetTItms380 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4, 2))
chipSetTItms380c16 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4, 3))
mibBuilder.exportSymbols("RFC1231-MIB", dot5TimerErrorReport=dot5TimerErrorReport, dot5StatsFreqErrors=dot5StatsFreqErrors, dot5Commands=dot5Commands, dot5RingOpenStatus=dot5RingOpenStatus, dot5TimerReturnRepeat=dot5TimerReturnRepeat, dot5ChipSets=dot5ChipSets, chipSetTItms380=chipSetTItms380, dot5ActMonParticipate=dot5ActMonParticipate, dot5TimerIfIndex=dot5TimerIfIndex, dot5IfIndex=dot5IfIndex, dot5StatsIfIndex=dot5StatsIfIndex, dot5TimerValidTransmit=dot5TimerValidTransmit, dot5StatsReceiveCongestions=dot5StatsReceiveCongestions, dot5StatsRecoverys=dot5StatsRecoverys, dot5TimerActiveMon=dot5TimerActiveMon, dot5Table=dot5Table, dot5StatsRemoves=dot5StatsRemoves, dot5StatsLostFrameErrors=dot5StatsLostFrameErrors, dot5StatsLineErrors=dot5StatsLineErrors, dot5=dot5, dot5TimerHolding=dot5TimerHolding, dot5StatsACErrors=dot5StatsACErrors, dot5TimerBeaconReceive=dot5TimerBeaconReceive, MacAddress=MacAddress, dot5StatsAbortTransErrors=dot5StatsAbortTransErrors, dot5TimerTable=dot5TimerTable, dot5StatsSoftErrors=dot5StatsSoftErrors, dot5Functional=dot5Functional, dot5StatsSignalLoss=dot5StatsSignalLoss, dot5UpStream=dot5UpStream, dot5StatsLobeWires=dot5StatsLobeWires, dot5StatsFrameCopiedErrors=dot5StatsFrameCopiedErrors, dot5StatsBurstErrors=dot5StatsBurstErrors, dot5TimerStandbyMon=dot5TimerStandbyMon, dot5RingSpeed=dot5RingSpeed, dot5TimerNoToken=dot5TimerNoToken, dot5StatsTable=dot5StatsTable, dot5StatsSingles=dot5StatsSingles, dot5TimerEntry=dot5TimerEntry, dot5TimerQueuePDU=dot5TimerQueuePDU, dot5RingState=dot5RingState, dot5Entry=dot5Entry, dot5RingStatus=dot5RingStatus, dot5TimerBeaconTransmit=dot5TimerBeaconTransmit, dot5StatsTokenErrors=dot5StatsTokenErrors, testInsertFunc=testInsertFunc, dot5StatsTransmitBeacons=dot5StatsTransmitBeacons, chipSetIBM16=chipSetIBM16, dot5StatsInternalErrors=dot5StatsInternalErrors, chipSetTItms380c16=chipSetTItms380c16, dot5StatsHardErrors=dot5StatsHardErrors, dot5StatsEntry=dot5StatsEntry, dot5Tests=dot5Tests)
