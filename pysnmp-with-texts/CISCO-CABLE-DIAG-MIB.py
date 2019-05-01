#
# PySNMP MIB module CISCO-CABLE-DIAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CABLE-DIAG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:51:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter64, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, Bits, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter64", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32", "iso")
TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
ciscoCableDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 390))
ciscoCableDiagMIB.setRevisions(('2004-09-13 00:00', '2004-01-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableDiagMIB.setRevisionsDescriptions(('Added a new enum value indeterminate(9) in ccdTdrIfResultPairStatus.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCableDiagMIB.setLastUpdated('200409130000Z')
if mibBuilder.loadTexts: ciscoCableDiagMIB.setOrganization('Cisco Systems Inc. ')
if mibBuilder.loadTexts: ciscoCableDiagMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCableDiagMIB.setDescription('This MIB module defines objects for managing cable diagnostic test capabilites supported by the Cisco devices. Cable diagnostic tests are tests intended to exercise the functional integrity of the cable attached to a physical interface. Examples of cable diagnostic test methods are: PRBS (Pesudo Random Binary Sequence), TDR (Time Domain reflectometery), etc..')
ciscoCableDiagMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 390, 0))
ciscoCableDiagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 390, 1))
ciscoCableDiagMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 390, 2))
ccdPrbsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1))
ccdTdrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2))
ccdPrbsIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1), )
if mibBuilder.loadTexts: ccdPrbsIfTable.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsIfTable.setDescription("A table containing information about PRBS (Pesudo Random Binary Sequence) test on the device's interfaces. An entry appears in this table for each interface which is capable to run PRBS test.")
ccdPrbsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ccdPrbsIfEntry.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsIfEntry.setDescription('An entry in the ccdPrbsIfTable, containing the information about PRBS test on an interface.')
ccdPrbsIfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("start", 1), ("stop", 2), ("errorReset", 3), ("running", 4), ("notRunning", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccdPrbsIfAction.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsIfAction.setDescription("Indicates the PRBS test action to be executed on the interface and whether the test is currently running or not. 'start' -- start the PRBS test on the interface. 'stop' -- stop the PRBS test on the interface. 'errorReset' -- reset the object value of ccdPrbsIfTestErrors to zero on the interface. 'running' -- the PRBS test is currently running on the interface. This value is a read-only value and can not be set on the interface. 'notRunning' -- the PRBS test is currently not running on the interface. This value is a read-only value and can not be set on the interface.")
ccdPrbsIfActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("succeeded", 1), ("failedDueToUnknownReason", 2), ("failedDueToResourceUnavailable", 3), ("failedDueToInternalError", 4), ("failedDueToTestAlreadyStarted", 5), ("failedDueToTestAlreadyStopped", 6), ("failedDueToInterfaceDisabled", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdPrbsIfActionStatus.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsIfActionStatus.setDescription('Indicates the status of the last PRBS test action set on the interface.')
ccdPrbsIfTestErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdPrbsIfTestErrors.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsIfTestErrors.setDescription("Indicates the number of errors which occurred during the current or most recent running of a test. This Gauge is reset to zero each time a test starts (e.g., when ccdPrbsIfAction is set to 'start') or each time ccdPrbsIfAction is set to 'errorReset' on an interface. If and when an instance of ccdPrbsIfTestErrors reaches its maximum value as indicated by the corresponding instance of ccdPrbsIfTestErrorsMaxValue, its value will be less or equal to the actual number of errors.")
ccdPrbsIfTestErrorsResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdPrbsIfTestErrorsResetTime.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsIfTestErrorsResetTime.setDescription('Indicates the most recent time that the corresponding instance of ccdPrbsIfTestErrors is reset to zero. If the the corresponding instance of ccdPrbsIfTestErrors is never reset to zero, then the instance value for ccdPrbsIfTestErrorsResetTime will be zero.')
ccdPrbsIfTestErrorsMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdPrbsIfTestErrorsMaxValue.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsIfTestErrorsMaxValue.setDescription('Indicates the maximum value of the corresponding instance of ccdPrbsIfTestErrors.')
ccdTdrIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1), )
if mibBuilder.loadTexts: ccdTdrIfTable.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfTable.setDescription("A table containing information about TDR (Time Domain Reflectometery) test on the device's interfaces. An entry appears in this table for each interface which is capable to run TDR test.")
ccdTdrIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ccdTdrIfEntry.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfEntry.setDescription('An entry in the ccdTdrIfTable, containing the information about TDR test on an interface.')
ccdTdrIfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("start", 1), ("clear", 2), ("running", 3), ("notRunning", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccdTdrIfAction.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfAction.setDescription("Indicates the TDR test action to be executed on the interface and whether the test is currently running or not. 'start' -- start the TDR test on the interface. 'clear' -- clear all the TDR test results on the interface. After this action is executed on an interface, the object value of ccdTdrIfResultValid for the corresponding interface will be false(2). 'running' -- the TDR test is currently running on the interface. This value is a read-only value and can not be set on the interface. 'notRunning' -- the TDR test is currently not running on the interface. This value is a read-only value and can not be set on the interface.")
ccdTdrIfActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("succeeded", 1), ("failedDueToUnknownReason", 2), ("failedDueToResourceUnavailable", 3), ("failedDueToInternalError", 4), ("failedDueToTestAlreadyRunning", 5), ("failedDueToInterfaceDisabled", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfActionStatus.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfActionStatus.setDescription('Indicates the status of the last TDR test action set on the interface.')
ccdTdrIfLastTestTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfLastTestTime.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfLastTestTime.setDescription('Indicates the timestamp when TDR test is last run on the interface. If TDR test is never run on an interface, then this object value will be zero.')
ccdTdrIfResultValid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultValid.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultValid.setDescription('Indicates whether the TDR test result on the interface is valid for the user to retrieve or not.')
ccdTdrIfResultTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2), )
if mibBuilder.loadTexts: ccdTdrIfResultTable.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultTable.setDescription("A table containing information about TDR test result on the device's interfaces. An entry appears in this table for each cable pair on an interface which has valid TDR test result, i.e., the value of ccdTdrIfResultValid for the interface is true(1).")
ccdTdrIfResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairIndex"))
if mibBuilder.loadTexts: ccdTdrIfResultEntry.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultEntry.setDescription('An entry in the ccdTdrIfResultTable, containing the information about TDR test on an interface.')
ccdTdrIfResultPairIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pair1to2", 1), ("pair3to6", 2), ("pair4to5", 3), ("pair7to8", 4))))
if mibBuilder.loadTexts: ccdTdrIfResultPairIndex.setReference('IEEE 802.3-2002: Sections 40.8.1')
if mibBuilder.loadTexts: ccdTdrIfResultPairIndex.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairIndex.setDescription("The local cable pair index. 'pair1to2' -- the pair with cable connectors 1 and 2. 'pair3to6' -- the pair with cable connectors 3 and 6. 'pair4to5' -- the pair with cable connectors 4 and 5. 'pair7to8' -- the pair with cable connectors 7 and 8.")
ccdTdrIfResultPairChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("channelA", 2), ("channelB", 3), ("channelC", 4), ("channelD", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultPairChannel.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairChannel.setDescription("The channels that the cable pair is connected to. 'other' -- none of the following. 'channelA' -- channel A. 'channelB' -- channel B. 'channelC' -- channel C. 'channelD' -- channel D.")
ccdTdrIfResultPairLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultPairLength.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairLength.setDescription('The length of the cable pair. A value of -1 indicates the length value is invalid. The unit of this value is indicated by ccdTdrIfResultPairLengthUnit of the same cable pair.')
ccdTdrIfResultPairLenAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultPairLenAccuracy.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairLenAccuracy.setDescription('The length accuracy of the cable pair. This value should be added to and deducted from the value of ccdTdrIfResultPairLength of the same cable pair to form the upper and lower range of the cable pair length. A value of -1 indicates the length accuracy value is invalid. The unit of this value is indicated by ccdTdrIfResultPairLengthUnit of the same cable pair. ')
ccdTdrIfResultPairDistToFault = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultPairDistToFault.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairDistToFault.setDescription('The distance to the fault point of the cable pair. A value of -1 indicates this value is invalid. The unit of this value is indicated by ccdTdrIfResultPairLengthUnit of the same cable pair.')
ccdTdrIfResultPairDistAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultPairDistAccuracy.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairDistAccuracy.setDescription('The accuracy of the distance to the fault point for the cable pair. This value should be added to and deducted from the value of ccdTdrIfResultPairDistToFault of the same cable pair to form the upper and lower range of the distance to fault point for the cable pair. A value of -1 indicates this value is invalid. The unit of this value is indicated by ccdTdrIfResultPairLengthUnit of the same cable pair.')
ccdTdrIfResultPairLengthUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("meter", 2), ("centimeter", 3), ("kilometer", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultPairLengthUnit.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairLengthUnit.setDescription("The measurement unit on the length or the distance to fault point for the cable pair. 'unknown' -- none of the following. 'meter' -- the unit is meter. 'centimeter' -- the unit is centimeter. 'kilometer' -- the unit is kilometer.")
ccdTdrIfResultPairStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 390, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 1), ("terminated", 2), ("notCompleted", 3), ("notSupported", 4), ("open", 5), ("shorted", 6), ("impedanceMismatch", 7), ("broken", 8), ("indeterminate", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccdTdrIfResultPairStatus.setStatus('current')
if mibBuilder.loadTexts: ccdTdrIfResultPairStatus.setDescription("The status of the cable pair. 'unknown' -- none of the following. 'terminated' -- the pair is properly terminated at the remote end. 'notCompleted' -- the test on this pair is not completed. 'notSupported' -- the test on this pair is not supported. 'open' -- the pair is open. 'shorted' -- the pair is shorted. 'impedanceMismatch' -- the impedance of the pair is mismatched. 'broken' -- the pair is broken. 'indeterminate' -- the status of the pair is indeterminate.")
ciscoCableDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 1))
ciscoCableDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 2))
ciscoCableDiagMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 1, 1)).setObjects(("CISCO-CABLE-DIAG-MIB", "ccdPrbsGroup"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableDiagMIBComplianceRev1 = ciscoCableDiagMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoCableDiagMIBComplianceRev1.setDescription('The compliance statement for SNMP entities that implement the CISCO-CABLE-DIAG-MIB.')
ccdPrbsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 2, 1)).setObjects(("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfAction"), ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfActionStatus"), ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfTestErrors"), ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfTestErrorsResetTime"), ("CISCO-CABLE-DIAG-MIB", "ccdPrbsIfTestErrorsMaxValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccdPrbsGroup = ccdPrbsGroup.setStatus('current')
if mibBuilder.loadTexts: ccdPrbsGroup.setDescription('A collection of managed objects to support PRBS cable diagnotic test on the interfaces of the device.')
ccdTdrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 390, 2, 2, 2)).setObjects(("CISCO-CABLE-DIAG-MIB", "ccdTdrIfAction"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfActionStatus"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfLastTestTime"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultValid"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairChannel"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairLength"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairLenAccuracy"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairDistToFault"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairDistAccuracy"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairLengthUnit"), ("CISCO-CABLE-DIAG-MIB", "ccdTdrIfResultPairStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccdTdrGroup = ccdTdrGroup.setStatus('current')
if mibBuilder.loadTexts: ccdTdrGroup.setDescription('A collection of managed objects to support TDR cable diagnotic test on the interfaces of the device.')
mibBuilder.exportSymbols("CISCO-CABLE-DIAG-MIB", ccdTdrIfResultValid=ccdTdrIfResultValid, ccdTdrIfResultPairLenAccuracy=ccdTdrIfResultPairLenAccuracy, ciscoCableDiagMIB=ciscoCableDiagMIB, ccdTdrIfResultTable=ccdTdrIfResultTable, ccdTdrIfResultEntry=ccdTdrIfResultEntry, PYSNMP_MODULE_ID=ciscoCableDiagMIB, ccdPrbsIfAction=ccdPrbsIfAction, ccdPrbsIfTestErrorsResetTime=ccdPrbsIfTestErrorsResetTime, ccdPrbsIfTestErrors=ccdPrbsIfTestErrors, ccdTdrIfAction=ccdTdrIfAction, ccdPrbsIfTable=ccdPrbsIfTable, ccdTdrIfTable=ccdTdrIfTable, ccdTdrIfResultPairChannel=ccdTdrIfResultPairChannel, ciscoCableDiagMIBObjects=ciscoCableDiagMIBObjects, ccdPrbsIfEntry=ccdPrbsIfEntry, ccdPrbsIfActionStatus=ccdPrbsIfActionStatus, ccdPrbsObjects=ccdPrbsObjects, ccdTdrIfResultPairStatus=ccdTdrIfResultPairStatus, ccdTdrIfResultPairIndex=ccdTdrIfResultPairIndex, ccdTdrIfResultPairLengthUnit=ccdTdrIfResultPairLengthUnit, ccdTdrIfResultPairDistToFault=ccdTdrIfResultPairDistToFault, ccdPrbsGroup=ccdPrbsGroup, ciscoCableDiagMIBComplianceRev1=ciscoCableDiagMIBComplianceRev1, ccdPrbsIfTestErrorsMaxValue=ccdPrbsIfTestErrorsMaxValue, ccdTdrIfLastTestTime=ccdTdrIfLastTestTime, ccdTdrObjects=ccdTdrObjects, ccdTdrIfResultPairDistAccuracy=ccdTdrIfResultPairDistAccuracy, ccdTdrIfResultPairLength=ccdTdrIfResultPairLength, ccdTdrGroup=ccdTdrGroup, ciscoCableDiagMIBCompliances=ciscoCableDiagMIBCompliances, ciscoCableDiagMIBGroups=ciscoCableDiagMIBGroups, ccdTdrIfActionStatus=ccdTdrIfActionStatus, ccdTdrIfEntry=ccdTdrIfEntry, ciscoCableDiagMIBConform=ciscoCableDiagMIBConform, ciscoCableDiagMIBNotifs=ciscoCableDiagMIBNotifs)
