#
# PySNMP MIB module WAN-RESTORAL-REROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WAN-RESTORAL-REROUTE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, enterprises, Gauge32, NotificationType, TimeTicks, Bits, Unsigned32, Counter32, Integer32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Gauge32", "NotificationType", "TimeTicks", "Bits", "Unsigned32", "Counter32", "Integer32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibmWanRestoralRerouteMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11))
ibmWanRestoral = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1))
ibmWanReroute = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2))
ibmWanRestoralTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1), )
if mibBuilder.loadTexts: ibmWanRestoralTable.setStatus('mandatory')
ibmWanRestoralEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1), ).setIndexNames((0, "WAN-RESTORAL-REROUTE-MIB", "ibmwrsPriNetifIndex"))
if mibBuilder.loadTexts: ibmWanRestoralEntry.setStatus('mandatory')
ibmwrsPriNetifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsPriNetifIndex.setStatus('mandatory')
ibmwrsSecNetifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsSecNetifIndex.setStatus('mandatory')
ibmwrsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsEnabled.setStatus('mandatory')
ibmwrsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsActive.setStatus('mandatory')
ibmwrsDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsDuration.setStatus('mandatory')
ibmwrsAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsAttempts.setStatus('mandatory')
ibmwrsActuals = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsActuals.setStatus('mandatory')
ibmwrsFwdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrsFwdPkts.setStatus('mandatory')
ibmWanRerouteTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1), )
if mibBuilder.loadTexts: ibmWanRerouteTable.setStatus('mandatory')
ibmWanRerouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1), ).setIndexNames((0, "WAN-RESTORAL-REROUTE-MIB", "ibmwrrPriNetifIndex"))
if mibBuilder.loadTexts: ibmWanRerouteEntry.setStatus('mandatory')
ibmwrrPriNetifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrPriNetifIndex.setStatus('mandatory')
ibmwrrAltNetifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrAltNetifIndex.setStatus('mandatory')
ibmwrrEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrEnabled.setStatus('mandatory')
ibmwrrActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrActive.setStatus('mandatory')
ibmwrrDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrDuration.setStatus('mandatory')
ibmwrrAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrAttempts.setStatus('mandatory')
ibmwrrActuals = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrActuals.setStatus('mandatory')
ibmwrrOverflowEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrOverflowEnabled.setStatus('mandatory')
ibmwrrOverflowActive = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrOverflowActive.setStatus('mandatory')
ibmwrrOverflowDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrOverflowDuration.setStatus('mandatory')
ibmwrrOverflowAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrOverflowAttempts.setStatus('mandatory')
ibmwrrOverflowActuals = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 11, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmwrrOverflowActuals.setStatus('mandatory')
mibBuilder.exportSymbols("WAN-RESTORAL-REROUTE-MIB", ibmwrrAltNetifIndex=ibmwrrAltNetifIndex, ibmwrrActuals=ibmwrrActuals, ibmwrsDuration=ibmwrsDuration, ibmwrrActive=ibmwrrActive, ibmwrrOverflowEnabled=ibmwrrOverflowEnabled, ibmwrrOverflowActive=ibmwrrOverflowActive, ibmWanRestoralTable=ibmWanRestoralTable, ibmwrrOverflowAttempts=ibmwrrOverflowAttempts, ibmWanRerouteEntry=ibmWanRerouteEntry, ibmwrsAttempts=ibmwrsAttempts, ibmWanRestoralRerouteMIB=ibmWanRestoralRerouteMIB, ibmwrrOverflowActuals=ibmwrrOverflowActuals, ibmwrsPriNetifIndex=ibmwrsPriNetifIndex, ibmwrsFwdPkts=ibmwrsFwdPkts, ibmwrrDuration=ibmwrrDuration, ibmwrsActuals=ibmwrsActuals, ibmWanRerouteTable=ibmWanRerouteTable, ibmWanReroute=ibmWanReroute, ibmwrsActive=ibmwrsActive, ibmwrrOverflowDuration=ibmwrrOverflowDuration, ibmwrrPriNetifIndex=ibmwrrPriNetifIndex, ibmwrsSecNetifIndex=ibmwrsSecNetifIndex, ibmWanRestoral=ibmWanRestoral, ibmwrrAttempts=ibmwrrAttempts, ibmwrrEnabled=ibmwrrEnabled, ibmwrsEnabled=ibmwrsEnabled, ibmWanRestoralEntry=ibmWanRestoralEntry)
