#
# PySNMP MIB module TPLINK-RIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-RIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Unsigned32, Gauge32, TimeTicks, Integer32, ObjectIdentity, NotificationType, ModuleIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Unsigned32", "Gauge32", "TimeTicks", "Integer32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkRipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 40))
tplinkRipMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkRipMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkRipMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkRipMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkRipMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkRipMIB.setDescription('Private MIB for RIP configuration.')
tplinkRipMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1))
tplinkRipNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 40, 2))
tpRipBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1))
tpRipNetworkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2))
tpRipInterfaceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3))
tpRipRouteItems = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4))
tpRipProtocolCtrl = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipProtocolCtrl.setStatus('current')
if mibBuilder.loadTexts: tpRipProtocolCtrl.setDescription('Enable or disable the RIP function on the switch.')
tpRipProtocolVersion = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("default", 0), ("ripv1", 1), ("ripv2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipProtocolVersion.setStatus('current')
if mibBuilder.loadTexts: tpRipProtocolVersion.setDescription('Choose the global RIP version.')
tpRipDistance = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipDistance.setStatus('current')
if mibBuilder.loadTexts: tpRipDistance.setDescription('Set the RIP router distance.')
tpRipAutoSumm = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipAutoSumm.setStatus('current')
if mibBuilder.loadTexts: tpRipAutoSumm.setDescription('If you select enable groups of adjacent routes will be summarized into single entries.')
tpRipDefaultMetric = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipDefaultMetric.setStatus('current')
if mibBuilder.loadTexts: tpRipDefaultMetric.setDescription('Set the default metric for redistributed routes.')
tpRipRedistriStatic = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipRedistriStatic.setStatus('current')
if mibBuilder.loadTexts: tpRipRedistriStatic.setDescription('Choose to distribute Static router entries to RIP,the default is disable.')
tpRipRedistriOspf = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipRedistriOspf.setStatus('current')
if mibBuilder.loadTexts: tpRipRedistriOspf.setDescription('Choose to distribute OSPF router entries to RIP,the default is disable..')
tpRipRedistStaticMetric = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipRedistStaticMetric.setStatus('current')
if mibBuilder.loadTexts: tpRipRedistStaticMetric.setDescription('Set the metric for redistributed static routes.')
tpRipRedistOspfMetric = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipRedistOspfMetric.setStatus('current')
if mibBuilder.loadTexts: tpRipRedistOspfMetric.setDescription('Set the metric for redistributed OSPF routes.')
tpRipUpdateTimer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipUpdateTimer.setStatus('current')
if mibBuilder.loadTexts: tpRipUpdateTimer.setDescription('The timer interval to generate a complete response to every neighboring gateway.')
tpRipTimeOutTimer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipTimeOutTimer.setStatus('current')
if mibBuilder.loadTexts: tpRipTimeOutTimer.setDescription('Upon expiration of the timeout, the route is no longer valid and setted to unreachable. ')
tpRipGarbageTimer = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipGarbageTimer.setStatus('current')
if mibBuilder.loadTexts: tpRipGarbageTimer.setDescription('Upon expiration of the garbage-collection timer, the route is finally removed from the tables.')
tpRipNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1), )
if mibBuilder.loadTexts: tpRipNetworkTable.setStatus('current')
if mibBuilder.loadTexts: tpRipNetworkTable.setDescription('The list of rip network.')
tpRipNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1, 1), ).setIndexNames((0, "TPLINK-RIP-MIB", "tpRipNetworkAddress"))
if mibBuilder.loadTexts: tpRipNetworkEntry.setStatus('current')
if mibBuilder.loadTexts: tpRipNetworkEntry.setDescription('RIP network entries.')
tpRipNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpRipNetworkAddress.setStatus('current')
if mibBuilder.loadTexts: tpRipNetworkAddress.setDescription('RIP network IP address.')
tpRipNetworkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 2, 1, 1, 2), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpRipNetworkStatus.setStatus('current')
if mibBuilder.loadTexts: tpRipNetworkStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. notInService(2),destory the entry. notReady(3),destory the entry. createAndGo(4),not being used createAndWait(5),creat a new entry destroy(6),destory the entry.')
tpRipInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1), )
if mibBuilder.loadTexts: tpRipInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceTable.setDescription('The list of rip interfaces.')
tpRipInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1), ).setIndexNames((0, "TPLINK-RIP-MIB", "tpRipInterfaceID"))
if mibBuilder.loadTexts: tpRipInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceEntry.setDescription('Config the RIP parameters of the interface.')
tpRipInterfaceID = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpRipInterfaceID.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceID.setDescription('The interface IP address and subnet mask.')
tpRipInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpRipInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceStatus.setDescription('The interface RIP status(up or down).')
tpRipInterfaceSendVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ripv1", 1), ("ripv2", 2), ("rip-1c", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfaceSendVersion.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceSendVersion.setDescription('Select the version of RIP control packets sended from the interface.')
tpRipInterfaceRecvVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ripv1", 1), ("ripv2", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfaceRecvVersion.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceRecvVersion.setDescription('Select the version of RIP control packets received from the interface.')
tpRipInterfaceRIPv2Broad = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfaceRIPv2Broad.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceRIPv2Broad.setDescription('Send RIP version 2 formatted packets via broadcast.')
tpRipInterfaceAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("simple", 2), ("md5", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfaceAuthMode.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceAuthMode.setDescription('Select an authentication type.')
tpRipInterfaceKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfaceKeyID.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceKeyID.setDescription('Enter the RIP Authentication Key ID for the specified interface.')
tpRipInterfaceKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfaceKey.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceKey.setDescription('Enter the RIP Authentication Key for the specified interface. ')
tpRipInterfaceSplitHorizon = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfaceSplitHorizon.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceSplitHorizon.setDescription('Enable or disable the split horizon.')
tpRipInterfacePoisonReverse = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpRipInterfacePoisonReverse.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfacePoisonReverse.setDescription('Enable or disable the poison reverse.')
tpRipRouteTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1), )
if mibBuilder.loadTexts: tpRipRouteTable.setStatus('current')
if mibBuilder.loadTexts: tpRipRouteTable.setDescription('Display the route entries generated by RIP protocol.')
tpRipRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1), ).setIndexNames((0, "TPLINK-RIP-MIB", "tpRipIpAddressMask"))
if mibBuilder.loadTexts: tpRipRouteEntry.setStatus('current')
if mibBuilder.loadTexts: tpRipRouteEntry.setDescription('RIP route entries.')
tpRipIpAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpRipIpAddressMask.setStatus('current')
if mibBuilder.loadTexts: tpRipIpAddressMask.setDescription('The destination IP address and subnet mask.')
tpRipGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpRipGateway.setStatus('current')
if mibBuilder.loadTexts: tpRipGateway.setDescription('The gateway interface to send the data packet.')
tpRipMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpRipMetric.setStatus('current')
if mibBuilder.loadTexts: tpRipMetric.setDescription('The metric to reach the destination IP address.')
tpRipInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpRipInterfaceName.setStatus('current')
if mibBuilder.loadTexts: tpRipInterfaceName.setDescription('The gateway interface name.')
tpRipTimers = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 40, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpRipTimers.setStatus('current')
if mibBuilder.loadTexts: tpRipTimers.setDescription('The time of the route entry.')
mibBuilder.exportSymbols("TPLINK-RIP-MIB", tpRipGarbageTimer=tpRipGarbageTimer, tpRipInterfaceKeyID=tpRipInterfaceKeyID, tpRipInterfaceID=tpRipInterfaceID, tpRipTimers=tpRipTimers, tpRipTimeOutTimer=tpRipTimeOutTimer, tpRipInterfaceAuthMode=tpRipInterfaceAuthMode, tpRipRouteEntry=tpRipRouteEntry, tpRipIpAddressMask=tpRipIpAddressMask, tpRipNetworkEntry=tpRipNetworkEntry, tpRipInterfaceEntry=tpRipInterfaceEntry, tpRipInterfaceSplitHorizon=tpRipInterfaceSplitHorizon, PYSNMP_MODULE_ID=tplinkRipMIB, tpRipInterfaceRIPv2Broad=tpRipInterfaceRIPv2Broad, tpRipInterfaceName=tpRipInterfaceName, tpRipRedistOspfMetric=tpRipRedistOspfMetric, tplinkRipNotifications=tplinkRipNotifications, tplinkRipMIBObjects=tplinkRipMIBObjects, tpRipRouteTable=tpRipRouteTable, tpRipAutoSumm=tpRipAutoSumm, tpRipBasicConfig=tpRipBasicConfig, tpRipNetworkConfig=tpRipNetworkConfig, tpRipNetworkStatus=tpRipNetworkStatus, tpRipInterfaceConfig=tpRipInterfaceConfig, tpRipDistance=tpRipDistance, tpRipInterfacePoisonReverse=tpRipInterfacePoisonReverse, tpRipMetric=tpRipMetric, tpRipNetworkAddress=tpRipNetworkAddress, tpRipUpdateTimer=tpRipUpdateTimer, tpRipRouteItems=tpRipRouteItems, tpRipProtocolCtrl=tpRipProtocolCtrl, tpRipDefaultMetric=tpRipDefaultMetric, tpRipRedistriOspf=tpRipRedistriOspf, tpRipInterfaceStatus=tpRipInterfaceStatus, tpRipProtocolVersion=tpRipProtocolVersion, tpRipInterfaceKey=tpRipInterfaceKey, tpRipRedistStaticMetric=tpRipRedistStaticMetric, tpRipInterfaceRecvVersion=tpRipInterfaceRecvVersion, tpRipGateway=tpRipGateway, tplinkRipMIB=tplinkRipMIB, tpRipNetworkTable=tpRipNetworkTable, tpRipInterfaceTable=tpRipInterfaceTable, tpRipInterfaceSendVersion=tpRipInterfaceSendVersion, tpRipRedistriStatic=tpRipRedistriStatic)
