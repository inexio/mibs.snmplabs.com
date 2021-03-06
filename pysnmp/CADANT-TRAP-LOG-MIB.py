#
# PySNMP MIB module CADANT-TRAP-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-TRAP-LOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:28:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
cadNotification, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadNotification")
InetAddressIPv4or6, = mibBuilder.importSymbols("CADANT-TC", "InetAddressIPv4or6")
docsDevEvControlEntry, = mibBuilder.importSymbols("DOCS-CABLE-DEVICE-MIB", "docsDevEvControlEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, ObjectIdentity, iso, TimeTicks, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Integer32, NotificationType, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "ObjectIdentity", "iso", "TimeTicks", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Integer32", "NotificationType", "Counter32", "Unsigned32")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
cadTrapLogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2))
cadTrapLogMib.setRevisions(('2006-04-20 00:00', '2005-03-31 00:00', '2004-03-16 00:00', '2004-02-04 00:00', '2003-06-30 00:00', '2003-05-30 00:00', '2003-05-07 00:00', '2003-04-29 00:00', '2002-08-13 00:00', '2002-08-06 00:00', '2001-06-19 00:00', '2001-06-11 00:00',))
if mibBuilder.loadTexts: cadTrapLogMib.setLastUpdated('200604200000Z')
if mibBuilder.loadTexts: cadTrapLogMib.setOrganization('Arris International, Inc.')
cadTrapLogGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1))
cadProprietaryLoggingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadProprietaryLoggingEnabled.setStatus('current')
cadLocalLogSize = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadLocalLogSize.setStatus('current')
cadLogHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2000)).clone(2000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadLogHistorySize.setStatus('current')
cadSyslogFacility = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("local0", 0), ("local1", 1), ("local2", 2), ("local3", 3), ("local4", 4), ("local5", 5), ("local6", 6), ("local7", 7))).clone('local0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadSyslogFacility.setStatus('current')
cadCmTrapInhibit = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 1, 5), Bits().clone(namedValues=NamedValues(("resetRanging", 0), ("resetProvisioning", 1), ("resetRegistered", 2), ("resetClear", 3), ("registered", 4))).clone(hexValue="f8")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCmTrapInhibit.setStatus('current')
cadEvControlTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 2), )
if mibBuilder.loadTexts: cadEvControlTable.setStatus('current')
cadEvControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 2, 1), )
docsDevEvControlEntry.registerAugmentions(("CADANT-TRAP-LOG-MIB", "cadEvControlEntry"))
cadEvControlEntry.setIndexNames(*docsDevEvControlEntry.getIndexNames())
if mibBuilder.loadTexts: cadEvControlEntry.setStatus('current')
cadEvReporting = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 2, 1, 1), Bits().clone(namedValues=NamedValues(("console", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadEvReporting.setStatus('current')
cadEvOverrideTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3), )
if mibBuilder.loadTexts: cadEvOverrideTable.setStatus('current')
cadEvOverrideEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1), ).setIndexNames((0, "CADANT-TRAP-LOG-MIB", "cadEvOvrdEvId"))
if mibBuilder.loadTexts: cadEvOverrideEntry.setStatus('current')
cadEvOvrdEvId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadEvOvrdEvId.setStatus('current')
cadEvOvrdState = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("admit", 1), ("inhibit", 2), ("priority", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadEvOvrdState.setStatus('current')
cadEvOvrdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadEvOvrdRowStatus.setStatus('current')
cadEvOvrdPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("invalid", 0), ("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("information", 7), ("debug", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadEvOvrdPriority.setStatus('current')
cadSyslogSvrTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4), )
if mibBuilder.loadTexts: cadSyslogSvrTable.setStatus('current')
cadSyslogSvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1), ).setIndexNames((0, "CADANT-TRAP-LOG-MIB", "cadSyslogSvrIpAddr"))
if mibBuilder.loadTexts: cadSyslogSvrEntry.setStatus('current')
cadSyslogSvrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1, 1), InetAddressIPv4or6())
if mibBuilder.loadTexts: cadSyslogSvrIpAddr.setStatus('current')
cadSyslogSvrFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("local0", 0), ("local1", 1), ("local2", 2), ("local3", 3), ("local4", 4), ("local5", 5), ("local6", 6), ("local7", 7))).clone('local0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSyslogSvrFacility.setStatus('current')
cadSyslogSvrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadSyslogSvrRowStatus.setStatus('current')
cadCliAuthToLogLevelTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5), )
if mibBuilder.loadTexts: cadCliAuthToLogLevelTable.setStatus('current')
cadCliAuthToLogLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5, 1), ).setIndexNames((0, "CADANT-TRAP-LOG-MIB", "cadCliAuthLevel"))
if mibBuilder.loadTexts: cadCliAuthToLogLevelEntry.setStatus('current')
cadCliAuthLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: cadCliAuthLevel.setStatus('current')
cadCliLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("information", 7), ("debug", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadCliLogLevel.setStatus('current')
cadTrapLogMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10))
cadTrapLogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 1))
cadTrapLogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2))
cadTrapLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 1, 1)).setObjects(("CADANT-TRAP-LOG-MIB", "cadTrapLogGlobalsGroup"), ("CADANT-TRAP-LOG-MIB", "cadTrapLogEventGroup"), ("CADANT-TRAP-LOG-MIB", "cadSyslogGroup"), ("CADANT-TRAP-LOG-MIB", "cadCliAuthToLogLevelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadTrapLogCompliance = cadTrapLogCompliance.setStatus('current')
cadTrapLogGlobalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 1)).setObjects(("CADANT-TRAP-LOG-MIB", "cadProprietaryLoggingEnabled"), ("CADANT-TRAP-LOG-MIB", "cadLocalLogSize"), ("CADANT-TRAP-LOG-MIB", "cadLogHistorySize"), ("CADANT-TRAP-LOG-MIB", "cadSyslogFacility"), ("CADANT-TRAP-LOG-MIB", "cadCmTrapInhibit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadTrapLogGlobalsGroup = cadTrapLogGlobalsGroup.setStatus('current')
cadTrapLogEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 2)).setObjects(("CADANT-TRAP-LOG-MIB", "cadEvReporting"), ("CADANT-TRAP-LOG-MIB", "cadEvOvrdEvId"), ("CADANT-TRAP-LOG-MIB", "cadEvOvrdState"), ("CADANT-TRAP-LOG-MIB", "cadEvOvrdRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadTrapLogEventGroup = cadTrapLogEventGroup.setStatus('current')
cadSyslogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 3)).setObjects(("CADANT-TRAP-LOG-MIB", "cadSyslogSvrFacility"), ("CADANT-TRAP-LOG-MIB", "cadSyslogSvrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadSyslogGroup = cadSyslogGroup.setStatus('current')
cadCliAuthToLogLevelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4998, 1, 1, 6, 2, 10, 2, 4)).setObjects(("CADANT-TRAP-LOG-MIB", "cadCliLogLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cadCliAuthToLogLevelGroup = cadCliAuthToLogLevelGroup.setStatus('current')
mibBuilder.exportSymbols("CADANT-TRAP-LOG-MIB", cadTrapLogGroups=cadTrapLogGroups, cadCliAuthToLogLevelGroup=cadCliAuthToLogLevelGroup, cadEvControlEntry=cadEvControlEntry, cadCliAuthToLogLevelTable=cadCliAuthToLogLevelTable, cadEvOvrdRowStatus=cadEvOvrdRowStatus, cadEvOvrdEvId=cadEvOvrdEvId, cadTrapLogCompliances=cadTrapLogCompliances, cadLocalLogSize=cadLocalLogSize, cadCliLogLevel=cadCliLogLevel, cadTrapLogMibConformance=cadTrapLogMibConformance, cadSyslogFacility=cadSyslogFacility, PYSNMP_MODULE_ID=cadTrapLogMib, cadTrapLogMib=cadTrapLogMib, cadEvOverrideTable=cadEvOverrideTable, cadEvOvrdPriority=cadEvOvrdPriority, cadSyslogSvrEntry=cadSyslogSvrEntry, cadCmTrapInhibit=cadCmTrapInhibit, cadCliAuthLevel=cadCliAuthLevel, cadLogHistorySize=cadLogHistorySize, cadSyslogSvrFacility=cadSyslogSvrFacility, cadCliAuthToLogLevelEntry=cadCliAuthToLogLevelEntry, cadEvOvrdState=cadEvOvrdState, cadSyslogSvrTable=cadSyslogSvrTable, cadEvControlTable=cadEvControlTable, cadProprietaryLoggingEnabled=cadProprietaryLoggingEnabled, cadSyslogSvrIpAddr=cadSyslogSvrIpAddr, cadEvOverrideEntry=cadEvOverrideEntry, cadSyslogGroup=cadSyslogGroup, cadSyslogSvrRowStatus=cadSyslogSvrRowStatus, cadTrapLogCompliance=cadTrapLogCompliance, cadTrapLogGlobals=cadTrapLogGlobals, cadTrapLogGlobalsGroup=cadTrapLogGlobalsGroup, cadEvReporting=cadEvReporting, cadTrapLogEventGroup=cadTrapLogEventGroup)
