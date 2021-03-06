#
# PySNMP MIB module EXPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXPRESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, zeroDotZero, ModuleIdentity, Counter32, iso, IpAddress, Integer32, Bits, TimeTicks, ObjectIdentity, NotificationType, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "zeroDotZero", "ModuleIdentity", "Counter32", "iso", "IpAddress", "Integer32", "Bits", "TimeTicks", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter64")
DisplayString, RowStatus, TruthValue, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TimeStamp", "TextualConvention")
expressionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 22))
expressionMIB.setRevisions(('2005-11-24 00:00', '1998-02-25 17:00',))
if mibBuilder.loadTexts: expressionMIB.setLastUpdated('200511240000Z')
if mibBuilder.loadTexts: expressionMIB.setOrganization('IETF Distributed Management Working Group')
class ExpressionName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class ExpressionIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class ExpressionIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

expressionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 1))
expResource = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1))
expNames = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2))
expDefine = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3))
expValue = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4))
expResourceDeltaMinimum = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 600), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: expResourceDeltaMinimum.setStatus('current')
expResourceDeltaWildcardInstanceMaximum = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 2), Unsigned32()).setUnits('instances').setMaxAccess("readwrite")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstanceMaximum.setStatus('current')
expResourceDeltaWildcardInstances = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 3), Gauge32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstances.setStatus('current')
expResourceDeltaWildcardInstancesHigh = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 4), Gauge32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstancesHigh.setStatus('current')
expResourceDeltaWildcardInstanceResourceLacks = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 1, 5), Counter32()).setUnits('instances').setMaxAccess("readonly")
if mibBuilder.loadTexts: expResourceDeltaWildcardInstanceResourceLacks.setStatus('current')
expNameLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expNameLastChange.setStatus('current')
expNameHighestIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 2), ExpressionIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expNameHighestIndex.setStatus('current')
expNameTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3), )
if mibBuilder.loadTexts: expNameTable.setStatus('current')
expNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1), ).setIndexNames((0, "EXPRESSION-MIB", "expName"))
if mibBuilder.loadTexts: expNameEntry.setStatus('current')
expName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1, 1), ExpressionName())
if mibBuilder.loadTexts: expName.setStatus('current')
expExpressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1, 2), ExpressionIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expExpressionIndex.setStatus('current')
expNameStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expNameStatus.setStatus('current')
expExpressionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1), )
if mibBuilder.loadTexts: expExpressionTable.setStatus('current')
expExpressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1), ).setIndexNames((0, "EXPRESSION-MIB", "expExpressionIndex"))
if mibBuilder.loadTexts: expExpressionEntry.setStatus('current')
expExpressionName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 1), ExpressionName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expExpressionName.setStatus('current')
expExpression = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expExpression.setStatus('current')
expExpressionValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("counter32", 1), ("unsignedOrGauge32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8))).clone('counter32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expExpressionValueType.setStatus('current')
expExpressionComment = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expExpressionComment.setStatus('current')
expExpressionDeltaInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: expExpressionDeltaInterval.setStatus('current')
expExpressionPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionPrefix.setStatus('current')
expExpressionErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionErrors.setStatus('current')
expExpressionErrorTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionErrorTime.setStatus('current')
expExpressionErrorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionErrorIndex.setStatus('current')
expExpressionError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("invalidSyntax", 1), ("undefinedObjectIndex", 2), ("unrecognizedOperator", 3), ("unrecognizedFunction", 4), ("invalidOperandType", 5), ("unmatchedParenthesis", 6), ("tooManyWildcardValues", 7), ("recursion", 8), ("deltaTooShort", 9), ("resourceUnavailable", 10), ("divideByZero", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionError.setStatus('current')
expExpressionInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 11), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expExpressionInstance.setStatus('current')
expExpressionOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: expExpressionOwner.setStatus('current')
expObjectTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2), )
if mibBuilder.loadTexts: expObjectTable.setStatus('current')
expObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1), ).setIndexNames((0, "EXPRESSION-MIB", "expExpressionIndex"), (0, "EXPRESSION-MIB", "expObjectIndex"))
if mibBuilder.loadTexts: expObjectEntry.setStatus('current')
expObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: expObjectIndex.setStatus('current')
expObjectID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectID.setStatus('current')
expObjectIDWildcard = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectIDWildcard.setStatus('current')
expObjectSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2))).clone('absoluteValue')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectSampleType.setStatus('current')
sysUpTimeInstance = MibIdentifier((1, 3, 6, 1, 2, 1, 1, 3, 0))
expObjectDeltaDiscontinuityID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 5), ObjectIdentifier().clone((1, 3, 6, 1, 2, 1, 1, 3, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectDeltaDiscontinuityID.setStatus('current')
expObjectDiscontinuityIDWildcard = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectDiscontinuityIDWildcard.setStatus('current')
expObjectDiscontinuityIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("timeTicks", 1), ("timeStamp", 2))).clone('timeTicks')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectDiscontinuityIDType.setStatus('current')
expObjectConditional = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 8), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectConditional.setStatus('current')
expObjectConditionalWildcard = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectConditionalWildcard.setStatus('current')
expObjectStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 3, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: expObjectStatus.setStatus('current')
expValueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1), )
if mibBuilder.loadTexts: expValueTable.setStatus('current')
expValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1), ).setIndexNames((0, "EXPRESSION-MIB", "expExpressionIndex"), (0, "EXPRESSION-MIB", "expValueInstance"))
if mibBuilder.loadTexts: expValueEntry.setStatus('current')
expValueInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: expValueInstance.setStatus('current')
expValueCounter32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueCounter32Val.setStatus('current')
expValueUnsigned32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueUnsigned32Val.setStatus('current')
expValueInteger32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueInteger32Val.setStatus('current')
expValueIpAddressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueIpAddressVal.setStatus('current')
expValueOctetStringVal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueOctetStringVal.setStatus('current')
expValueOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueOidVal.setStatus('current')
expValueCounter64Val = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 22, 1, 4, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expValueCounter64Val.setStatus('current')
expressionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 3))
expressionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 1))
expressionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2))
expressionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 1, 1)).setObjects(("EXPRESSION-MIB", "expressionResourceGroup"), ("EXPRESSION-MIB", "expressionDefinitionGroup"), ("EXPRESSION-MIB", "expressionValueGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressionMIBCompliance = expressionMIBCompliance.setStatus('current')
expressionResourceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2, 1)).setObjects(("EXPRESSION-MIB", "expResourceDeltaMinimum"), ("EXPRESSION-MIB", "expResourceDeltaWildcardInstanceMaximum"), ("EXPRESSION-MIB", "expResourceDeltaWildcardInstances"), ("EXPRESSION-MIB", "expResourceDeltaWildcardInstancesHigh"), ("EXPRESSION-MIB", "expResourceDeltaWildcardInstanceResourceLacks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressionResourceGroup = expressionResourceGroup.setStatus('current')
expressionDefinitionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2, 2)).setObjects(("EXPRESSION-MIB", "expNameLastChange"), ("EXPRESSION-MIB", "expNameHighestIndex"), ("EXPRESSION-MIB", "expExpressionIndex"), ("EXPRESSION-MIB", "expNameStatus"), ("EXPRESSION-MIB", "expExpressionName"), ("EXPRESSION-MIB", "expExpression"), ("EXPRESSION-MIB", "expExpressionValueType"), ("EXPRESSION-MIB", "expExpressionComment"), ("EXPRESSION-MIB", "expExpressionDeltaInterval"), ("EXPRESSION-MIB", "expExpressionPrefix"), ("EXPRESSION-MIB", "expExpressionErrors"), ("EXPRESSION-MIB", "expExpressionErrorTime"), ("EXPRESSION-MIB", "expExpressionErrorIndex"), ("EXPRESSION-MIB", "expExpressionError"), ("EXPRESSION-MIB", "expExpressionInstance"), ("EXPRESSION-MIB", "expExpressionOwner"), ("EXPRESSION-MIB", "expObjectID"), ("EXPRESSION-MIB", "expObjectIDWildcard"), ("EXPRESSION-MIB", "expObjectSampleType"), ("EXPRESSION-MIB", "expObjectDeltaDiscontinuityID"), ("EXPRESSION-MIB", "expObjectDiscontinuityIDWildcard"), ("EXPRESSION-MIB", "expObjectDiscontinuityIDType"), ("EXPRESSION-MIB", "expObjectConditional"), ("EXPRESSION-MIB", "expObjectConditionalWildcard"), ("EXPRESSION-MIB", "expObjectStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressionDefinitionGroup = expressionDefinitionGroup.setStatus('current')
expressionValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 22, 3, 2, 3)).setObjects(("EXPRESSION-MIB", "expValueCounter32Val"), ("EXPRESSION-MIB", "expValueUnsigned32Val"), ("EXPRESSION-MIB", "expValueInteger32Val"), ("EXPRESSION-MIB", "expValueIpAddressVal"), ("EXPRESSION-MIB", "expValueOctetStringVal"), ("EXPRESSION-MIB", "expValueOidVal"), ("EXPRESSION-MIB", "expValueCounter64Val"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    expressionValueGroup = expressionValueGroup.setStatus('current')
mibBuilder.exportSymbols("EXPRESSION-MIB", expValueIpAddressVal=expValueIpAddressVal, expValue=expValue, expObjectIDWildcard=expObjectIDWildcard, expValueCounter32Val=expValueCounter32Val, expValueOidVal=expValueOidVal, ExpressionName=ExpressionName, expExpressionErrorIndex=expExpressionErrorIndex, expResourceDeltaWildcardInstanceResourceLacks=expResourceDeltaWildcardInstanceResourceLacks, expValueOctetStringVal=expValueOctetStringVal, expResourceDeltaMinimum=expResourceDeltaMinimum, expResource=expResource, expNameTable=expNameTable, expExpressionInstance=expExpressionInstance, expressionMIBCompliances=expressionMIBCompliances, expResourceDeltaWildcardInstances=expResourceDeltaWildcardInstances, expExpressionTable=expExpressionTable, expValueUnsigned32Val=expValueUnsigned32Val, expNameLastChange=expNameLastChange, expNames=expNames, expExpression=expExpression, expValueCounter64Val=expValueCounter64Val, PYSNMP_MODULE_ID=expressionMIB, expNameStatus=expNameStatus, expExpressionName=expExpressionName, expObjectEntry=expObjectEntry, expValueTable=expValueTable, expressionMIBObjects=expressionMIBObjects, expName=expName, expExpressionEntry=expExpressionEntry, expValueInstance=expValueInstance, expDefine=expDefine, expResourceDeltaWildcardInstancesHigh=expResourceDeltaWildcardInstancesHigh, expExpressionPrefix=expExpressionPrefix, expObjectDiscontinuityIDWildcard=expObjectDiscontinuityIDWildcard, expressionMIBGroups=expressionMIBGroups, expNameEntry=expNameEntry, expressionResourceGroup=expressionResourceGroup, expResourceDeltaWildcardInstanceMaximum=expResourceDeltaWildcardInstanceMaximum, expressionDefinitionGroup=expressionDefinitionGroup, expObjectSampleType=expObjectSampleType, expressionMIB=expressionMIB, expExpressionErrors=expExpressionErrors, ExpressionIndex=ExpressionIndex, expExpressionDeltaInterval=expExpressionDeltaInterval, expObjectDeltaDiscontinuityID=expObjectDeltaDiscontinuityID, expObjectConditionalWildcard=expObjectConditionalWildcard, expExpressionErrorTime=expExpressionErrorTime, expValueEntry=expValueEntry, expValueInteger32Val=expValueInteger32Val, expExpressionValueType=expExpressionValueType, expExpressionError=expExpressionError, sysUpTimeInstance=sysUpTimeInstance, expObjectID=expObjectID, expressionValueGroup=expressionValueGroup, expNameHighestIndex=expNameHighestIndex, expExpressionOwner=expExpressionOwner, expressionMIBConformance=expressionMIBConformance, expObjectTable=expObjectTable, expObjectIndex=expObjectIndex, expObjectDiscontinuityIDType=expObjectDiscontinuityIDType, expressionMIBCompliance=expressionMIBCompliance, expObjectConditional=expObjectConditional, expObjectStatus=expObjectStatus, expExpressionIndex=expExpressionIndex, ExpressionIndexOrZero=ExpressionIndexOrZero, expExpressionComment=expExpressionComment)
