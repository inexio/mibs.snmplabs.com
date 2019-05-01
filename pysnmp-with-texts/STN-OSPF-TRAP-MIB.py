#
# PySNMP MIB module STN-OSPF-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-OSPF-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ospfIfState, ospfNbrRtrId, ospfNbrState, ospf, ospfVirtNbrRtrId, ospfVirtNbrState, ospfLsdbType, ospfVirtNbrArea, ospfIfIpAddress, ospfVirtIfState, ospfVirtIfAreaId, ospfRouterId, ospfVirtIfNeighbor, ospfAddressLessIf, ospfExtLsdbLimit, ospfLsdbLsid, ospfNbrAddressLessIndex, ospfLsdbRouterId, ospfLsdbAreaId, ospfNbrIpAddr = mibBuilder.importSymbols("OSPF-MIB", "ospfIfState", "ospfNbrRtrId", "ospfNbrState", "ospf", "ospfVirtNbrRtrId", "ospfVirtNbrState", "ospfLsdbType", "ospfVirtNbrArea", "ospfIfIpAddress", "ospfVirtIfState", "ospfVirtIfAreaId", "ospfRouterId", "ospfVirtIfNeighbor", "ospfAddressLessIf", "ospfExtLsdbLimit", "ospfLsdbLsid", "ospfNbrAddressLessIndex", "ospfLsdbRouterId", "ospfLsdbAreaId", "ospfNbrIpAddr")
ospfPacketSrc, ospfPacketType, ospfConfigErrorType = mibBuilder.importSymbols("OSPF-TRAP-MIB", "ospfPacketSrc", "ospfPacketType", "ospfConfigErrorType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, NotificationType, Counter64, MibIdentifier, Unsigned32, Integer32, ModuleIdentity, ObjectIdentity, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "NotificationType", "Counter64", "MibIdentifier", "Unsigned32", "Integer32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnNotification, = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification")
stnOspfTraps, = mibBuilder.importSymbols("STN-IPROUTING-MIB", "stnOspfTraps")
stnRouterIndex, = mibBuilder.importSymbols("STN-ROUTER-MIB", "stnRouterIndex")
stnOspfTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1))
if mibBuilder.loadTexts: stnOspfTrap.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnOspfTrap.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: stnOspfTrap.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: stnOspfTrap.setDescription('This MIB module describes traps for the OSPF Version 2 Protocol.')
stnOspfTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 1))
stnOspfNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2))
stnOspfNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0))
stnOspfVirtIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 1)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-MIB", "ospfVirtIfState"))
if mibBuilder.loadTexts: stnOspfVirtIfStateChange.setStatus('current')
if mibBuilder.loadTexts: stnOspfVirtIfStateChange.setDescription('A stnOspfVirtIfStateChange trap signifies that there has been a change in the state of an OSPF virtual interface. This trap should be generated when the interface state regresses (e.g., goes from Point-to-Point to Down) or progresses to a terminal state (i.e., Point-to-Point). The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 2)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfNbrIpAddr"), ("OSPF-MIB", "ospfNbrAddressLessIndex"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-MIB", "ospfNbrState"))
if mibBuilder.loadTexts: stnOspfNbrStateChange.setStatus('current')
if mibBuilder.loadTexts: stnOspfNbrStateChange.setDescription('A stnOspfNbrStateChange trap signifies that there has been a change in the state of a non-virtual OSPF neighbor. This trap should be generated when the neighbor state regresses (e.g., goes from Attempt or Full to 1-Way or Down) or progresses to a terminal state (e.g., 2-Way or Full). When an neighbor transitions from or to Full on non-broadcast multi-access and broadcast networks, the trap should be generated by the designated router. A designated router transitioning to Down will be noted by ospfIfStateChange. The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfVirtNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 3)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtNbrArea"), ("OSPF-MIB", "ospfVirtNbrRtrId"), ("OSPF-MIB", "ospfVirtNbrState"))
if mibBuilder.loadTexts: stnOspfVirtNbrStateChange.setStatus('current')
if mibBuilder.loadTexts: stnOspfVirtNbrStateChange.setDescription('A stnOspfVirtNbrStateChange trap signifies that there has been a change in the state of an OSPF virtual neighbor. This trap should be generated when the neighbor state regresses (e.g., goes from Attempt or Full to 1-Way or Down) or progresses to a terminal state (e.g., Full). The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 4)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfIfConfigError.setStatus('current')
if mibBuilder.loadTexts: stnOspfIfConfigError.setDescription("An stnOspfIfConfigError trap signifies that a packet has been received on a non-virtual interface from a router whose configuration parameters conflict with this router's configuration parameters. Note that the event optionMismatch should cause a trap only if it prevents an adjacency from forming. The generation of this trap can be controlled by the OSPFTraps configuration object.")
stnOspfVirtIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 5)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfVirtIfConfigError.setStatus('current')
if mibBuilder.loadTexts: stnOspfVirtIfConfigError.setDescription("A stnOspfVirtIfConfigError trap signifies that a packet has been received on a virtual interface from a router whose configuration parameters conflict with this router's configuration parameters. Note that the event optionMismatch should cause a trap only if it prevents an adjacency from forming. The generation of this trap can be controlled by the OSPFTraps configuration object.")
stnOspfIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 6)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfIfAuthFailure.setStatus('current')
if mibBuilder.loadTexts: stnOspfIfAuthFailure.setDescription("A stnOspfIfAuthFailure trap signifies that a packet has been received on a non-virtual interface from a router whose authentication key or authentication type conflicts with this router's authentication key or authentication type. The generation of this trap can be controlled by the OSPFTraps configuration object.")
stnOspfVirtIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 7)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfConfigErrorType"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfVirtIfAuthFailure.setStatus('current')
if mibBuilder.loadTexts: stnOspfVirtIfAuthFailure.setDescription("A stnOspfVirtIfAuthFailure trap signifies that a packet has been received on a virtual interface from a router whose authentication key or authentication type conflicts with this router's authentication key or authentication type. The generation of this trap can be controlled by the OSPFTraps configuration object.")
stnOspfIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 8)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-TRAP-MIB", "ospfPacketSrc"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfIfRxBadPacket.setStatus('current')
if mibBuilder.loadTexts: stnOspfIfRxBadPacket.setDescription('A stnOspfIfRxBadPacket trap signifies that an OSPF packet has been received on a non-virtual interface that cannot be parsed. The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfVirtIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 9)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"))
if mibBuilder.loadTexts: stnOspfVirtIfRxBadPacket.setStatus('current')
if mibBuilder.loadTexts: stnOspfVirtIfRxBadPacket.setDescription('An stnOspfVirtIfRxBadPacket trap signifies that an OSPF packet has been received on a virtual interface that cannot be parsed. The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 10)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfNbrRtrId"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfTxRetransmit.setStatus('current')
if mibBuilder.loadTexts: stnOspfTxRetransmit.setDescription('A stnOspfTxRetransmit trap signifies than an OSPF packet has been retransmitted on a non-virtual interface. All packets that may be retransmitted are associated with an LSDB entry. The LS type, LS ID, and Router ID are used to identify the LSDB entry. The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 11)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfVirtIfAreaId"), ("OSPF-MIB", "ospfVirtIfNeighbor"), ("OSPF-TRAP-MIB", "ospfPacketType"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfVirtIfTxRetransmit.setStatus('current')
if mibBuilder.loadTexts: stnOspfVirtIfTxRetransmit.setDescription('A stnOspfVirtIfTxRetransmit trap signifies than an OSPF packet has been retransmitted on a virtual interface. All packets that may be retransmitted are associated with an LSDB entry. The LS type, LS ID, and Router ID are used to identify the LSDB entry. The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfOriginateLsa = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 12)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfOriginateLsa.setStatus('current')
if mibBuilder.loadTexts: stnOspfOriginateLsa.setDescription('A stnOspfOriginateLsa trap signifies that a new LSA has been originated by this router. This trap should not be invoked for simple refreshes of LSAs (which happens every 30 minutes), but instead will only be invoked when an LSA is (re)originated due to a topology change. Additionally, this trap does not include LSAs that are being flushed because they have reached MaxAge. The generation of this trap can be controlled by the OSPFTraps configuration object.')
stnOspfMaxAgeLsa = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 13)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfLsdbAreaId"), ("OSPF-MIB", "ospfLsdbType"), ("OSPF-MIB", "ospfLsdbLsid"), ("OSPF-MIB", "ospfLsdbRouterId"))
if mibBuilder.loadTexts: stnOspfMaxAgeLsa.setStatus('current')
if mibBuilder.loadTexts: stnOspfMaxAgeLsa.setDescription("A stnOspfMaxAgeLsa trap signifies that one of the LSA in the router's link-state database has aged to MaxAge. The generation of this trap can be controlled by the OSPFTraps configuration object.")
stnOspfLsdbOverflow = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 14)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: stnOspfLsdbOverflow.setStatus('current')
if mibBuilder.loadTexts: stnOspfLsdbOverflow.setDescription("A stnOspfLsdbOverflow trap signifies that the number of LSAs in the router's link-state database has exceeded ospfExtLsdbLimit. The generation of this trap can be controlled by the OSPFTraps configuration object.")
stnOspfLsdbApproachingOverflow = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 15)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfExtLsdbLimit"))
if mibBuilder.loadTexts: stnOspfLsdbApproachingOverflow.setStatus('current')
if mibBuilder.loadTexts: stnOspfLsdbApproachingOverflow.setDescription("A stnOspfLsdbApproachingOverflow trap signifies that the number of LSAs in the router's link state database has exceeded ninety percent of ospfExtLsdbLimit. The generation of this trap can be controlled by the OSPFTraps configuration object.")
stnOspfIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8, 1, 2, 0, 16)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("OSPF-MIB", "ospfRouterId"), ("OSPF-MIB", "ospfIfIpAddress"), ("OSPF-MIB", "ospfAddressLessIf"), ("OSPF-MIB", "ospfIfState"))
if mibBuilder.loadTexts: stnOspfIfStateChange.setStatus('current')
if mibBuilder.loadTexts: stnOspfIfStateChange.setDescription('A stnOspfIfStateChange trap signifies that there has been a change in the state of a non-virtual OSPF interface. This trap should be generated when the interface state regresses (e.g., goes from Dr to Down) or progresses to a terminal state (i.e., Point-to-Point, DR Other, Dr, or Backup). The generation of this trap can be controlled by the OSPFTraps configuration object.')
mibBuilder.exportSymbols("STN-OSPF-TRAP-MIB", stnOspfVirtIfConfigError=stnOspfVirtIfConfigError, stnOspfTrapVars=stnOspfTrapVars, stnOspfNotification=stnOspfNotification, stnOspfNotificationPrefix=stnOspfNotificationPrefix, stnOspfOriginateLsa=stnOspfOriginateLsa, stnOspfVirtIfTxRetransmit=stnOspfVirtIfTxRetransmit, stnOspfTxRetransmit=stnOspfTxRetransmit, stnOspfLsdbApproachingOverflow=stnOspfLsdbApproachingOverflow, stnOspfTrap=stnOspfTrap, stnOspfVirtIfRxBadPacket=stnOspfVirtIfRxBadPacket, stnOspfVirtNbrStateChange=stnOspfVirtNbrStateChange, stnOspfMaxAgeLsa=stnOspfMaxAgeLsa, stnOspfLsdbOverflow=stnOspfLsdbOverflow, stnOspfIfStateChange=stnOspfIfStateChange, stnOspfIfConfigError=stnOspfIfConfigError, stnOspfVirtIfStateChange=stnOspfVirtIfStateChange, stnOspfIfAuthFailure=stnOspfIfAuthFailure, stnOspfNbrStateChange=stnOspfNbrStateChange, stnOspfIfRxBadPacket=stnOspfIfRxBadPacket, PYSNMP_MODULE_ID=stnOspfTrap, stnOspfVirtIfAuthFailure=stnOspfVirtIfAuthFailure)
