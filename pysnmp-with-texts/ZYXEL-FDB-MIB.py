#
# PySNMP MIB module ZYXEL-FDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-FDB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:49:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, ObjectIdentity, NotificationType, MibIdentifier, IpAddress, Integer32, Gauge32, Unsigned32, iso, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibIdentifier", "IpAddress", "Integer32", "Gauge32", "Unsigned32", "iso", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelFdb = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48))
if mibBuilder.loadTexts: zyxelFdb.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelFdb.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelFdb.setContactInfo('')
if mibBuilder.loadTexts: zyxelFdb.setDescription('The subtree for forwarding and/or filtering database')
zyxelMacStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1))
zyxelMacStatusNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2))
zyMacFlush = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFlush.setStatus('current')
if mibBuilder.loadTexts: zyMacFlush.setDescription('Active to clear the MAC address table.')
zyMacFlushPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFlushPort.setStatus('current')
if mibBuilder.loadTexts: zyMacFlushPort.setDescription('Clear all learned MAC address on the specified port.')
zyMacFlushVlan = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFlushVlan.setStatus('current')
if mibBuilder.loadTexts: zyMacFlushVlan.setDescription('Clear all learned MAC address on the specified VLAN.')
zyMacForwardingTableFull = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 1))
if mibBuilder.loadTexts: zyMacForwardingTableFull.setStatus('current')
if mibBuilder.loadTexts: zyMacForwardingTableFull.setDescription('MAC address switching table has become full.')
zyMacForwardingTableFullRecovered = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 48, 2, 2))
if mibBuilder.loadTexts: zyMacForwardingTableFullRecovered.setStatus('current')
if mibBuilder.loadTexts: zyMacForwardingTableFullRecovered.setDescription('MAC address switching table has recovered from full.')
mibBuilder.exportSymbols("ZYXEL-FDB-MIB", zyMacFlushVlan=zyMacFlushVlan, zyMacForwardingTableFullRecovered=zyMacForwardingTableFullRecovered, PYSNMP_MODULE_ID=zyxelFdb, zyxelMacStatus=zyxelMacStatus, zyMacFlush=zyMacFlush, zyxelMacStatusNotifications=zyxelMacStatusNotifications, zyMacForwardingTableFull=zyMacForwardingTableFull, zyxelFdb=zyxelFdb, zyMacFlushPort=zyMacFlushPort)
