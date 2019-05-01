#
# PySNMP MIB module MITEL-ROUTERGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-ROUTERGROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, iso, IpAddress, Bits, enterprises, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Integer32, Counter64, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "iso", "IpAddress", "Bits", "enterprises", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Integer32", "Counter64", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
mitelRouterIpRouterGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5))
mitelRouterIpRouterGroup.setRevisions(('2003-03-24 10:45', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelRouterIpRouterGroup.setRevisionsDescriptions(('Convert to SMIv2', 'Router Table MIB Version 1.0',))
if mibBuilder.loadTexts: mitelRouterIpRouterGroup.setLastUpdated('200303241045Z')
if mibBuilder.loadTexts: mitelRouterIpRouterGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelRouterIpRouterGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelRouterIpRouterGroup.setDescription('The MITEL Router MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1), )
if mibBuilder.loadTexts: mitelIpRouteTable.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTable.setDescription('This table is a list of IP Routing Entries.')
mitelIpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1), ).setIndexNames((0, "MITEL-ROUTERGROUP-MIB", "mitelIpRouteTblDestAddress"), (0, "MITEL-ROUTERGROUP-MIB", "mitelIpRouteTblGateAddress"))
if mibBuilder.loadTexts: mitelIpRouteEntry.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteEntry.setDescription('Each entry in this table contains information of an IP Route Entry.')
mitelIpRouteTblDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblDestAddress.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblDestAddress.setDescription('The IP address of the destination network')
mitelIpRouteTblGateAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblGateAddress.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblGateAddress.setDescription('The Destination Gateway IP address. ')
mitelIpRouteTblNetmaskAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblNetmaskAddress.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblNetmaskAddress.setDescription('Specifies the netmask to apply to this network. ')
mitelIpRouteTblIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblIfIndex.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblIfIndex.setDescription('Specifies the IfIndex to use as a key into the table. 0 & 1 are not used ')
mitelIpRouteTblMetric1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric1.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblMetric1.setDescription('Metric 1')
mitelIpRouteTblMetric2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric2.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblMetric2.setDescription('Metric 2')
mitelIpRouteTblMetric3 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric3.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblMetric3.setDescription('Metric 3')
mitelIpRouteTblMetric4 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric4.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblMetric4.setDescription('Metric 4')
mitelIpRouteTblMetric5 = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblMetric5.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblMetric5.setDescription('Metric 5')
mitelIpRouteTblRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblRouteType.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblRouteType.setDescription('Specifies what kind of route this is.')
mitelIpRouteTblRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblRouteProto.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblRouteProto.setDescription('Specifies what protocol to use for the routing table entry.')
mitelIpRouteTblRouteAge = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblRouteAge.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblRouteAge.setDescription('Specifies the age of the route entry in the table.')
mitelIpRouteTblBlockLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblBlockLearning.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblBlockLearning.setDescription('If enabled will block the learned route in question')
mitelIpRouteTblInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblInUse.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblInUse.setDescription('Specifies whether this routing entry is in use or not')
mitelIpRouteTblDisableLearned = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblDisableLearned.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblDisableLearned.setDescription('Determines whether learned routes should be disabled or not')
mitelIpRouteTblConvertStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpRouteTblConvertStatic.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblConvertStatic.setDescription('An action to convert a learned route into a static route.')
mitelIpRouteTblRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelIpRouteTblRowStatus.setStatus('current')
if mibBuilder.loadTexts: mitelIpRouteTblRowStatus.setDescription('The current status of this entry. ')
mibBuilder.exportSymbols("MITEL-ROUTERGROUP-MIB", mitelIpRouteTblNetmaskAddress=mitelIpRouteTblNetmaskAddress, mitelIpRouteTable=mitelIpRouteTable, mitelIpRouteTblMetric1=mitelIpRouteTblMetric1, mitelIpRouteEntry=mitelIpRouteEntry, mitelIpRouteTblConvertStatic=mitelIpRouteTblConvertStatic, mitelIpRouteTblRouteProto=mitelIpRouteTblRouteProto, mitelIpRouteTblMetric4=mitelIpRouteTblMetric4, mitelIpRouteTblGateAddress=mitelIpRouteTblGateAddress, mitelIpRouteTblRouteAge=mitelIpRouteTblRouteAge, mitelIpRouteTblMetric2=mitelIpRouteTblMetric2, mitelProprietary=mitelProprietary, mitelIpRouteTblRouteType=mitelIpRouteTblRouteType, PYSNMP_MODULE_ID=mitelRouterIpRouterGroup, mitelIpNetRouter=mitelIpNetRouter, mitelIpRouteTblDestAddress=mitelIpRouteTblDestAddress, mitelIpRouteTblIfIndex=mitelIpRouteTblIfIndex, mitelIpRouteTblInUse=mitelIpRouteTblInUse, mitelPropIpNetworking=mitelPropIpNetworking, mitelIpRouteTblMetric3=mitelIpRouteTblMetric3, mitel=mitel, mitelIpRouteTblDisableLearned=mitelIpRouteTblDisableLearned, mitelRouterIpRouterGroup=mitelRouterIpRouterGroup, mitelIpRouteTblBlockLearning=mitelIpRouteTblBlockLearning, mitelIpRouteTblRowStatus=mitelIpRouteTblRowStatus, mitelIpRouteTblMetric5=mitelIpRouteTblMetric5)
