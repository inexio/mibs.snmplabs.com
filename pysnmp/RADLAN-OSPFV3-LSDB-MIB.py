#
# PySNMP MIB module RADLAN-OSPFV3-LSDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-OSPFV3-LSDB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:39:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddress, InetAddressPrefixLength, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressIPv6", "InetAddressType")
AreaID, RouterID = mibBuilder.importSymbols("OSPF-MIB", "AreaID", "RouterID")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
RlOspfProcessID, = mibBuilder.importSymbols("RADLAN-OSPF-MIB", "RlOspfProcessID")
rlOspfv3, = mibBuilder.importSymbols("RADLAN-OSPFV3-MIB", "rlOspfv3")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Unsigned32, iso, ModuleIdentity, IpAddress, TimeTicks, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, NotificationType, ObjectIdentity, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Unsigned32", "iso", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "NotificationType", "ObjectIdentity", "mib-2")
TruthValue, RowStatus, TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "TimeStamp", "DisplayString")
rlOspfv3Lsdb = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 222))
rlOspfv3Lsdb.setRevisions(('2011-05-04 17:00',))
if mibBuilder.loadTexts: rlOspfv3Lsdb.setLastUpdated('201105041700Z')
if mibBuilder.loadTexts: rlOspfv3Lsdb.setOrganization('Radlan Computer Communications Ltd.')
rlOspfv3RouterLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 222, 1), )
if mibBuilder.loadTexts: rlOspfv3RouterLsaTable.setStatus('current')
rlOspfv3RouterLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 222, 1, 1), ).setIndexNames((0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaProcessId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaAreaId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaLsid"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaRouterId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3RouterLsaIdx"))
if mibBuilder.loadTexts: rlOspfv3RouterLsaEntry.setStatus('current')
rlOspfv3RouterLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaProcessId.setStatus('current')
rlOspfv3RouterLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaAreaId.setStatus('current')
rlOspfv3RouterLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaLsid.setStatus('current')
rlOspfv3RouterLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaRouterId.setStatus('current')
rlOspfv3RouterLsaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaIdx.setStatus('current')
rlOspfv3RouterLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaCount.setStatus('current')
rlOspfv3RouterLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaSequence.setStatus('current')
rlOspfv3RouterLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaAge.setStatus('current')
rlOspfv3RouterLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaChecksum.setStatus('current')
rlOspfv3RouterLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaLength.setStatus('current')
rlOspfv3RouterLsaBitW = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaBitW.setStatus('current')
rlOspfv3RouterLsaBitV = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaBitV.setStatus('current')
rlOspfv3RouterLsaBitE = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaBitE.setStatus('current')
rlOspfv3RouterLsaBitB = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaBitB.setStatus('current')
rlOspfv3RouterLsaOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaOptions.setStatus('current')
rlOspfv3RouterLsaType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pointToPoint", 1), ("transitNetwork", 2), ("stubNetwork", 3), ("virtualLink", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaType.setStatus('current')
rlOspfv3RouterLsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaMetric.setStatus('current')
rlOspfv3RouterLsaInterfaceID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaInterfaceID.setStatus('current')
rlOspfv3RouterLsaNeighborInterfaceID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaNeighborInterfaceID.setStatus('current')
rlOspfv3RouterLsaNeighborRouterID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 1, 1, 20), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3RouterLsaNeighborRouterID.setStatus('current')
rlOspfv3NetworkLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 222, 2), )
if mibBuilder.loadTexts: rlOspfv3NetworkLsaTable.setStatus('current')
rlOspfv3NetworkLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 222, 2, 1), ).setIndexNames((0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaProcessId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaAreaId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaLsid"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaRouterId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3NetworkLsaIdx"))
if mibBuilder.loadTexts: rlOspfv3NetworkLsaEntry.setStatus('current')
rlOspfv3NetworkLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaProcessId.setStatus('current')
rlOspfv3NetworkLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaAreaId.setStatus('current')
rlOspfv3NetworkLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaLsid.setStatus('current')
rlOspfv3NetworkLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaRouterId.setStatus('current')
rlOspfv3NetworkLsaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaIdx.setStatus('current')
rlOspfv3NetworkLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaCount.setStatus('current')
rlOspfv3NetworkLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaSequence.setStatus('current')
rlOspfv3NetworkLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaAge.setStatus('current')
rlOspfv3NetworkLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaChecksum.setStatus('current')
rlOspfv3NetworkLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaLength.setStatus('current')
rlOspfv3NetworkLsaOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaOptions.setStatus('current')
rlOspfv3NetworkLsaAttRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 2, 1, 12), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3NetworkLsaAttRouter.setStatus('current')
rlOspfv3InterAreaPrefixLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 222, 3), )
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaTable.setStatus('current')
rlOspfv3InterAreaPrefixLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 222, 3, 1), ).setIndexNames((0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaProcessId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaAreaId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaLsid"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaPrefixLsaRouterId"))
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaEntry.setStatus('current')
rlOspfv3InterAreaPrefixLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaProcessId.setStatus('current')
rlOspfv3InterAreaPrefixLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaAreaId.setStatus('current')
rlOspfv3InterAreaPrefixLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaLsid.setStatus('current')
rlOspfv3InterAreaPrefixLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaRouterId.setStatus('current')
rlOspfv3InterAreaPrefixLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaSequence.setStatus('current')
rlOspfv3InterAreaPrefixLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaAge.setStatus('current')
rlOspfv3InterAreaPrefixLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaChecksum.setStatus('current')
rlOspfv3InterAreaPrefixLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaLength.setStatus('current')
rlOspfv3InterAreaPrefixLsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaMetric.setStatus('current')
rlOspfv3InterAreaPrefixLsaPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaPrefixLength.setStatus('current')
rlOspfv3InterAreaPrefixLsaPrefixOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaPrefixOptions.setStatus('current')
rlOspfv3InterAreaPrefixLsaAddressPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 3, 1, 12), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaPrefixLsaAddressPrefix.setStatus('current')
rlOspfv3InterAreaRouterLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 222, 4), )
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaTable.setStatus('current')
rlOspfv3InterAreaRouterLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 222, 4, 1), ).setIndexNames((0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaProcessId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaAreaId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaLsid"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3InterAreaRouterLsaRouterId"))
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaEntry.setStatus('current')
rlOspfv3InterAreaRouterLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaProcessId.setStatus('current')
rlOspfv3InterAreaRouterLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaAreaId.setStatus('current')
rlOspfv3InterAreaRouterLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaLsid.setStatus('current')
rlOspfv3InterAreaRouterLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaRouterId.setStatus('current')
rlOspfv3InterAreaRouterLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaSequence.setStatus('current')
rlOspfv3InterAreaRouterLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaAge.setStatus('current')
rlOspfv3InterAreaRouterLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaChecksum.setStatus('current')
rlOspfv3InterAreaRouterLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaLength.setStatus('current')
rlOspfv3InterAreaRouterLsaOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaOptions.setStatus('current')
rlOspfv3InterAreaRouterLsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaMetric.setStatus('current')
rlOspfv3InterAreaRouterLsaDestinationRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 4, 1, 11), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3InterAreaRouterLsaDestinationRouterId.setStatus('current')
rlOspfv3AsExternalLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 222, 5), )
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaTable.setStatus('current')
rlOspfv3AsExternalLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 222, 5, 1), ).setIndexNames((0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaProcessId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaAreaId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaLsid"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3AsExternalLsaRouterId"))
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaEntry.setStatus('current')
rlOspfv3AsExternalLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaProcessId.setStatus('current')
rlOspfv3AsExternalLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaAreaId.setStatus('current')
rlOspfv3AsExternalLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaLsid.setStatus('current')
rlOspfv3AsExternalLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaRouterId.setStatus('current')
rlOspfv3AsExternalLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaSequence.setStatus('current')
rlOspfv3AsExternalLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaAge.setStatus('current')
rlOspfv3AsExternalLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaChecksum.setStatus('current')
rlOspfv3AsExternalLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaLength.setStatus('current')
rlOspfv3AsExternalLsaBitE = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaBitE.setStatus('current')
rlOspfv3AsExternalLsaBitF = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaBitF.setStatus('current')
rlOspfv3AsExternalLsaBitT = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaBitT.setStatus('current')
rlOspfv3AsExternalLsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaMetric.setStatus('current')
rlOspfv3AsExternalLsaReferencedLsType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaReferencedLsType.setStatus('current')
rlOspfv3AsExternalLsaPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaPrefixLength.setStatus('current')
rlOspfv3AsExternalLsaPrefixOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaPrefixOptions.setStatus('current')
rlOspfv3AsExternalLsaAddressPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 16), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaAddressPrefix.setStatus('current')
rlOspfv3AsExternalLsaForwardingAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 17), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaForwardingAddress.setStatus('current')
rlOspfv3AsExternalLsaExternalRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaExternalRouteTag.setStatus('current')
rlOspfv3AsExternalLsaReferencedLinkStateId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 5, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3AsExternalLsaReferencedLinkStateId.setStatus('current')
rlOspfv3LinkLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 222, 6), )
if mibBuilder.loadTexts: rlOspfv3LinkLsaTable.setStatus('current')
rlOspfv3LinkLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 222, 6, 1), ).setIndexNames((0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaProcessId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaIfIndex"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaIfInstId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaLsid"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaRouterId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3LinkLsaIdx"))
if mibBuilder.loadTexts: rlOspfv3LinkLsaEntry.setStatus('current')
rlOspfv3LinkLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaProcessId.setStatus('current')
rlOspfv3LinkLsaIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 2), Unsigned32())
if mibBuilder.loadTexts: rlOspfv3LinkLsaIfIndex.setStatus('current')
rlOspfv3LinkLsaIfInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: rlOspfv3LinkLsaIfInstId.setStatus('current')
rlOspfv3LinkLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaLsid.setStatus('current')
rlOspfv3LinkLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 5), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaRouterId.setStatus('current')
rlOspfv3LinkLsaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaIdx.setStatus('current')
rlOspfv3LinkLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaCount.setStatus('current')
rlOspfv3LinkLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaSequence.setStatus('current')
rlOspfv3LinkLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaAge.setStatus('current')
rlOspfv3LinkLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaChecksum.setStatus('current')
rlOspfv3LinkLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaLength.setStatus('current')
rlOspfv3LinkLsaRtrPri = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaRtrPri.setStatus('current')
rlOspfv3LinkLsaOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaOptions.setStatus('current')
rlOspfv3LinkLsaLinkLocalInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 14), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaLinkLocalInterfaceAddress.setStatus('current')
rlOspfv3LinkLsaPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaPrefixLength.setStatus('current')
rlOspfv3LinkLsaPrefixOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaPrefixOptions.setStatus('current')
rlOspfv3LinkLsaAddressPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 6, 1, 17), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3LinkLsaAddressPrefix.setStatus('current')
rlOspfv3IntraAreaPrefixLsaTable = MibTable((1, 3, 6, 1, 4, 1, 89, 222, 7), )
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaTable.setStatus('current')
rlOspfv3IntraAreaPrefixLsaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 222, 7, 1), ).setIndexNames((0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaProcessId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaAreaId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaLsid"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaRouterId"), (0, "RADLAN-OSPFV3-LSDB-MIB", "rlOspfv3IntraAreaPrefixLsaIdx"))
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaEntry.setStatus('current')
rlOspfv3IntraAreaPrefixLsaProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 1), RlOspfProcessID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaProcessId.setStatus('current')
rlOspfv3IntraAreaPrefixLsaAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 2), AreaID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaAreaId.setStatus('current')
rlOspfv3IntraAreaPrefixLsaLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaLsid.setStatus('current')
rlOspfv3IntraAreaPrefixLsaRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 4), RouterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaRouterId.setStatus('current')
rlOspfv3IntraAreaPrefixLsaIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaIdx.setStatus('current')
rlOspfv3IntraAreaPrefixLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaCount.setStatus('current')
rlOspfv3IntraAreaPrefixLsaSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaSequence.setStatus('current')
rlOspfv3IntraAreaPrefixLsaAge = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaAge.setStatus('current')
rlOspfv3IntraAreaPrefixLsaChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaChecksum.setStatus('current')
rlOspfv3IntraAreaPrefixLsaLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaLength.setStatus('current')
rlOspfv3IntraAreaPrefixLsaNumPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaNumPrefixes.setStatus('current')
rlOspfv3IntraAreaPrefixLsaReferenceLsType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaReferenceLsType.setStatus('current')
rlOspfv3IntraAreaPrefixLsaReferenceLsId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaReferenceLsId.setStatus('current')
rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter.setStatus('current')
rlOspfv3IntraAreaPrefixLsaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaMetric.setStatus('current')
rlOspfv3IntraAreaPrefixLsaPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaPrefixLength.setStatus('current')
rlOspfv3IntraAreaPrefixLsaPrefixOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaPrefixOptions.setStatus('current')
rlOspfv3IntraAreaPrefixLsaAddressPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 222, 7, 1, 18), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlOspfv3IntraAreaPrefixLsaAddressPrefix.setStatus('current')
mibBuilder.exportSymbols("RADLAN-OSPFV3-LSDB-MIB", rlOspfv3AsExternalLsaReferencedLinkStateId=rlOspfv3AsExternalLsaReferencedLinkStateId, rlOspfv3RouterLsaLsid=rlOspfv3RouterLsaLsid, rlOspfv3RouterLsaOptions=rlOspfv3RouterLsaOptions, rlOspfv3LinkLsaEntry=rlOspfv3LinkLsaEntry, rlOspfv3IntraAreaPrefixLsaPrefixLength=rlOspfv3IntraAreaPrefixLsaPrefixLength, rlOspfv3AsExternalLsaLsid=rlOspfv3AsExternalLsaLsid, rlOspfv3NetworkLsaCount=rlOspfv3NetworkLsaCount, rlOspfv3AsExternalLsaLength=rlOspfv3AsExternalLsaLength, rlOspfv3AsExternalLsaExternalRouteTag=rlOspfv3AsExternalLsaExternalRouteTag, rlOspfv3InterAreaPrefixLsaAreaId=rlOspfv3InterAreaPrefixLsaAreaId, rlOspfv3NetworkLsaAreaId=rlOspfv3NetworkLsaAreaId, rlOspfv3NetworkLsaSequence=rlOspfv3NetworkLsaSequence, rlOspfv3AsExternalLsaBitT=rlOspfv3AsExternalLsaBitT, rlOspfv3IntraAreaPrefixLsaAreaId=rlOspfv3IntraAreaPrefixLsaAreaId, rlOspfv3IntraAreaPrefixLsaReferenceLsId=rlOspfv3IntraAreaPrefixLsaReferenceLsId, rlOspfv3NetworkLsaAttRouter=rlOspfv3NetworkLsaAttRouter, rlOspfv3IntraAreaPrefixLsaChecksum=rlOspfv3IntraAreaPrefixLsaChecksum, rlOspfv3RouterLsaAge=rlOspfv3RouterLsaAge, rlOspfv3IntraAreaPrefixLsaCount=rlOspfv3IntraAreaPrefixLsaCount, rlOspfv3Lsdb=rlOspfv3Lsdb, rlOspfv3IntraAreaPrefixLsaAge=rlOspfv3IntraAreaPrefixLsaAge, rlOspfv3InterAreaRouterLsaProcessId=rlOspfv3InterAreaRouterLsaProcessId, rlOspfv3InterAreaPrefixLsaAge=rlOspfv3InterAreaPrefixLsaAge, rlOspfv3RouterLsaRouterId=rlOspfv3RouterLsaRouterId, rlOspfv3InterAreaPrefixLsaRouterId=rlOspfv3InterAreaPrefixLsaRouterId, rlOspfv3NetworkLsaProcessId=rlOspfv3NetworkLsaProcessId, rlOspfv3LinkLsaLength=rlOspfv3LinkLsaLength, rlOspfv3InterAreaRouterLsaAreaId=rlOspfv3InterAreaRouterLsaAreaId, rlOspfv3LinkLsaTable=rlOspfv3LinkLsaTable, rlOspfv3AsExternalLsaAreaId=rlOspfv3AsExternalLsaAreaId, rlOspfv3InterAreaPrefixLsaPrefixLength=rlOspfv3InterAreaPrefixLsaPrefixLength, rlOspfv3LinkLsaIdx=rlOspfv3LinkLsaIdx, rlOspfv3LinkLsaRtrPri=rlOspfv3LinkLsaRtrPri, rlOspfv3InterAreaPrefixLsaMetric=rlOspfv3InterAreaPrefixLsaMetric, rlOspfv3NetworkLsaLsid=rlOspfv3NetworkLsaLsid, rlOspfv3RouterLsaInterfaceID=rlOspfv3RouterLsaInterfaceID, rlOspfv3InterAreaRouterLsaDestinationRouterId=rlOspfv3InterAreaRouterLsaDestinationRouterId, rlOspfv3AsExternalLsaBitF=rlOspfv3AsExternalLsaBitF, rlOspfv3AsExternalLsaSequence=rlOspfv3AsExternalLsaSequence, rlOspfv3IntraAreaPrefixLsaLsid=rlOspfv3IntraAreaPrefixLsaLsid, rlOspfv3RouterLsaBitW=rlOspfv3RouterLsaBitW, rlOspfv3InterAreaPrefixLsaLength=rlOspfv3InterAreaPrefixLsaLength, rlOspfv3IntraAreaPrefixLsaLength=rlOspfv3IntraAreaPrefixLsaLength, rlOspfv3IntraAreaPrefixLsaTable=rlOspfv3IntraAreaPrefixLsaTable, rlOspfv3AsExternalLsaRouterId=rlOspfv3AsExternalLsaRouterId, rlOspfv3NetworkLsaAge=rlOspfv3NetworkLsaAge, rlOspfv3AsExternalLsaReferencedLsType=rlOspfv3AsExternalLsaReferencedLsType, rlOspfv3InterAreaRouterLsaAge=rlOspfv3InterAreaRouterLsaAge, rlOspfv3IntraAreaPrefixLsaPrefixOptions=rlOspfv3IntraAreaPrefixLsaPrefixOptions, rlOspfv3IntraAreaPrefixLsaRouterId=rlOspfv3IntraAreaPrefixLsaRouterId, rlOspfv3InterAreaRouterLsaMetric=rlOspfv3InterAreaRouterLsaMetric, rlOspfv3LinkLsaLinkLocalInterfaceAddress=rlOspfv3LinkLsaLinkLocalInterfaceAddress, rlOspfv3RouterLsaEntry=rlOspfv3RouterLsaEntry, rlOspfv3NetworkLsaChecksum=rlOspfv3NetworkLsaChecksum, rlOspfv3LinkLsaOptions=rlOspfv3LinkLsaOptions, rlOspfv3LinkLsaLsid=rlOspfv3LinkLsaLsid, rlOspfv3IntraAreaPrefixLsaMetric=rlOspfv3IntraAreaPrefixLsaMetric, rlOspfv3IntraAreaPrefixLsaProcessId=rlOspfv3IntraAreaPrefixLsaProcessId, rlOspfv3RouterLsaAreaId=rlOspfv3RouterLsaAreaId, PYSNMP_MODULE_ID=rlOspfv3Lsdb, rlOspfv3AsExternalLsaAddressPrefix=rlOspfv3AsExternalLsaAddressPrefix, rlOspfv3LinkLsaAge=rlOspfv3LinkLsaAge, rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter=rlOspfv3IntraAreaPrefixLsaReferenceAdvRouter, rlOspfv3RouterLsaNeighborInterfaceID=rlOspfv3RouterLsaNeighborInterfaceID, rlOspfv3LinkLsaSequence=rlOspfv3LinkLsaSequence, rlOspfv3InterAreaRouterLsaEntry=rlOspfv3InterAreaRouterLsaEntry, rlOspfv3AsExternalLsaTable=rlOspfv3AsExternalLsaTable, rlOspfv3NetworkLsaRouterId=rlOspfv3NetworkLsaRouterId, rlOspfv3RouterLsaProcessId=rlOspfv3RouterLsaProcessId, rlOspfv3IntraAreaPrefixLsaNumPrefixes=rlOspfv3IntraAreaPrefixLsaNumPrefixes, rlOspfv3NetworkLsaOptions=rlOspfv3NetworkLsaOptions, rlOspfv3AsExternalLsaProcessId=rlOspfv3AsExternalLsaProcessId, rlOspfv3AsExternalLsaEntry=rlOspfv3AsExternalLsaEntry, rlOspfv3InterAreaRouterLsaLength=rlOspfv3InterAreaRouterLsaLength, rlOspfv3InterAreaPrefixLsaEntry=rlOspfv3InterAreaPrefixLsaEntry, rlOspfv3AsExternalLsaBitE=rlOspfv3AsExternalLsaBitE, rlOspfv3LinkLsaIfIndex=rlOspfv3LinkLsaIfIndex, rlOspfv3AsExternalLsaPrefixLength=rlOspfv3AsExternalLsaPrefixLength, rlOspfv3RouterLsaMetric=rlOspfv3RouterLsaMetric, rlOspfv3InterAreaPrefixLsaTable=rlOspfv3InterAreaPrefixLsaTable, rlOspfv3NetworkLsaLength=rlOspfv3NetworkLsaLength, rlOspfv3RouterLsaBitB=rlOspfv3RouterLsaBitB, rlOspfv3InterAreaPrefixLsaAddressPrefix=rlOspfv3InterAreaPrefixLsaAddressPrefix, rlOspfv3LinkLsaIfInstId=rlOspfv3LinkLsaIfInstId, rlOspfv3RouterLsaNeighborRouterID=rlOspfv3RouterLsaNeighborRouterID, rlOspfv3AsExternalLsaAge=rlOspfv3AsExternalLsaAge, rlOspfv3AsExternalLsaMetric=rlOspfv3AsExternalLsaMetric, rlOspfv3RouterLsaType=rlOspfv3RouterLsaType, rlOspfv3InterAreaRouterLsaOptions=rlOspfv3InterAreaRouterLsaOptions, rlOspfv3RouterLsaTable=rlOspfv3RouterLsaTable, rlOspfv3InterAreaRouterLsaSequence=rlOspfv3InterAreaRouterLsaSequence, rlOspfv3InterAreaRouterLsaRouterId=rlOspfv3InterAreaRouterLsaRouterId, rlOspfv3LinkLsaRouterId=rlOspfv3LinkLsaRouterId, rlOspfv3InterAreaRouterLsaChecksum=rlOspfv3InterAreaRouterLsaChecksum, rlOspfv3IntraAreaPrefixLsaSequence=rlOspfv3IntraAreaPrefixLsaSequence, rlOspfv3AsExternalLsaChecksum=rlOspfv3AsExternalLsaChecksum, rlOspfv3RouterLsaChecksum=rlOspfv3RouterLsaChecksum, rlOspfv3LinkLsaPrefixOptions=rlOspfv3LinkLsaPrefixOptions, rlOspfv3LinkLsaPrefixLength=rlOspfv3LinkLsaPrefixLength, rlOspfv3RouterLsaIdx=rlOspfv3RouterLsaIdx, rlOspfv3InterAreaPrefixLsaChecksum=rlOspfv3InterAreaPrefixLsaChecksum, rlOspfv3RouterLsaSequence=rlOspfv3RouterLsaSequence, rlOspfv3RouterLsaBitE=rlOspfv3RouterLsaBitE, rlOspfv3AsExternalLsaPrefixOptions=rlOspfv3AsExternalLsaPrefixOptions, rlOspfv3IntraAreaPrefixLsaAddressPrefix=rlOspfv3IntraAreaPrefixLsaAddressPrefix, rlOspfv3LinkLsaChecksum=rlOspfv3LinkLsaChecksum, rlOspfv3LinkLsaAddressPrefix=rlOspfv3LinkLsaAddressPrefix, rlOspfv3RouterLsaCount=rlOspfv3RouterLsaCount, rlOspfv3InterAreaPrefixLsaSequence=rlOspfv3InterAreaPrefixLsaSequence, rlOspfv3NetworkLsaEntry=rlOspfv3NetworkLsaEntry, rlOspfv3AsExternalLsaForwardingAddress=rlOspfv3AsExternalLsaForwardingAddress, rlOspfv3LinkLsaCount=rlOspfv3LinkLsaCount, rlOspfv3InterAreaRouterLsaTable=rlOspfv3InterAreaRouterLsaTable, rlOspfv3RouterLsaLength=rlOspfv3RouterLsaLength, rlOspfv3InterAreaRouterLsaLsid=rlOspfv3InterAreaRouterLsaLsid, rlOspfv3InterAreaPrefixLsaProcessId=rlOspfv3InterAreaPrefixLsaProcessId, rlOspfv3NetworkLsaTable=rlOspfv3NetworkLsaTable, rlOspfv3IntraAreaPrefixLsaReferenceLsType=rlOspfv3IntraAreaPrefixLsaReferenceLsType, rlOspfv3IntraAreaPrefixLsaIdx=rlOspfv3IntraAreaPrefixLsaIdx, rlOspfv3LinkLsaProcessId=rlOspfv3LinkLsaProcessId, rlOspfv3RouterLsaBitV=rlOspfv3RouterLsaBitV, rlOspfv3InterAreaPrefixLsaPrefixOptions=rlOspfv3InterAreaPrefixLsaPrefixOptions, rlOspfv3NetworkLsaIdx=rlOspfv3NetworkLsaIdx, rlOspfv3IntraAreaPrefixLsaEntry=rlOspfv3IntraAreaPrefixLsaEntry, rlOspfv3InterAreaPrefixLsaLsid=rlOspfv3InterAreaPrefixLsaLsid)
