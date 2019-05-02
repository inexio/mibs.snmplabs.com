#
# PySNMP MIB module VISM-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VISM-SESSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
voice, = mibBuilder.importSymbols("BASIS-MIB", "voice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Gauge32, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, MibIdentifier, IpAddress, Bits, ObjectIdentity, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Gauge32", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "MibIdentifier", "IpAddress", "Bits", "ObjectIdentity", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vismSessionGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11))
class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

vismSessionSetTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1), )
if mibBuilder.loadTexts: vismSessionSetTable.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetTable.setDescription('This table has entries for a collection of sessGrp(s) each providing connectivity to a different Media gateway Controller (MGC).')
vismSessionSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1), ).setIndexNames((0, "VISM-SESSION-MIB", "vismSessionSetNum"))
if mibBuilder.loadTexts: vismSessionSetEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetEntry.setDescription('An entry for vismSessionSetTable.')
vismSessionSetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionSetNum.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetNum.setDescription('This is the logical index of this table. Currently only set 1 is used and all the signaling channels are implicitly mapped to set 1. ')
vismSessionSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismSessionSetRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetRowStatus.setDescription("This variable is used to allow add or delete a session set. createAndGo: Use this to add an entry in set table. vismSessionSetNum and vismSessionSetFaultTolerant are the mandatory parameters while adding a set. Currently only one set (set #1) can be created. The entry will become 'active' after creation. A set entry may be deleted by setting this object to 'destory'. Deletion of a set is not allowed if there is still group in this set. ")
vismSessionSetState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("oos", 2), ("activeIs", 3), ("standbyIs", 4), ("fullIs", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionSetState.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetState.setDescription("When an entry in sessionSet table is created and no group has been added to this set yet or group has been created in this set but no session has been added yet the set state is 'idle'. After a group has been created in this set and one session has been added to the group the set state becomes 'oos',i.e, out of service. After successfully open socket and the session has sent START message to MGC, the state of the set will be changed based on whether this set is fault tolerant(FT) or none fault tolerant(NFT). In NFT case the set state becomes 'activeIs'. In FT case, if one session from a group received an active message from MGC and no standby message received from a session in the other group, the state of the set will change to 'activeIs'. On the other hand, if at least one session from a group received standby message from MGC and no other session from the other group received active message then the set state is transferred to 'standbyIs'. The set becomes 'fullIs' when at least one session from one group receives active message and at least one session from the other group receives standby message. 'unknown' is a state other than the above states. ")
vismSessionSetTotalGrps = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionSetTotalGrps.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetTotalGrps.setDescription('This counter keeps track the number of session groups that has been added to a session set.')
vismSessionSetActiveGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionSetActiveGrp.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetActiveGrp.setDescription('This is the current active group number.')
vismSessionSetSwitchFails = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionSetSwitchFails.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetSwitchFails.setDescription('This counter keeps track of failed attempts to switch between session groups in this set.')
vismSessionSetSwitchSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionSetSwitchSuccesses.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetSwitchSuccesses.setDescription('This counter keeps track of successful attempts to switch between session groups in this set. ')
vismSessionSetFaultTolerant = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismSessionSetFaultTolerant.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionSetFaultTolerant.setDescription('This object indicates whether the set configuration is fault tolerant or not. If the set is fault tolerant then there can be two groups in this set. If the set is non-fault tolerant then only one group can be added in this set. Once the entry is created this object cannot be modified. ')
vismSessionGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2), )
if mibBuilder.loadTexts: vismSessionGrpTable.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpTable.setDescription('This table has entries for a collection of sessions')
vismSessionGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1), ).setIndexNames((0, "VISM-SESSION-MIB", "vismSessionGrpNum"))
if mibBuilder.loadTexts: vismSessionGrpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpEntry.setDescription('An entry for vismSessionGrpTable.')
vismSessionGrpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionGrpNum.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpNum.setDescription('Index for vismSessionGrpEntry table. Currently the range of 1 to 16 is used. One set can have upto two groups. ')
vismSessionGrpSetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismSessionGrpSetNum.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpSetNum.setDescription('This is the session set number to which this session Group belongs. Once the entry is created this object cannot be modified. ')
vismSessionGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismSessionGrpRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpRowStatus.setDescription('This variable allows to add or delete an entry in this table. createAndGo: Use this to add an entry in this table. vismSessionGrpNum, vismSessionGrpSetNum and vismSessionGrpMgcName are required to add an entry. Before adding the session group, the session set should already be created. active: This value is returned once the session group is created destroy: Use this to delete a session group. Session group number is the only mandatory parameter to delete an entry. ')
vismSessionGrpState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("oos", 2), ("is", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionGrpState.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpState.setDescription("'idle': This is the initial state. 'oos': Out of service state. when a session group has been created the state of the session group becomes 'oos' or when all sessions belonging to this group are deleted, session group state becomes 'oos' 'is': In service state. After at least one session has been added to the group, socket has been successfully set up and the session has sent a START message to MGC the group state changes to 'is'. 'unknown': This is the state other than the above states. ")
vismSessionGrpCurrSession = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionGrpCurrSession.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpCurrSession.setDescription('This object indicates the current session that is open to communication with MGC. There is only one active session per session group.')
vismSessionGrpTotalSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionGrpTotalSessions.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpTotalSessions.setDescription('This object keeps track the total number of sessions that have been added to this group. ')
vismSessionGrpSwitchFails = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionGrpSwitchFails.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpSwitchFails.setDescription('This counter keeps track of failed attempts to switch between sessions in this group.')
vismSessionGrpSwitchSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismSessionGrpSwitchSuccesses.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpSwitchSuccesses.setDescription('This counter keeps track of successful attempts to switch between sessions in this group.')
vismSessionGrpMgcName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismSessionGrpMgcName.setStatus('mandatory')
if mibBuilder.loadTexts: vismSessionGrpMgcName.setDescription('This denotes the name of the media gateway controller. This corresponds to a domain name under which the MGC could also be registered in a DNS. Once this entry becomes active, this value may not be modified. ')
vismRudpSessionCnfTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3), )
if mibBuilder.loadTexts: vismRudpSessionCnfTable.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionCnfTable.setDescription('This table has entries of sessions, which are the connection between MGC and a gateway (VISM). A session is identified by a local IP address, port, remote IP address and remote port. The combination of these four numbers has to be unique to identify one session. This table also maintains the configuration for every session.')
vismRudpSessionCnfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1), ).setIndexNames((0, "VISM-SESSION-MIB", "vismRudpSessionNum"))
if mibBuilder.loadTexts: vismRudpSessionCnfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionCnfEntry.setDescription('An entry for vismSessionCnfEntry.')
vismRudpSessionNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionNum.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionNum.setDescription('This is the index of vismRudpSessionCnfEntry table. Currently the range of 1 to 64 is used. One group can have maximum four sessions. ')
vismRudpSessionGrpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionGrpNum.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionGrpNum.setDescription('This indicates the session group that this session belongs to. Currently the range of 1 to 16 is used. Once the entry is created, it cannot be modified. ')
vismRudpSessionCnfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionCnfRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionCnfRowStatus.setDescription('This variable allows the user to add or delete the entry for this table. createAndGo: Use this to add a Rudp session in this table. Rudp session number, session group number, priority, local port and remote port are required while creating an entry for PRI Backhaul. On the other hand Rudp session number, local port, remote port, remote VISM IP and rudp session type are required for Lapd trunking. active: This value is returned, once the row is created. destroy: Use this to delete an RUDP session from this table. Only RUDP session number is needed for deleting. The last session shall not be deleted if there are still active LAPD entries. ')
vismRudpSessionPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionPriority.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionPriority.setDescription('This object is used when creating a Rudp session. Once a session has been added it can not be modified. When a session fails it indicates which session the session manager should try to bring active. A lower number means higher priority. ')
vismRudpSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oos", 1), ("is", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionState.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionState.setDescription("'oos': Out of service state. This is the initial state when create a RUDP session. 'is': In service state. When a channel has been created between gateway (VISM) and MGC and VISM has sent Start message the state of the session changes to 'is'. If the communication is lost between VISM and the MGC, the state of this session becomes 'oos'. 'unknown': This is the state other than the above states. ")
vismRudpSessionCurrSession = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionCurrSession.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionCurrSession.setDescription("This object indicates which session has got active message from MGC. The session manager will always try to bring the first added session to active. If the current active session fails the state of this session is changed to 'oos' and the session manager will try to bring the 'primary-is' session with highest priority among the rest of sessions in this group to active. ")
vismRudpSessionLocalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionLocalIp.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionLocalIp.setDescription('The IP address of gateway (VISM).')
vismRudpSessionLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1124, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionLocalPort.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionLocalPort.setDescription('The port number of gateway (VISM) for this session. It can be modified after creation. This port number should be unique across other sessions and XGCP/SRCP. ')
vismRudpSessionRmtIp = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionRmtIp.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRmtIp.setDescription('This is the IP address of the media gateway controller. It is resolved by using vismSessionGrpMgcName in vismSessionGrpTable. ')
vismRudpSessionRmtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1124, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionRmtPort.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRmtPort.setDescription('The port number of MGC for this session. It can be modified after creation. This port number should be unique across other sessions and XGCP/SRCP. ')
vismRudpSessionMaxWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionMaxWindow.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionMaxWindow.setDescription('This object is the maximum number of segments that should be sent without getting an acknowledgment, i.e. the max size of the receive window in segments. This is used for flow control. This object can be modified after a session is created. ')
vismRudpSessionSyncAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionSyncAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionSyncAttempts.setDescription('Maximum number of attempts to synchronize with other side (MGC). This object can be modified after a session is created. ')
vismRudpSessionMaxSegSize = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(384)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionMaxSegSize.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionMaxSegSize.setDescription('The maximum number of octets that can be received by the peer sending the SYN segment. This object can be modified after a session is created. ')
vismRudpSessionMaxAutoReset = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionMaxAutoReset.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionMaxAutoReset.setDescription('The maximum number of consecutive auto reset that will be performed before a connection is reset. A value 0 indicates that an auto reset will not be attempted, the connection will be reset immediately if an auto reset condition occurs. This object can be modified after a session is created. ')
vismRudpSessionRetransTmout = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 65535)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionRetransTmout.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRetransTmout.setDescription('The timeout value for retransmission of unacknowledged packets in milliseconds. This is a negotiable parameter, MGC and VISM must agree on the same value for this parameter. This object can be modified after a session is created. ')
vismRudpSessionMaxRetrans = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionMaxRetrans.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionMaxRetrans.setDescription('The maximum number of times consecutive retransmission will be attempted before the connection is considered broken. A value 0 indicates retransmission should be attempted forever. This is a negotiable parameter, both MGC and VISM must agree on the value for this parameter. This object can be modified after a session is created. ')
vismRudpSessionMaxCumAck = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionMaxCumAck.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionMaxCumAck.setDescription('This object indicates the maximum number of acknowledgments that will be accumulated before sending an acknowledgment if another segment is not sent. A value of 0 indicates an acknowledgment segment will be sent immediately when a data, null, or reset segment is received. Negotiable parameter. This object can be modified after a session is created. ')
vismRudpSessionCumAckTmout = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 65535)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionCumAckTmout.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionCumAckTmout.setDescription('This object is the timeout value for sending an acknowledgment segment if another segment is not sent. This value is specified in milliseconds. This parameter should be smaller than rudpRetransTmout. Negotiable parameter. This object can be modified after a session is created. ')
vismRudpSessionMaxOutOfSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionMaxOutOfSeq.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionMaxOutOfSeq.setDescription('This object is the maximum number of out of sequence packets that will be accumulated before an EACK segment is sent. The EACK segment is used to acknowledge segments received out of sequence. A value of 0 indicates a EACK will be sent immediately if an out of order segment is received. Negotiable parameter. This object can be modified after a session is created. ')
vismRudpSessionNullSegTmout = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(2000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionNullSegTmout.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionNullSegTmout.setDescription('This object is the number of milliseconds of idle time before sending a null segment. A value of 0 disables null segments. Negotiable parameter. This object can be modified after a session is created. ')
vismRudpSessionTransStateTmout = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(2000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionTransStateTmout.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionTransStateTmout.setDescription('This object indicates the number of milliseconds to wait for transfer state before an auto reset occurs. 0 indicates the connection will be auto-reset immediately and would not be used with redundant links. This object can be modified after a session is created. ')
vismRudpSessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backhaul", 1), ("lapdTrunking", 2))).clone('backhaul')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionType.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionType.setDescription("This object indicates if the session is configured for Trunking or PRI Backhaul. By default the object is set to 'backhaul' and it needs to set to lapdTrunking if Lapd trunking needs to be done. ")
vismRudpSessionRmtGwIp = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 3, 1, 23), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismRudpSessionRmtGwIp.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRmtGwIp.setDescription('This is the IP address of the remote VISM. This will be used only for Lapd Trunking applications and the vismRudpSessionType must be set to Lapd trunking. ')
vismRudpSessionStatTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4), )
if mibBuilder.loadTexts: vismRudpSessionStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionStatTable.setDescription('This table keeps track of state and connection-specific counts. It is per connection based.')
vismRudpSessionStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1), ).setIndexNames((0, "VISM-SESSION-MIB", "vismRudpSessionStatNum"))
if mibBuilder.loadTexts: vismRudpSessionStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionStatEntry.setDescription('An entry for vismSessionStatEntry.')
vismRudpSessionStatNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionStatNum.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionStatNum.setDescription('This is the index of vismRudpSessionStatEntry table. Currently the range of 1 to 64 is used. It is the same as the index of vismRudpSessionCnfEntry table.')
vismRudpSessionAutoResets = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionAutoResets.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionAutoResets.setDescription('Auto reset is also known as soft reset. VISM (gateway) initiates an auto reset when it detects that a connection has failed. This keeps track of the number of auto resets initiated by VISM. ')
vismRudpSessionRcvdAutoResets = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionRcvdAutoResets.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRcvdAutoResets.setDescription('This is the counter for the number of auto resets initiated by MGC and received by VISM. ')
vismRudpSessionRcvdInSeqs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionRcvdInSeqs.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRcvdInSeqs.setDescription('This object indicates number of packets received in sequence. ')
vismRudpSessionRcvdOutSeqs = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionRcvdOutSeqs.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRcvdOutSeqs.setDescription('Number of packets received out of sequence.')
vismRudpSessionSentPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionSentPackets.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionSentPackets.setDescription('This is the number of packets sent by VISM. Including SYN message.')
vismRudpSessionRcvdPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionRcvdPackets.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRcvdPackets.setDescription('This is the number of packets received by VISM. Including active message. ')
vismRudpSessionSentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionSentBytes.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionSentBytes.setDescription('This object indicates the number of bytes sent to MGC.')
vismRudpSessionRcvdBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionRcvdBytes.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRcvdBytes.setDescription('This object keeps track of the number of bytes received from MGC. ')
vismRudpSessionDataSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionDataSentPkts.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionDataSentPkts.setDescription('This object is the number of data packets sent to MGC.')
vismRudpSessionDataRcvdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionDataRcvdPkts.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionDataRcvdPkts.setDescription('This object is the number of data packets received from MGC.')
vismRudpSessionDiscardPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionDiscardPkts.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionDiscardPkts.setDescription('This is the number of packets discarded.')
vismRudpSessionRetransPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 11, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismRudpSessionRetransPkts.setStatus('mandatory')
if mibBuilder.loadTexts: vismRudpSessionRetransPkts.setDescription('This is the number of packets retransmitted.')
mibBuilder.exportSymbols("VISM-SESSION-MIB", vismRudpSessionMaxRetrans=vismRudpSessionMaxRetrans, vismRudpSessionStatTable=vismRudpSessionStatTable, TruthValue=TruthValue, vismRudpSessionGrpNum=vismRudpSessionGrpNum, vismRudpSessionDataRcvdPkts=vismRudpSessionDataRcvdPkts, vismSessionSetEntry=vismSessionSetEntry, vismSessionGrpSetNum=vismSessionGrpSetNum, vismRudpSessionRcvdInSeqs=vismRudpSessionRcvdInSeqs, vismSessionSetSwitchFails=vismSessionSetSwitchFails, vismRudpSessionRcvdOutSeqs=vismRudpSessionRcvdOutSeqs, vismSessionGrpNum=vismSessionGrpNum, vismRudpSessionLocalIp=vismRudpSessionLocalIp, vismRudpSessionCnfTable=vismRudpSessionCnfTable, vismRudpSessionRcvdAutoResets=vismRudpSessionRcvdAutoResets, vismRudpSessionDiscardPkts=vismRudpSessionDiscardPkts, vismRudpSessionTransStateTmout=vismRudpSessionTransStateTmout, vismRudpSessionState=vismRudpSessionState, vismRudpSessionLocalPort=vismRudpSessionLocalPort, vismSessionSetNum=vismSessionSetNum, vismRudpSessionCnfEntry=vismRudpSessionCnfEntry, vismRudpSessionMaxAutoReset=vismRudpSessionMaxAutoReset, vismRudpSessionDataSentPkts=vismRudpSessionDataSentPkts, vismSessionGrpSwitchFails=vismSessionGrpSwitchFails, vismRudpSessionSentBytes=vismRudpSessionSentBytes, vismSessionGrpCurrSession=vismSessionGrpCurrSession, vismSessionGrpTable=vismSessionGrpTable, vismRudpSessionType=vismRudpSessionType, vismRudpSessionMaxOutOfSeq=vismRudpSessionMaxOutOfSeq, vismRudpSessionRmtGwIp=vismRudpSessionRmtGwIp, vismRudpSessionRcvdBytes=vismRudpSessionRcvdBytes, vismSessionGrpState=vismSessionGrpState, vismSessionSetTotalGrps=vismSessionSetTotalGrps, vismRudpSessionAutoResets=vismRudpSessionAutoResets, vismRudpSessionRmtIp=vismRudpSessionRmtIp, vismRudpSessionRetransPkts=vismRudpSessionRetransPkts, vismRudpSessionNullSegTmout=vismRudpSessionNullSegTmout, vismRudpSessionMaxCumAck=vismRudpSessionMaxCumAck, vismRudpSessionCumAckTmout=vismRudpSessionCumAckTmout, vismSessionGrpRowStatus=vismSessionGrpRowStatus, vismRudpSessionCurrSession=vismRudpSessionCurrSession, vismRudpSessionStatEntry=vismRudpSessionStatEntry, vismSessionSetTable=vismSessionSetTable, vismRudpSessionStatNum=vismRudpSessionStatNum, vismRudpSessionSentPackets=vismRudpSessionSentPackets, vismSessionSetState=vismSessionSetState, vismSessionGrpEntry=vismSessionGrpEntry, vismRudpSessionMaxSegSize=vismRudpSessionMaxSegSize, vismSessionSetSwitchSuccesses=vismSessionSetSwitchSuccesses, vismRudpSessionMaxWindow=vismRudpSessionMaxWindow, vismRudpSessionNum=vismRudpSessionNum, vismSessionSetActiveGrp=vismSessionSetActiveGrp, vismSessionSetFaultTolerant=vismSessionSetFaultTolerant, vismRudpSessionRetransTmout=vismRudpSessionRetransTmout, vismRudpSessionRcvdPackets=vismRudpSessionRcvdPackets, vismSessionGrpMgcName=vismSessionGrpMgcName, vismSessionSetRowStatus=vismSessionSetRowStatus, vismSessionGrpTotalSessions=vismSessionGrpTotalSessions, vismRudpSessionPriority=vismRudpSessionPriority, vismRudpSessionSyncAttempts=vismRudpSessionSyncAttempts, vismRudpSessionCnfRowStatus=vismRudpSessionCnfRowStatus, vismSessionGrpSwitchSuccesses=vismSessionGrpSwitchSuccesses, vismRudpSessionRmtPort=vismRudpSessionRmtPort, vismSessionGrp=vismSessionGrp)