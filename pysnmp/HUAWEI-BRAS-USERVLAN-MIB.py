#
# PySNMP MIB module HUAWEI-BRAS-USERVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-USERVLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
VlanId, VlanIdOrNone = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "VlanIdOrNone")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, Bits, ModuleIdentity, Counter64, Integer32, TimeTicks, Gauge32, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "Bits", "ModuleIdentity", "Counter64", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwUSERVLAN = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12))
if mibBuilder.loadTexts: hwUSERVLAN.setLastUpdated('200508101200Z')
if mibBuilder.loadTexts: hwUSERVLAN.setOrganization('Huawei Technologies Co., Ltd. ')
hwhwUSERVLANMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1))
hwUserVlanTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1))
hwUserVlanIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserVlanIfIndex.setStatus('current')
hwUserInnerStartVlan = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserInnerStartVlan.setStatus('current')
hwUserInnerEndVlan = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 3), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserInnerEndVlan.setStatus('current')
hwUserVlanOuterVlan = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserVlanOuterVlan.setStatus('current')
hwUserVlanOpType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("set", 1), ("undo", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserVlanOpType.setStatus('current')
hwQueryUserVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2), )
if mibBuilder.loadTexts: hwQueryUserVlanTable.setStatus('current')
hwQueryUserVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1), ).setIndexNames((0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanIfIndex"), (0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserInnerVlan"), (0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserOuterVlan"))
if mibBuilder.loadTexts: hwQueryUserVlanEntry.setStatus('current')
hwQueryUserVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryUserVlanIfIndex.setStatus('current')
hwQueryUserInnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 2), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryUserInnerVlan.setStatus('current')
hwQueryUserOuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 3), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryUserOuterVlan.setStatus('current')
hwUserVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2))
hwUserVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1))
hwUserVlanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 1)).setObjects(("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanTableGroup"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserVlanCompliance = hwUserVlanCompliance.setStatus('current')
hwUserVlanObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2))
hwUserVlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2, 1)).setObjects(("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanIfIndex"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserInnerStartVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserInnerEndVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanOuterVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanOpType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserVlanTableGroup = hwUserVlanTableGroup.setStatus('current')
hwQueryUserVlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2, 2)).setObjects(("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanIfIndex"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserInnerVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserOuterVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwQueryUserVlanTableGroup = hwQueryUserVlanTableGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BRAS-USERVLAN-MIB", hwUSERVLAN=hwUSERVLAN, hwUserInnerStartVlan=hwUserInnerStartVlan, hwQueryUserVlanTable=hwQueryUserVlanTable, hwhwUSERVLANMibObjects=hwhwUSERVLANMibObjects, hwQueryUserInnerVlan=hwQueryUserInnerVlan, hwUserInnerEndVlan=hwUserInnerEndVlan, hwQueryUserVlanEntry=hwQueryUserVlanEntry, hwQueryUserVlanTableGroup=hwQueryUserVlanTableGroup, hwUserVlanTable=hwUserVlanTable, hwUserVlanCompliances=hwUserVlanCompliances, hwUserVlanTableGroup=hwUserVlanTableGroup, hwUserVlanOuterVlan=hwUserVlanOuterVlan, hwUserVlanConformance=hwUserVlanConformance, hwQueryUserOuterVlan=hwQueryUserOuterVlan, hwUserVlanIfIndex=hwUserVlanIfIndex, PYSNMP_MODULE_ID=hwUSERVLAN, hwUserVlanOpType=hwUserVlanOpType, hwUserVlanCompliance=hwUserVlanCompliance, hwQueryUserVlanIfIndex=hwQueryUserVlanIfIndex, hwUserVlanObjectGroups=hwUserVlanObjectGroups)
