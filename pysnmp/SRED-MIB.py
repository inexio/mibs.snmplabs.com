#
# PySNMP MIB module SRED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SRED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:02:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, ModuleIdentity, TimeTicks, ObjectIdentity, IpAddress, iso, Gauge32, MibIdentifier, Unsigned32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "IpAddress", "iso", "Gauge32", "MibIdentifier", "Unsigned32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swSredMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 51))
if mibBuilder.loadTexts: swSredMIB.setLastUpdated('0902160000Z')
if mibBuilder.loadTexts: swSredMIB.setOrganization('D-Link Corp.')
swSredCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 51, 1))
swSredInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 51, 2))
swSredMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 51, 3))
swSredGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 51, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSredGlobalState.setStatus('current')
swSredDropCounterTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1), )
if mibBuilder.loadTexts: swSredDropCounterTable.setStatus('current')
swSredDropCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1), ).setIndexNames((0, "SRED-MIB", "swSredPortIndex"))
if mibBuilder.loadTexts: swSredDropCounterEntry.setStatus('current')
swSredPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSredPortIndex.setStatus('current')
swSredLowDropCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSredLowDropCounter.setStatus('current')
swSredHighDropCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSredHighDropCounter.setStatus('current')
swSredCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1), )
if mibBuilder.loadTexts: swSredCtrlTable.setStatus('current')
swSredCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1), ).setIndexNames((0, "SRED-MIB", "swSredCtrlPortIndex"), (0, "SRED-MIB", "swSredCtrlClassIndex"))
if mibBuilder.loadTexts: swSredCtrlEntry.setStatus('current')
swSredCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSredCtrlPortIndex.setStatus('current')
swSredCtrlClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSredCtrlClassIndex.setStatus('current')
swSredCtrlThresholdLow = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSredCtrlThresholdLow.setStatus('current')
swSredCtrlThresholdHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSredCtrlThresholdHigh.setStatus('current')
swSredCtrlDropRateLow = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSredCtrlDropRateLow.setStatus('current')
swSredCtrlDropRateHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSredCtrlDropRateHigh.setStatus('current')
swSredCtrlDropGreenState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSredCtrlDropGreenState.setStatus('current')
sw8021pColorMapCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2), )
if mibBuilder.loadTexts: sw8021pColorMapCtrlTable.setStatus('obsolete')
sw8021pColorMapCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1), ).setIndexNames((0, "SRED-MIB", "sw8021pColorMapCtrlPortIndex"), (0, "SRED-MIB", "sw8021pColorMapCtrlPriorityIndex"))
if mibBuilder.loadTexts: sw8021pColorMapCtrlEntry.setStatus('obsolete')
sw8021pColorMapCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sw8021pColorMapCtrlPortIndex.setStatus('obsolete')
sw8021pColorMapCtrlPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sw8021pColorMapCtrlPriorityIndex.setStatus('obsolete')
sw8021pColorMapCtrlColor = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("green", 1), ("red", 2), ("yellow", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sw8021pColorMapCtrlColor.setStatus('obsolete')
swDscpTrustPortCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3), )
if mibBuilder.loadTexts: swDscpTrustPortCtrlTable.setStatus('obsolete')
swDscpTrustPortCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3, 1), ).setIndexNames((0, "SRED-MIB", "swDscpTrustPortCtrlPortIndex"))
if mibBuilder.loadTexts: swDscpTrustPortCtrlEntry.setStatus('obsolete')
swDscpTrustPortCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDscpTrustPortCtrlPortIndex.setStatus('obsolete')
swDscpTrustPortCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDscpTrustPortCtrlState.setStatus('obsolete')
swDscpMapCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4), )
if mibBuilder.loadTexts: swDscpMapCtrlTable.setStatus('obsolete')
swDscpMapCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1), ).setIndexNames((0, "SRED-MIB", "swDscpMapCtrlPortIndex"), (0, "SRED-MIB", "swDscpMapCtrlDscpIndex"))
if mibBuilder.loadTexts: swDscpMapCtrlEntry.setStatus('obsolete')
swDscpMapCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDscpMapCtrlPortIndex.setStatus('obsolete')
swDscpMapCtrlDscpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDscpMapCtrlDscpIndex.setStatus('obsolete')
swDscpMapCtrl8021pPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDscpMapCtrl8021pPriority.setStatus('obsolete')
swDscpMapCtrlNewDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDscpMapCtrlNewDscp.setStatus('obsolete')
swDscpMapCtrlColor = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("green", 1), ("red", 2), ("yellow", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDscpMapCtrlColor.setStatus('obsolete')
mibBuilder.exportSymbols("SRED-MIB", swSredMIB=swSredMIB, swDscpMapCtrl8021pPriority=swDscpMapCtrl8021pPriority, swSredCtrlDropRateHigh=swSredCtrlDropRateHigh, swSredCtrlDropGreenState=swSredCtrlDropGreenState, swDscpMapCtrlTable=swDscpMapCtrlTable, swSredCtrlTable=swSredCtrlTable, sw8021pColorMapCtrlPriorityIndex=sw8021pColorMapCtrlPriorityIndex, PYSNMP_MODULE_ID=swSredMIB, swDscpMapCtrlPortIndex=swDscpMapCtrlPortIndex, swSredPortIndex=swSredPortIndex, swSredLowDropCounter=swSredLowDropCounter, swDscpTrustPortCtrlTable=swDscpTrustPortCtrlTable, swSredGlobalState=swSredGlobalState, swSredInfo=swSredInfo, swSredCtrlThresholdLow=swSredCtrlThresholdLow, swDscpTrustPortCtrlPortIndex=swDscpTrustPortCtrlPortIndex, sw8021pColorMapCtrlColor=sw8021pColorMapCtrlColor, sw8021pColorMapCtrlEntry=sw8021pColorMapCtrlEntry, swSredCtrlEntry=swSredCtrlEntry, swSredCtrl=swSredCtrl, swSredMgmt=swSredMgmt, swSredCtrlDropRateLow=swSredCtrlDropRateLow, swDscpMapCtrlColor=swDscpMapCtrlColor, swSredCtrlPortIndex=swSredCtrlPortIndex, swSredHighDropCounter=swSredHighDropCounter, sw8021pColorMapCtrlPortIndex=sw8021pColorMapCtrlPortIndex, swDscpMapCtrlEntry=swDscpMapCtrlEntry, sw8021pColorMapCtrlTable=sw8021pColorMapCtrlTable, swSredCtrlThresholdHigh=swSredCtrlThresholdHigh, swSredCtrlClassIndex=swSredCtrlClassIndex, swDscpMapCtrlDscpIndex=swDscpMapCtrlDscpIndex, swDscpMapCtrlNewDscp=swDscpMapCtrlNewDscp, swSredDropCounterTable=swSredDropCounterTable, swSredDropCounterEntry=swSredDropCounterEntry, swDscpTrustPortCtrlEntry=swDscpTrustPortCtrlEntry, swDscpTrustPortCtrlState=swDscpTrustPortCtrlState)
