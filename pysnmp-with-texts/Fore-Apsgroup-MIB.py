#
# PySNMP MIB module Fore-Apsgroup-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Apsgroup-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
atmSwitch, asx = mibBuilder.importSymbols("Fore-Common-MIB", "atmSwitch", "asx")
hwPortNumber, hwPortBoard, hwPortModule, hwPortName = mibBuilder.importSymbols("Fore-Switch-MIB", "hwPortNumber", "hwPortBoard", "hwPortModule", "hwPortName")
trapLogIndex, = mibBuilder.importSymbols("Fore-TrapLog-MIB", "trapLogIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, ObjectIdentity, IpAddress, Unsigned32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, iso, Bits, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ObjectIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "iso", "Bits", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreAps = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16))
if mibBuilder.loadTexts: foreAps.setLastUpdated('9912090000Z')
if mibBuilder.loadTexts: foreAps.setOrganization('FORE')
if mibBuilder.loadTexts: foreAps.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreAps.setDescription('SONET APS ')
apsPortGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1))
apsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2))
apsPortTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1), )
if mibBuilder.loadTexts: apsPortTable.setStatus('current')
if mibBuilder.loadTexts: apsPortTable.setDescription('A table of SONET APS port configuration information.')
apsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1), ).setIndexNames((0, "Fore-Apsgroup-MIB", "apsBoard"), (0, "Fore-Apsgroup-MIB", "apsModule"), (0, "Fore-Apsgroup-MIB", "apsPort"))
if mibBuilder.loadTexts: apsPortEntry.setStatus('current')
if mibBuilder.loadTexts: apsPortEntry.setDescription('A table entry containing SONET APS configuration information for each APS port. ')
apsBoard = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsBoard.setStatus('current')
if mibBuilder.loadTexts: apsBoard.setDescription("The index of this port's switch board.")
apsModule = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsModule.setStatus('current')
if mibBuilder.loadTexts: apsModule.setDescription('The network module of this port.')
apsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsPort.setStatus('current')
if mibBuilder.loadTexts: apsPort.setDescription('The number of this port.')
apsAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("protection", 2), ("unprotected", 3))).clone('unprotected')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsAdminMode.setStatus('current')
if mibBuilder.loadTexts: apsAdminMode.setDescription('This variable indicates the APS configuration for this port. Unprotected indicates that APS is not configured for this port. Working indicates that this port is a working channel. Protection indicates that this port is a protection channel.')
apsOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("active", 1), ("standby", 2), ("notApplicable", 3), ("loopbackOn", 4), ("loopbackOff", 5))).clone('notApplicable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsOperMode.setStatus('current')
if mibBuilder.loadTexts: apsOperMode.setDescription('This variable indicates if this port is an active or standby APS channel. If APS is not configured for this port, the mode is notApplicable. loopbackOn indicates that the port is configured in the loopback mode and is the port on which the loopback has been enabled(or is under test). loopbackOff indicates that the port is configured in the loopback mode and is the port which is in the disabled state (not under test).')
apsPortGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsPortGroupName.setStatus('current')
if mibBuilder.loadTexts: apsPortGroupName.setDescription('This object identifies the APS group this port is associated with.')
apsGroupTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1), )
if mibBuilder.loadTexts: apsGroupTable.setStatus('current')
if mibBuilder.loadTexts: apsGroupTable.setDescription('A table of SONET APS port group configuration information.')
apsGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1), ).setIndexNames((0, "Fore-Apsgroup-MIB", "apsGroupName"))
if mibBuilder.loadTexts: apsGroupEntry.setStatus('current')
if mibBuilder.loadTexts: apsGroupEntry.setDescription('A table entry containing SONET APS configuration information for each APS group. ')
apsGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsGroupName.setStatus('current')
if mibBuilder.loadTexts: apsGroupName.setDescription('This object identifies the APS group. of all the ports associated with this group.')
apsGroupStateCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("clear", 1), ("lockout", 2), ("forceSwitchToWorking", 3), ("forceSwitchToProtection", 4), ("manualSwitchToWorking", 5), ("manualSwitchToProtection", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsGroupStateCommand.setStatus('current')
if mibBuilder.loadTexts: apsGroupStateCommand.setDescription('A user initiated APS command. Note this object is write-only and reading it will result in implementation-specific results.')
apsGroupLastCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("clear", 1), ("lockout", 2), ("forceSwitchToWorking", 3), ("forceSwitchToProtection", 4), ("manualSwitchToWorking", 5), ("manualSwitchToProtection", 6), ("suspendWorking", 7), ("suspendProtection", 8), ("noRequest", 9))).clone('noRequest')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsGroupLastCommand.setStatus('current')
if mibBuilder.loadTexts: apsGroupLastCommand.setDescription('Last Aps Command issued by the user.')
apsWorkingLineState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("signalFailure", 1), ("signalDegrade", 2), ("none", 3), ("notAvailable", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsWorkingLineState.setStatus('current')
if mibBuilder.loadTexts: apsWorkingLineState.setDescription('Line State of the Working Port of the APS Group. ')
apsProtectionLineState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("signalFailure", 1), ("signalDegrade", 2), ("none", 3), ("notAvailable", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsProtectionLineState.setStatus('current')
if mibBuilder.loadTexts: apsProtectionLineState.setDescription('Line State of the Protection Port of the APS Group. ')
apsGroupMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uni-directional", 1), ("bi-directional", 2))).clone('uni-directional')).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsGroupMode.setStatus('current')
if mibBuilder.loadTexts: apsGroupMode.setDescription('This variable indicates the APS switching mode for this APS group.')
apsRxK1K2 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("lockout", 1), ("forceSwitch", 2), ("manualSwitch", 3), ("signalFailure", 4), ("signalDegrade", 5), ("exercise", 6), ("waitToRestore", 7), ("reverseRequest", 8), ("doNotRevert", 9), ("noRequest", 10), ("none", 11), ("notAvailable", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsRxK1K2.setStatus('current')
if mibBuilder.loadTexts: apsRxK1K2.setDescription('Command specified in the received K1K2 bytes. ')
apsRxChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("protection", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsRxChannel.setStatus('current')
if mibBuilder.loadTexts: apsRxChannel.setDescription('Channel specified in received K1K2 bytes. ')
apsTxK1K2 = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("lockout", 1), ("forceSwitch", 2), ("manualSwitch", 3), ("signalFailure", 4), ("signalDegrade", 5), ("exercise", 6), ("waitToRestore", 7), ("reverseRequest", 8), ("doNotRevert", 9), ("noRequest", 10), ("none", 11), ("notAvailable", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTxK1K2.setStatus('current')
if mibBuilder.loadTexts: apsTxK1K2.setDescription('Command specified in the transmitted K1K2 bytes. ')
apsTxChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("protection", 2), ("not-applicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsTxChannel.setStatus('current')
if mibBuilder.loadTexts: apsTxChannel.setDescription('Channel specified in transmitted K1K2 bytes. ')
apsRevertMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsRevertMode.setStatus('current')
if mibBuilder.loadTexts: apsRevertMode.setDescription('APS revertive mode configuration')
apsRevertTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 12), Integer32().clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsRevertTimer.setStatus('current')
if mibBuilder.loadTexts: apsRevertTimer.setDescription('APS revertive timer value in minutes')
apsSwitchOver = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2017)).setObjects(("Fore-Switch-MIB", "hwPortName"), ("Fore-Switch-MIB", "hwPortBoard"), ("Fore-Switch-MIB", "hwPortModule"), ("Fore-Switch-MIB", "hwPortNumber"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: apsSwitchOver.setStatus('current')
if mibBuilder.loadTexts: apsSwitchOver.setDescription('This trap alerts that an aps switchover has occurred and the active port is identified by the tuple {hwPortBoard, hwPortModule, hwPortNumber}.')
mibBuilder.exportSymbols("Fore-Apsgroup-MIB", apsTxK1K2=apsTxK1K2, apsProtectionLineState=apsProtectionLineState, apsRevertTimer=apsRevertTimer, apsGroup=apsGroup, apsPortTable=apsPortTable, apsGroupMode=apsGroupMode, apsWorkingLineState=apsWorkingLineState, apsTxChannel=apsTxChannel, apsPortEntry=apsPortEntry, apsPortGroup=apsPortGroup, apsRevertMode=apsRevertMode, apsGroupLastCommand=apsGroupLastCommand, apsGroupTable=apsGroupTable, apsPortGroupName=apsPortGroupName, apsGroupName=apsGroupName, apsBoard=apsBoard, apsGroupEntry=apsGroupEntry, apsAdminMode=apsAdminMode, PYSNMP_MODULE_ID=foreAps, apsGroupStateCommand=apsGroupStateCommand, apsModule=apsModule, foreAps=foreAps, apsPort=apsPort, apsRxK1K2=apsRxK1K2, apsSwitchOver=apsSwitchOver, apsOperMode=apsOperMode, apsRxChannel=apsRxChannel)
