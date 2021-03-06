#
# PySNMP MIB module VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
preDot1qVlanMIB, = mibBuilder.importSymbols("Fore-Common-MIB", "preDot1qVlanMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, ModuleIdentity, Unsigned32, Gauge32, Counter32, NotificationType, iso, MibIdentifier, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "ModuleIdentity", "Unsigned32", "Gauge32", "Counter32", "NotificationType", "iso", "MibIdentifier", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress")
TestAndIncr, TextualConvention, MacAddress, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "TextualConvention", "MacAddress", "RowStatus", "DisplayString")
vlanMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 8, 1))
if mibBuilder.loadTexts: vlanMIBObjects.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: vlanMIBObjects.setOrganization('FORE')
vlanConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1))
vlanConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1), )
if mibBuilder.loadTexts: vlanConfTable.setStatus('current')
vlanConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1), ).setIndexNames((0, "VLAN-MIB", "vlanName"))
if mibBuilder.loadTexts: vlanConfEntry.setStatus('current')
vlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanName.setStatus('current')
vlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanID.setStatus('current')
vlanConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanConfRowStatus.setStatus('current')
vlanCreatedBy = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanCreatedBy.setStatus('current')
vlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 5), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanType.setStatus('current')
vlanPortGroupInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanPortGroupInstance.setStatus('current')
vlanMacListInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanMacListInstance.setStatus('current')
vlanProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ethernetv2", 2), ("ieee802dot3", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanProtocolType.setStatus('current')
vlanProtocolSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanProtocolSubtype.setStatus('current')
vlanIPSubnetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanIPSubnetAddress.setStatus('current')
vlanBridgeName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanBridgeName.setStatus('current')
vlanIPMulticastFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanIPMulticastFilter.setStatus('current')
vlanPortGroupTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2), )
if mibBuilder.loadTexts: vlanPortGroupTable.setStatus('current')
vlanPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1), ).setIndexNames((0, "VLAN-MIB", "vlanPortGroupIndex"), (0, "VLAN-MIB", "vlanPort"))
if mibBuilder.loadTexts: vlanPortGroupEntry.setStatus('current')
vlanPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: vlanPortGroupIndex.setStatus('current')
vlanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: vlanPort.setStatus('current')
vlanPortGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanPortGroupRowStatus.setStatus('current')
vlanPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("autoActive", 1), ("allowed", 2), ("allowedActive", 3), ("allowedNotAvail", 4), ("notAssociated", 5))).clone('allowed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortStatus.setStatus('current')
vlanPortGroupNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPortGroupNextIndex.setStatus('current')
vlanMacListTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4), )
if mibBuilder.loadTexts: vlanMacListTable.setStatus('current')
vlanMacListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1), ).setIndexNames((0, "VLAN-MIB", "vlanMacListIndex"), (0, "VLAN-MIB", "vlanMacAddress"))
if mibBuilder.loadTexts: vlanMacListEntry.setStatus('current')
vlanMacListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanMacListNextIndex.setStatus('current')
vlanMacListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: vlanMacListIndex.setStatus('current')
vlanMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: vlanMacAddress.setStatus('current')
vlanMacListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanMacListRowStatus.setStatus('current')
mibBuilder.exportSymbols("VLAN-MIB", vlanPortGroupNextIndex=vlanPortGroupNextIndex, vlanProtocolSubtype=vlanProtocolSubtype, vlanName=vlanName, vlanPortGroupEntry=vlanPortGroupEntry, vlanMacListTable=vlanMacListTable, vlanMacListInstance=vlanMacListInstance, vlanPortGroupIndex=vlanPortGroupIndex, vlanPort=vlanPort, vlanID=vlanID, vlanConfEntry=vlanConfEntry, vlanPortGroupInstance=vlanPortGroupInstance, PYSNMP_MODULE_ID=vlanMIBObjects, vlanIPMulticastFilter=vlanIPMulticastFilter, vlanConfTable=vlanConfTable, vlanConfRowStatus=vlanConfRowStatus, vlanProtocolType=vlanProtocolType, vlanIPSubnetAddress=vlanIPSubnetAddress, vlanPortGroupTable=vlanPortGroupTable, vlanBridgeName=vlanBridgeName, vlanMIBObjects=vlanMIBObjects, vlanMacListEntry=vlanMacListEntry, vlanCreatedBy=vlanCreatedBy, vlanConfGroup=vlanConfGroup, vlanType=vlanType, vlanMacListNextIndex=vlanMacListNextIndex, vlanMacListIndex=vlanMacListIndex, vlanMacListRowStatus=vlanMacListRowStatus, vlanPortStatus=vlanPortStatus, vlanPortGroupRowStatus=vlanPortGroupRowStatus, vlanMacAddress=vlanMacAddress)
