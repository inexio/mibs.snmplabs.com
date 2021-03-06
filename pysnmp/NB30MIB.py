#
# PySNMP MIB module NB30MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NB30MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
nb30Rev1, = mibBuilder.importSymbols("IRM-OIDS", "nb30Rev1")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, Integer32, Bits, TimeTicks, iso, Counter64, Gauge32, MibIdentifier, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Integer32", "Bits", "TimeTicks", "iso", "Counter64", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nb30Device = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1))
nb30Dsx = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2))
nb30DsxChannel = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3))
nb30Port = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4))
nb30RemPort = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5))
nb30FilterDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6))
nb30AcqDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1))
nb30PermDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2))
nb30SpecDB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3))
nb30DeviceDisableBdg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("disableBridge", 2), ("enableBridge", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceDisableBdg.setStatus('mandatory')
nb30DeviceRestoreSettings = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("restoreSettings", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceRestoreSettings.setStatus('mandatory')
nb30DeviceBdgName = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceBdgName.setStatus('mandatory')
nb30DeviceNumPorts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceNumPorts.setStatus('mandatory')
nb30DeviceType = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceType.setStatus('mandatory')
nb30DeviceVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceVersion.setStatus('mandatory')
nb30DeviceLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceLocation.setStatus('mandatory')
nb30DeviceStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceStatus.setStatus('mandatory')
nb30DeviceRestartBdg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("restartBridge", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceRestartBdg.setStatus('mandatory')
nb30DeviceFrFwds = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceFrFwds.setStatus('mandatory')
nb30DeviceFrRxs = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceFrRxs.setStatus('mandatory')
nb30DeviceFrFlts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceFrFlts.setStatus('mandatory')
nb30DeviceErrs = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceErrs.setStatus('mandatory')
nb30DeviceNumRestarts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceNumRestarts.setStatus('mandatory')
nb30DeviceTypeFiltering = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ieee8021", 1), ("specialDB", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceTypeFiltering.setStatus('mandatory')
nb30DeviceSTAProtocol = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ieee8021", 1), ("dec", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceSTAProtocol.setStatus('mandatory')
nb30DeviceBridgeID = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 17), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceBridgeID.setStatus('mandatory')
nb30DeviceTopChgCnts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceTopChgCnts.setStatus('mandatory')
nb30DeviceTimeTopChg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceTimeTopChg.setStatus('mandatory')
nb30DeviceTopChg = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noTopologyChangeInProgress", 1), ("topologyChangeInProgress", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceTopChg.setStatus('mandatory')
nb30DeviceRootCost = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceRootCost.setStatus('mandatory')
nb30DeviceRootPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceRootPort.setStatus('mandatory')
nb30DeviceDesigRoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 23), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceDesigRoot.setStatus('mandatory')
nb30DeviceMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceMaxAge.setStatus('mandatory')
nb30DeviceHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceHoldTime.setStatus('mandatory')
nb30DeviceFwdDly = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceFwdDly.setStatus('mandatory')
nb30DeviceHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceHelloTime.setStatus('mandatory')
nb30DeviceBdgFwdDly = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceBdgFwdDly.setStatus('mandatory')
nb30DeviceBdgMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 29), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceBdgMaxAge.setStatus('mandatory')
nb30DeviceBdgHello = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 30), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceBdgHello.setStatus('mandatory')
nb30DeviceBdgPriority = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 31), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceBdgPriority.setStatus('mandatory')
nb30DeviceResetCounts = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounts", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceResetCounts.setStatus('mandatory')
nb30DeviceUptime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceUptime.setStatus('mandatory')
nb30DeviceRootSwitch = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noRoot", 1), ("root", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceRootSwitch.setStatus('mandatory')
nb30DeviceFwdBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwardBroadcast", 1), ("filterBroadcast", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceFwdBroadcast.setStatus('mandatory')
nb30DeviceConfigSw1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchOff", 1), ("switchOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceConfigSw1.setStatus('mandatory')
nb30DeviceConfigSw2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchOff", 1), ("switchOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceConfigSw2.setStatus('mandatory')
nb30DeviceConfigSw3 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchOff", 1), ("switchOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceConfigSw3.setStatus('mandatory')
nb30DeviceConfigSw4 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 39), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchOff", 1), ("switchOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DeviceConfigSw4.setStatus('mandatory')
nb30DevicePortActive = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DevicePortActive.setStatus('mandatory')
nb30DeviceDefPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernetPort1", 1), ("ethernetPort2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceDefPort.setStatus('mandatory')
nb30DeviceRedEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disableRedundancy", 1), ("enableRedundancy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DeviceRedEnable.setStatus('mandatory')
nb30DsxLoopUp = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("loopUp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DsxLoopUp.setStatus('mandatory')
nb30DsxLoopDn = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("loopDown", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DsxLoopDn.setStatus('mandatory')
nb30DsxLoopSt = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notInLoopback", 1), ("loopbackInProgress", 2), ("networkLoopback", 3), ("loopbackPassed", 4), ("loopbackFailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30DsxLoopSt.setStatus('mandatory')
nb30DsxLoopPattern = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("alternate1sAnd0s", 1), ("all1s", 2), ("all0s", 3), ("incrementingData", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DsxLoopPattern.setStatus('mandatory')
nb30DsxChannelTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1), )
if mibBuilder.loadTexts: nb30DsxChannelTable.setStatus('mandatory')
nb30DsxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1, 1), ).setIndexNames((0, "NB30MIB", "nb30DsxChannelId"))
if mibBuilder.loadTexts: nb30DsxEntry.setStatus('mandatory')
nb30DsxChannelControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disableChannel", 1), ("enableChannel", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DsxChannelControl.setStatus('mandatory')
nb30DsxChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30DsxChannelId.setStatus('mandatory')
nb30PortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1), )
if mibBuilder.loadTexts: nb30PortTable.setStatus('mandatory')
nb30PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1), ).setIndexNames((0, "NB30MIB", "nb30PortId"))
if mibBuilder.loadTexts: nb30PortEntry.setStatus('mandatory')
nb30PortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortAddress.setStatus('mandatory')
nb30PortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PortName.setStatus('mandatory')
nb30PortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortType.setStatus('mandatory')
nb30PortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortStatus.setStatus('mandatory')
nb30PortNetName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PortNetName.setStatus('mandatory')
nb30PortFrRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortFrRxs.setStatus('mandatory')
nb30PortDisInbounds = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortDisInbounds.setStatus('mandatory')
nb30PortFwdOutbs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortFwdOutbs.setStatus('mandatory')
nb30PortDisLOBs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortDisLOBs.setStatus('mandatory')
nb30PortDisTDEs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortDisTDEs.setStatus('mandatory')
nb30PortCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortCollisions.setStatus('mandatory')
nb30PortTxAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortTxAborts.setStatus('mandatory')
nb30PortOowCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortOowCollisions.setStatus('mandatory')
nb30PortCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortCRCErrs.setStatus('mandatory')
nb30PortFrAlignErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortFrAlignErrs.setStatus('mandatory')
nb30PortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PortPriority.setStatus('mandatory')
nb30PortState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 17), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortState.setStatus('mandatory')
nb30PortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PortPathCost.setStatus('mandatory')
nb30PortDesigCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortDesigCost.setStatus('mandatory')
nb30PortDesigBrdg = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 20), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortDesigBrdg.setStatus('mandatory')
nb30PortDesigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortDesigPort.setStatus('mandatory')
nb30PortTopChgAck = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noTopologyChangeIsOccurring", 1), ("topologyChangeIsOccurring", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortTopChgAck.setStatus('mandatory')
nb30PortDesigRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 23), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortDesigRoot.setStatus('mandatory')
nb30PortOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortOversizePkts.setStatus('mandatory')
nb30PortFrFiltereds = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortFrFiltereds.setStatus('mandatory')
nb30PortPollAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 26), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PortPollAddress.setStatus('mandatory')
nb30PortPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 27), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PortPollInterval.setStatus('mandatory')
nb30PortMaxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 28), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PortMaxRetry.setStatus('mandatory')
nb30PortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PortId.setStatus('mandatory')
nb30RemPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1), )
if mibBuilder.loadTexts: nb30RemPortTable.setStatus('mandatory')
nb30RemPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1), ).setIndexNames((0, "NB30MIB", "nb30RemPortId"))
if mibBuilder.loadTexts: nb30RemPortEntry.setStatus('mandatory')
nb30RemPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30RemPortName.setStatus('mandatory')
nb30RemPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortType.setStatus('mandatory')
nb30RemPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortStatus.setStatus('mandatory')
nb30RemPortNetName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30RemPortNetName.setStatus('mandatory')
nb30RemPortFrRxs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortFrRxs.setStatus('mandatory')
nb30RemPortFwdOutbs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortFwdOutbs.setStatus('mandatory')
nb30RemPortDisLOBs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortDisLOBs.setStatus('mandatory')
nb30RemPortDisTDEs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortDisTDEs.setStatus('mandatory')
nb30RemPortCRCErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortCRCErrs.setStatus('mandatory')
nb30RemPortFrAlErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortFrAlErrs.setStatus('mandatory')
nb30RemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30RemPortId.setStatus('mandatory')
nb30AcqTotalEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqTotalEntries.setStatus('mandatory')
nb30AcqMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqMaxEntries.setStatus('mandatory')
nb30AcqStaticEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqStaticEntries.setStatus('mandatory')
nb30AcqDynamicEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqDynamicEntries.setStatus('mandatory')
nb30AcqDynAgeTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30AcqDynAgeTime.setStatus('mandatory')
nb30AcqEraseDatabase = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("eraseAcquiredDatabase", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30AcqEraseDatabase.setStatus('mandatory')
nb30AcqDBTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7), )
if mibBuilder.loadTexts: nb30AcqDBTable.setStatus('mandatory')
nb30AcqDBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1), ).setIndexNames((0, "NB30MIB", "nb30AcqMacAddress"))
if mibBuilder.loadTexts: nb30AcqDBEntry.setStatus('mandatory')
nb30AcqCreateFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("createAcquiredFilter", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30AcqCreateFilter.setStatus('mandatory')
nb30AcqCreateForward = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("createAcquiredForward", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30AcqCreateForward.setStatus('mandatory')
nb30AcqDeleteFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deleteAcquiredEntry", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30AcqDeleteFilter.setStatus('mandatory')
nb30AcqFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqFilterType.setStatus('mandatory')
nb30AcqFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("relay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqFilterAction.setStatus('mandatory')
nb30AcqSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqSourceAddress.setStatus('mandatory')
nb30AcqMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30AcqMacAddress.setStatus('mandatory')
nb30PermMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PermMaxEntries.setStatus('mandatory')
nb30PermCurrentEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PermCurrentEntries.setStatus('mandatory')
nb30PermEraseDatabase = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("erasePermanentDatabase", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PermEraseDatabase.setStatus('mandatory')
nb30PermDBTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4), )
if mibBuilder.loadTexts: nb30PermDBTable.setStatus('mandatory')
nb30PermDBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1), ).setIndexNames((0, "NB30MIB", "nb30PermDBMacAddress"))
if mibBuilder.loadTexts: nb30PermDBEntry.setStatus('mandatory')
nb30PermCreateFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("createPermanentFilter", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PermCreateFilter.setStatus('mandatory')
nb30PermCreateForward = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("createPermanentForward", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PermCreateForward.setStatus('mandatory')
nb30PermDeleteEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deletePermanentEntry", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30PermDeleteEntry.setStatus('mandatory')
nb30PermFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PermFilterType.setStatus('mandatory')
nb30PermFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("relay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PermFilterAction.setStatus('mandatory')
nb30PermSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PermSourceAddress.setStatus('mandatory')
nb30PermDBMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30PermDBMacAddress.setStatus('mandatory')
nb30SpecNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30SpecNumEntries.setStatus('mandatory')
nb30SpecMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30SpecMaxEntries.setStatus('mandatory')
nb30SpecNextFilterNum = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30SpecNextFilterNum.setStatus('mandatory')
nb30SpecDBTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4), )
if mibBuilder.loadTexts: nb30SpecDBTable.setStatus('mandatory')
nb30SpecDBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1), ).setIndexNames((0, "NB30MIB", "nb30SpecDbFilterNumber"))
if mibBuilder.loadTexts: nb30SpecDBEntry.setStatus('mandatory')
nb30SpecEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disableFilter", 1), ("enableFilter", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30SpecEnable.setStatus('mandatory')
nb30SpecPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filter", 1), ("relay", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30SpecPort1.setStatus('mandatory')
nb30SpecDestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30SpecDestAddress.setStatus('mandatory')
nb30SpecSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30SpecSrcAddress.setStatus('mandatory')
nb30SpecType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30SpecType.setStatus('mandatory')
nb30SpecDataField = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30SpecDataField.setStatus('mandatory')
nb30SpecDeleteFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("deleteFilter", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nb30SpecDeleteFilter.setStatus('mandatory')
nb30SpecDbFilterNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nb30SpecDbFilterNumber.setStatus('mandatory')
mibBuilder.exportSymbols("NB30MIB", nb30PortDesigCost=nb30PortDesigCost, nb30Device=nb30Device, nb30DeviceBdgName=nb30DeviceBdgName, nb30SpecDBTable=nb30SpecDBTable, nb30PortOowCollisions=nb30PortOowCollisions, nb30PortFrAlignErrs=nb30PortFrAlignErrs, nb30PortTxAborts=nb30PortTxAborts, nb30PermSourceAddress=nb30PermSourceAddress, nb30DeviceRootPort=nb30DeviceRootPort, nb30FilterDB=nb30FilterDB, nb30DeviceConfigSw4=nb30DeviceConfigSw4, nb30SpecEnable=nb30SpecEnable, nb30AcqEraseDatabase=nb30AcqEraseDatabase, nb30DeviceTypeFiltering=nb30DeviceTypeFiltering, nb30PermDB=nb30PermDB, nb30DeviceFwdBroadcast=nb30DeviceFwdBroadcast, nb30RemPortFrRxs=nb30RemPortFrRxs, nb30RemPortCRCErrs=nb30RemPortCRCErrs, nb30PortDisLOBs=nb30PortDisLOBs, nb30DeviceFwdDly=nb30DeviceFwdDly, nb30PortDisInbounds=nb30PortDisInbounds, nb30PortPriority=nb30PortPriority, nb30RemPortEntry=nb30RemPortEntry, nb30PortFrFiltereds=nb30PortFrFiltereds, nb30PortPollInterval=nb30PortPollInterval, nb30DeviceRootCost=nb30DeviceRootCost, nb30DsxChannelControl=nb30DsxChannelControl, nb30AcqFilterAction=nb30AcqFilterAction, nb30DeviceDefPort=nb30DeviceDefPort, nb30DeviceSTAProtocol=nb30DeviceSTAProtocol, nb30DeviceBdgHello=nb30DeviceBdgHello, nb30AcqDB=nb30AcqDB, nb30SpecNextFilterNum=nb30SpecNextFilterNum, nb30DeviceMaxAge=nb30DeviceMaxAge, nb30DsxLoopDn=nb30DsxLoopDn, nb30RemPortStatus=nb30RemPortStatus, nb30PermDBMacAddress=nb30PermDBMacAddress, nb30DsxLoopSt=nb30DsxLoopSt, nb30SpecDBEntry=nb30SpecDBEntry, nb30RemPortType=nb30RemPortType, nb30DeviceRootSwitch=nb30DeviceRootSwitch, nb30SpecSrcAddress=nb30SpecSrcAddress, nb30DeviceHelloTime=nb30DeviceHelloTime, nb30SpecDbFilterNumber=nb30SpecDbFilterNumber, nb30AcqDynamicEntries=nb30AcqDynamicEntries, nb30DeviceStatus=nb30DeviceStatus, nb30SpecDB=nb30SpecDB, nb30DeviceTopChg=nb30DeviceTopChg, nb30PortTable=nb30PortTable, nb30AcqMacAddress=nb30AcqMacAddress, nb30SpecType=nb30SpecType, nb30DeviceDisableBdg=nb30DeviceDisableBdg, nb30PortNetName=nb30PortNetName, nb30AcqStaticEntries=nb30AcqStaticEntries, nb30PortFwdOutbs=nb30PortFwdOutbs, nb30DeviceDesigRoot=nb30DeviceDesigRoot, nb30DeviceVersion=nb30DeviceVersion, nb30PortCRCErrs=nb30PortCRCErrs, nb30PermCreateForward=nb30PermCreateForward, nb30PortPollAddress=nb30PortPollAddress, nb30DeviceRedEnable=nb30DeviceRedEnable, nb30PortName=nb30PortName, nb30PermMaxEntries=nb30PermMaxEntries, nb30SpecNumEntries=nb30SpecNumEntries, nb30DeviceType=nb30DeviceType, nb30DeviceFrRxs=nb30DeviceFrRxs, nb30Dsx=nb30Dsx, nb30SpecPort1=nb30SpecPort1, nb30SpecDeleteFilter=nb30SpecDeleteFilter, nb30DeviceUptime=nb30DeviceUptime, nb30PermEraseDatabase=nb30PermEraseDatabase, nb30RemPortTable=nb30RemPortTable, nb30DeviceConfigSw2=nb30DeviceConfigSw2, nb30PortMaxRetry=nb30PortMaxRetry, nb30DeviceResetCounts=nb30DeviceResetCounts, nb30DeviceBdgMaxAge=nb30DeviceBdgMaxAge, nb30AcqDeleteFilter=nb30AcqDeleteFilter, nb30RemPortFwdOutbs=nb30RemPortFwdOutbs, nb30DsxEntry=nb30DsxEntry, nb30DsxChannel=nb30DsxChannel, nb30PortState=nb30PortState, nb30AcqCreateFilter=nb30AcqCreateFilter, nb30DeviceRestoreSettings=nb30DeviceRestoreSettings, nb30DevicePortActive=nb30DevicePortActive, nb30PortStatus=nb30PortStatus, nb30DeviceHoldTime=nb30DeviceHoldTime, nb30PortAddress=nb30PortAddress, nb30SpecMaxEntries=nb30SpecMaxEntries, nb30PortDisTDEs=nb30PortDisTDEs, nb30RemPortDisTDEs=nb30RemPortDisTDEs, nb30PortFrRxs=nb30PortFrRxs, nb30PortPathCost=nb30PortPathCost, nb30DeviceBdgFwdDly=nb30DeviceBdgFwdDly, nb30AcqTotalEntries=nb30AcqTotalEntries, nb30PortCollisions=nb30PortCollisions, nb30PermFilterType=nb30PermFilterType, nb30PortDesigRoot=nb30PortDesigRoot, nb30DsxLoopUp=nb30DsxLoopUp, nb30DeviceTimeTopChg=nb30DeviceTimeTopChg, nb30PermDBEntry=nb30PermDBEntry, nb30SpecDestAddress=nb30SpecDestAddress, nb30DeviceErrs=nb30DeviceErrs, nb30DeviceRestartBdg=nb30DeviceRestartBdg, nb30RemPortId=nb30RemPortId, nb30AcqDBTable=nb30AcqDBTable, nb30PortTopChgAck=nb30PortTopChgAck, nb30DeviceBridgeID=nb30DeviceBridgeID, nb30DsxChannelTable=nb30DsxChannelTable, nb30DeviceFrFlts=nb30DeviceFrFlts, nb30DeviceTopChgCnts=nb30DeviceTopChgCnts, nb30RemPort=nb30RemPort, nb30PortDesigBrdg=nb30PortDesigBrdg, nb30PermCurrentEntries=nb30PermCurrentEntries, nb30AcqMaxEntries=nb30AcqMaxEntries, nb30PortOversizePkts=nb30PortOversizePkts, nb30PermDBTable=nb30PermDBTable, nb30DeviceConfigSw1=nb30DeviceConfigSw1, nb30RemPortFrAlErrs=nb30RemPortFrAlErrs, nb30AcqFilterType=nb30AcqFilterType, nb30SpecDataField=nb30SpecDataField, nb30PermCreateFilter=nb30PermCreateFilter, nb30PortType=nb30PortType, nb30PortEntry=nb30PortEntry, nb30Port=nb30Port, nb30DeviceBdgPriority=nb30DeviceBdgPriority, nb30DeviceFrFwds=nb30DeviceFrFwds, nb30DeviceNumPorts=nb30DeviceNumPorts, nb30RemPortDisLOBs=nb30RemPortDisLOBs, nb30DeviceNumRestarts=nb30DeviceNumRestarts, nb30AcqDynAgeTime=nb30AcqDynAgeTime, nb30AcqSourceAddress=nb30AcqSourceAddress, nb30PortId=nb30PortId, nb30DeviceConfigSw3=nb30DeviceConfigSw3, nb30PermDeleteEntry=nb30PermDeleteEntry, nb30PermFilterAction=nb30PermFilterAction, nb30RemPortNetName=nb30RemPortNetName, nb30DeviceLocation=nb30DeviceLocation, nb30DsxLoopPattern=nb30DsxLoopPattern, nb30DsxChannelId=nb30DsxChannelId, nb30AcqCreateForward=nb30AcqCreateForward, nb30RemPortName=nb30RemPortName, nb30PortDesigPort=nb30PortDesigPort, nb30AcqDBEntry=nb30AcqDBEntry)
