#
# PySNMP MIB module HH3C-WEB-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-WEB-AUTHENTICATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:17:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifDescr, = mibBuilder.importSymbols("IF-MIB", "ifDescr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, MibIdentifier, Bits, iso, NotificationType, ObjectIdentity, Counter32, Unsigned32, ModuleIdentity, Gauge32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "MibIdentifier", "Bits", "iso", "NotificationType", "ObjectIdentity", "Counter32", "Unsigned32", "ModuleIdentity", "Gauge32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
hh3cWebAuthentication = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 93))
hh3cWebAuthentication.setRevisions(('2008-06-25 00:00',))
if mibBuilder.loadTexts: hh3cWebAuthentication.setLastUpdated('200806250000Z')
if mibBuilder.loadTexts: hh3cWebAuthentication.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cWaTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 93, 1))
hh3cWaVlanID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cWaVlanID.setStatus('current')
hh3cWaReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("globalNumberMax", 1), ("configNumberMax", 2), ("portNumberMax", 3), ("invalidUsername", 4), ("authFail", 5), ("setACLFail", 6), ("changeVlanFail", 7), ("other", 8), ("onlineOverTime", 9), ("noTransferData", 10), ("cutOperation", 11), ("portDisabled", 12), ("portDown", 13), ("userLogout", 14), ("vlanChanged", 15), ("vlanDelted", 16)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cWaReasonCode.setStatus('current')
hh3cWaActionCode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cWaActionCode.setStatus('current')
hh3cWaClientMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 93, 1, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cWaClientMacAddr.setStatus('current')
hh3cWaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 93, 2))
hh3cWaTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0))
hh3cWaClientLogon = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 1)).setObjects(("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaClientMacAddr"), ("IF-MIB", "ifDescr"), ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaVlanID"))
if mibBuilder.loadTexts: hh3cWaClientLogon.setStatus('current')
hh3cWaClientLogonFail = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 2)).setObjects(("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaClientMacAddr"), ("IF-MIB", "ifDescr"), ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaVlanID"), ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaReasonCode"))
if mibBuilder.loadTexts: hh3cWaClientLogonFail.setStatus('current')
hh3cWaClientLogout = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 3)).setObjects(("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaClientMacAddr"), ("IF-MIB", "ifDescr"), ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaVlanID"), ("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaReasonCode"))
if mibBuilder.loadTexts: hh3cWaClientLogout.setStatus('current')
hh3cWaSysAction = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 93, 2, 0, 4)).setObjects(("HH3C-WEB-AUTHENTICATION-MIB", "hh3cWaActionCode"))
if mibBuilder.loadTexts: hh3cWaSysAction.setStatus('current')
mibBuilder.exportSymbols("HH3C-WEB-AUTHENTICATION-MIB", hh3cWaTrapPrefix=hh3cWaTrapPrefix, hh3cWaVlanID=hh3cWaVlanID, hh3cWaActionCode=hh3cWaActionCode, hh3cWaClientMacAddr=hh3cWaClientMacAddr, hh3cWebAuthentication=hh3cWebAuthentication, hh3cWaReasonCode=hh3cWaReasonCode, hh3cWaSysAction=hh3cWaSysAction, PYSNMP_MODULE_ID=hh3cWebAuthentication, hh3cWaTrap=hh3cWaTrap, hh3cWaTrapObjects=hh3cWaTrapObjects, hh3cWaClientLogout=hh3cWaClientLogout, hh3cWaClientLogonFail=hh3cWaClientLogonFail, hh3cWaClientLogon=hh3cWaClientLogon)
