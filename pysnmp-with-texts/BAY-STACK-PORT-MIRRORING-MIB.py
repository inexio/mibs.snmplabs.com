#
# PySNMP MIB module BAY-STACK-PORT-MIRRORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-PORT-MIRRORING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, IpAddress, ObjectIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Gauge32, Unsigned32, ModuleIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "IpAddress", "ObjectIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Gauge32", "Unsigned32", "ModuleIdentity", "Bits", "TimeTicks")
TextualConvention, MacAddress, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "RowStatus", "TruthValue")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackPortMirroringMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 28))
bayStackPortMirroringMib.setRevisions(('2012-10-10 00:00', '2009-05-28 00:00', '2008-01-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackPortMirroringMib.setRevisionsDescriptions(('v3: Added support for RSPAN settings: Added bsPortMirroringCtrlRspanVlan object. Added bsPortMirroringRspanTable table.', "v2: Added support for 'allow-traffic'", 'v1: Initial version.',))
if mibBuilder.loadTexts: bayStackPortMirroringMib.setLastUpdated('201210100000Z')
if mibBuilder.loadTexts: bayStackPortMirroringMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: bayStackPortMirroringMib.setContactInfo('Nortel Networks')
if mibBuilder.loadTexts: bayStackPortMirroringMib.setDescription("Nortel Networks Port Mirroring MIB Copyright 2008 Nortel Networks, Inc. All rights reserved. This Nortel Networks SNMP Management Information Base Specification embodies Nortel Networks' confidential and proprietary intellectual property. Nortel Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
bsPortMirroringNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 28, 0))
bsPortMirroringObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 28, 1))
bsPortMirroringCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1), )
if mibBuilder.loadTexts: bsPortMirroringCtrlTable.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlTable.setDescription('A table containing port mirroring control information about every instance.')
bsPortMirroringCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-PORT-MIRRORING-MIB", "bsPortMirroringCtrlInstance"))
if mibBuilder.loadTexts: bsPortMirroringCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlEntry.setDescription('A list of port miroring control information for an instance.')
bsPortMirroringCtrlInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: bsPortMirroringCtrlInstance.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlInstance.setDescription('The port mirroring instance number')
bsPortMirroringCtrlPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("disable", 1), ("adst", 2), ("asrc", 3), ("asrcBdst", 4), ("asrcBdstOrBsrcAdst", 5), ("asrcOrAdst", 6), ("manytoOneRx", 7), ("manytoOneRxTx", 8), ("manytoOneTx", 9), ("xrx", 10), ("xrxOrXtx", 11), ("xrxOrYtx", 12), ("xrxYtx", 13), ("xrxYtxOrYrxXtx", 14), ("xtx", 15)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlPortMode.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlPortMode.setDescription('These are the supported port mirroring modes: disable(1) - Disable port mirroring Adst(2) - Mirror packets with destination MAC address A Asrc(3) - Mirror packets with source MAC address A AsrcBdst(4) - Mirror packets with source MAC address A and destination MAC address B AsrcBdstOrBsrcAdst(5) - Mirror packets with source MAC address A and destination MAC address B, or packets with source MAC address B and destination MAC address A AsrcOrAdst(6) - Mirror packets with source or destination MAC address A ManytoOneRx(7) - Many to one port mirroring ingress traffic ManytoOneRxTx(8) - Many to one port mirroring ingress & egress traffic ManytoOneTx(9) - Many to one port mirroring egress traffic Xrx(10) - Mirror packets received on port X XrxOrXtx(11) - Mirror packets received or transmitted on port X XrxOrYtx(12) - Mirror packets received on port X or transmitted on port Y XrxYtx(13) - Mirror packets received on port X and transmitted on port Y XrxYtxOrYrxXtx(14) - Mirror packets received on port X and transmitted on port Y, or packets received on port Y and transmitted on port X Xtx(15) - Mirror packets transmitted on port X')
bsPortMirroringCtrlMonitorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlMonitorPort.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlMonitorPort.setDescription('The monitor port')
bsPortMirroringCtrlPortListX = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 4), PortList().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlPortListX.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlPortListX.setDescription('The port list X')
bsPortMirroringCtrlPortListY = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 5), PortList().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlPortListY.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlPortListY.setDescription('The port list Y')
bsPortMirroringCtrlMacAddressA = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 6), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlMacAddressA.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlMacAddressA.setDescription('The MAC address A')
bsPortMirroringCtrlMacAddressB = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlMacAddressB.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlMacAddressB.setDescription('The MAC address B')
bsPortMirroringCtrlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlRowStatus.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlRowStatus.setDescription('Used to create/delete entries in the bsPortMirroringCtrlTable.')
bsPortMirroringCtrlAllowTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlAllowTraffic.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlAllowTraffic.setDescription('Allow port to participate in normal frame switching.')
bsPortMirroringCtrlRspanVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 4094), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringCtrlRspanVlan.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringCtrlRspanVlan.setDescription('The VLAN of the RSPAN source session which is associated to a standard port mirroring session on the source device. A value of 0 means RSPAN vlan is not specified.')
bsPortMirroringRspanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2), )
if mibBuilder.loadTexts: bsPortMirroringRspanTable.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringRspanTable.setDescription('A table containing port mirroring RSPAN settings of every instance.')
bsPortMirroringRspanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-PORT-MIRRORING-MIB", "bsPortMirroringRspanInstance"))
if mibBuilder.loadTexts: bsPortMirroringRspanEntry.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringRspanEntry.setDescription('A list of port miroring RSPAN settings for an instance.')
bsPortMirroringRspanInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: bsPortMirroringRspanInstance.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringRspanInstance.setDescription('The RSPAN instance number')
bsPortMirroringRspanMtp = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringRspanMtp.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringRspanMtp.setDescription('The RSPAN destination port')
bsPortMirroringRspanVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringRspanVlan.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringRspanVlan.setDescription('The VLAN of a RSPAN destination session configured on the destination device')
bsPortMirroringRspanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsPortMirroringRspanRowStatus.setStatus('current')
if mibBuilder.loadTexts: bsPortMirroringRspanRowStatus.setDescription('Used to create/delete entries in the bsPortMirroringRspanTable.')
mibBuilder.exportSymbols("BAY-STACK-PORT-MIRRORING-MIB", bayStackPortMirroringMib=bayStackPortMirroringMib, PYSNMP_MODULE_ID=bayStackPortMirroringMib, bsPortMirroringObjects=bsPortMirroringObjects, bsPortMirroringCtrlAllowTraffic=bsPortMirroringCtrlAllowTraffic, bsPortMirroringCtrlMonitorPort=bsPortMirroringCtrlMonitorPort, bsPortMirroringCtrlMacAddressA=bsPortMirroringCtrlMacAddressA, bsPortMirroringCtrlRowStatus=bsPortMirroringCtrlRowStatus, bsPortMirroringRspanEntry=bsPortMirroringRspanEntry, bsPortMirroringRspanInstance=bsPortMirroringRspanInstance, bsPortMirroringNotifications=bsPortMirroringNotifications, bsPortMirroringRspanRowStatus=bsPortMirroringRspanRowStatus, bsPortMirroringCtrlTable=bsPortMirroringCtrlTable, bsPortMirroringCtrlPortMode=bsPortMirroringCtrlPortMode, bsPortMirroringCtrlMacAddressB=bsPortMirroringCtrlMacAddressB, bsPortMirroringCtrlEntry=bsPortMirroringCtrlEntry, bsPortMirroringCtrlPortListX=bsPortMirroringCtrlPortListX, bsPortMirroringCtrlRspanVlan=bsPortMirroringCtrlRspanVlan, bsPortMirroringRspanTable=bsPortMirroringRspanTable, bsPortMirroringRspanMtp=bsPortMirroringRspanMtp, bsPortMirroringCtrlPortListY=bsPortMirroringCtrlPortListY, bsPortMirroringRspanVlan=bsPortMirroringRspanVlan, bsPortMirroringCtrlInstance=bsPortMirroringCtrlInstance)
