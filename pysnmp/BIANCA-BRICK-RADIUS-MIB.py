#
# PySNMP MIB module BIANCA-BRICK-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-RADIUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Integer32, iso, NotificationType, ObjectIdentity, Counter64, Unsigned32, IpAddress, TimeTicks, MibIdentifier, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "iso", "NotificationType", "ObjectIdentity", "Counter64", "Unsigned32", "IpAddress", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bintecsec = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 254))
radius = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 254, 8))
radiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 272, 254, 8, 1), )
if mibBuilder.loadTexts: radiusServerTable.setStatus('mandatory')
radiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-RADIUS-MIB", "radiusSrvProtocol"))
if mibBuilder.loadTexts: radiusServerEntry.setStatus('mandatory')
radiusSrvProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authentication", 1), ("accounting", 2), ("login", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvProtocol.setStatus('mandatory')
radiusSrvAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvAddress.setStatus('mandatory')
radiusSrvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvPort.setStatus('mandatory')
radiusSrvSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvSecret.setStatus('mandatory')
radiusSrvPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvPriority.setStatus('mandatory')
radiusSrvTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 50000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvTimeout.setStatus('mandatory')
radiusSrvRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvRetries.setStatus('mandatory')
radiusSrvState = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("disabled", 3), ("delete", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvState.setStatus('mandatory')
radiusSrvPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authoritative", 1), ("non-authoritative", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvPolicy.setStatus('mandatory')
radiusSrvValidate = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvValidate.setStatus('mandatory')
radiusSrvDialout = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("reload", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvDialout.setStatus('mandatory')
radiusSrvDefaultPW = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvDefaultPW.setStatus('mandatory')
radiusSrvReloadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvReloadInterval.setStatus('mandatory')
radiusSrvAuthRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAuthRequests.setStatus('mandatory')
radiusSrvAuthAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAuthAccepts.setStatus('mandatory')
radiusSrvAuthRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAuthRejects.setStatus('mandatory')
radiusSrvAuthReqRetrans = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAuthReqRetrans.setStatus('mandatory')
radiusSrvAuthReqFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAuthReqFailed.setStatus('mandatory')
radiusSrvAuthReqPending = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAuthReqPending.setStatus('mandatory')
radiusSrvAcctStarts = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAcctStarts.setStatus('mandatory')
radiusSrvAcctStops = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusSrvAcctStops.setStatus('mandatory')
radiusSrvKeepalive = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 254, 8, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: radiusSrvKeepalive.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-RADIUS-MIB", radiusSrvAuthRequests=radiusSrvAuthRequests, bintecsec=bintecsec, radiusSrvAcctStarts=radiusSrvAcctStarts, radiusSrvAuthReqRetrans=radiusSrvAuthReqRetrans, radiusSrvReloadInterval=radiusSrvReloadInterval, radiusSrvSecret=radiusSrvSecret, radiusSrvAddress=radiusSrvAddress, radiusSrvDialout=radiusSrvDialout, bintec=bintec, radiusSrvAuthAccepts=radiusSrvAuthAccepts, radius=radius, radiusServerTable=radiusServerTable, radiusSrvValidate=radiusSrvValidate, radiusSrvDefaultPW=radiusSrvDefaultPW, private=private, radiusSrvPolicy=radiusSrvPolicy, radiusSrvRetries=radiusSrvRetries, radiusSrvState=radiusSrvState, dod=dod, radiusSrvProtocol=radiusSrvProtocol, radiusServerEntry=radiusServerEntry, radiusSrvTimeout=radiusSrvTimeout, radiusSrvAcctStops=radiusSrvAcctStops, radiusSrvAuthReqFailed=radiusSrvAuthReqFailed, enterprises=enterprises, radiusSrvAuthReqPending=radiusSrvAuthReqPending, internet=internet, radiusSrvAuthRejects=radiusSrvAuthRejects, radiusSrvKeepalive=radiusSrvKeepalive, org=org, radiusSrvPort=radiusSrvPort, radiusSrvPriority=radiusSrvPriority)
