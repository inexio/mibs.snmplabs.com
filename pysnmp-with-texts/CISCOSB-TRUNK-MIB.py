#
# PySNMP MIB module CISCOSB-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-TRUNK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:23:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
dot3adAggIndex, dot3adAggPortIndex = mibBuilder.importSymbols("IEEE8023-LAG-MIB", "dot3adAggIndex", "dot3adAggPortIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, IpAddress, iso, ObjectIdentity, MibIdentifier, Integer32, NotificationType, Counter64, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "IpAddress", "iso", "ObjectIdentity", "MibIdentifier", "Integer32", "NotificationType", "Counter64", "ModuleIdentity", "Counter32")
PhysAddress, RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
rlDot3adAgg = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65))
rlDot3adAgg.setRevisions(('2006-12-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDot3adAgg.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlDot3adAgg.setLastUpdated('200612020000Z')
if mibBuilder.loadTexts: rlDot3adAgg.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlDot3adAgg.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlDot3adAgg.setDescription('The private MIB module definition for trunk support in CISCOSB devices.')
rlDot3adAggMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggMibVersion.setDescription("MIB's version, the current version is 1.")
rlDot3adAggBalanceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2), )
if mibBuilder.loadTexts: rlDot3adAggBalanceTable.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggBalanceTable.setDescription('An entry of this table specifies a balancing criterion used for the corresponding dot3adAggIndex.')
rlDot3adAggBalanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"), (0, "CISCOSB-TRUNK-MIB", "rlDot3adAggBalanceForwardType"))
if mibBuilder.loadTexts: rlDot3adAggBalanceEntry.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggBalanceEntry.setDescription('A list of information for each dot3adAggIndex.')
rlDot3adAggBalanceForwardType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bridging", 1), ("routing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggBalanceForwardType.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggBalanceForwardType.setDescription('A Forwarding type: Bridging or Routing.')
rlDot3adAggBalanceLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggBalanceLayer.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggBalanceLayer.setDescription('A Network Layer Number, may have the following values: 2, 3 or 4. The default value is: Bridging: 2 Routing: 3.')
rlDot3adAggBalanceUsedAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplied", 0), ("dstAddr", 1), ("srcAddr", 2), ("dstAndSrcAddr", 3), ("vlanId", 4), ("ethType", 5))).clone('dstAddr')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggBalanceUsedAddresses.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggBalanceUsedAddresses.setDescription('Specifies the Network Layer addresses used for Balancing of unicast frames. The function sets the criterion (by layer and used address in it).')
rlDot3adAggBalanceBroadcastType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("common", 0), ("dedicated", 1))).clone('common')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggBalanceBroadcastType.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggBalanceBroadcastType.setDescription('Specifies a balancing criterion used for L2 broadcast and unknown frames: common: a link allocated for broadcast and unknown frames is used for unicast frames too dedicated: a link allocated for broadcast and unknown frames is not used for unicast frames')
rlDot3adAggNumOfTrunks = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggNumOfTrunks.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggNumOfTrunks.setDescription('The number of trunks supported by the device.')
rlDot3adAggMaxPortsInTrunks = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggMaxPortsInTrunks.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggMaxPortsInTrunks.setDescription('The maximun number of ports in a trunk.')
rlDot3adAggTrunkCreationSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notSupported", 0), ("supportsTrunkOrLacp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggTrunkCreationSupport.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggTrunkCreationSupport.setDescription('Specifies if there is support to rldot3adAggCreationTable, and the type of the support: supportedTrunkOrLacp - ports that are members in some trunk are belongs to it by manual configuration or by lacp, but not togther. notSupported - there is not support to rldot3adAggCreationTable.')
rlDot3adAggCreationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6), )
if mibBuilder.loadTexts: rlDot3adAggCreationTable.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggCreationTable.setDescription('An entry of this table is for creation of an aggregator for the corresponding dot3adAggIndex, when the value of the rlDot3adAggCreationSupport is diffrent from notSupported.')
rlDot3adAggCreationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: rlDot3adAggCreationEntry.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggCreationEntry.setDescription('An information for each dot3adAggIndex.')
rlDot3adAggCreationTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggCreationTrunk.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggCreationTrunk.setDescription('The aggregator can aggregate ports in manual configuration.')
rlDot3adAggCreationLacp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 6, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggCreationLacp.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggCreationLacp.setDescription('The aggregator can aggregate ports by lacp.')
rlDot3adAggLoadBalancingPerTrunk = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggLoadBalancingPerTrunk.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLoadBalancingPerTrunk.setDescription('Specifies if load balancing is defined per trunk or per device.')
rlDot3adAggPortLacpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8), )
if mibBuilder.loadTexts: rlDot3adAggPortLacpTable.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpTable.setDescription('An entry of this table specifies lacp protocol state and statistics for the corresponding dot3adAggPortIndex.')
rlDot3adAggPortLacpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: rlDot3adAggPortLacpEntry.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpEntry.setDescription('A list of information for each dot3adAggPortIndex.')
rlDot3adAggPortLacpPdusRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPdusRx.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpPdusRx.setDescription('The number of valid LACPDUs received on this Aggregation Port. This value is read-only.')
rlDot3adAggPortLacpPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPDUsTx.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpPDUsTx.setDescription('The number of LACPDUs transmitted on this Aggregation Port. This value is read-only.')
rlDot3adAggPortLacpRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("current", 1), ("expired", 2), ("defaulted", 3), ("initialize", 4), ("portDisabled", 5), ("lacpDisabled", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpRxState.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpRxState.setDescription("This attribute holds the value 'current' if the Receive state machine for the Aggregation Port is in the CURRENT state, 'expired' if the Receive state machine is in the EXPIRED state, 'defaulted' if the Receive state machine is in the DEFAULTED state, 'initialize' if the Receive state machine is in the INITIALIZE state, 'portDisabled' if the Receive state machine is in the PORT_DISABLED state, or 'lacpDisabled' if the Receive state machine is in the LACP_DISABLED state. This value is read-only.")
rlDot3adAggPortLacpMuxState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("detached", 1), ("waiting", 2), ("attached", 3), ("collecting", 4), ("distributing", 5), ("collectingDistributing", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpMuxState.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpMuxState.setDescription("This attribute holds the value 'detached' if the Mux state machine for the Aggregation Port is in the DETACHED state, 'waiting' if the Mux state machine is in the WAITING state, 'attached' if the Mux state machine for the Aggregation Port is in the ATTACHED state, 'collecting' if the Mux state machine for the Aggregation Port is in the COLLECTING state, 'distributing' if the Mux state machine for the Aggregation Port is in the DISTRIBUTING state, and 'collecting_ distributing' if the Mux state machine for the Aggregation Port is in the COLLECTING_DISTRIBUTING state. This value is read-only.")
rlDot3adAggPortLacpPeriodicState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noPeriodic", 1), ("fastPeriodic", 2), ("slowPeriodic", 3), ("periodicTx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPeriodicState.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpPeriodicState.setDescription("This attribute holds the value 'noPeriodic' if the Periodic state machine for the Aggregation Port is in the NO_PERIODIC state, 'fastPeriodic' if the Mux state machine is in the FAST_PERIODIC state, 'slowPeriodic' if the Mux state machine for the Aggregation Port is in the SLOW_PERIODIC state, or 'periodicTx' if the Periodic state machine for the Aggregation Port is in the PERIODIC_TX state. This value is read-only.")
rlDot3adAggPortLacpSelected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unselected", 1), ("selected", 2), ("waiting", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpSelected.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpSelected.setDescription("This attribute holds the value 'unselected' if the Selected variable for the Aggregation Port is set to UNSELECTED, 'selected' if the Selected variable for the Aggregation Port is set to SELECTED, or 'waiting' if the Selected variable for the Aggregation Port is set to WAITING. This value is read-only.")
rlDot3adAggPortLacpReady = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpReady.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpReady.setDescription("A read-only Boolean value indicating whether the Aggregation Port is in the WAITING state in the Mux state machine and its wait_while_timer has expired ('TRUE'). otherwise, its valus is 'FALSE'.")
rlDot3adAggPortLacpPortMoved = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPortMoved.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpPortMoved.setDescription("A read-only Boolean value indicating whether the Partner_Oper_System or Partner_Oper_Port_Number in use by the Aggregation Port has been changed in an incoming LACPDU ('TRUE'). otherwise, its valus is 'FALSE'.")
rlDot3adAggPortLacpNNT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpNNT.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpNNT.setDescription("A read-only Boolean value indicating whether there is a new protocol information that should be transmitted on the link, or that the Partner needs to be reminded of the old information. otherwise, its valus is 'FALSE'.")
rlDot3adAggPortLacpPeriodicTxTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpPeriodicTxTimer.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpPeriodicTxTimer.setDescription('The amount of time in seconds remaining before the Periodeic Tx timer will expire. This value is read-only.')
rlDot3adAggPortLacpCurrentWhileTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpCurrentWhileTimer.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpCurrentWhileTimer.setDescription('The amount of time in seconds remaining before the Current While timer will expire. This value is read-only.')
rlDot3adAggPortLacpWaitWhileTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 8, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDot3adAggPortLacpWaitWhileTimer.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggPortLacpWaitWhileTimer.setDescription('The amount of time in seconds remaining before the Wait While timer will expire. This value is read-only.')
rlDot3adAggLacpMembershipRestrictionsSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsSupport.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsSupport.setDescription('Specifies if there is support to rlDot3adAggLacpMembershipRestrictionsTable.')
rlDot3adAggLacpMembershipRestrictionsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10), )
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsTable.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsTable.setDescription('An entry of this table specifies membership restrictions for ports that lacp is enbaled on them, and try to attach to the corresponding dot3adAggIndex.')
rlDot3adAggLacpMembershipRestrictionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsEntry.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsEntry.setDescription('A list of information for each dot3adAggIndex.')
rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey.setDescription("This variable specifies the administrative key of the remote LACP aggregator. A value of 0 is returned if the value of the variable hasn't been set.")
rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode.setDescription("This variable specifies the required speed of the LACP aggregator in bits per second. A value of 10 is returned for 10G. A value of 0 is returned if the value of the variable hasn't been set.")
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 3), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId.setDescription("This variable specifies the administrative MAC Address of the remote LACP aggregator. A null mac address is returned if the value of the variable hasn't been set.")
rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority.setDescription("This variable specifies the administrative System Priority of the remote LACP aggregator. A value of 0 is returned if the value of the variable hasn't been set.")
rlDot3adAggLacpMembershipRestrictionsIndividualAggregator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65, 10, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsIndividualAggregator.setStatus('current')
if mibBuilder.loadTexts: rlDot3adAggLacpMembershipRestrictionsIndividualAggregator.setDescription("This variable specifies if the lacp aggregator represents an Aggregate ('FALSE') or an Individual link ('TRUE').")
mibBuilder.exportSymbols("CISCOSB-TRUNK-MIB", rlDot3adAggCreationLacp=rlDot3adAggCreationLacp, rlDot3adAggPortLacpEntry=rlDot3adAggPortLacpEntry, rlDot3adAggPortLacpCurrentWhileTimer=rlDot3adAggPortLacpCurrentWhileTimer, rlDot3adAggBalanceForwardType=rlDot3adAggBalanceForwardType, rlDot3adAggPortLacpTable=rlDot3adAggPortLacpTable, rlDot3adAggPortLacpPdusRx=rlDot3adAggPortLacpPdusRx, rlDot3adAggPortLacpWaitWhileTimer=rlDot3adAggPortLacpWaitWhileTimer, rlDot3adAggPortLacpPDUsTx=rlDot3adAggPortLacpPDUsTx, rlDot3adAggLacpMembershipRestrictionsIndividualAggregator=rlDot3adAggLacpMembershipRestrictionsIndividualAggregator, rlDot3adAggLacpMembershipRestrictionsSupport=rlDot3adAggLacpMembershipRestrictionsSupport, rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode=rlDot3adAggLacpMembershipRestrictionsSpeedAdminMode, rlDot3adAggPortLacpPeriodicTxTimer=rlDot3adAggPortLacpPeriodicTxTimer, rlDot3adAggBalanceLayer=rlDot3adAggBalanceLayer, rlDot3adAggMaxPortsInTrunks=rlDot3adAggMaxPortsInTrunks, rlDot3adAggPortLacpMuxState=rlDot3adAggPortLacpMuxState, rlDot3adAggCreationEntry=rlDot3adAggCreationEntry, rlDot3adAggPortLacpRxState=rlDot3adAggPortLacpRxState, rlDot3adAggNumOfTrunks=rlDot3adAggNumOfTrunks, rlDot3adAggLacpMembershipRestrictionsEntry=rlDot3adAggLacpMembershipRestrictionsEntry, rlDot3adAggLoadBalancingPerTrunk=rlDot3adAggLoadBalancingPerTrunk, PYSNMP_MODULE_ID=rlDot3adAgg, rlDot3adAggMibVersion=rlDot3adAggMibVersion, rlDot3adAggBalanceUsedAddresses=rlDot3adAggBalanceUsedAddresses, rlDot3adAggPortLacpReady=rlDot3adAggPortLacpReady, rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority=rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemPriority, rlDot3adAggPortLacpSelected=rlDot3adAggPortLacpSelected, rlDot3adAggBalanceEntry=rlDot3adAggBalanceEntry, rlDot3adAggLacpMembershipRestrictionsTable=rlDot3adAggLacpMembershipRestrictionsTable, rlDot3adAggTrunkCreationSupport=rlDot3adAggTrunkCreationSupport, rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId=rlDot3adAggLacpMembershipRestrictionsPartnerAdminSystemId, rlDot3adAggPortLacpNNT=rlDot3adAggPortLacpNNT, rlDot3adAggCreationTable=rlDot3adAggCreationTable, rlDot3adAggPortLacpPeriodicState=rlDot3adAggPortLacpPeriodicState, rlDot3adAggCreationTrunk=rlDot3adAggCreationTrunk, rlDot3adAggPortLacpPortMoved=rlDot3adAggPortLacpPortMoved, rlDot3adAgg=rlDot3adAgg, rlDot3adAggBalanceBroadcastType=rlDot3adAggBalanceBroadcastType, rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey=rlDot3adAggLacpMembershipRestrictionsPartnerAdminKey, rlDot3adAggBalanceTable=rlDot3adAggBalanceTable)
