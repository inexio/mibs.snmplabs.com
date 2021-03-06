#
# PySNMP MIB module ZHONE-IUA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-IUA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
applIndex, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Counter64, Unsigned32, ObjectIdentity, Integer32, Gauge32, NotificationType, MibIdentifier, ModuleIdentity, iso, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter64", "Unsigned32", "ObjectIdentity", "Integer32", "Gauge32", "NotificationType", "MibIdentifier", "ModuleIdentity", "iso", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneIua, = mibBuilder.importSymbols("Zhone", "zhoneIua")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
zhoneIuaModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1))
zhoneIuaModule.setRevisions(('2009-05-25 23:16',))
if mibBuilder.loadTexts: zhoneIuaModule.setLastUpdated('200905270656Z')
if mibBuilder.loadTexts: zhoneIuaModule.setOrganization('Zhone Technologies.')
zhoneIuaServerCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1))
zhoneIuaServerTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1), )
if mibBuilder.loadTexts: zhoneIuaServerTable.setStatus('current')
zhoneIuaServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ZHONE-IUA-MIB", "zhoneIuaServerAddressIndex"))
if mibBuilder.loadTexts: zhoneIuaServerEntry.setStatus('current')
zhoneIuaServerAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: zhoneIuaServerAddressIndex.setStatus('current')
zhoneIuaServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 2), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIuaServerRowStatus.setStatus('current')
zhoneIuaServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIuaServerAddress.setStatus('current')
zhoneIuaServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(9900)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIuaServerPortNumber.setStatus('current')
mibBuilder.exportSymbols("ZHONE-IUA-MIB", zhoneIuaServerCfg=zhoneIuaServerCfg, zhoneIuaServerPortNumber=zhoneIuaServerPortNumber, zhoneIuaServerTable=zhoneIuaServerTable, zhoneIuaModule=zhoneIuaModule, zhoneIuaServerAddress=zhoneIuaServerAddress, zhoneIuaServerRowStatus=zhoneIuaServerRowStatus, zhoneIuaServerAddressIndex=zhoneIuaServerAddressIndex, PYSNMP_MODULE_ID=zhoneIuaModule, zhoneIuaServerEntry=zhoneIuaServerEntry)
