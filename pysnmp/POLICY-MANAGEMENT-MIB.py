#
# PySNMP MIB module POLICY-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POLICY-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, TimeTicks, Integer32, Unsigned32, experimental, Counter32, Bits, IpAddress, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Integer32", "Unsigned32", "experimental", "Counter32", "Bits", "IpAddress", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "RowPointer")
policyMgt = ModuleIdentity((1, 3, 6, 1, 3, 107))
policyMgt.setRevisions(('2000-10-11 15:00',))
if mibBuilder.loadTexts: policyMgt.setLastUpdated('200010111500Z')
if mibBuilder.loadTexts: policyMgt.setOrganization('IETF SNMP Configuration Working Group')
class UTF8String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'

pmPolicyTable = MibTable((1, 3, 6, 1, 3, 107, 1), )
if mibBuilder.loadTexts: pmPolicyTable.setStatus('current')
pmPolicyEntry = MibTableRow((1, 3, 6, 1, 3, 107, 1, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"))
if mibBuilder.loadTexts: pmPolicyEntry.setStatus('current')
pmPolicyIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pmPolicyIndex.setStatus('current')
pmPolicyFilter = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 2), UTF8String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyFilter.setStatus('current')
pmPolicyCalendar = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 3), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyCalendar.setStatus('current')
pmPolicyAction = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 4), UTF8String()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyAction.setStatus('current')
pmPolicyFilterMaxLatency = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 5), Unsigned32()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyFilterMaxLatency.setStatus('current')
pmPolicyActionMaxLatency = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 6), Unsigned32()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyActionMaxLatency.setStatus('current')
pmPolicyPrecedence = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyPrecedence.setStatus('current')
pmPolicyGroup = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 8), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyGroup.setStatus('current')
pmPolicyDescription = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 9), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyDescription.setStatus('current')
pmPolicyMatches = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 10), Gauge32()).setUnits('elements').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyMatches.setStatus('current')
pmPolicyExecutionErrors = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 11), Counter32()).setUnits('errors').setMaxAccess("readonly")
if mibBuilder.loadTexts: pmPolicyExecutionErrors.setStatus('current')
pmPolicyDebugging = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyDebugging.setStatus('current')
pmPolicyStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmPolicyStatus.setStatus('current')
pmElementTypeRegTable = MibTable((1, 3, 6, 1, 3, 107, 2), )
if mibBuilder.loadTexts: pmElementTypeRegTable.setStatus('current')
pmElementTypeRegEntry = MibTableRow((1, 3, 6, 1, 3, 107, 2, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmElementTypeRegIndex"))
if mibBuilder.loadTexts: pmElementTypeRegEntry.setStatus('current')
pmElementTypeRegIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pmElementTypeRegIndex.setStatus('current')
pmElementTypeRegOIDPrefix = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmElementTypeRegOIDPrefix.setStatus('current')
pmElementTypeRegName = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 3), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmElementTypeRegName.setStatus('current')
pmElementTypeRegRowStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmElementTypeRegRowStatus.setStatus('current')
pmRoleESTable = MibTable((1, 3, 6, 1, 3, 107, 3), )
if mibBuilder.loadTexts: pmRoleESTable.setStatus('current')
pmRoleESEntry = MibTableRow((1, 3, 6, 1, 3, 107, 3, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmRoleESElement"), (0, "POLICY-MANAGEMENT-MIB", "pmRoleESString"))
if mibBuilder.loadTexts: pmRoleESEntry.setStatus('current')
pmRoleESElement = MibTableColumn((1, 3, 6, 1, 3, 107, 3, 1, 1), RowPointer())
if mibBuilder.loadTexts: pmRoleESElement.setStatus('current')
pmRoleESString = MibTableColumn((1, 3, 6, 1, 3, 107, 3, 1, 2), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: pmRoleESString.setStatus('current')
pmRoleESStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRoleESStatus.setStatus('current')
pmRoleSETable = MibTable((1, 3, 6, 1, 3, 107, 4), )
if mibBuilder.loadTexts: pmRoleSETable.setStatus('current')
pmRoleSEEntry = MibTableRow((1, 3, 6, 1, 3, 107, 4, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmRoleSEString"), (0, "POLICY-MANAGEMENT-MIB", "pmRoleSEElement"))
if mibBuilder.loadTexts: pmRoleSEEntry.setStatus('current')
pmRoleSEString = MibTableColumn((1, 3, 6, 1, 3, 107, 4, 1, 1), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: pmRoleSEString.setStatus('current')
pmRoleSEElement = MibTableColumn((1, 3, 6, 1, 3, 107, 4, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRoleSEElement.setStatus('current')
pmCapabilitiesTable = MibTable((1, 3, 6, 1, 3, 107, 5), )
if mibBuilder.loadTexts: pmCapabilitiesTable.setStatus('current')
pmCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 3, 107, 5, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmCapabilitiesIndex"))
if mibBuilder.loadTexts: pmCapabilitiesEntry.setStatus('current')
pmCapabilitiesIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pmCapabilitiesIndex.setStatus('current')
pmCapabilitiesType = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesType.setStatus('current')
pmCapabilitiesSubType = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesSubType.setStatus('current')
pmCapabilitiesModificationOID = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationOID.setStatus('current')
pmCapabilitiesModificationType = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unsupported", 0), ("restricted", 1), ("additional", 2), ("addvalue", 3), ("maxlimit", 4), ("minlimit", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationType.setStatus('current')
pmCapabilitiesModificationValue = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationValue.setStatus('current')
pmCapabilitiesModificationString = MibTableColumn((1, 3, 6, 1, 3, 107, 5, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmCapabilitiesModificationString.setStatus('current')
pmTrackingPolicyToElementTable = MibTable((1, 3, 6, 1, 3, 107, 6), )
if mibBuilder.loadTexts: pmTrackingPolicyToElementTable.setStatus('current')
pmTrackingPolicyToElementEntry = MibTableRow((1, 3, 6, 1, 3, 107, 6, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"), (0, "POLICY-MANAGEMENT-MIB", "pmTrackingPolicyToElementElement"))
if mibBuilder.loadTexts: pmTrackingPolicyToElementEntry.setStatus('current')
pmTrackingPolicyToElementElement = MibTableColumn((1, 3, 6, 1, 3, 107, 6, 1, 1), RowPointer())
if mibBuilder.loadTexts: pmTrackingPolicyToElementElement.setStatus('current')
pmTrackingPolicyToElementStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTrackingPolicyToElementStatus.setStatus('current')
pmTrackingElementToPolicyTable = MibTable((1, 3, 6, 1, 3, 107, 7), )
if mibBuilder.loadTexts: pmTrackingElementToPolicyTable.setStatus('current')
pmTrackingElementToPolicyEntry = MibTableRow((1, 3, 6, 1, 3, 107, 7, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmTrackingElementToPolicyElement"), (0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"))
if mibBuilder.loadTexts: pmTrackingElementToPolicyEntry.setStatus('current')
pmTrackingElementToPolicyElement = MibTableColumn((1, 3, 6, 1, 3, 107, 7, 1, 1), RowPointer())
if mibBuilder.loadTexts: pmTrackingElementToPolicyElement.setStatus('current')
pmTrackingElementToPolicyStatus = MibTableColumn((1, 3, 6, 1, 3, 107, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("forceOff", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTrackingElementToPolicyStatus.setStatus('current')
pmDebuggingTable = MibTable((1, 3, 6, 1, 3, 107, 8), )
if mibBuilder.loadTexts: pmDebuggingTable.setStatus('current')
pmDebuggingEntry = MibTableRow((1, 3, 6, 1, 3, 107, 8, 1), ).setIndexNames((0, "POLICY-MANAGEMENT-MIB", "pmPolicyIndex"), (0, "POLICY-MANAGEMENT-MIB", "pmDebuggingElement"), (0, "POLICY-MANAGEMENT-MIB", "pmDebuggingLogIndex"))
if mibBuilder.loadTexts: pmDebuggingEntry.setStatus('current')
pmDebuggingElement = MibTableColumn((1, 3, 6, 1, 3, 107, 8, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmDebuggingElement.setStatus('current')
pmDebuggingLogIndex = MibTableColumn((1, 3, 6, 1, 3, 107, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmDebuggingLogIndex.setStatus('current')
pmDebuggingMessage = MibTableColumn((1, 3, 6, 1, 3, 107, 8, 1, 3), UTF8String().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmDebuggingMessage.setStatus('current')
pmConformance = MibIdentifier((1, 3, 6, 1, 3, 107, 20))
pmCompliances = MibIdentifier((1, 3, 6, 1, 3, 107, 20, 1))
pmGroups = MibIdentifier((1, 3, 6, 1, 3, 107, 20, 2))
pmCompliance = ModuleCompliance((1, 3, 6, 1, 3, 107, 20, 1, 1)).setObjects(("POLICY-MANAGEMENT-MIB", "pmPolicyManagementGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmCompliance = pmCompliance.setStatus('current')
pmPolicyManagementGroup = ObjectGroup((1, 3, 6, 1, 3, 107, 20, 2, 1)).setObjects(("POLICY-MANAGEMENT-MIB", "pmPolicyFilter"), ("POLICY-MANAGEMENT-MIB", "pmPolicyCalendar"), ("POLICY-MANAGEMENT-MIB", "pmPolicyAction"), ("POLICY-MANAGEMENT-MIB", "pmPolicyFilterMaxLatency"), ("POLICY-MANAGEMENT-MIB", "pmPolicyActionMaxLatency"), ("POLICY-MANAGEMENT-MIB", "pmPolicyPrecedence"), ("POLICY-MANAGEMENT-MIB", "pmPolicyGroup"), ("POLICY-MANAGEMENT-MIB", "pmPolicyDescription"), ("POLICY-MANAGEMENT-MIB", "pmPolicyMatches"), ("POLICY-MANAGEMENT-MIB", "pmPolicyExecutionErrors"), ("POLICY-MANAGEMENT-MIB", "pmPolicyDebugging"), ("POLICY-MANAGEMENT-MIB", "pmPolicyStatus"), ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegOIDPrefix"), ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegName"), ("POLICY-MANAGEMENT-MIB", "pmElementTypeRegRowStatus"), ("POLICY-MANAGEMENT-MIB", "pmRoleESStatus"), ("POLICY-MANAGEMENT-MIB", "pmRoleSEElement"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesType"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesSubType"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationOID"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationType"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationValue"), ("POLICY-MANAGEMENT-MIB", "pmCapabilitiesModificationString"), ("POLICY-MANAGEMENT-MIB", "pmTrackingPolicyToElementStatus"), ("POLICY-MANAGEMENT-MIB", "pmTrackingElementToPolicyStatus"), ("POLICY-MANAGEMENT-MIB", "pmDebuggingElement"), ("POLICY-MANAGEMENT-MIB", "pmDebuggingLogIndex"), ("POLICY-MANAGEMENT-MIB", "pmDebuggingMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmPolicyManagementGroup = pmPolicyManagementGroup.setStatus('current')
pmBaseFunctionLibrary = MibIdentifier((1, 3, 6, 1, 3, 107, 20, 2, 2))
mibBuilder.exportSymbols("POLICY-MANAGEMENT-MIB", pmCapabilitiesModificationOID=pmCapabilitiesModificationOID, pmPolicyStatus=pmPolicyStatus, pmPolicyDescription=pmPolicyDescription, pmPolicyFilterMaxLatency=pmPolicyFilterMaxLatency, pmElementTypeRegEntry=pmElementTypeRegEntry, pmTrackingElementToPolicyElement=pmTrackingElementToPolicyElement, pmTrackingPolicyToElementStatus=pmTrackingPolicyToElementStatus, pmTrackingPolicyToElementEntry=pmTrackingPolicyToElementEntry, pmRoleESEntry=pmRoleESEntry, pmPolicyExecutionErrors=pmPolicyExecutionErrors, pmDebuggingTable=pmDebuggingTable, pmRoleSEElement=pmRoleSEElement, pmElementTypeRegOIDPrefix=pmElementTypeRegOIDPrefix, pmTrackingPolicyToElementTable=pmTrackingPolicyToElementTable, pmTrackingPolicyToElementElement=pmTrackingPolicyToElementElement, pmCapabilitiesEntry=pmCapabilitiesEntry, pmRoleESElement=pmRoleESElement, pmPolicyPrecedence=pmPolicyPrecedence, pmPolicyDebugging=pmPolicyDebugging, pmCapabilitiesIndex=pmCapabilitiesIndex, pmDebuggingElement=pmDebuggingElement, pmCapabilitiesType=pmCapabilitiesType, pmElementTypeRegRowStatus=pmElementTypeRegRowStatus, pmRoleSEEntry=pmRoleSEEntry, pmPolicyTable=pmPolicyTable, pmRoleESTable=pmRoleESTable, pmConformance=pmConformance, pmElementTypeRegIndex=pmElementTypeRegIndex, pmPolicyFilter=pmPolicyFilter, pmRoleESString=pmRoleESString, pmGroups=pmGroups, pmCapabilitiesSubType=pmCapabilitiesSubType, PYSNMP_MODULE_ID=policyMgt, pmCapabilitiesModificationValue=pmCapabilitiesModificationValue, pmPolicyMatches=pmPolicyMatches, pmTrackingElementToPolicyStatus=pmTrackingElementToPolicyStatus, pmDebuggingLogIndex=pmDebuggingLogIndex, pmPolicyGroup=pmPolicyGroup, pmCapabilitiesTable=pmCapabilitiesTable, pmBaseFunctionLibrary=pmBaseFunctionLibrary, pmPolicyCalendar=pmPolicyCalendar, pmElementTypeRegName=pmElementTypeRegName, pmRoleSETable=pmRoleSETable, pmPolicyIndex=pmPolicyIndex, UTF8String=UTF8String, pmCapabilitiesModificationString=pmCapabilitiesModificationString, pmDebuggingEntry=pmDebuggingEntry, pmElementTypeRegTable=pmElementTypeRegTable, pmPolicyActionMaxLatency=pmPolicyActionMaxLatency, pmTrackingElementToPolicyEntry=pmTrackingElementToPolicyEntry, pmPolicyAction=pmPolicyAction, pmDebuggingMessage=pmDebuggingMessage, pmCompliances=pmCompliances, pmPolicyEntry=pmPolicyEntry, pmRoleESStatus=pmRoleESStatus, pmPolicyManagementGroup=pmPolicyManagementGroup, pmTrackingElementToPolicyTable=pmTrackingElementToPolicyTable, pmCapabilitiesModificationType=pmCapabilitiesModificationType, pmRoleSEString=pmRoleSEString, policyMgt=policyMgt, pmCompliance=pmCompliance)
