#
# PySNMP MIB module STN-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-ROUTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, TimeTicks, iso, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter64, ObjectIdentity, MibIdentifier, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "TimeTicks", "iso", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter64", "ObjectIdentity", "MibIdentifier", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnNotification, stnSystems = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnNotification", "stnSystems")
stnEngineIndex, stnEngineSlot, stnEngineCpu = mibBuilder.importSymbols("STN-CHASSIS-MIB", "stnEngineIndex", "stnEngineSlot", "stnEngineCpu")
stnRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 2, 7))
if mibBuilder.loadTexts: stnRouter.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnRouter.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: stnRouter.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: stnRouter.setDescription('This MIB module describes managed objects of Spring Tide Networks virtual routers plus associated IP, PPP, and PPPOE interfaces.')
stnRouterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1))
stnRouterMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 2))
stnRouterNAT = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5))
stnRouterVEI = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 6))
stnRouterAtmVpn = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 7))
stnRouterVimuxMpls = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 8))
stnRouterVTI = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 9))
class InterfaceConnectionType(TextualConvention, Integer32):
    description = 'The type of an interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))
    namedValues = NamedValues(("customer", 1), ("provider", 2), ("ppp", 4), ("pppoe", 5), ("home", 6))

class OperationState(TextualConvention, Integer32):
    description = 'Operational states of a router or an interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unassigned", 1), ("bufpend", 2), ("assignpend", 3), ("assigned", 4), ("unassignbufpend", 5), ("unassignpend", 6), ("failedassign", 7), ("error", 8))

stnRouterTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1), )
if mibBuilder.loadTexts: stnRouterTable.setStatus('current')
if mibBuilder.loadTexts: stnRouterTable.setDescription('A list of router entries.')
stnRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1), ).setIndexNames((0, "STN-ROUTER-MIB", "stnRouterIndex"))
if mibBuilder.loadTexts: stnRouterEntry.setStatus('current')
if mibBuilder.loadTexts: stnRouterEntry.setDescription('Entry contains information about a particular router.')
stnRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterIndex.setStatus('current')
if mibBuilder.loadTexts: stnRouterIndex.setDescription('A sequence number that identifies a router entry in the table.')
stnRouterType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("customer", 1), ("provider", 2), ("admin", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterType.setStatus('current')
if mibBuilder.loadTexts: stnRouterType.setDescription('The router type.')
stnRouterState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 3), OperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterState.setStatus('current')
if mibBuilder.loadTexts: stnRouterState.setDescription('The operational state of the router.')
stnRouterEngineID = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterEngineID.setStatus('current')
if mibBuilder.loadTexts: stnRouterEngineID.setDescription('The engine to which this router is currently assigned.')
stnRouterHomeIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterHomeIpAddress.setStatus('current')
if mibBuilder.loadTexts: stnRouterHomeIpAddress.setDescription('The Home IP address of this router.')
stnRouterEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterEnabled.setStatus('current')
if mibBuilder.loadTexts: stnRouterEnabled.setDescription('The variable to indicate if this router is enabled.')
stnRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterName.setStatus('current')
if mibBuilder.loadTexts: stnRouterName.setDescription('The name of this router.')
stnRouterUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterUpTime.setStatus('current')
if mibBuilder.loadTexts: stnRouterUpTime.setDescription('The time (in hundredths of a second) since the router was last re-initialized.')
stnRouterActiveSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterActiveSlot.setStatus('current')
if mibBuilder.loadTexts: stnRouterActiveSlot.setDescription('The slot/module to which this router is currently assigned.')
stnRouterActiveCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterActiveCpu.setStatus('current')
if mibBuilder.loadTexts: stnRouterActiveCpu.setDescription('The CPU to which this router is currently assigned.')
stnRouterConfiguredSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterConfiguredSlot.setStatus('current')
if mibBuilder.loadTexts: stnRouterConfiguredSlot.setDescription('The configured slot/module for this router.')
stnRouterConfiguredCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterConfiguredCpu.setStatus('current')
if mibBuilder.loadTexts: stnRouterConfiguredCpu.setDescription('The configured CPU for this router.')
stnRouterStandbySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterStandbySlot.setStatus('current')
if mibBuilder.loadTexts: stnRouterStandbySlot.setDescription('The standby slot/module for this router.')
stnRouterStandbyCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterStandbyCpu.setStatus('current')
if mibBuilder.loadTexts: stnRouterStandbyCpu.setDescription('The standby CPU for this router.')
stnRouterReassignOnFault = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterReassignOnFault.setStatus('current')
if mibBuilder.loadTexts: stnRouterReassignOnFault.setDescription('The variable to indicate if this router should be reassigned if the module where to fail.')
stnRouterServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterServiceName.setStatus('current')
if mibBuilder.loadTexts: stnRouterServiceName.setDescription('The service to which this router belongs.')
stnRouterServiceDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterServiceDomain.setStatus('current')
if mibBuilder.loadTexts: stnRouterServiceDomain.setDescription('The service domain to which this router belongs.')
stnRouterDefaultPolicyAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("permit", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnRouterDefaultPolicyAction.setStatus('current')
if mibBuilder.loadTexts: stnRouterDefaultPolicyAction.setDescription('Action to take when a packet does not match any policies.')
stnSubnetInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2), )
if mibBuilder.loadTexts: stnSubnetInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceTable.setDescription('A list of sub-network interface entries.')
stnSubnetInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1), ).setIndexNames((0, "STN-ROUTER-MIB", "stnSubnetInterfaceIndex"))
if mibBuilder.loadTexts: stnSubnetInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceEntry.setDescription('Entry contains information about a particular sub-network interface.')
stnSubnetInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceIndex.setDescription('A sequence number that identifies a sub-network interface entry in the table.')
stnSubnetInterfaceEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceEnabled.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceEnabled.setDescription('Enable or disable the sub-network interface.')
stnSubnetInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceAddress.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceAddress.setDescription('The IP address of this interface.')
stnSubnetInterfaceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceMask.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceMask.setDescription('The sub-network mask of this interface.')
stnSubnetInterfaceVclid = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceVclid.setStatus('deprecated')
if mibBuilder.loadTexts: stnSubnetInterfaceVclid.setDescription('The vcl ID associated with this sub-network interface.')
stnSubnetInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 6), InterfaceConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceType.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceType.setDescription('The interface type.')
stnSubnetInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 7), OperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceState.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceState.setDescription('The operational state of the sub-network interface.')
stnSubnetInterfaceRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceRouterIndex.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceRouterIndex.setDescription('The router this sub-network interface is associated with.')
stnSubnetInterfaceLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("vcLink", 1), ("vei", 2), ("home", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceLinkType.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceLinkType.setDescription('Indicates the type of link the subnet interface is configured over.')
stnSubnetInterfaceLinkInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceLinkInstance.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceLinkInstance.setDescription('The instance of the configuration record for the link the subnet interface is configured over.')
stnSubnetInterfaceForcedNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceForcedNextHop.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceForcedNextHop.setDescription('The IP address of the next hop router that all IP traffic received on this interface will be sent to')
stnSubnetInterfaceServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnSubnetInterfaceServiceName.setStatus('current')
if mibBuilder.loadTexts: stnSubnetInterfaceServiceName.setDescription('The service to which this interface belongs.')
stnPppoeTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3), )
if mibBuilder.loadTexts: stnPppoeTable.setStatus('current')
if mibBuilder.loadTexts: stnPppoeTable.setDescription('A list of PPPOE interface entries.')
stnPppoeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1), ).setIndexNames((0, "STN-ROUTER-MIB", "stnPppoeIndex"))
if mibBuilder.loadTexts: stnPppoeEntry.setStatus('current')
if mibBuilder.loadTexts: stnPppoeEntry.setDescription('Entry contains information about a particular PPPOE interface.')
stnPppoeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeIndex.setStatus('current')
if mibBuilder.loadTexts: stnPppoeIndex.setDescription('A sequence number that identifies a PPPOE interface entry in the table.')
stnPppoeType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 2), InterfaceConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeType.setStatus('current')
if mibBuilder.loadTexts: stnPppoeType.setDescription('The interface type.')
stnPppoeState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 3), OperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeState.setStatus('current')
if mibBuilder.loadTexts: stnPppoeState.setDescription('The operational state of the PPPOE interface.')
stnPppoeVclid = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeVclid.setStatus('deprecated')
if mibBuilder.loadTexts: stnPppoeVclid.setDescription('The vcl ID associated with this PPPOE interface.')
stnPppoeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnPppoeIfIndex.setDescription('The ifindex.')
stnPppoeRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeRouterIndex.setStatus('current')
if mibBuilder.loadTexts: stnPppoeRouterIndex.setDescription('The router this PPPOE interface is associated with.')
stnPppoeLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vcLink", 1), ("vei", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeLinkType.setStatus('current')
if mibBuilder.loadTexts: stnPppoeLinkType.setDescription('Indicates the type of link the PPPoE interface is configured over.')
stnPppoeLinkInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppoeLinkInstance.setStatus('current')
if mibBuilder.loadTexts: stnPppoeLinkInstance.setDescription('The instance of the configuration record for the link the PPPoE interface is configured over.')
stnPppTable = MibTable((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4), )
if mibBuilder.loadTexts: stnPppTable.setStatus('current')
if mibBuilder.loadTexts: stnPppTable.setDescription('A list of PPP interface entries.')
stnPppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1), ).setIndexNames((0, "STN-ROUTER-MIB", "stnPppIndex"))
if mibBuilder.loadTexts: stnPppEntry.setStatus('current')
if mibBuilder.loadTexts: stnPppEntry.setDescription('Entry contains information about a particular session.')
stnPppIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppIndex.setStatus('current')
if mibBuilder.loadTexts: stnPppIndex.setDescription('A sequence number that identifies a PPP interface entry in the table.')
stnPppType = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 2), InterfaceConnectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppType.setStatus('current')
if mibBuilder.loadTexts: stnPppType.setDescription('The interface type.')
stnPppState = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 3), OperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppState.setStatus('current')
if mibBuilder.loadTexts: stnPppState.setDescription('The operational state or the PPP interface.')
stnPppVclid = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppVclid.setStatus('current')
if mibBuilder.loadTexts: stnPppVclid.setDescription('The vcl ID associated with this PPP interface.')
stnPppIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppIfIndex.setStatus('current')
if mibBuilder.loadTexts: stnPppIfIndex.setDescription('The ifindex.')
stnPppRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnPppRouterIndex.setStatus('current')
if mibBuilder.loadTexts: stnPppRouterIndex.setDescription('The router this PPP interface is associated with.')
stnRouterUp = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 26)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnRouterState"), ("STN-ROUTER-MIB", "stnRouterName"), ("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"))
if mibBuilder.loadTexts: stnRouterUp.setStatus('current')
if mibBuilder.loadTexts: stnRouterUp.setDescription('A stnRouterUp trap signifies that the agent entity has detected that the stnRouterState object in the STN-ROUTER-MIB has transitioned to the assigned(4) state for one of its routers. The generation of this trap can be controlled by the RouterUpTraps configuration object.')
stnRouterDown = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 27)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnRouterState"), ("STN-ROUTER-MIB", "stnRouterName"), ("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"))
if mibBuilder.loadTexts: stnRouterDown.setStatus('current')
if mibBuilder.loadTexts: stnRouterDown.setDescription('A stnRouterDown trap signifies that the agent entity has detected that the stnRouterState object in the STN-ROUTER-MIB has transitioned to the failedassign(7) or error(8) state for one of its routers. The generation of this trap can be controlled by the RouterDownTraps configuration object.')
stnRouterReassigned = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 28)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnRouterState"), ("STN-ROUTER-MIB", "stnRouterName"), ("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"))
if mibBuilder.loadTexts: stnRouterReassigned.setStatus('current')
if mibBuilder.loadTexts: stnRouterReassigned.setDescription('A stnRouterReassigned trap signifies that the agent entity has detected that the stnRouterState object in the STN-ROUTER-MIB has transitioned to the the assigned(1) state for one of its routers. The generation of this trap can be controlled by the RouterReassignedTraps configuration object.')
stnRouterReassignFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 29)).setObjects(("STN-ROUTER-MIB", "stnRouterIndex"), ("STN-ROUTER-MIB", "stnRouterState"), ("STN-ROUTER-MIB", "stnRouterName"), ("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"))
if mibBuilder.loadTexts: stnRouterReassignFailure.setStatus('current')
if mibBuilder.loadTexts: stnRouterReassignFailure.setDescription('A stnRouterReassignFailure trap signifies that the agent entity has detected that the stnRouterState object in the STN-ROUTER-MIB has transitioned to the failedassign(7) or error(8) state for one of its routers. The generation of this trap can be controlled by the RouterReassignFailureTraps configuration object.')
stnSubnetIfAssignFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 30)).setObjects(("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"), ("STN-ROUTER-MIB", "stnSubnetInterfaceAddress"), ("STN-ROUTER-MIB", "stnSubnetInterfaceVclid"), ("STN-ROUTER-MIB", "stnSubnetInterfaceState"), ("STN-ROUTER-MIB", "stnSubnetInterfaceRouterIndex"), ("STN-ROUTER-MIB", "stnSubnetInterfaceLinkType"), ("STN-ROUTER-MIB", "stnSubnetInterfaceLinkInstance"))
if mibBuilder.loadTexts: stnSubnetIfAssignFailure.setStatus('current')
if mibBuilder.loadTexts: stnSubnetIfAssignFailure.setDescription('A stnSubnetIfAssignFailure trap signifies that the agent entity has detected that the stnSubnetInterfaceState object in the STN-ROUTER-MIB has transitioned to the failedassign(7) or error(8) state for one of its interfaces. The generation of this trap can be controlled by the stnEnableSubnetInterfaceTraps configuration object.')
stnConfigAuditRouterFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 33)).setObjects(("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"), ("STN-ROUTER-MIB", "stnRouterIndex"))
if mibBuilder.loadTexts: stnConfigAuditRouterFailure.setStatus('current')
if mibBuilder.loadTexts: stnConfigAuditRouterFailure.setDescription('A stnConfigAuditRouterFailure trap signifies that the agent entity has detected an inconsistency between an active and configured routers after a failover. The generation of this trap can be controlled by the CfgAuditRouterTraps configuration object.')
stnConfigAuditSubnetIfFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 34)).setObjects(("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"), ("STN-ROUTER-MIB", "stnSubnetInterfaceIndex"))
if mibBuilder.loadTexts: stnConfigAuditSubnetIfFailure.setStatus('current')
if mibBuilder.loadTexts: stnConfigAuditSubnetIfFailure.setDescription('A stnConfigAuditSubnetIfFailure trap signifies that agent entity has detected an inconsistency between an active and configured subnet interface after a failover. The generation of this trap can be controlled by the CfgAuditSubnetIfTraps configuration object.')
stnConfigAuditPppoeIfFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 35)).setObjects(("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"), ("STN-ROUTER-MIB", "stnPppoeRouterIndex"))
if mibBuilder.loadTexts: stnConfigAuditPppoeIfFailure.setStatus('current')
if mibBuilder.loadTexts: stnConfigAuditPppoeIfFailure.setDescription('A stnConfigAuditPppoeIfFailure trap signifies that agent entity has detected an inconsistency between an active and configured PPPOE interface after a failover. The generation of this trap can be controlled by the CfgAuditPppoeIfTraps configuration object.')
stnConfigAuditPppIfFailure = NotificationType((1, 3, 6, 1, 4, 1, 3551, 2, 100, 0, 36)).setObjects(("STN-CHASSIS-MIB", "stnEngineIndex"), ("STN-CHASSIS-MIB", "stnEngineSlot"), ("STN-CHASSIS-MIB", "stnEngineCpu"), ("STN-ROUTER-MIB", "stnPppRouterIndex"))
if mibBuilder.loadTexts: stnConfigAuditPppIfFailure.setStatus('current')
if mibBuilder.loadTexts: stnConfigAuditPppIfFailure.setDescription('A stnConfigAuditPppIfFailure trap signifies that agent entity has detected an inconsistency between an active and configured PPP interface after a failover. The generation of this trap can be controlled by the CfgAuditPppIfTraps configuration object.')
mibBuilder.exportSymbols("STN-ROUTER-MIB", stnConfigAuditSubnetIfFailure=stnConfigAuditSubnetIfFailure, stnSubnetInterfaceTable=stnSubnetInterfaceTable, stnRouterName=stnRouterName, stnRouterVimuxMpls=stnRouterVimuxMpls, stnSubnetInterfaceForcedNextHop=stnSubnetInterfaceForcedNextHop, stnPppoeTable=stnPppoeTable, stnPppoeVclid=stnPppoeVclid, stnRouterVTI=stnRouterVTI, stnRouterConfiguredSlot=stnRouterConfiguredSlot, stnConfigAuditRouterFailure=stnConfigAuditRouterFailure, stnRouterUp=stnRouterUp, stnRouterObjects=stnRouterObjects, stnRouterTable=stnRouterTable, stnRouterServiceName=stnRouterServiceName, stnPppState=stnPppState, stnRouterActiveSlot=stnRouterActiveSlot, stnSubnetInterfaceServiceName=stnSubnetInterfaceServiceName, stnSubnetInterfaceIndex=stnSubnetInterfaceIndex, stnSubnetInterfaceLinkType=stnSubnetInterfaceLinkType, stnPppTable=stnPppTable, stnRouterReassigned=stnRouterReassigned, stnRouterStandbyCpu=stnRouterStandbyCpu, stnPppEntry=stnPppEntry, stnRouterUpTime=stnRouterUpTime, stnRouterState=stnRouterState, stnPppType=stnPppType, stnRouterIndex=stnRouterIndex, stnRouterEngineID=stnRouterEngineID, stnSubnetInterfaceMask=stnSubnetInterfaceMask, stnSubnetInterfaceVclid=stnSubnetInterfaceVclid, stnRouterReassignOnFault=stnRouterReassignOnFault, stnPppRouterIndex=stnPppRouterIndex, stnRouterReassignFailure=stnRouterReassignFailure, stnPppoeType=stnPppoeType, stnSubnetInterfaceRouterIndex=stnSubnetInterfaceRouterIndex, stnPppoeState=stnPppoeState, stnConfigAuditPppoeIfFailure=stnConfigAuditPppoeIfFailure, stnPppoeIndex=stnPppoeIndex, stnSubnetInterfaceState=stnSubnetInterfaceState, stnRouterEnabled=stnRouterEnabled, stnRouterActiveCpu=stnRouterActiveCpu, stnPppVclid=stnPppVclid, OperationState=OperationState, stnRouterDown=stnRouterDown, stnRouterHomeIpAddress=stnRouterHomeIpAddress, stnRouterConfiguredCpu=stnRouterConfiguredCpu, stnPppoeEntry=stnPppoeEntry, stnRouterVEI=stnRouterVEI, stnPppoeIfIndex=stnPppoeIfIndex, stnPppIfIndex=stnPppIfIndex, stnSubnetInterfaceEnabled=stnSubnetInterfaceEnabled, stnRouterNAT=stnRouterNAT, InterfaceConnectionType=InterfaceConnectionType, stnSubnetInterfaceLinkInstance=stnSubnetInterfaceLinkInstance, stnSubnetInterfaceAddress=stnSubnetInterfaceAddress, stnPppoeLinkInstance=stnPppoeLinkInstance, stnPppoeLinkType=stnPppoeLinkType, stnRouterDefaultPolicyAction=stnRouterDefaultPolicyAction, stnPppoeRouterIndex=stnPppoeRouterIndex, stnRouter=stnRouter, stnPppIndex=stnPppIndex, stnSubnetInterfaceEntry=stnSubnetInterfaceEntry, stnRouterStandbySlot=stnRouterStandbySlot, stnRouterEntry=stnRouterEntry, stnRouterMibConformance=stnRouterMibConformance, stnRouterAtmVpn=stnRouterAtmVpn, stnRouterServiceDomain=stnRouterServiceDomain, stnSubnetIfAssignFailure=stnSubnetIfAssignFailure, stnConfigAuditPppIfFailure=stnConfigAuditPppIfFailure, stnRouterType=stnRouterType, PYSNMP_MODULE_ID=stnRouter, stnSubnetInterfaceType=stnSubnetInterfaceType)
