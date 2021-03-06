#
# PySNMP MIB module TPLINK-PIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-PIM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, iso, Gauge32, Integer32, Bits, NotificationType, Counter64, Counter32, MibIdentifier, IpAddress, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "iso", "Gauge32", "Integer32", "Bits", "NotificationType", "Counter64", "Counter32", "MibIdentifier", "IpAddress", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkPimMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 77))
tplinkPimMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkPimMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkPimMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkPimMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkPimMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkPimMIB.setDescription('Private MIB for PIM configuration.')
tplinkPimMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1))
tplinkPimNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 77, 2))
tpPim = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1))
tpSGExpiryTimer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpSGExpiryTimer.setStatus('current')
if mibBuilder.loadTexts: tpSGExpiryTimer.setDescription('Specify the expiry timer for the entry.')
tpPimdataThresholdRate = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("zero", 0), ("infinity", 1)))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimdataThresholdRate.setStatus('current')
if mibBuilder.loadTexts: tpPimdataThresholdRate.setDescription('Select rate which the last-hop router will switch to a source-specific shortest path tree. Specify infinity if you want all sources for the specified group to use the shared tree, never switching to the source tree.The default is 0 kbps. ')
tpPimInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3), )
if mibBuilder.loadTexts: tpPimInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceTable.setDescription("The (conceptual) table listing the router's PIM interfaces. IGMP and PIM are enabled on all interfaces listed in this table.")
tpPimInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1), ).setIndexNames((0, "TPLINK-PIM-MIB", "tpPimInterfaceIndex"))
if mibBuilder.loadTexts: tpPimInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceEntry.setDescription('An entry (conceptual row) in the pimInterfaceTable.')
tpPimInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimInterface.setStatus('current')
if mibBuilder.loadTexts: tpPimInterface.setDescription(' Display the interface which you can configure.')
tpPimInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceIndex.setDescription('The Index value of this PIM interface.')
tpPimInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vlan", 0), ("loopback", 1), ("routeport", 2))).clone('vlan')).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimInterfaceType.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceType.setDescription('The configured type of this interface.')
tpPimInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimInterfaceAddress.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceAddress.setDescription('The IP address of the PIM interface.')
tpPimInterfaceNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimInterfaceNetMask.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceNetMask.setDescription('The network mask for the IP address of the PIM interface.')
tpPimInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("dense", 1), ("sparse", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimInterfaceMode.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceMode.setDescription('The configured mode of this PIM interface.')
tpPimInterfaceDRPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 7), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimInterfaceDRPriority.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceDRPriority.setDescription('The Designated Router Priority value inserted into the DR Priority option on this interface.Numerically higher values for this object indicate higher priorities.')
tpPimInterfaceDRAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimInterfaceDRAddress.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceDRAddress.setDescription('The Designated Router on this PIM interface. For point- to-point interfaces, this object has the value 0.0.0.0.')
tpPimInterfaceHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 18725)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimInterfaceHelloInterval.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceHelloInterval.setDescription('The frequency at which PIM Hello messages are transmitted on this interface.')
tpPimInterfaceBsrBorder = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimInterfaceBsrBorder.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceBsrBorder.setDescription('The frequency at which PIM Hello messages are transmitted on this interface.')
tpPimInterfaceJoinPruneInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 18724)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimInterfaceJoinPruneInterval.setStatus('current')
if mibBuilder.loadTexts: tpPimInterfaceJoinPruneInterval.setDescription("The frequency at which PIM Join/Prune messages are transmitted on this PIM interface. This object corresponds to the 't_periodic' timer value defined in the PIM-SM specification [I-D.ietf-pim-sm-v2-new]. A value of 0 represents an 'infinite' interval, and indicates that periodic PIM Join/Prune messages should not be sent on this interface.")
tpPimNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4), )
if mibBuilder.loadTexts: tpPimNeighborTable.setStatus('current')
if mibBuilder.loadTexts: tpPimNeighborTable.setDescription("The (conceptual) table listing the router's PIM neighbors.")
tpPimNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1), ).setIndexNames((0, "TPLINK-PIM-MIB", "tpPimNeighborAddress"))
if mibBuilder.loadTexts: tpPimNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: tpPimNeighborEntry.setDescription('An entry (conceptual row) in the pimNeighborTable.')
tpPimNeighborInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimNeighborInterface.setStatus('current')
if mibBuilder.loadTexts: tpPimNeighborInterface.setDescription('The interface used to reach this PIM neighbor.')
tpPimNeighborInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimNeighborInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: tpPimNeighborInterfaceIndex.setDescription('The value of ifIndex for the interface used to reach this PIM neighbor.')
tpPimNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimNeighborAddress.setStatus('current')
if mibBuilder.loadTexts: tpPimNeighborAddress.setDescription('The IP address of the PIM neighbor for which this entry contains information.')
tpPimNeighborUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimNeighborUpTime.setStatus('current')
if mibBuilder.loadTexts: tpPimNeighborUpTime.setDescription('The time since this PIM neighbor (last) became a neighbor of the local router.')
tpPimNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimNeighborExpiryTime.setStatus('current')
if mibBuilder.loadTexts: tpPimNeighborExpiryTime.setDescription('The minimum time remaining before this PIM neighbor will be aged out.')
tpPimNeighborMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dense", 1), ("sparse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimNeighborMode.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimNeighborMode.setDescription('The active PIM mode of this neighbor. This object is deprecated for PIMv2 routers since all neighbors on the interface must be either dense or sparse as determined by the protocol running on the interface.')
tpPimCandidateBSRSet = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5))
tpPimCBSRInterface = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimCBSRInterface.setStatus('current')
if mibBuilder.loadTexts: tpPimCBSRInterface.setDescription('Specify the interface of the BSR. ')
tpPimCBSRInterfaceIndex = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimCBSRInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: tpPimCBSRInterfaceIndex.setDescription('Specify the interface index of the BSR. ')
tpPimCBSRHashMaskLength = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimCBSRHashMaskLength.setStatus('current')
if mibBuilder.loadTexts: tpPimCBSRHashMaskLength.setDescription('Specify the hash mask length of the BSR. The default value is 30. ')
tpPimCBSRPriority = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimCBSRPriority.setStatus('current')
if mibBuilder.loadTexts: tpPimCBSRPriority.setDescription('Specify the priority of the BSR. The default value is 64. ')
tpPimStaticRpSet = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 6))
tpPimStaticRpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimStaticRpAddress.setStatus('current')
if mibBuilder.loadTexts: tpPimStaticRpAddress.setDescription('Specify the static RP address. ')
tpPimStaticRpOverride = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimStaticRpOverride.setStatus('current')
if mibBuilder.loadTexts: tpPimStaticRpOverride.setDescription(' Select to enable or disable override mode. If the override mode is enabled, the static RP will take effect no matter the candidate RP is configured or not. Otherwise the static RP will be invalid when the candidate RP is configured. ')
tpPimCandidateRPSetTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7), )
if mibBuilder.loadTexts: tpPimCandidateRPSetTable.setStatus('current')
if mibBuilder.loadTexts: tpPimCandidateRPSetTable.setDescription('The (conceptual) table listing PIM information for candidate Rendezvous Points (RPs) for IP multicast groups. When the local router is the BSR, this information is obtained from received Candidate-RP-Advertisements. When the local router is not the BSR, this information is obtained from received RP-Set messages.')
tpPimCandidateRPSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1), ).setIndexNames((0, "TPLINK-PIM-MIB", "tpPimCRPSetInterfaceIndex"))
if mibBuilder.loadTexts: tpPimCandidateRPSetEntry.setStatus('current')
if mibBuilder.loadTexts: tpPimCandidateRPSetEntry.setDescription('An entry (conceptual row) in the pimRPSetTable.')
tpPimCRPSetInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimCRPSetInterface.setStatus('current')
if mibBuilder.loadTexts: tpPimCRPSetInterface.setDescription(' The c rp interface.')
tpPimCRPSetInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimCRPSetInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: tpPimCRPSetInterfaceIndex.setDescription('The ifIndex value of this c rp interface.')
tpPimCRPSetInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vlan", 0), ("loopback", 1), ("routeport", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimCRPSetInterfaceType.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimCRPSetInterfaceType.setDescription('The interface type.')
tpPimCRPSetPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(192)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimCRPSetPriority.setStatus('current')
if mibBuilder.loadTexts: tpPimCRPSetPriority.setDescription('Specify the priority of the candidate RP. The default value is 192. ')
tpPimCRPSetInterVal = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimCRPSetInterVal.setStatus('current')
if mibBuilder.loadTexts: tpPimCRPSetInterVal.setDescription('Specify the interval of advertisement message of the candidate RP in seconds. The default value is 60. ')
tpPimCRPSetNextAdvertisementTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimCRPSetNextAdvertisementTime.setStatus('current')
if mibBuilder.loadTexts: tpPimCRPSetNextAdvertisementTime.setDescription('Show the remain time of next RP advertisement packet send. ')
tpPimCRPSetInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpPimCRPSetInterfaceStatus.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimCRPSetInterfaceStatus.setDescription('The interface type.')
tpPimRPMappingTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8), )
if mibBuilder.loadTexts: tpPimRPMappingTable.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPMappingTable.setDescription('Show the RP mapping information. ')
tpPimRPMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1), ).setIndexNames((0, "TPLINK-PIM-MIB", "tpPimRPGroupAddress"), (0, "TPLINK-PIM-MIB", "tpPimRPAddress"))
if mibBuilder.loadTexts: tpPimRPMappingEntry.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPMappingEntry.setDescription('An entry (conceptual row) in the tpPimRPMappingTable. There is one entry per RP address for each IP multicast group.')
tpPimRPGroupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimRPGroupAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPGroupAddress.setDescription('The IP multicast group address for which this entry contains information about an RP.')
tpPimRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimRPAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPAddress.setDescription('The IP multicast group address for which this entry contains PIM version 1 information about an RP.')
tpPimRPInfoSource = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimRPInfoSource.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPInfoSource.setDescription('The state of the RP.')
tpPimRPPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimRPPriority.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPPriority.setDescription('Show the priority of the RP. ')
tpPimRPHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimRPHoldTime.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPHoldTime.setDescription('Show the holdtime of the RP.')
tpPimRPExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPimRPExpire.setStatus('deprecated')
if mibBuilder.loadTexts: tpPimRPExpire.setDescription('Show the expiry time of the RP. If RP is static, the expiry time will be Never.')
mibBuilder.exportSymbols("TPLINK-PIM-MIB", tpPimNeighborUpTime=tpPimNeighborUpTime, tpPimInterfaceTable=tpPimInterfaceTable, tpPimCRPSetInterfaceStatus=tpPimCRPSetInterfaceStatus, tpPimRPGroupAddress=tpPimRPGroupAddress, tpPimCBSRInterfaceIndex=tpPimCBSRInterfaceIndex, tpPimStaticRpAddress=tpPimStaticRpAddress, tpPimRPPriority=tpPimRPPriority, tpPimNeighborTable=tpPimNeighborTable, tpPimNeighborExpiryTime=tpPimNeighborExpiryTime, tpPimCRPSetPriority=tpPimCRPSetPriority, tpPimInterfaceType=tpPimInterfaceType, tpPimCBSRInterface=tpPimCBSRInterface, tpPimCBSRPriority=tpPimCBSRPriority, tplinkPimMIB=tplinkPimMIB, tpPimCRPSetInterfaceIndex=tpPimCRPSetInterfaceIndex, tpPimNeighborMode=tpPimNeighborMode, tpPimRPMappingTable=tpPimRPMappingTable, tpPimInterfaceMode=tpPimInterfaceMode, tpPimCRPSetInterVal=tpPimCRPSetInterVal, tplinkPimNotifications=tplinkPimNotifications, PYSNMP_MODULE_ID=tplinkPimMIB, tpPimRPExpire=tpPimRPExpire, tpPimInterfaceBsrBorder=tpPimInterfaceBsrBorder, tpPimInterfaceNetMask=tpPimInterfaceNetMask, tpPimInterfaceJoinPruneInterval=tpPimInterfaceJoinPruneInterval, tpPimNeighborAddress=tpPimNeighborAddress, tpPimCandidateBSRSet=tpPimCandidateBSRSet, tpPimCandidateRPSetTable=tpPimCandidateRPSetTable, tpPimInterfaceHelloInterval=tpPimInterfaceHelloInterval, tpPimRPInfoSource=tpPimRPInfoSource, tpPimInterfaceAddress=tpPimInterfaceAddress, tpPimInterfaceIndex=tpPimInterfaceIndex, tplinkPimMIBObjects=tplinkPimMIBObjects, tpPimInterfaceDRPriority=tpPimInterfaceDRPriority, tpPimNeighborInterface=tpPimNeighborInterface, tpPimStaticRpOverride=tpPimStaticRpOverride, tpPimInterface=tpPimInterface, tpPimdataThresholdRate=tpPimdataThresholdRate, tpPimInterfaceEntry=tpPimInterfaceEntry, tpPimCandidateRPSetEntry=tpPimCandidateRPSetEntry, tpPimInterfaceDRAddress=tpPimInterfaceDRAddress, tpPimRPHoldTime=tpPimRPHoldTime, tpPimStaticRpSet=tpPimStaticRpSet, tpPimCRPSetNextAdvertisementTime=tpPimCRPSetNextAdvertisementTime, tpPimCRPSetInterface=tpPimCRPSetInterface, tpPim=tpPim, tpPimNeighborEntry=tpPimNeighborEntry, tpPimRPMappingEntry=tpPimRPMappingEntry, tpPimRPAddress=tpPimRPAddress, tpPimCRPSetInterfaceType=tpPimCRPSetInterfaceType, tpPimNeighborInterfaceIndex=tpPimNeighborInterfaceIndex, tpSGExpiryTimer=tpSGExpiryTimer, tpPimCBSRHashMaskLength=tpPimCBSRHashMaskLength)
