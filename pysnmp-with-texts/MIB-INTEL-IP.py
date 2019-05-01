#
# PySNMP MIB module MIB-INTEL-IP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIB-INTEL-IP
# Produced by pysmi-0.3.4 at Wed May  1 14:12:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Bits, Gauge32, MibIdentifier, Integer32, IpAddress, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Bits", "Gauge32", "MibIdentifier", "Integer32", "IpAddress", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipr = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 38))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

rtIpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 38, 1), )
if mibBuilder.loadTexts: rtIpRouteTable.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteTable.setDescription("This entity's IP Routing table.")
rtIpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1), ).setIndexNames((0, "MIB-INTEL-IP", "rtIpRouteChassis"), (0, "MIB-INTEL-IP", "rtIpRouteModule"), (0, "MIB-INTEL-IP", "rtIpRouteInst"), (0, "MIB-INTEL-IP", "rtIpRouteDest"), (0, "MIB-INTEL-IP", "rtIpRouteMask"), (0, "MIB-INTEL-IP", "rtIpRouteIfIndex"), (0, "MIB-INTEL-IP", "rtIpRouteNextHop"))
if mibBuilder.loadTexts: rtIpRouteEntry.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteEntry.setDescription('A route to a particular destination.')
rtIpRouteChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteChassis.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteChassis.setDescription('Chassis number in stack that contains the module.')
rtIpRouteModule = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteModule.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteModule.setDescription('Module number in the chassis.')
rtIpRouteInst = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteInst.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteInst.setDescription('Routing table instance number.')
rtIpRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteDest.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteDest.setDescription('The destination IP address of this route.')
rtIpRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteMask.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteMask.setDescription('Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the rtIpRouteDest field.')
rtIpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteIfIndex.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteIfIndex.setDescription('The interface that the frame is forwarded on.')
rtIpRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteNextHop.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteNextHop.setDescription('The IP address of the next hop of this route.')
rtIpRoutePref = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRoutePref.setStatus('optional')
if mibBuilder.loadTexts: rtIpRoutePref.setDescription('The preference value for this route.')
rtIpRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteMetric.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteMetric.setDescription("The routing metric for this route. The semantics of this metric are determined by the routing-protocol specified in the route's rtIpRouteProto value.")
rtIpRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("direct", 1), ("static", 2), ("ospf", 3), ("rip", 4), ("other", 5), ("all", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteProto.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteProto.setDescription('The routing mechanism via which this route was learned.')
rtIpRouteAge = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRouteAge.setStatus('optional')
if mibBuilder.loadTexts: rtIpRouteAge.setDescription("The number of seconds since this route was last updated or otherwise detemined to be correct. Note that no semantics of 'too old' can be implied except through knowledge of the routing protocol by which the route was learned.")
rtIpRteTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 38, 2), )
if mibBuilder.loadTexts: rtIpRteTable.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteTable.setDescription('The list of all routing table entries (RTE). There may be several entries describing a route to the same destination (entries with the same IP address and mask but different preference, protocol or metric). Forwarding engine uses only the best one - this one which can be found in the Routing Table. All other entries as well the best one are available in rtIpRteTable. If for some reason the best entry has been lost then the best one will be chosen from other entries to the same destination.')
rtIpRteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1), ).setIndexNames((0, "MIB-INTEL-IP", "rtIpRteChassis"), (0, "MIB-INTEL-IP", "rtIpRteModule"), (0, "MIB-INTEL-IP", "rtIpRteInst"), (0, "MIB-INTEL-IP", "rtIpRteDest"), (0, "MIB-INTEL-IP", "rtIpRteMask"), (0, "MIB-INTEL-IP", "rtIpRtePref"), (0, "MIB-INTEL-IP", "rtIpRteProto"), (0, "MIB-INTEL-IP", "rtIpRteIfIndex"), (0, "MIB-INTEL-IP", "rtIpRteNextHop"))
if mibBuilder.loadTexts: rtIpRteEntry.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteEntry.setDescription('A route to a particular destination.')
rtIpRteChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteChassis.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteChassis.setDescription('Chassis number in stack that contains the module.')
rtIpRteModule = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteModule.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteModule.setDescription('Module number in the chassis.')
rtIpRteInst = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteInst.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteInst.setDescription('Alternative routing table instance number.')
rtIpRteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteDest.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteDest.setDescription('The destination IP address of this route.')
rtIpRteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteMask.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteMask.setDescription('Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the rtIpRteDest field.')
rtIpRtePref = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRtePref.setStatus('optional')
if mibBuilder.loadTexts: rtIpRtePref.setDescription('The preference value for this route.')
rtIpRteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("direct", 1), ("static", 2), ("ospf", 3), ("rip", 4), ("other", 5), ("all", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteProto.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteProto.setDescription('The routing mechanism via which this route was learned.')
rtIpRteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteIfIndex.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteIfIndex.setDescription('The interface that the frame is forwarded on.')
rtIpRteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteNextHop.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteNextHop.setDescription('The IP address of the next hop of this route.')
rtIpRteState = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpRteState.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteState.setDescription('The state of the route.')
rtIpRteAge = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtIpRteAge.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteAge.setDescription("The number of seconds since this route was last updated or otherwise detemined to be correct. Note that no semantics of 'too old' can be implied except through knowledge of the routing protocol by which the route was learned.")
rtIpRteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpRteMetric.setStatus('optional')
if mibBuilder.loadTexts: rtIpRteMetric.setDescription('The metric of the alternative route.')
rtIpStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 38, 3), )
if mibBuilder.loadTexts: rtIpStaticRouteTable.setStatus('optional')
if mibBuilder.loadTexts: rtIpStaticRouteTable.setDescription('A table of all configured static routes.')
rtIpStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1), ).setIndexNames((0, "MIB-INTEL-IP", "rtIpStRtChassis"), (0, "MIB-INTEL-IP", "rtIpStRtModule"), (0, "MIB-INTEL-IP", "rtIpStRtInst"), (0, "MIB-INTEL-IP", "rtIpStRtDest"), (0, "MIB-INTEL-IP", "rtIpStRtMask"), (0, "MIB-INTEL-IP", "rtIpStRtPref"), (0, "MIB-INTEL-IP", "rtIpStRtIfIndex"), (0, "MIB-INTEL-IP", "rtIpStRtNextHop"))
if mibBuilder.loadTexts: rtIpStaticRouteEntry.setStatus('optional')
if mibBuilder.loadTexts: rtIpStaticRouteEntry.setDescription('An entry describing a single static route.')
rtIpStRtChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtChassis.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtChassis.setDescription('Chassis number in stack that contains the module.')
rtIpStRtModule = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtModule.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtModule.setDescription('Module number in the chassis.')
rtIpStRtInst = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtInst.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtInst.setDescription('Static routing table instance number.')
rtIpStRtDest = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtDest.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtDest.setDescription('The destination IP address of this route.')
rtIpStRtMask = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtMask.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtMask.setDescription('The destination IP mask of this route.')
rtIpStRtPref = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtPref.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtPref.setDescription('The preference value for this route. This value should be unique (neither other static routes to the same destination nor other protocols can use this value).')
rtIpStRtIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtIfIndex.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtIfIndex.setDescription('The interface that the frame is forwarded on.')
rtIpStRtNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtNextHop.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtNextHop.setDescription('The IP address of the next hop of this route.')
rtIpStRtMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtMetric.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtMetric.setDescription('The routing metric for this route.')
rtIpStRtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtStatus.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtStatus.setDescription("The status of the route. Setting it to 'destroy'(6) removes the static route from router's configuration.")
rtIpStRtState = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 38, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rtIpStRtState.setStatus('optional')
if mibBuilder.loadTexts: rtIpStRtState.setDescription('The current state of the route.')
mibBuilder.exportSymbols("MIB-INTEL-IP", rtIpRoutePref=rtIpRoutePref, rtIpStRtIfIndex=rtIpStRtIfIndex, rtIpRteEntry=rtIpRteEntry, rtIpRouteInst=rtIpRouteInst, rtIpStRtMask=rtIpStRtMask, rtIpRouteEntry=rtIpRouteEntry, rtIpRteMask=rtIpRteMask, rtIpRteState=rtIpRteState, rtIpRteProto=rtIpRteProto, rtIpRouteMetric=rtIpRouteMetric, rtIpRteDest=rtIpRteDest, rtIpRteInst=rtIpRteInst, ipr=ipr, rtIpRteAge=rtIpRteAge, rtIpRouteProto=rtIpRouteProto, rtIpRouteNextHop=rtIpRouteNextHop, rtIpRouteModule=rtIpRouteModule, rtIpRteNextHop=rtIpRteNextHop, rtIpRteModule=rtIpRteModule, rtIpStRtDest=rtIpStRtDest, rtIpRteIfIndex=rtIpRteIfIndex, rtIpStaticRouteEntry=rtIpStaticRouteEntry, RowStatus=RowStatus, rtIpStRtMetric=rtIpStRtMetric, rtIpRouteDest=rtIpRouteDest, rtIpRouteChassis=rtIpRouteChassis, rtIpRouteMask=rtIpRouteMask, rtIpRteTable=rtIpRteTable, rtIpRouteTable=rtIpRouteTable, rtIpStRtPref=rtIpStRtPref, rtIpStaticRouteTable=rtIpStaticRouteTable, rtIpRteChassis=rtIpRteChassis, rtIpRouteAge=rtIpRouteAge, rtIpRteMetric=rtIpRteMetric, rtIpStRtState=rtIpStRtState, rtIpRtePref=rtIpRtePref, rtIpStRtChassis=rtIpStRtChassis, rtIpStRtStatus=rtIpStRtStatus, rtIpStRtModule=rtIpStRtModule, rtIpStRtNextHop=rtIpStRtNextHop, rtIpStRtInst=rtIpStRtInst, rtIpRouteIfIndex=rtIpRouteIfIndex)
