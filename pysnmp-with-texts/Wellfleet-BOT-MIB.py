#
# PySNMP MIB module Wellfleet-BOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-BOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:39:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, ModuleIdentity, IpAddress, Unsigned32, Counter32, Bits, Counter64, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "ModuleIdentity", "IpAddress", "Unsigned32", "Counter32", "Bits", "Counter64", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfBotGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfBotGroup")
wfBot = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1))
wfBotDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotDelete.setDescription('Create/Delete parameter. Default is created. User perform an SNMP SET operation on this object in order to create/delete BOT')
wfBotDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotDisable.setDescription('Enable/Disable parameter. Default is enabled. User perform an SNMP SET operation on this object in order to enable/disable BOT')
wfBotState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotState.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotState.setDescription('The current state of BOT')
wfBotInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2), )
if mibBuilder.loadTexts: wfBotInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceTable.setDescription('Interface table which lists all BISYNC line entries and other line related information')
wfBotInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1), ).setIndexNames((0, "Wellfleet-BOT-MIB", "wfBotInterfaceSlotNumber"), (0, "Wellfleet-BOT-MIB", "wfBotInterfaceCctNumber"))
if mibBuilder.loadTexts: wfBotInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceEntry.setDescription('An entry in wfBotInterfaceTable')
wfBotInterfaceDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceDelete.setDescription('Create/Delete attribute. Default is Created Users perform SNMP SET operation on this object in order to create/delete a translation interface record')
wfBotInterfaceDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceDisable.setDescription('Enables/Disables this mapping entry Setting of this attribute to DISABLED will disconnect all active sessions pertaining to this interface entry')
wfBotInterfaceCctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfaceCctNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceCctNumber.setDescription('The circuit from which the connection attempt is received that initiates a translation session.')
wfBotInterfaceSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfaceSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceSlotNumber.setDescription('Slot number on which this interface is running')
wfBotInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfaceState.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceState.setDescription('The current state of the Interface')
wfBotInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("singledrop", 1), ("multidrop", 2))).clone('singledrop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceType.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceType.setDescription('If this interface is point-to-point, i.e. no splitting occours we can straight away deliver BSC frame to designated TCP circuit, without looking into the CU address')
wfBotInterfaceAttachedTo = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotInterfaceAttachedTo.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfaceAttachedTo.setDescription('Information that this interface is attached to the Primary or secondary BSC station')
wfBotInterfacePktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotInterfacePktCnt.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotInterfacePktCnt.setDescription('Interface packet count ...')
wfBotKeepaliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotKeepaliveInterval.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotKeepaliveInterval.setDescription('Idle session timeout period, in seconds. If an established TCP connection remains inactive for this interval, KEEPALIVE messages will be sent to the peer (if the Keepalive Timer is non-zero). Setting the Idle Timer to zero disables the keepalive feature.')
wfBotKeepaliveRto = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotKeepaliveRto.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotKeepaliveRto.setDescription('KEEPALIVE retransmit timeout period, in seconds. This is the interval at which unacknowledged KEEPALIVE messages will be retransmitted. If the Idle Timer is set to zero, this timer ignored. If the Idle Timer is non-zero and this timer IS zero, no KEEPALIVEs are sent and the session is terminated upon expiration of the Idle Timer.')
wfBotKeepaliveMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotKeepaliveMaxRetry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotKeepaliveMaxRetry.setDescription('Number of unacknowledged KEEPALIVE messages retransmitted before the TCP session is terminated. If this count is set to zero, only one KEEPALIVE message will be sent.')
wfBotPeerTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3), )
if mibBuilder.loadTexts: wfBotPeerTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerTable.setDescription('Peer table lists all TCP connections this router will have with its peers')
wfBotPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1), ).setIndexNames((0, "Wellfleet-BOT-MIB", "wfBotPeerSlotNumber"), (0, "Wellfleet-BOT-MIB", "wfBotPeerCctNumber"), (0, "Wellfleet-BOT-MIB", "wfBotPeerRemoteIpAddr"), (0, "Wellfleet-BOT-MIB", "wfBotPeerLocalTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotPeerRemoteTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotConnOriginator"))
if mibBuilder.loadTexts: wfBotPeerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerEntry.setDescription('An entry in wfBotPeerTable')
wfBotPeerEntryDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotPeerEntryDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerEntryDelete.setDescription('Create/Delete attribute. Default is Created Users perform SNMP SET operation on this object in order to create/delete a peer record')
wfBotPeerEntryDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotPeerEntryDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerEntryDisable.setDescription('Enables/Disables this mapping entry Setting of this attribute to DISABLED will disconnect all active sessions pertaining to this interface entry')
wfBotPeerSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerSlotNumber.setDescription('Slot number on which this peer entry is configured')
wfBotPeerCctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerCctNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerCctNumber.setDescription('The circuit from which the connection attempt is received that initiates a translation session.')
wfBotPeerRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerRemoteIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerRemoteIpAddr.setDescription('IP Address of the remote host with which this translation session is established.')
wfBotConnOriginator = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("self", 1), ("partner", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotConnOriginator.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotConnOriginator.setDescription('Upon start up, based on the configuration either partner is going to initiate TCP conn. or myself')
wfBotPeerLocalTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerLocalTcpListenPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerLocalTcpListenPort.setDescription('Based on the field wfBotConnOriginator, SiteManager will allow user to configure only one of following two fields: if Originator = SELF then through SiteManager ask user to enter PeerTcpListenPort# else through SiteManager ask user to enter LocalTcpListenPort# So, in any case one of the two fields will have NULL_VALUE.')
wfBotPeerRemoteTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerRemoteTcpListenPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerRemoteTcpListenPort.setDescription('Peer listen port for TCP connection')
wfBotPeerLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerLocalTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerLocalTcpPort.setDescription('When TCP connection is established, we will have other TCP port number available which is assigned by the system from the available pool. We will fill in this information here in this READ_ONLY variable. Again, based on Originator only one of the following two fields will have valid value. if Originator = SELF then fill in LocalTcpPort field inside the BOT module else fill in PeerTcpPort field inside the BOT module In short, ========= For Originator = SELF PeerTcpListenPort and LocalTcpPort entries are valid For Originator = PARTNER LocalTcpListenPort and PeerTcpPort entries are valid')
wfBotPeerRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotPeerRemoteTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotPeerRemoteTcpPort.setDescription('Peer TCP port of the connection')
wfBotCUTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4), )
if mibBuilder.loadTexts: wfBotCUTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCUTable.setDescription('CU table lists all CUs reachable from this router on all TCP connections listed in PEER_TABLE')
wfBotCUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1), ).setIndexNames((0, "Wellfleet-BOT-MIB", "wfBotCUSlotNumber"), (0, "Wellfleet-BOT-MIB", "wfBotCUCctNumber"), (0, "Wellfleet-BOT-MIB", "wfBotCURemoteIpAddr"), (0, "Wellfleet-BOT-MIB", "wfBotCULocalTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotCURemoteTcpListenPort"), (0, "Wellfleet-BOT-MIB", "wfBotCUAddrReachable"))
if mibBuilder.loadTexts: wfBotCUEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCUEntry.setDescription('An entry in wfBotCUTable')
wfBotCUEntryDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotCUEntryDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCUEntryDelete.setDescription('Create/Delete attribute. Default is Created Users perform SNMP SET operation on this object in order to create/delete a peer record')
wfBotCUEntryDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBotCUEntryDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCUEntryDisable.setDescription('Enables/Disables this cu entry Setting of this attribute to DISABLED will disconnect active TCP conn. pertaining to the peer entry')
wfBotCUSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCUSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCUSlotNumber.setDescription('slot number used as an index')
wfBotCUCctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCUCctNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCUCctNumber.setDescription('The circuit from which the connection attempt is CCT number for easy link between peer table and cu table')
wfBotCURemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCURemoteIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCURemoteIpAddr.setDescription('IP Address of the remote host with which this translation session is established.')
wfBotCULocalTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCULocalTcpListenPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCULocalTcpListenPort.setDescription('As mentioned earlier only one of following two field will have a valid value, while other will be NULL_VAL, based on who is the ConnOriginator')
wfBotCURemoteTcpListenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCURemoteTcpListenPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCURemoteTcpListenPort.setDescription('field from the peer table entry')
wfBotCUAddrReachable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(254))).clone(namedValues=NamedValues(("address", 254)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBotCUAddrReachable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBotCUAddrReachable.setDescription('In BISYNC controller addresses range from 0-31. In MDL currently there is no way to represent the integer range. As lower bound is zero, here we specify only max possible')
mibBuilder.exportSymbols("Wellfleet-BOT-MIB", wfBotPeerLocalTcpPort=wfBotPeerLocalTcpPort, wfBotInterfaceState=wfBotInterfaceState, wfBotInterfaceSlotNumber=wfBotInterfaceSlotNumber, wfBotPeerTable=wfBotPeerTable, wfBotPeerRemoteTcpPort=wfBotPeerRemoteTcpPort, wfBotInterfacePktCnt=wfBotInterfacePktCnt, wfBotPeerCctNumber=wfBotPeerCctNumber, wfBotConnOriginator=wfBotConnOriginator, wfBotPeerRemoteIpAddr=wfBotPeerRemoteIpAddr, wfBotDisable=wfBotDisable, wfBotCURemoteIpAddr=wfBotCURemoteIpAddr, wfBotInterfaceEntry=wfBotInterfaceEntry, wfBotInterfaceDisable=wfBotInterfaceDisable, wfBotCUSlotNumber=wfBotCUSlotNumber, wfBotInterfaceTable=wfBotInterfaceTable, wfBotPeerEntryDisable=wfBotPeerEntryDisable, wfBotCULocalTcpListenPort=wfBotCULocalTcpListenPort, wfBotCUEntry=wfBotCUEntry, wfBotState=wfBotState, wfBotPeerSlotNumber=wfBotPeerSlotNumber, wfBotInterfaceAttachedTo=wfBotInterfaceAttachedTo, wfBotDelete=wfBotDelete, wfBotInterfaceCctNumber=wfBotInterfaceCctNumber, wfBotKeepaliveMaxRetry=wfBotKeepaliveMaxRetry, wfBotInterfaceDelete=wfBotInterfaceDelete, wfBotPeerEntryDelete=wfBotPeerEntryDelete, wfBotInterfaceType=wfBotInterfaceType, wfBotCUTable=wfBotCUTable, wfBot=wfBot, wfBotCURemoteTcpListenPort=wfBotCURemoteTcpListenPort, wfBotCUAddrReachable=wfBotCUAddrReachable, wfBotPeerRemoteTcpListenPort=wfBotPeerRemoteTcpListenPort, wfBotPeerEntry=wfBotPeerEntry, wfBotKeepaliveRto=wfBotKeepaliveRto, wfBotCUEntryDisable=wfBotCUEntryDisable, wfBotKeepaliveInterval=wfBotKeepaliveInterval, wfBotCUEntryDelete=wfBotCUEntryDelete, wfBotPeerLocalTcpListenPort=wfBotPeerLocalTcpListenPort, wfBotCUCctNumber=wfBotCUCctNumber)
