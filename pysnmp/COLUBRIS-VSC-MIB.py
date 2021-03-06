#
# PySNMP MIB module COLUBRIS-VSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-VSC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSID, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSID")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, MibIdentifier, Counter64, iso, Counter32, Bits, ModuleIdentity, Unsigned32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "iso", "Counter32", "Bits", "ModuleIdentity", "Unsigned32", "NotificationType", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
colubrisVscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 22))
if mibBuilder.loadTexts: colubrisVscMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisVscMIB.setOrganization('Colubris Networks, Inc.')
colubrisVscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1))
coVscConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1))
coVscConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1), )
if mibBuilder.loadTexts: coVscConfigTable.setStatus('current')
coVscConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-VSC-MIB", "coVscCfgIndex"))
if mibBuilder.loadTexts: coVscConfigEntry.setStatus('current')
coVscCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coVscCfgIndex.setStatus('current')
coVscCfgFriendlyVscName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgFriendlyVscName.setStatus('current')
coVscCfgSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 3), ColubrisSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSSID.setStatus('current')
coVscCfgAccessControlled = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgAccessControlled.setStatus('current')
coVscCfgSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("ieee802dot1x", 2), ("wpa", 3), ("wpa2", 4), ("wpaAndWpa2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSecurity.setStatus('current')
coVscCfgEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4), ("tkipAndAes", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgEncryption.setStatus('current')
coVscCfg8021xAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("radius", 2), ("psk", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfg8021xAuthentication.setStatus('current')
coVscCfgMACAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgMACAuthentication.setStatus('current')
coVscCfgHTMLAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 22, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgHTMLAuthentication.setStatus('current')
colubrisVscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2))
colubrisVscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 1))
colubrisVscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 2))
colubrisVscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 1, 1)).setObjects(("COLUBRIS-VSC-MIB", "colubrisVscMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVscMIBCompliance = colubrisVscMIBCompliance.setStatus('current')
colubrisVscMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 22, 2, 2, 1)).setObjects(("COLUBRIS-VSC-MIB", "coVscCfgFriendlyVscName"), ("COLUBRIS-VSC-MIB", "coVscCfgSSID"), ("COLUBRIS-VSC-MIB", "coVscCfgAccessControlled"), ("COLUBRIS-VSC-MIB", "coVscCfgSecurity"), ("COLUBRIS-VSC-MIB", "coVscCfgEncryption"), ("COLUBRIS-VSC-MIB", "coVscCfg8021xAuthentication"), ("COLUBRIS-VSC-MIB", "coVscCfgMACAuthentication"), ("COLUBRIS-VSC-MIB", "coVscCfgHTMLAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisVscMIBGroup = colubrisVscMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-VSC-MIB", coVscCfgHTMLAuthentication=coVscCfgHTMLAuthentication, coVscConfigTable=coVscConfigTable, colubrisVscMIBGroups=colubrisVscMIBGroups, coVscCfgEncryption=coVscCfgEncryption, coVscCfgFriendlyVscName=coVscCfgFriendlyVscName, colubrisVscMIB=colubrisVscMIB, coVscConfigEntry=coVscConfigEntry, colubrisVscMIBObjects=colubrisVscMIBObjects, colubrisVscMIBCompliance=colubrisVscMIBCompliance, coVscCfgSSID=coVscCfgSSID, coVscCfg8021xAuthentication=coVscCfg8021xAuthentication, coVscConfigGroup=coVscConfigGroup, PYSNMP_MODULE_ID=colubrisVscMIB, colubrisVscMIBConformance=colubrisVscMIBConformance, coVscCfgIndex=coVscCfgIndex, coVscCfgSecurity=coVscCfgSecurity, colubrisVscMIBCompliances=colubrisVscMIBCompliances, colubrisVscMIBGroup=colubrisVscMIBGroup, coVscCfgAccessControlled=coVscCfgAccessControlled, coVscCfgMACAuthentication=coVscCfgMACAuthentication)
